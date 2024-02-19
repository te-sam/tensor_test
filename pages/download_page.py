from pages.base_page import BasePage
from selenium.webdriver.common.by import By

locator_left_list = (By.CSS_SELECTOR, '.sbis_ru-VerticalTabs__tabs .controls-TabButton__right-align')
locator_link_exe = (By.PARTIAL_LINK_TEXT, 'Скачать (Exe')

class DownloadPage(BasePage):
    def plugin_click(self):
        self.wait((By.CSS_SELECTOR, '.sbisru-CookieAgreement'))
        self.wait((By.CSS_SELECTOR, '.sbisru-CookieAgreement__message'))
        self.wait(locator_left_list)
        self.finds(locator_left_list)[1].click()
    @property
    def get_link_exe(self):
        return self.find(locator_link_exe).get_attribute('href')
    @property
    def get_text_link_exe(self):
        return self.find(locator_link_exe).text