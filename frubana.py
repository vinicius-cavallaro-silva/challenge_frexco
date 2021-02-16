from view.get_products import GetProductsFrubana
from components.insert_csv import CsvFiles
from components.database import Database


class FrubanaFlow:
    def __init__(self):
        self.get_products_frubana = GetProductsFrubana()
        self.csv_files = CsvFiles()
        self.database = Database()

    def frubana_flow(self):
        """
        It's the system's process flow, where all steps are initialized.
        :return: none
        """

        # Step 1 - Get information
        self.get_products_frubana.load_page()
        list_items = self.get_products_frubana.scroll_page()
        self.get_products_frubana.close_page()

        # Step 2 - Save information in a cvs file
        self.csv_files.csv_creator(list_product=list_items)

        # Step 3 - Save in database
        self.database.connection()
        self.database.create_table()
        self.database.insert_data(list_data=list_items)
        self.database.close_connection()