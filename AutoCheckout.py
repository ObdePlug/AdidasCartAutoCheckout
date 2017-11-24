import json
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
print ('********************************')
print ('********************************')
print ('********************************')
print ('***********CartCopper***********')
print ('**************FOR***************')
print ('********************************')
print ('*************ADIDAS*************')
print ('********************************')
print ('********************************')
print ('********************************')
statenum = 1
ccmonthn = 1
ccyear = 1
confFile = None
orders = []
try:
        confFile = open("checkout.conf")
        orders = json.loads(confFile.read())["orders"]
except Exception as e:
                print('Error: either no checkout.conf was found, Error Details: ' + str(e))
for order in orders:
                Username = input("Enter Username: ")
                Password = input("Enter Password: ")
                states = order['state']
                if states == ('AA Military'):
                        statenum = 2
                if states == ('AE Military'):
                        statenum = 3
                if states == ('AP Military'):
                        statenum = 4
                if states == ('Alabama'):
                        statenum = 5
                if states == ('Alaska'):
                        statenum = 6
                if states == ('Arizona'):
                        statenum = 7
                if states == ('Arkansas'):
                        statenum = 8
                if states == ('California'):
                        statenum = 9
                if states == ('Colorado'):
                        statenum = 10
                if states == ('Connecticut'):
                        statenum = 11
                if states == ('Delaware'):
                        statenum = 12
                if states == ('District of Colombia'):
                        statenum = 13
                if states == ('Florida'):
                        statenum = 14
                if states == ('Georgia'):
                        statenum = 15
                if states == ('Hawaii'):
                        statenum = 16
                if states == ('Idaho'):
                        statenum = 17
                if states == ('Illinois'):
                        statenum = 18
                if states == ('Indiana'):
                        statenum = 19
                if states == ('Iowa'):
                        statenum = 20
                if states == ('Kansas'):
                        statenum = 21
                if states == ('Kentucky'):
                        statenum = 22
                if states == ('Louisiana'):
                        statenum = 23
                if states == ('Maine'):
                        statenum = 24
                if states == ('Maryland'):
                        statenum = 25
                if states == ('Massachusetts'):
                        statenum = 26
                if states == ('Michigan'):
                        statenum = 27
                if states == ('Minnesota'):
                        statenum = 28
                if states == ('Mississippi'):
                        statenum = 29
                if states == ('Missouri'):
                        statenum = 30
                if states == ('Montana'):
                        statenum = 31
                if states == ('Nebraska'):
                        statenum = 32
                if states == ('Nevada'):
                        statenum = 33
                if states == ('New Hampshire'):
                        statenum = 34
                if states == ('New Jersey'):
                        statenum = 35
                if states == ('New Mexico'):
                        statenum = 36
                if states == ('New York'):
                        statenum = 37
                if states == ('North Carolina'):
                        statenum = 38
                if states == ('North Dakota'):
                        statenum = 39
                if states == ('Ohio'):
                        statenum = 40
                if states == ('Oklahoma'):
                        statenum = 41
                if states == ('Oregon'):
                        statenum = 42
                if states == ('Pennsylvania'):
                        statenum = 43
                if states == ('Rhode Island'):
                        statenum = 44
                if states == ('South Carolina'):
                        statenum = 45
                if states == ('South Dakota'):
                        statenum = 46
                if states == ('Tennessee'):
                        statenum = 47
                if states == ('Texas'):
                        statenum = 48
                if states == ('Utah'):
                        statenum = 49
                if states == ('Vermont'):
                        statenum = 50
                if states == ('Virginia'):
                        statenum = 51
                if states == ('Washington'):
                        statenum = 52
                if states == ('West Virginia'):
                        statenum = 53
                if states == ('Wisonsin'):
                        statenum = 54
                if states == ('Wyoming'):
                        statenum = 55
                ccmonths = order['credit_card_expiration_month']
                if ccmonths == ('1'):
                        ccmonth = 2
                if ccmonths == ('2'):
                        ccmonth = 3
                if ccmonths == ('3'):
                        ccmonth = 4
                if ccmonths == ('4'):
                        ccmonth = 5
                if ccmonths == ('5'):
                        ccmonth = 6
                if ccmonths == ('6'):
                        ccmonth = 7
                if ccmonths == ('7'):
                        ccmonth = 8
                if ccmonths == ('8'):
                        ccmonth = 9
                if ccmonths == ('9'):
                        ccmonth = 10
                if ccmonths == ('10'):
                        ccmonth = 11
                if ccmonths == ('11'):
                        ccmonth = 12
                if ccmonths == ('12'):
                        ccmonth = 13
                ccyears = order['credit_card_expiration_year']
                if ccyears == ('2017'):
                        ccyear = 2
                if ccyears == ('2018'):
                        ccyear = 3
                if ccyears == ('2019'):
                        ccyear = 4
                if ccyears == ('2020'):
                        ccyear = 5
                if ccyears == ('2021'):
                        ccyear = 6
                if ccyears == ('2022'):
                        ccyear = 7
                if ccyears == ('2023'):
                        ccyear = 8
                if ccyears == ('2024'):
                        ccyear = 9
                if ccyears == ('2025'):
                        ccyear = 10
                if ccyears == ('2026'):
                        ccyear = 11
                if ccyears == ('2027'):
                        ccyear = 12
                if ccyears == ('2028'):
                        ccyear = 13
                if ccyears == ('2029'):
                        ccyear = 14
                if ccyears == ('2030'):
                        ccyear = 15
                if ccyears == ('2031'):
                        ccyear = 16
                if ccyears == ('2032'):
                        ccyear = 17
                if ccyears == ('2033'):
                        ccyear = 18
                if ccyears == ('2034'):
                        ccyear = 19
                if ccyears == ('2035'):
                        ccyear = 20
                if ccyears == ('2036'):
                        ccyear = 21
                if ccyears == ('2037'):
                        ccyear = 22         
                driver = webdriver.Chrome();
                driver.get('http://www.adidas.com/us/myaccount-create-or-login')
                driver.switch_to.frame("loginaccountframe")
                driver.find_element_by_id("username").send_keys(Username)
                driver.find_element_by_id("password").send_keys(Password)
                driver.find_element_by_id("signinSubmit").click()
                Test = driver.current_url
                if Test == 'https://www.adidas.com/us/myaccount-show?fromlogin=true':
                        print('Logged In')
                        checker = driver.find_element_by_css_selector('.myaccount-your-items-product a').get_attribute('href')
                        print(checker)
                        CheckerTest = input("Does URL Look Like The Shoe You Want? Y or N:")
                        if CheckerTest == 'N' or CheckerTest == 'n':
                                print ('Faulty Cart, Do Not But')
                        if CheckerTest == 'Y' or CheckerTest == 'y':
                                print ('Processing Info...')
                                driver.get('https://www.adidas.com/on/demandware.store/Sites-adidas-US-Site/en_US/COShipping-Show')
                                driver.find_element_by_id("dwfrm_shipping_shiptoaddress_shippingAddress_firstName").send_keys(order['first'])
                                driver.find_element_by_id("dwfrm_shipping_shiptoaddress_shippingAddress_lastName").send_keys(order['last'])
                                driver.find_element_by_id("dwfrm_shipping_shiptoaddress_shippingAddress_address1").send_keys(order['address'])
                                driver.find_element_by_id("dwfrm_shipping_shiptoaddress_shippingAddress_address2").send_keys(order['unit'])
                                driver.find_element_by_id("dwfrm_shipping_shiptoaddress_shippingAddress_city").send_keys(order['city'])
                                driver.find_element_by_id("dwfrm_shipping_shiptoaddress_shippingAddress_postalCode").send_keys(order['zip'])
                                driver.find_element_by_id("dwfrm_shipping_shiptoaddress_shippingAddress_phone").send_keys(order['phone'])
                                driver.find_element_by_xpath('//*[@id="shippingForm"]/div[1]/ng-form/div[1]/div/div[3]/div[6]/div[1]/div[1]').click()
                                time.sleep(1)
                                driver.find_element_by_xpath("//*[@id='shippingForm']/div[1]/ng-form/div[1]/div/div[3]/div[6]/div[1]/div[2]/div[%s]" % statenum).click()
                                driver.find_element_by_xpath('//*[@id="shippingForm"]/div[1]/ng-form/div[5]/div/button').click();
                                time.sleep(1)
                                print ('Processing Info, Almost Done...')
                                driver.find_element_by_id("dwfrm_payment_creditCard_number").send_keys(order['credit_card_number'])
                                driver.find_element_by_xpath('//*[@id="dwfrm_payment"]/fieldset/div/div[4]/div[2]/div/div/div/a').click()
                                time.sleep(4)
                                driver.find_element_by_xpath("//*[@id='dwfrm_payment']/fieldset/div/div[4]/div[2]/div/div/div/div/div[2]/div/ul/li[%(ccmonth)i]" %
                                                             {'ccmonth': ccmonth}).click()
                                driver.find_element_by_xpath('//*[@id="dwfrm_payment"]/fieldset/div/div[4]/div[3]/div[1]/div/div/a').click()
                                time.sleep(4)
                                driver.find_element_by_xpath("//*[@id='dwfrm_payment']/fieldset/div/div[4]/div[3]/div[1]/div/div/div/div[2]/div/ul/li[%(ccyear)i]" %
                                                             {'ccyear': ccyear}).click()
                                driver.find_element_by_id("dwfrm_payment_creditCard_cvn").send_keys(order['credit_card_crn'])
                                driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div[5]/div/button').click()
                                time.sleep(10)
                                print ('Shoe Copped; Check Email')
                if Test != 'https://www.adidas.com/us/myaccount-show?fromlogin=true':
                        print('Incorrect Login')
