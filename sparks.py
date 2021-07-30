from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from webdriver-manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.thesparksfoundationsingapore.org/")