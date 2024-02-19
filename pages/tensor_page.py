from pages.base_page import BasePage
from selenium.webdriver.common.by import By

locator_block_strong = (By.CLASS_NAME, 'tensor_ru-Index__block4-content')
locator_about = (By.CLASS_NAME, 'tensor_ru-Index__block4-content .tensor_ru-link')
class TensorPage(BasePage):
    def block_strong_is_displayed(self):
        return self.find(locator_block_strong).is_displayed()
    def click_about(self):
        self.find(locator_about).click()
