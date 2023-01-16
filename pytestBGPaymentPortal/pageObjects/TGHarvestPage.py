from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TGHarvest:

    def __init__(self, driver):
        self.driver = driver

    def harvest_page(self):
        self.driver.find_element(By.XPATH, "//div[text()='TG Harvest Payment']").click()

    def harvest_page_next(self):
        self.driver.find_element(By.XPATH, "//button[text()='Next']").click()

    def wait_for_element(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "(//button[text()='View Details'])[1]")))

    def set_filter(self):
        self.driver.find_element(By.XPATH, "(//div[@role='button'])[1]").click();

    def set_unpaid(self):
        self.driver.find_element(By.XPATH, "//li[text()='Unpaid']").click()

    def set_payee(self):
        self.driver.find_element(By.XPATH, "//input[contains(@aria-labelledby,'enhanced-table-checkbox-0')]").click()

    def set_payees(self):
        self.driver.find_element(By.XPATH, "(//input[@aria-label='select all rows'])").click()

    def wait_for_paynow_button(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Pay Now')]")))

    def set_paynow_button(self):
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Pay Now')]").click()

    def wait_for_paynow_confirmation(self):
        wait = WebDriverWait(self.driver, 200)
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[.='Yes']")))

    def set_confirmation_button(self):
        self.driver.find_element(By.XPATH, "//button[.='Yes']").click()

    def payment_success(self):
        try:
            actual_text = self.driver.find_element(By.XPATH, "//div[text()='Payment successfully queued']").text
            expected_text = "Payment successfully queued"
            assert (actual_text == expected_text)
        except NoSuchElementException:
            print("Oppps! payment did not go through.")

    def export_paid(self):
        self.driver.find_element(By.ID, "export-button").click()

    def export_paid_button(self):
        self.driver.find_element(By.XPATH, "//li[text()='Paid/Overpaid']").click()

    def export_unpaid(self):
        self.driver.find_element(By.XPATH, "//li[text()='Unpaid/Partial/Zero Value']").click()

    def export_paid_download(self):
        self.driver.find_element(By.XPATH, "//li[text()='Paid/Overpaid']").is_displayed()
        print("Paid download in progress")

    def export_unpaid_download(self):
        self.driver.find_element(By.XPATH, "//li[text()='Unpaid/Partial/Zero Value']").is_displayed()
        print("Unpaid download in progress")

    def toggle_off(self):
        self.driver.find_element(By.XPATH, '//span[text()="Payment ON"]').click()

    def toggle_off_confirmation(self):
        self.driver.find_element(By.XPATH, "//button[.='Yes']").click()

    def toggle_off_assertion(self):
        actual_text = self.driver.find_element(By.CSS_SELECTOR,
                                               '[class="MuiAlert-message css-1pxa9xg-MuiAlert-message"]').text
        expected_text = "All TG Harvest payments have been halted"
        assert (actual_text == expected_text)
        print(expected_text)
