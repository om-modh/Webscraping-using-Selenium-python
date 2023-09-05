from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def open_geogames():    
    try:
        # Connect
        FirefoxOptions = webdriver.FirefoxOptions()
        browser = webdriver.Firefox(options=FirefoxOptions)
        browser.get("http://www.geonames.org/")
        browser.find_element(By.NAME, 'q').send_keys('Vatican City', Keys.TAB, Keys.TAB, Keys.ENTER)
        # city_name = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//table/tbody/tr[3]/td[2]/a[1]')))
        # print(city_name.text)
        

        # city_name = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/table/tbody/tr[52]/td[2]/a[1]')))
        # latitude = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/table/tbody/tr[52]/td[5]')))
        # longitude = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/table/tbody/tr[52]/td[6]')))
        # print(city_name.text, "\t", latitude.text, "\t", longitude.text)
        
        time.sleep(2)
        with open('data.csv', 'w', encoding='utf-8') as f:
            data = "City Name" + "," + "City link" + "," + "Latitude" + "," + "Longitude" + "\n"
            f.write(data)
            while True:
                flag = False
                city_names = WebDriverWait(browser, 15).until(EC.visibility_of_all_elements_located((By.XPATH,'//table/tbody/tr/td[2]/a[1]')))
                latitudes = WebDriverWait(browser,10).until(EC.visibility_of_all_elements_located((By.XPATH, '//table/tbody/tr/td[5]')))
                longitudes = WebDriverWait(browser,10).until(EC.visibility_of_all_elements_located((By.XPATH, '//table/tbody/tr/td[6]')))
                print(len(city_names), len(latitudes), len(longitudes))
                clicks = browser.find_elements(By.XPATH, '//div[1]/a')
                for city_name, latitude, longitude in zip(city_names, latitudes, longitudes):
                    data = city_name.text + "," + city_name.get_attribute('href') + "," +  latitude.text + "," + longitude.text + "\n"
                    f.write(data)
                
                for click in clicks:
                    print(click.text)
                    if click.text=="next >":
                        flag = True
                        print("yes")           
                        click.click()

                if flag == False:
                    break

    except Exception as e:
        print (e, 'Geonames')
        
    browser.close()


open_geogames()
