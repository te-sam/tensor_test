from pages.base_page import BasePage
from selenium.webdriver.common.by import By

locator_logo = (By.CSS_SELECTOR, '.sbisru-Contacts__border-left--border-xm .sbisru-Contacts__logo-tensor img')
locator_partners = (By.CSS_SELECTOR, '.sbis_ru-Region-Chooser.ml-16')
class ContactPage(BasePage):
    def click_logo(self):
        self.wait(locator_logo)
        self.find(locator_logo).click()
    @property
    def region(self):
        return self.find(locator_partners)
    def region_check(self, region):
        self.wait(locator_logo)
        return self.region.text == region
    def region_click(self):
        self.region.click()
    @property
    def partners_list(self):
        return self.find((By.NAME, 'itemsContainer'))
    def partners_list_is_displayed(self):
        return self.partners_list.is_displayed()
    def check_partners_city(self, city):
         return self.find((By.ID, 'city-id-2')).text == city
    def region_specific_click(self, region):
        locator = (By.CSS_SELECTOR, f'[title="{region}"]')
        self.wait(locator)
        self.find(locator).click()
    def region_in_url(self, region):
        return region in self.driver.current_url
    def region_in_title(self, region):
        return region in self.driver.title



