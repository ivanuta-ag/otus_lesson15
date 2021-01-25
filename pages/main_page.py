from .base import BasePage
from locators.locators import MainPageLocators
from selenium.common.exceptions import TimeoutException
import logging
import allure


class MainPage(BasePage):

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.driver = driver
        self.logger = logging.getLogger(type(self).__name__)

    @allure.step('Wait for download "MainPageLocators.HEART"')
    def wait_for_download(self):
        self.logger.info("Find element {}".format(MainPageLocators.HEART))
        try:
            self.find_element(locator=MainPageLocators.HEART)
        except TimeoutException:
            print('Страница не загружена')

    @allure.step('Check wish list')
    def check_wish_list(self):
        self.logger.info("Check element {}".format(MainPageLocators.HEART))
        assert self.find_element(locator=MainPageLocators.HEART), 'Отсутствует wish list'

    @allure.step('Check len_menu_items')
    def check_len_menu_items(self):
        self.logger.info("Check len_menu_items {}".format(MainPageLocators.HEART))
        len_menu_items = len(self.find_elements(locator=MainPageLocators.NAVBAR_1))
        assert len_menu_items == 8, 'Неверное количество элементов меню'

    @allure.step('Check navbar')
    def navbar(self):
        self.logger.info("Check if element {} is present".format(MainPageLocators.HEART))
        assert self.is_element_present(*MainPageLocators.NAVBAR_2), 'Отсутствует navbar'

    @allure.step('Check logo')
    def check_logo(self):
        self.logger.info("Check if element {} is present".format(MainPageLocators.HEART))
        assert self.is_element_present(*MainPageLocators.LOGO), 'Отсутствует logo'
