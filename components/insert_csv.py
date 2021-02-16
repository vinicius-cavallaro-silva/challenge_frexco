import csv
import datetime
from datetime import datetime
from components.utils import logger


class CsvFiles:

    def csv_creator(self, list_product:list) -> None:
        """
        It generates a new CSV file named with current's execution date and hour that contains all the 'list_product' data in an organized way._
        :param list_product: list
        :return: none
        """
        current_date = (datetime.now()).strftime("%d_%m_%y")
        current_time = (datetime.now()).strftime("%H_%M")

        file_name = f"files\\frubana_precos_data_{current_date}_hora_{current_time}.csv"
        logger(f'Criando o arquivo: {file_name}')
        with open(file_name, "w", newline="") as csv_file:
            csv_pages = csv.writer(csv_file, delimiter=",")
            for item in list_product:
                    csv_pages.writerow(item)
            logger(f'Foram registrados {len(list_product)} produtos!')