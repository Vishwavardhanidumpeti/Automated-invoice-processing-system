import pandas as pd
import PyPDF2
import fitz
with open(r"C:/Users/ADMIN/OneDrive/Desktop/vishwavardhani_resume.pdf",'rb') as f:
   text = PyPDF2.PdfReader(f)  
   for i in range(len(text.pages)):
      page=text.pages[i]
      content_page=page.extract_text()
      with open(r"C:/Users/ADMIN/OneDrive/Desktop/vishwavardhani_resume.txt",'w',encoding="utf-8") as f:
         f.write(content_page+"\n")
# with fitz.open(r"C:/Users/ADMIN/OneDrive/Desktop/vishwavardhani_resume.pdf") as f:
#     for i in f:
#         text=i.get_text
#         print(text)
    

