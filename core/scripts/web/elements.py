from selenium.webdriver.common.by import By


class TagXPath:
    
    def __init__(self) -> None:
        
        self.text_datetime = (By.XPATH, '//*[@id="drawer_push_nav_kyc"]/div[2]/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div/div/div[1]/strong')
        self.text_status = (By.XPATH, '//*[@id="drawer_push_nav_kyc"]/div[2]/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div/div/div[2]/span')
        self.text_content = (By.XPATH, '//*[@id="drawer_push_nav_kyc"]/div[2]/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div')

class TagId:
    
    def __init__(self) -> None:
        self.search_document = (By.ID, 'documento')
        self.btn_period = (By.ID, 'periodo_button')
        self.input_period = (By.ID, 'periodo')
        
class TagClass:
    def __init__(self) -> None:
        
        self.login_entry = (By.CLASS_NAME, 'btn-load__text')

class TagName:
    def __init__(self) -> None:
        
        self.username = (By.NAME, 'username')
        self.password = (By.NAME, 'password')
        
class TagCss:
    def __init__(self) -> None:
        
        self.filter_docs = (By.CSS_SELECTOR, "span[data-target='#seletorMaisFiltros2']")
        self.search_button = (By.CSS_SELECTOR, ".btn.btn-cel_onboarding.btn-sm.btn-block.btnAplicarFiltro3")
        self.icon_expander_text = (By.CSS_SELECTOR, ".fa-solid.fa-magnifying-glass")
        self.text_content = (By.CSS_SELECTOR, ".card-body.fs-8")
        
        self.filter_date = (By.CSS_SELECTOR, ".btn.btn-custom.btn-primary.btn-xs.sm-3.drawer-toggle-link.btn-activate-filter.btn-cel_onboarding")
        self.btn_apply_period = (By.CSS_SELECTOR, ".applyBtn.btn.btn-sm.btn-primary")
        self.confirm_filter_date = (By.CSS_SELECTOR, ".btn.btn-primary.btnAplicarFiltro.btn-block.btn.btn-xs")