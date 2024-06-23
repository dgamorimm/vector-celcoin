from selenium.webdriver.common.by import By

class TagId:
    
    def __init__(self) -> None:
        self.username = (By.ID, 'accountId')
        self.password = (By.ID, 'password')
        
class TagClass:
    def __init__(self) -> None:
        
        self.login_entry = (By.CLASS_NAME, 'btn-load__text')

class TagName:
    def __init__(self) -> None:
        
        self.username = (By.NAME, 'username')
        self.password = (By.NAME, 'password')