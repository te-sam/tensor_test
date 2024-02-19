from pages.home_page import HomePage
from pages.contact_page import ContactPage
from pages.tensor_page import TensorPage
from pages.about_page import AboutPage
import allure


@allure.feature('Первый сценарий')
def test_one(driver):
    home = HomePage(driver)
    with allure.step('Открыть главную страницу'):
        home.open()
    with allure.step('Кликнуть на кнопку Контакты'):
        home.click_contact()

    contact = ContactPage(driver)
    with allure.step('Кликнуть на баннер Тензор'):
        contact.click_logo()

    tensor_page = TensorPage(driver)
    with allure.step('Переключиться на новую вкладку'):
        tensor_page.switch_new_tab()
    with allure.step('Скролл до блока Сильные люди'):
        tensor_page.scroll_to_element('.nl-LastCovers__header_title')
    with allure.step('Проверка на существование блока Сильные люди'):
        assert tensor_page.block_strong_is_displayed()
    with allure.step('Клик на кнопку подробнее'):
        tensor_page.click_about()

    about = AboutPage(driver)
    with allure.step('Проверка URL на вкладке О компании'):
        assert about.true_url('https://tensor.ru/about')
    with allure.step('Скролл до блока с картинками'):
        about.scroll_to_element('.tensor_ru-About__block3')
    with allure.step('Проверка на одинаковый размер картинок'):
        about.same_size()