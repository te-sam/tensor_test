from pages.home_page import HomePage
from pages.download_page import DownloadPage
from pages.local_page import LocalPage
import allure


@allure.feature('Третий сценарий')
def test_three_sbis(driver):
    home = HomePage(driver)
    with allure.step('Открыть главную страницу'):
        home.open()

    with allure.step('Проскроллить до Footer'):
        home.scroll_to_element('.sbisru-Footer__btn-feedback-wrap')
    with allure.step('Кликнуть Скачать локальные версии'):
        home.click_download()

    download = DownloadPage(driver)
    with allure.step('Кликнуть Сбис Плагин'):
        download.plugin_click()

    local = LocalPage(driver)
    with allure.step('Скачать плагин'):
        local.download_exe()
    with allure.step('Проверка, что плагин скачался'):
        assert local.check_file()
    with allure.step('Проверка на соответствие размера файла'):
        assert local.get_initial_size() == local.get_result_size()

