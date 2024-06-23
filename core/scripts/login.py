from core.scripts.web.driver import Driver
from core.scripts.web.tools import Action
from core.scripts.web.elements import TagName, TagClass
from dotenv import load_dotenv
import os

load_dotenv()

def login(driver : Driver):
    action = Action(driver)
    tag_name = TagName()
    tag_class = TagClass()
    
    action.access_page(
        url=os.getenv('URL_LOGIN', None),
        load_time=7
    )
    
    action.login(
        username_tag=tag_name.username,
        password_tag=tag_name.password,
        login_tag=tag_class.login_entry,
        username=os.getenv('CELCOIN_USR', None),
        password=os.getenv('CELCOIN_PWD', None)
    )