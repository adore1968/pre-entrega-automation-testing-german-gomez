from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_url(driver, url):
  wait = WebDriverWait(driver, 10)
  wait.until(EC.url_contains(url))