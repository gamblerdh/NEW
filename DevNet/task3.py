import openpyxl
def excel_read(target):
    wb = openpyxl.reader.excel.load_workbook(filename="excel.xlsx")
    wb.active = 0
    table = wb.active
    for i in range(5, 150):
        if table['B'+str(i)].value == None:
            continue
        if table['B'+str(i)].value.lower() == target.lower():
            result = (table['B'+str(i)].value, table['E'+str(i)].value, table['F'+str(i)].value)
            break
    else:
        result = None
    return result