from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='p', unit='mm', format='a4')
pdf2 = FPDF(orientation='p', unit='mm', format='a4')
# to avoid getting content out of the pages
pdf.set_auto_page_break(auto=False)
pdf2.set_auto_page_break(auto=False)

df = pd.read_csv("topics.csv")


def footer(obj):
    obj.set_font(family='Times', style='IB', size=10)
    obj.set_text_color(130, 130, 130)
    obj.cell(w=0, txt=item['Topic'], ln=1, align='R')


for index, item in df.iterrows():
    pdf.add_page()
    pdf.set_font(family='Times', style='B', size=24)
    pdf.set_text_color(100, 100, 100)  # gray color
    pdf.cell(w=0, h=10, txt=item["Topic"], ln=1, align='L')
    pdf.line(10, 21, 200, 21)
    pdf.ln(258)  # EMPTY BREAK LINES
    footer(pdf)
    if int(item["Pages"]) != 1:  # adding pages
        for i in range(int(item["Pages"]) - 1):
            pdf.add_page()
            pdf.ln(268)
            footer(pdf)

def rulelines():
    X1 = 10
    y1 = 21
    X2 = 200
    y2 = 21
    while True:
        # 10mm
        pdf2.line(X1, y1, X2, y2)
        y1 += 10 #10mm
        y2 += 10 #10mm
        if y1 > 290:
            break

for index, item in df.iterrows():
    pdf2.add_page()
    pdf2.set_font(family='Times', style='B', size=24)
    pdf2.set_text_color(100, 100, 100)  # gray color
    pdf2.cell(w=0, h=10, txt=item["Topic"], ln=1, align='L')
    rulelines()
    pdf2.ln(268) #empty breaklines
    footer(pdf2)
    if int(item["Pages"]) != 1:  # adding pages
        for i in range(int(item["Pages"]) - 1):
            pdf2.add_page()
            rulelines()
            pdf2.ln(278)
            footer(pdf2)

pdf.output('output.pdf')
pdf2.output("LinedOutput.pdf")




