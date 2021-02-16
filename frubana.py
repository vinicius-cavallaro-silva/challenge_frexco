from view.get_products import GetProductsFrubana
from components.insert_csv import CsvFiles
from components.database import Database


class FrubanaFlow:
    def __init__(self):
        self.get_products_fubana = GetProductsFrubana()
        self.csv_files = CsvFiles()
        self.database = Database()


    def frubana_flow(self):
        self.get_products_fubana.load_page()
        list_items = self.get_products_fubana.scroll_page()
        self.get_products_fubana.close_page()
        self.csv_files.csv_creator(list_product=list_items)
        self.database.connection()
        self.database.create_table()
        self.database.insert_data(list_data=list_items)
        self.database.close_connection()