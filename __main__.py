from core.scripts.web.driver import Driver
from core.scripts.input import get_inputs
from core.scripts.login import login
from core.scripts.scrapper import Scrapper

if __name__ == '__main__':
    df, documents = get_inputs()
    
    driver = Driver().get()
    login(driver)
    
    scrapper = Scrapper(driver)
    df = scrapper.execute(documents, df)
    
    df.to_excel('output.xlsx', index=False, header=True)