from fpdf import FPDF
import pandas as pd
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    # Set the Header
    pdf.set_font(family="Times", style="BI", size=24)
    pdf.set_text_color(25, 178, 367)
    pdf.cell(w=0, h=12, txt=row["Topic"],
             align="L", ln=1)
    # pdf.line(10, 21, 200,21)
    # pdf.line(10, 21.5, 200, 21.5)

    for y in range(20, 298,10):
        pdf.line(10, y, 200, y)

    # Set the footer
    pdf.ln(267)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=8, txt=row["Topic"],
             align="R", ln=1)
    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # Set the footer
        pdf.ln(279)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=8, txt=row["Topic"],
                 align="R", ln=1)
        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)
pdf.output("output.pdf")

