from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

df = pd.read_csv('/Users/apple/welcome101/project/final_project/oaqjp-final-project-emb-ai/Financial_chatbot/Hospital_ER/Hospital ER_Data.csv')

def analysis():
    df['Age Group'] = pd.cut(df['Patient Age'], bins = [0, 18, 35, 50, 100], labels= ['0-18', '19-35', '36-50', '51+'])

    #Analyze wait times by department & Age group
    Wait_time = df.groupby(['Department Referral', 'Age Group'], observed=False)['Patient Waittime'].mean().reset_index()

    #analyze correlation between Patient wait time and Satistfaction
    Corr = df['Patient Waittime'].corr(df['Patient Satisfaction Score'])

    #demographic analysis
    Demographics = df.groupby(['Department Referral', 'Patient Gender', 'Patient Race']).size().reset_index(name = 'Referral Count')

    #analyze patient admission rate by department
    admission_analysis = df.groupby(['Patient Race', 'Patient Gender', 'Department Referral'])['Patient Admission Flag'].mean().reset_index()

    return Wait_time, Corr, Demographics, admission_analysis

#define the home route
@app.route('/')
def home():
    Wait_time, Corr, Demographics, admission_analysis = analysis()
    
    return render_template('index.html', Wait_time=Wait_time.to_dict('records'),
                            Corr = Corr, 
                            Demographics = Demographics.to_dict('records'),
                            admission_analysis = admission_analysis.to_dict('records'))


#Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug = True)

    
