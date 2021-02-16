from selenium import webdriver
from time import sleep


class GetProductsFrubana:
    list_items = list()

    def __init__(self):
        self.driver = webdriver.Chrome()


    def load_page(self):
        self.driver.get("https://br.frubana.com/spo")
        self.driver.find_element_by_xpath('/html/body/div[7]/div/div[1]/div[4]/div[1]/div/div/div/div[1]/div/a').click()
        sleep(2)

    def scroll_page(self):
        SCROLL_PAUSE_TIME = 1

        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                list_products = self.get_products()
                break
            last_height = new_height
        return list_products

    def get_products(self):
        items = self.driver.find_elements_by_class_name("product-info")
#        return ((item.text).split("\n") for item in items)

        for num, item in enumerate(items, start=1):
            text_item = (item.text).split("\n")
            self.list_items.append(text_item)
#           print(f'Produto: {num} - {product} - Preço:  {price} - Unidade: + {unidade}')
        return self.list_items

    def close_page(self):
        self.driver.close()
