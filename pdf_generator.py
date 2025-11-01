from fpdf import FPDF
from datetime import date

def create_pdf(problems: list[str], filename: str):
    if filename.strip() == "":
        filename = f"math_problems_{date.today().isoformat()}.pdf"

    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    pdf.set_font("Arial", size=16)
    pdf.cell(0, 10, "Daily Math Problems", 0, 1, 'C')

    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f"Date: {date.today().isoformat()}", 0, 1, 'C')

    pdf.set_font("Arial", "I", 12)
    pdf.multi_cell(0, 7, "Instructions: Read each problem carefully and show your work below. Good luck!", 0, "L")
    pdf.ln(5)

    for problem in problems:
        pdf.set_font("Arial", "B", 12)
        pdf.multi_cell(0, 8, f"{problem}", 0, "L")
        pdf.ln(30)  # Space for working out the problem

        pdf.set_font("Arial", size=12)
        pdf.ln(10)  # Additional space after the line

    pdf.output(filename)
    print(f"PDF generated and saved as '{filename}'")
    return filename