from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.thesparksfoundationsingapore.org/")

#checking the existance of logo

logo = driver.find_element_by_xpath("//*[@id='home']/div/div[1]/h1/a/img")

if logo:
    print("Logo Exists\n\n")

else :
    print("Logo doesn't exists") 

#checking the copyright

copy = driver.find_element_by_link_text("W3layouts")
driver.find_element_by_link_text("W3layouts")

if copy:
   print("Copyright is present\n\n")

else : 
   print("Copyright absent")

#checking connect

more = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[2]/div[2]/i")
driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[2]/div[2]/i")

if more:
   print("Connect option is working properly\n\n")

else:
   print("Not working")

# checking About Us section

about_us = driver.find_element_by_xpath("//*[@id='link-effect-3']/ul/li[1]/a")

driver.find_element_by_xpath("//*[@id='link-effect-3']/ul/li[1]/a").click()

if about_us:
    print("About Us section is working properly\n\n")

else:
    print("About Us section is not working")

#checking the working of Policies and Code

policies_code = driver.find_element_by_xpath("//*[@id='link-effect-3']/ul/li[2]/a")

driver.find_element_by_xpath("//*[@id='link-effect-3']/ul/li[2]/a").click()

if policies_code :
    print("Policies and Code section is working properly\n\n")

else:
    print("Policies and Code is not working")

#checking the working of Programs section

programs = driver.find_element_by_xpath("//*[@id='link-effect-3']/ul/li[3]/a")

driver.find_element_by_xpath("//*[@id='link-effect-3']/ul/li[3]/a").click()

if programs :
   print("Programs section is working properly\n\n")

else:
   print("Programs is not working")

#checking the working of links section

links = driver.find_element_by_xpath("//*[@id='link-effect-3']/ul/li[4]/a")

driver.find_element_by_xpath("//*[@id='link-effect-3']/ul/li[4]/a").click()

if links :
   print("Links section is working properly\n\n")

else:
   print("Links is not working")

#checking the working of Join Us section

join_us = driver.find_element_by_xpath("//*[@id='link-effect-3']/ul/li[5]/a")

driver.find_element_by_xpath("//*[@id='link-effect-3']/ul/li[5]/a").click()

if join_us :
   print("Join Us section is working properly\n\n")

else:
   print("Join Us is not working")

#checking the working of Contact Us section

contact_us = driver.find_element_by_xpath("//*[@id='link-effect-3']/ul/li[6]/a")

driver.find_element_by_xpath("//*[@id='link-effect-3']/ul/li[6]/a").click()

if contact_us :
   print("Contact Us section is working properly\n\n")

else:
   print("Contact Us is not working")

#Checking the spelling 

spell = driver.find_element_by_css_selector("h1")
sp = spell.text

print(sp)
print("\n\n")

if spell :
   print("Tagline is present \n\n ")

else:

   print("No tagline")




driver.close()



