from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent

class Driver:
    def __init__(self):
        self.ua = UserAgent()
    
    def _get_driver(self, options : webdriver.ChromeOptions):
        driver = webdriver.Chrome(options=options)
        return driver

    def _options(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--flag-switches-begin")
        options.add_argument("--flag-switches-end")
        options.add_argument("--origin-trial-disabled-features=WebGPU")
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('start-maximized')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument(f'--user-agent={self.ua.random}')
        options.add_argument('--disable-notifications')
        options.add_argument('--no-sandbox')
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-gpu")
        options.add_argument("--ignore-certificate-errors")
        # options.add_argument('--blink-settings=imagesEnabled=false')
        options.add_experimental_option('useAutomationExtension', False)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        return options
    
    def get(self):
        driver = self._get_driver(options=self._options())
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})") 
        return driver