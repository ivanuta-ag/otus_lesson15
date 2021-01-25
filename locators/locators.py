from selenium.webdriver.common.by import By


class CommonPageLocators():
    CART = (By.XPATH, '//*[@id= "cart"]')
    INPUT_PASSWORD = (By.XPATH, '//*[@id = "input-password"]')


class MainPageLocators:
    HEART = (By.XPATH, '//*[@class = "fa fa-heart"]')
    LOGO = (By.XPATH, '//*[@id = "logo"]')
    NAVBAR_1 = (By.XPATH, '//*[@class = "nav navbar-nav"]/li')
    NAVBAR_2 = (By.XPATH, '//*[@class = "collapse navbar-collapse navbar-ex1-collapse"]')
