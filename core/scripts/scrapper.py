from time import sleep
from core.scripts.web.driver import Driver
from core.scripts.web.tools import Action
from core.scripts.web.elements import TagClass, TagId, TagCss
from dotenv import load_dotenv
from tqdm import tqdm
import pandas as pd
import os

load_dotenv()


class Scrapper:
    def __init__(self, driver : Driver):
        self.__driver = driver
        self.__action = Action(driver)
        self.__tag_id, self.__tag_class, self.__tag_css = TagId(), TagClass(), TagCss()
        
    def __access_report(self):
        self.__action.access_page(
            url=os.getenv('URL_REPORT', None),
            load_time=7
        )
    
    def __click_filter_document(self):
        self.__action.click(self.__tag_css.filter_docs)
        
    def __search_document(self, document: str):
        self.__action.text_clear(self.__tag_id.search_document)
        self.__action.text_input(self.__tag_id.search_document, document, 'lazy')
        self.__action.click(self.__tag_css.search_button)
        
    def __get_text(self):
        self.__action.click(self.__tag_css.icon_expander_text)
        return self.__action.get_content(self.__tag_css.text_content)
    
    def __save_dataframe(self, df: pd.DataFrame, df_output: pd.DataFrame):
        df_merge = pd.merge(df,
                            df_output,
                            left_on='CPF/CNPJ',
                            right_on='document',
                            how='left')
        
        return df_merge
        
    def execute(self, documents: list[str], df : pd.DataFrame) -> pd.DataFrame:
        self.__access_report()
        df_output = {'document': [], 'text': []}
        for document in tqdm(documents):
            self.__click_filter_document()
            self.__search_document(document)
            text = self.__get_text()
            
            df_output['document'].append(document)
            df_output['text'].append(text)
        
        return self.__save_dataframe(df, df_output)