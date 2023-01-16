from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BGLogout:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_logout(self):
        wait = WebDriverWait(self.driver, 200)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "(//button[text()='View Details'])[1]")))

    def set_logout(self):
        self.driver.find_element(By.XPATH, "//button[text()='LOG OUT']").click()

    def logout_assertion(self):
        self.driver.find_element(By.ID, "outlined-adornment-password").is_displayed()
        print("You are logged out")
