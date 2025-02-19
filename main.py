from fpdf import FPDF
import pandas as pd
pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="BI", size=24)
    pdf.set_text_color(25, 178, 367)
    pdf.cell(w=0.0, h=12.0, txt=row["Topic"], align="L", ln=1)
    pdf.line(10, 21, 200,21)
    pdf.line(10, 21.5, 200, 21.5)
pdf.output("output.pdf")

