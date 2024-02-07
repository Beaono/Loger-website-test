from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
class logerweb():
    def test(self):
        baseUrl = "https://loger-site.onrender.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(60)
        driver.execute_script("window.scrollBy(0, 2000);")



        # The Loger About us nav bar
        aboutUs = driver.find_element(By.XPATH, "//a[@class ='dropdown-toggle nav-link'] ")
        if aboutUs is not None:
            print("Attribute found by => XPath")
            time.sleep(5)

        # Select About Loger Note:
        aboutLoger = driver.find_element(By.XPATH, "//a [contains(@href, '/about-us') and contains(text(), 'About Loger')]")
        driver.execute_script("arguments[0].click();", aboutLoger)
        time.sleep(5)


        # Select Our Team
        ourTeam = driver.find_element(By.XPATH, "//a [contains(@href, '/team') and contains(text(), 'Our Team')]" )
        driver.execute_script("arguments[0].click();", ourTeam)
        time.sleep(5)


        # Select FAQ
        faq = driver.find_element(By.XPATH, "//a [contains(@href, '/faq') and contains(text(), 'FAQ')]")
        driver.execute_script("arguments[0].click();", faq)
        time.sleep(5)


        # Select Loger Users
        logusers = driver.find_element(By.XPATH, "//a [@href='/loger-user']")
        logusers.click()
        time.sleep(5)

        # Select Loger Agents
        logagents = driver.find_element(By.XPATH, "//a [@href='/loger-agent']")
        logagents.click()
        time.sleep(5)


        # Select Contact and fill the form and also accept the terms and privacy and then click on the submit button.
        logcontact = driver.find_element(By.XPATH, "//a [@href='/contact']")
        logcontact.click()

        sendName = driver.find_element(By.XPATH, "//input [@name='name']")
        sendName.send_keys("Kingdom")

        sendEmail = driver.find_element(By.XPATH, "//input [@name='email']")
        sendEmail.send_keys("ehitta.o@gmail.com")

        mailSub = driver.find_element(By.XPATH, "//input [@name='msg_subject']")
        mailSub.send_keys("Enquiries")

        sendPhone = driver.find_element(By.XPATH, "//input [@name='phone_number']")
        sendPhone.send_keys("07064461958")

        sendM = driver.find_element(By.XPATH, "//textarea [@name='message']")
        sendM.send_keys("Hello Loger Team! How can I download the app to start using it? Really looks like an interesting app")

        checkbox = driver.find_element(By.XPATH, "//input [@id='checkme']")
        driver.execute_script("arguments[0].click();", checkbox)
        time.sleep(10)

        """This bug will be fixed once the platform is moved to the production server"""
        # clickSend = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[4]/div/div[2]/div/div/form/div/div[7]/button")
        # clickSend.click()        #comment 1: This is not working as expected
        # time.sleep(10)



low = logerweb()
low.test()
