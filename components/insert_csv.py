import csv
import datetime
from datetime import datetime


class CsvFiles:

    def csv_creator(self, list_product):
        current_date = (datetime.now()).strftime("%d_%m_%y")
        current_time = (datetime.now()).strftime("%H_%M")

        file_name = f"files\\frubana_precos_data_{current_date}_hora_{current_time}.csv"
        with open(file_name, "w", newline="") as csv_file:
            csv_pages = csv.writer(csv_file, delimiter=",")
            for item in list_product:
                    csv_pages.writerow(item)
