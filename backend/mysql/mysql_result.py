from PyPDF2 import PdfMerger
import win32com.client
import time
import sys
from datetime import datetime
now = datetime.now()
date = now.strftime('%Y-%m-%d_%H-%M-%S')
py_path = sys.path[0]

excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = False


pdf_merger = PdfMerger()

pdf_files = [py_path+"/../output/mysql_report.pdf",
             py_path+"/../output/mysql_graph.pdf"]

for pdf_file in pdf_files:
    pdf_merger.append(pdf_file)

output_path = py_path+"/../../report/mysql_result_"+date+".pdf"
pdf_merger.write(output_path)
pdf_merger.close()
