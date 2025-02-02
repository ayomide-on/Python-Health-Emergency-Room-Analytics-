# Python-Health-Emergency-Response-Analytics

This project analyzes hospital emergency response data to uncover insights into patient wait times, satisfaction levels, demographic referrals, and admission trends. Using Python, Pandas, and Flask, the analysis is visualized on a web interface for better decision-making and performance tracking.

Dataset
The dataset includes key attributes of patient records:
Patient ID
Patient Admission Date
Patient First Initial & Last Name (anonymized for privacy)
Patient Gender
Patient Age
Patient Race
Department Referral
Patient Admission Flag (indicates admission status)
Patient Satisfaction Score
Patient Wait Time
Patients CM (Case Management)

Key Analyses Performed

Wait Time Analysis

Average wait times segmented by department and age group.

Satisfaction vs. Wait Time Correlation

Analyzed the relationship between wait times and patient satisfaction scores.

Demographic and Department Referrals

Evaluated referral trends based on race, gender, and department.

Admission Analysis

Studied admission rates segmented by demographics and department.

Technologies Used
Python (Pandas, Flask, Matplotlib, Seaborn)
HTML, CSS (Static Styling)
Flask Framework (for web hosting and data visualization)

Project Structure

├── static
│   ├── style.css  # Styling for the web interface
├── templates
│   ├── index.html  # Webpage template for displaying analysis
├── app.py  # Flask application for hosting the web interface
├── data
│   ├── patient_data.csv  # Sample dataset
├── README.md  # Project documentation

How to Run the Project

Clone the Repository
git clone https://github.com/your-username/health-emergency-response-analysis.git
cd health-emergency-response-analysis
Install Dependencies
pip install flask pandas matplotlib seaborn
Run the Flask Application
python app.py

The application will be available at http://127.0.0.1:5002/.

Web Interface Preview

The analysis results are displayed on a Flask-hosted web application with:
Tabular reports for wait times, demographic referrals, and admissions
A correlation summary between wait time and satisfaction
Future Improvements
Add interactive visualizations using Plotly.
Integrate database support for dynamic data updates.
Enhance predictive modeling for better patient flow optimization.

Contributing
Contributions are welcome! Feel free to fork this repository and submit a pull request with improvements or suggestions.

License
This project is licensed under the MIT License.

Developed by ODUNTAN AYOMIDE

