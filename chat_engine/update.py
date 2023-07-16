from dotenv import load_dotenv
import os
from database_connection import DatabaseConnection
from mysql_service import MySQLService
from excel_service import ExcelService
from data_export_service import DataExportService

def start():
    load_dotenv()

    # Configuração do banco de dados
    HOST = os.getenv("DB_HOST")
    DATABASE = os.getenv("DB_DATABASE")
    USER = os.getenv("DB_USER")
    PASSWORD = os.getenv("DB_PASSWORD")

    # Estabelecendo a conexão com o banco de dados MySQL
    db_connection = DatabaseConnection(HOST, DATABASE, USER, PASSWORD)
    db_connection.connect()

    # Serviços
    database_service = MySQLService(db_connection)
    excel_service = ExcelService()
    data_export_service = DataExportService(database_service, excel_service)

    # Exportar dados para o Excel
    data_export_service.export_data_to_excel(os.getenv("QUERY_SQL"), 'output.xlsx')

    # Fechando a conexão com o banco de dados
    db_connection.close()