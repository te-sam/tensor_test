from pages.base_page import BasePage
from selenium.webdriver.common.by import By

locator_img = (By.CSS_SELECTOR, '.tensor_ru-About__block3 .s-Grid-container img')

class AboutPage(BasePage):
    def same_size(self):
        images = self.finds(locator_img)
        for image in images:
            print(image.size)
            assert image.size == images[0].size