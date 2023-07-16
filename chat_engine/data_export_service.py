class DataExportService:
    def __init__(self, database_service, excel_service):
        self.database_service = database_service
        self.excel_service = excel_service

    def export_data_to_excel(self, query, filename):
        results = self.database_service.execute_query(query)
        dataframe = self.database_service.create_dataframe(results)
        workbook = self.excel_service.create_workbook()
        self.excel_service.add_dataframe_to_sheet(workbook, dataframe)
        self.excel_service.save_workbook(workbook, filename)