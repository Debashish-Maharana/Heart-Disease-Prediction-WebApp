from fpdf import FPDF
from datetime import datetime

def generate_pdf(user_input, prediction, probability, save_path):
    """
    Generate a PDF report of heart disease prediction results.

    Parameters:
    - user_input: dict of input data
    - prediction: array-like output from model (e.g., [0] or [1])
    - probability: float, probability of heart disease
    - save_path: str, path to save the generated PDF
    """

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, "Heart Disease Prediction Report", ln=True, align='C')
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, f"Date: {datetime.now().strftime('%d-%m-%Y %H:%M')}", ln=True)

    pdf.ln(10)
    result_text = "High Risk Detected!" if prediction[0] == 1 else "No Significant Risk"
    pdf.set_font("Arial", "B", 14)
    pdf.cell(200, 10, f"Prediction Result: {result_text}", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, f"Confidence: {probability:.2f}%", ln=True)

    pdf.ln(10)
    pdf.set_font("Arial", "B", 13)
    pdf.cell(200, 10, "User Inputs:", ln=True)
    pdf.set_font("Arial", size=11)
    for key, value in user_input.items():
        pdf.cell(200, 8, f"{key}: {value}", ln=True)

    pdf.output(save_path)
    return save_path
