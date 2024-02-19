from pages.base_page import BasePage
from selenium.webdriver.common.by import By

locator_contact = (By.CSS_SELECTOR, '.sbisru-Header__menu-item-1')
locator_button_call = (By.CSS_SELECTOR, '.clientWidget-Button__logo .clientWidget-Button__icon')
locator_download = (By.LINK_TEXT, 'Скачать локальные версии')
class HomePage(BasePage):
    def open(self):
        self.driver.get('https://sbis.ru/')
        self.wait(locator_button_call)
    def click_contact(self):
        self.find(locator_contact).click()
    def click_download(self):
        self.find(locator_download).click()