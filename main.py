from selenium import webdriver
from pages.login import Login
from pages.pim import PIM
from pages.employees import Employees

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

login = Login(driver)
pim = PIM(driver)
employees_page = Employees(driver)

login.login("Admin", "admin123")
pim.navigate_to_pim()

employees = [
    {"first_name": "Vishwas", "last_name": "Ravi", "emp_id": "B2213"},
    {"first_name": "Shreya", "last_name": "Joshi", "emp_id": "B2214"},
    {"first_name": "Megha", "last_name": "Sri", "emp_id": "B2215"},
    {"first_name": "Chethan", "last_name": "Kumar", "emp_id": "B2216"},
]

for emp in employees:
    pim.add_employee(emp["first_name"], emp["last_name"], emp["emp_id"])


for emp in employees:
    if employees_page.verify_employee(emp["emp_id"], emp["first_name"]):
        print("Name Verified")
    else:
        print("Not Found")

driver.quit()
