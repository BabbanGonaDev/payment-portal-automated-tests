import pytest
import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="class")
def setup(request):
    service_obj = Service("C:/Users/omaye/Downloads/chromedriver/chromedriver.exe");
    driver = webdriver.Chrome(service=service_obj)
    driver.implicitly_wait(15)
    driver.get("http://payments-portal-dev.babbangonaapps.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()