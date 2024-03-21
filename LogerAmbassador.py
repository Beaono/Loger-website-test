from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class logambassador():
    def test(self):
        baseurl4 = "https://loger-ambassador.onrender.com/"
        driver = webdriver.Chrome()
        driver.get(baseurl4)
        driver.maximize_window()
        driver.implicitly_wait(20)

        '''Apply as an ambassador on Loger'''

        ambapply = driver.find_element(By.XPATH, "//a[@href='/application/']")
        ambapply.click()

        baseurl5 = "https://loger-ambassador.onrender.com/application/apply"
        reg = driver.get(baseurl5)

        '''Personal Information of the 
        loger ambassador applicant'''

        #Applicant's first name
        fname = driver.find_element(By.XPATH, "//input [@name='firstname']")
        fname.send_keys("Byan")
        time.sleep(2)

        #Applicant's last name
        lname = driver.find_element(By.XPATH, "//input [@name='lastname']")
        lname.send_keys("Jams")
        time.sleep(2)

        #Applicant's email
        email = driver.find_element(By.XPATH, "//input [@name='email']")
        email.send_keys("jams@gmail.com")
        time.sleep(2)

        #Applicant's phone number
        phone = driver.find_element(By.XPATH, "//input [@name='phone']")
        phone.send_keys("08056745635")
        time.sleep(2)

        #Applicant's gender
        gen = driver.find_element(By.XPATH, "//select [@id='tomselect-1']")
        driver.execute_script("arguments[0].click();", gen)
        sel = Select(gen)


        sel.select_by_value("Female")         #Selected the female option from the gender dropdown
        print("Gender selected: Female")
        time.sleep(5)

        # sel.select_by_value("Male")
        # print("Gender selected: Male")
        # time.sleep(5)

        '''Marketing Information
        of Loger Ambassadors'''

        #Give a summary of what Loger is all about
        logsum = driver.find_element(By.XPATH, "//textarea [@name='aboutLoger']")
        logsum.send_keys("Lorem Ipsum is simply dummy "
                         "text of the printing and typesetting industry. "
                         "Lorem Ipsum has been the industry's standard dummy text"
                         " ever since the 1500s, when an unknown printer "
                         "took a galley of type and scrambled it to make a "
                         "type specimen book. It has survived not only five centuries, "
                         "but also the leap into electronic typesetting, remaining essentially"
                         " unchanged. It was popularised in the 1960s with the release of"
                         " Letraset sheets containing Lorem Ipsum passages, and more recently "
                         "with desktop publishing software like Aldus PageMaker including versions"
                         " of Lorem Ipsum.")
        time.sleep(2)

        #Why do you want to become a Loger Ambassador?
        amblog = driver.find_element(By.XPATH, "//textarea [@name='logerAmbassador']")
        amblog.send_keys("To assist in searching for the perfect house")
        time.sleep(2)

        #List your marketing skills
        skills = driver.find_element(By.XPATH, "//select [@name='skills']")
        marketingskills = Select(skills)

        skill1 = marketingskills.select_by_visible_text("Creativity")
        print("skill1: Creativity")
        time.sleep(2)
        skill2 = marketingskills.select_by_value("Communication")
        print("skill2: Communication")
        time.sleep(2)
        skill3 = marketingskills.select_by_value("Interpersonal Skills")
        print("skill3: Interpersonal Skills")
        time.sleep(2)

        #Give a brief outline of how you plan to market loger
        marketplan = driver.find_element(By.XPATH, "//textarea [@name='marketPlan']")
        marketplan.send_keys("Liase with marketing agencies")
        time.sleep(2)

        #What are the strategies or channels you intend to use to market loger
        marketstrat = driver.find_element(By.XPATH, "//textarea [@name='marketStrategy']")
        marketstrat.send_keys("The major platforms that will be used are: Tiktok, Instagram, and face-to-face")
        time.sleep(2)

        #State of Coverage
        states = driver.find_element(By.XPATH, "//div [@id='tomselect-3-ts-dropdown']")
        state = driver.find_element(By.XPATH, "//div [@data-value='Lagos']")
        state.click()
        print("selected state:" + str(state))
        time.sleep(5)

        covarea = driver.find_element(By.XPATH, "//select[@name='coverageArea']")
        area = Select(covarea)

        area1 = area.select_by_value("Badagry West")
        print("area selected:" + str(area1))
        time.sleep(25)

        submitA = driver.find_element(By.XPATH, "//button[@type='submit']")
        submitA.click()
        time.sleep(5)


loga = logambassador()
loga.test()



