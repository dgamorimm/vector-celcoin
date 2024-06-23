from selenium import webdriver
import undetected_chromedriver as uc

class Driver:
    def __init__(self):
        pass
    
    def _get_driver(self):
        driver = uc.Chrome()
        return driver

    def _options(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--flag-switches-begin")
        options.add_argument("--flag-switches-end")
        options.add_argument("--origin-trial-disabled-features=WebGPU")
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('start-maximized')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument(f'--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36')
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
        driver = self._get_driver()
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})") 
        return driver