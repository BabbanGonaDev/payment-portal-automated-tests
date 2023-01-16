from selenium.webdriver.common.by import By


class BGPaymentLogin:

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element(By.ID, "outlined-basic").send_keys("akinola.oladapo")

    def set_password(self, password):
        self.driver.find_element(By.ID, "outlined-adornment-password").send_keys("password")

    def click_login(self):
        self.driver.find_element(By.CLASS_NAME, "sc-bcXHqe").click()

    def set_displayed(self):
        self.driver.find_element(By.XPATH, "//div[text()='TG Harvest Payment']").is_displayed()
        print("Logged in!")
