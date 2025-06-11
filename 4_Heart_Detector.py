from utils.firebase_utils import upload_to_storage, list_reports
from datetime import datetime
import streamlit as st
import joblib
import pandas as pd
import tempfile
from fpdf import FPDF

# Sanitize email to use as Firebase DB key
def sanitize_email(email: str) -> str:
    return email.replace('@', '_at_').replace('.', '_dot_')

model = joblib.load("hdp_best_model.sav")
scaler = joblib.load("scaler.pkl")

binary_map = {'Yes': 1, 'No': 0, 'Male': 1, 'Female': 0}
ordinal_map = {
    'Exercise Habits': {'Low': 1, 'Medium': 2, 'High': 0},
    'Alcohol Consumption': {'Low': 1, 'Medium': 2, 'High': 0, 'None': 3},
    'Stress Level': {'Low': 1, 'Medium': 2, 'High': 0},
    'Sugar Consumption': {'Low': 1, 'Medium': 2, 'High': 0}
}

def preprocess_user_input(user_input):
    df = pd.DataFrame([user_input])
    for col in ['Gender', 'Smoking', 'Family Heart Disease', 'Diabetes',
                'High Blood Pressure', 'Low HDL Cholesterol', 'High LDL Cholesterol']:
        df[col] = df[col].map(binary_map)
    for col, mapping in ordinal_map.items():
        df[col] = df[col].map(mapping)
    numerical_cols = ['Age', 'Blood Pressure', 'Cholesterol Level', 'BMI',
                      'Sleep Hours', 'Triglyceride Level', 'Fasting Blood Sugar',
                      'CRP Level', 'Homocysteine Level']
    df[numerical_cols] = scaler.transform(df[numerical_cols])
    return df

def extract_datetime_from_filename(filename):
    """Extract datetime from filename format: YYYYMMDDHHMMSS.pdf"""
    try:
        # Extract the timestamp part from filename (assuming format: YYYYMMDDHHMMSS.pdf)
        timestamp_str = filename.split('/')[-1].replace('.pdf', '')
        if len(timestamp_str) == 14 and timestamp_str.isdigit():
            return datetime.strptime(timestamp_str, '%Y%m%d%H%M%S')
        else:
            # Fallback: return a very old date if format is unexpected
            return datetime.min
    except:
        return datetime.min

def format_datetime_display(dt):
    """Format datetime for display"""
    return dt.strftime('%d/%m/%Y at %H:%M')

def generate_pdf(user_input, prediction):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    normal_ranges = {
        'Blood Pressure': (90, 120),
        'Cholesterol Level': (125, 200),
        'BMI': (18.5, 24.9),
        'Sleep Hours': (7, 9),
        'Triglyceride Level': (0, 150),
        'Fasting Blood Sugar': (70, 99),
        'CRP Level': (0.0, 1.0),
        'Homocysteine Level': (4.0, 15.0)
    }

    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, txt="Heart Disease Prediction Report", ln=True, align="C")
    pdf.ln(10)

    current_date = datetime.now().strftime("%d.%m.%Y")
    current_time = datetime.now().strftime("%H:%M")
    pdf.set_font("Arial", "I", 12)
    pdf.cell(0, 10, txt=f"Date: {current_date}", ln=True, align="R")
    pdf.cell(0, 10, txt=f"Time: {current_time}", ln=True, align="R")
    pdf.ln(5)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, txt="Patient Input Details:", ln=True)
    pdf.ln(5)

    pdf.set_font("Arial", "B", 11)
    pdf.set_fill_color(200, 220, 255)
    pdf.cell(60, 10, "Parameter", border=1, align='C', fill=True)
    pdf.cell(60, 10, "User Value", border=1, align='C', fill=True)
    pdf.cell(60, 10, "Normal Value", border=1, align='C', fill=True)
    pdf.ln()

    pdf.set_font("Arial", size=11)
    for key, value in user_input.items():
        if key in normal_ranges:
            low, high = normal_ranges[key]
            is_abnormal = not (low <= float(value) <= high)
            if is_abnormal:
                pdf.set_fill_color(255, 200, 200)
            else:
                pdf.set_fill_color(200, 255, 200)
            normal_value = f"{low} - {high}"
        else:
            pdf.set_fill_color(255, 255, 255)
            normal_value = "N/A"

        pdf.cell(60, 8, str(key), border=1, fill=True)
        pdf.cell(60, 8, str(value), border=1, fill=True)
        pdf.cell(60, 8, normal_value, border=1, fill=True)
        pdf.ln()

    result = "High Risk of Heart Disease Detected!" if prediction[0] == 1 else "No Significant Risk Detected."
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, txt="Prediction Result: ", ln=True)
    pdf.set_font("Arial", size=11)
    pdf.multi_cell(0, 10, txt=f"{result}")

    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    pdf.output(temp_file.name)
    return temp_file.name

st.title("🫀 Heart Disease Prediction")

if "user" not in st.session_state:
    st.warning("Please login first.")
    st.stop()

user = st.session_state["user"]
user_email = user["email"]
safe_uid = sanitize_email(user_email)

tab1, tab2 = st.tabs(["📋 Predict", "📁 History"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        age = st.slider("Age", 20, 100, 40)
        gender = st.selectbox("Gender", ["Male", "Female"])
        blood_pressure = st.number_input("Blood Pressure", value=120.0)
        cholesterol = st.number_input("Cholesterol Level", value=200.0)
        bmi = st.number_input("BMI", value=25.0)
        sleep_hours = st.slider("Sleep Hours", 0, 12, 7)
        exercise = st.selectbox("Exercise Habits", ["Low", "Medium", "High"])
        alcohol = st.selectbox("Alcohol Consumption", ["Low", "Medium", "High", "None"])
        stress = st.selectbox("Stress Level", ["Low", "Medium", "High"])
        sugar = st.selectbox("Sugar Consumption", ["Low", "Medium", "High"])

    with col2:
        smoking = st.selectbox("Smoking", ["Yes", "No"])
        family_hd = st.selectbox("Family History", ["Yes", "No"])
        diabetes = st.selectbox("Diabetes", ["Yes", "No"])
        hbp = st.selectbox("High BP", ["Yes", "No"])
        low_hdl = st.selectbox("Low HDL", ["Yes", "No"])
        high_ldl = st.selectbox("High LDL", ["Yes", "No"])
        triglycerides = st.number_input("Triglyceride Level", value=150.0)
        fbs = st.number_input("Fasting Blood Sugar", value=90.0)
        crp = st.number_input("CRP Level", value=0.5)
        homocysteine = st.number_input("Homocysteine Level", value=10.0)

    if st.button("Predict"):
        user_input = {
            'Age': age, 'Gender': gender, 'Blood Pressure': blood_pressure,
            'Cholesterol Level': cholesterol, 'Exercise Habits': exercise,
            'Smoking': smoking, 'Family Heart Disease': family_hd, 'Diabetes': diabetes,
            'BMI': bmi, 'High Blood Pressure': hbp, 'Low HDL Cholesterol': low_hdl,
            'High LDL Cholesterol': high_ldl, 'Alcohol Consumption': alcohol,
            'Stress Level': stress, 'Sleep Hours': sleep_hours, 'Sugar Consumption': sugar,
            'Triglyceride Level': triglycerides, 'Fasting Blood Sugar': fbs,
            'CRP Level': crp, 'Homocysteine Level': homocysteine
        }

        processed = preprocess_user_input(user_input)
        prediction = model.predict(processed)
        #probability = model.predict_proba(processed)[0][1] * 100

        result = "High Risk Detected!" if prediction[0] == 1 else "No Significant Risk"
        if prediction[0] == 1:
            st.error(f"Prediction: {result}")
        else:
            st.success(f"Prediction: {result}")

        pdf_path = generate_pdf(user_input, prediction)
        filename = f"reports/{safe_uid}/{datetime.now().strftime('%Y%m%d%H%M%S')}.pdf"
        url = upload_to_storage(pdf_path, filename, user)

        with open(pdf_path, "rb") as f:
            st.download_button("Download Report", f, file_name="heart_disease_report.pdf")

with tab2:
    st.subheader("📁 Report History")
    reports = list_reports(user_email)
    if not reports:
        st.info("No reports found.")
    else:
        # Sort reports by datetime (most recent first)
        reports_with_datetime = []
        for file in reports:
            dt = extract_datetime_from_filename(file['name'])
            reports_with_datetime.append({
                'file': file,
                'datetime': dt
            })
        
        # Sort by datetime in descending order (most recent first)
        reports_with_datetime.sort(key=lambda x: x['datetime'], reverse=True)
        
        st.write(f"**Total Reports:** {len(reports)}")
        st.write("---")
        
        for item in reports_with_datetime:
            file = item['file']
            dt = item['datetime']
            filename = file['name'].split('/')[-1]
            
            # Create a more informative display
            col1, col2 = st.columns([3, 1])
            
            with col1:
                if dt != datetime.min:
                    display_date = format_datetime_display(dt)
                    st.markdown(f"📄 **[{filename}]({file['url']})**")
                    st.markdown(f"&nbsp;&nbsp;&nbsp;&nbsp;📅 Generated on: {display_date}")
                else:
                    st.markdown(f"📄 **[{filename}]({file['url']})**")
                    st.markdown("&nbsp;&nbsp;&nbsp;&nbsp;📅 Date: Unknown")
            
            with col2:
                st.markdown(f"[📥 Download]({file['url']})")
            
            st.write("---")