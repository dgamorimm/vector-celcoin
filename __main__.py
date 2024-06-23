from core.scripts.web.driver import Driver
from core.scripts.input import get_inputs
from core.scripts.login import login
import os

if __name__ == '__main__':
    df, doc_list = get_inputs()
    
    driver = Driver().get()
    login(driver)