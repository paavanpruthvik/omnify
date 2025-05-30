from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PIM:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def navigate_to_pim(self):
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='oxd-layout-navigation']//li[2]")))
        ActionChains(self.driver).move_to_element(element).click().perform()

    def add_employee(self, first_name, last_name, emp_id):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Add Employee']"))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='First Name']"))).send_keys(first_name)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys(last_name)
        self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "oxd-form-loader")))
        id_input = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")))
        self.driver.execute_script("arguments[0].focus(); arguments[0].click();", id_input)
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()
        id_input.send_keys(emp_id)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()
        self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "oxd-form-loader")))
        save_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@type='submit'][normalize-space()='Save'])[1]")))
        save_btn.click()
        self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "oxd-form-loader")))
