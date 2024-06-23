from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located, \
visibility_of_element_located, alert_is_present
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep
from utils.logger import logger
from selenium import webdriver

logger = logger()

class Action():
    
    def __init__(self, driver : webdriver.Chrome) -> None:
        self.driver = driver
    
    def element_exists(self, tag : object, timeout : int = 10) -> bool:
        try:
            _ = WebDriverWait(self.driver, timeout).until(presence_of_element_located(tag))
            logger.info('Element exists')
            return True
        except:
            logger.warning('Element not exists')
            return False
    
    def find(self, *locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(presence_of_element_located(*locator))

    def find_reduce(self, *locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(presence_of_element_located(*locator))

    def find_v(self, *locator, timeout=2):
        return WebDriverWait(self.driver, timeout).until(visibility_of_element_located(*locator))
    
    def access_page(self, url : str, load_time : int):
        driver = self.driver
        driver.get(url)
        sleep(load_time)
    
    def close_page(self):
        driver = self.driver
        driver.quit()
    
    def text_clear(self, text_tag):
        self.find(text_tag).clear()
        
    def text_input(self,text_tag, text:str, mode:str ='fast'):
        if mode == 'fast':
            driver = self.driver
            element = self.find(text_tag)
            driver.execute_script("arguments[0].value = arguments[1];", element, text)
        else:
            self.find(text_tag).send_keys(text)
        
    def login(self,
                     username_tag : str,
                     password_tag : str,
                     login_tag : str,
                     username : str,
                     password : str):
        self.find(username_tag).clear()
        self.find(username_tag).send_keys(username)
        sleep(2)
        self.find(password_tag).send_keys(password)
        # self.find(password_tag).send_keys(Keys.ENTER)
        self.click(login_tag, 2)
        sleep(10)

    def frame_switch_id(self, id):
        driver = self.driver
        driver.switch_to.frame(driver.find_element_by_id(id))

    def frame_switch_name(self, name):
        driver = self.driver
        driver.switch_to.frame(driver.find_element_by_name(name))
    
    def frame_switch_xpath(self, xpath):
        driver = self.driver
        driver.switch_to.frame(driver.find_element_by_xpath(xpath))
    
    def click(self,
                        click_tag : str,
                        qty_attempts: int = 5, 
                        attempts : int = 0):
        try:
            self.find(click_tag).click()
            sleep(2)
        except Exception as x:
            print(x)
            sleep(5)
            attempts =+ 1
            if attempts <= qty_attempts:
                return self.click(click_tag=click_tag, attempts=attempts)
            else:
                raise('Não foi possivel clicar no elemento')
            
    def select(self, select_tag, value_tag,  mode: str = 'value'):
        select = Select(self.find((select_tag)))
        if mode == 'value':
            select.select_by_value(value_tag)
        else:
            select.select_by_visible_text(value_tag.strip())
    
    def alert_accept(self, timeout=10):
        alert = WebDriverWait(self.driver, timeout).until(alert_is_present(),
                                    'Tempo limite esgotado aguardando o pop-up de alerta aparecer.')
        alert.accept()
    
    def get_content(self, tag_text):
        return self.find(tag_text).text