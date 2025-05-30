from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Employees:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def verify_employee(self, emp_id, first_name):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Employee List']"))).click()
        input_field = self.wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")))
        input_field.clear()
        input_field.send_keys(emp_id)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Search']").click()
        time.sleep(2)
        try:
            result_name = self.driver.find_element(By.XPATH, "//div[@class='oxd-table-card']//div[3]").text
            return first_name in result_name
        except:
            return False
