from fpdf import FPDF
import pandas as pd
pdf = FPDF(orientation='p',unit='mm',format='a4')

df=pd.read_csv("topics.csv")

for index,item in df.iterrows():
    pdf.add_page()
    pdf.set_font(family='Times',style='B',size=24)
    pdf.set_text_color(100,100,100) #gray color
    pdf.cell(w=0,h=10,txt=item["Topic"],ln=1,align='L')
    pdf.line(10,21,200,21)


pdf.output('output.pdf')
