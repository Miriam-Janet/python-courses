import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active

sheet['A1'] = "Name"  
sheet['B1'] = "Amount"  
sheet['C1'] = "Country"  


wb.save("sample_file.xlsx")  #se guarda aqui