from pages.home_page import HomePage
from pages.contact_page import ContactPage
import allure


@allure.feature("Второй сценарий")
def test_two_sbis(driver):
    home = HomePage(driver)
    with allure.step("Открыть главную страницу"):
        home.open()
    with allure.step('Кликнуть на кнопку Контакты'):
        home.click_contact()

    contact = ContactPage(driver)
    with allure.step('Проверка на правильное определение региона'):
        assert contact.region_check('Ярославская обл.')
    partners = contact.partners_list.text
    with allure.step('Проверка на отображение блока с партнерами'):
        assert contact.partners_list_is_displayed() and contact.check_partners_city('Ярославль')
    with allure.step('Кликнуть на регион'):
        contact.region_click()
    with allure.step('Кликнуть на Камчатский край'):
        contact.region_specific_click("Камчатский край")
    with allure.step('Проверить изменение региона на Камчатский край'):
        assert contact.region_check('Камчатский край')
    with allure.step('Проверить, что URL содержит информацию о регионе'):
        assert contact.region_in_url('41-kamchatskij-kraj')
    with allure.step('Проверить, что title содержит информацию о регионе'):
        assert contact.region_in_title('Камчатский край')
    with allure.step('Проверить, что список партнеров изменился'):
        assert contact.partners_list.text != partners
