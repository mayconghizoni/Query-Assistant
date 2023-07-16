from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

class ExcelService:
    def create_workbook(self):
        return Workbook()

    def add_dataframe_to_sheet(self, workbook, dataframe):
        sheet = workbook.active
        for row in dataframe_to_rows(dataframe, index=False, header=True):
            sheet.append(row)

    def save_workbook(self, workbook, filename):
        workbook.save(filename)