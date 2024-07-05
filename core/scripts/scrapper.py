from time import sleep
from core.scripts.web.driver import Driver
from core.scripts.web.tools import Action
from core.scripts.web.elements import TagId, TagCss, TagXPath
from dotenv import load_dotenv
from tqdm import tqdm
from datetime import datetime
import pandas as pd
import os

load_dotenv()


class Scrapper:
    def __init__(self, driver : Driver):
        self.__driver = driver
        self.__action = Action(driver)
        self.__tag_id, self.__tag_css, self.__tag_xpath = TagId(), TagCss(), TagXPath()
        
    def __access_report(self):
        self.__action.access_page(
            url=os.getenv('URL_REPORT', None),
            load_time=7
        )
        
    def __filter_date(self):
        self.__action.click(self.__tag_css.filter_date)
        self.__action.click(self.__tag_id.btn_period)
        self.__action.text_clear(self.__tag_id.input_period)
        start_date = '01/01/2020 00:00 - '
        end_date = datetime.now().strftime('%d/%m/%Y %H:%M')
        period = start_date + end_date
        self.__action.text_input(self.__tag_id.input_period, period, 'lazy')
        self.__action.click(self.__tag_css.btn_apply_period)
        self.__action.click(self.__tag_css.confirm_filter_date)
    
    def __click_filter_document(self):
        self.__action.click(self.__tag_css.filter_docs)
        
    def __search_document(self, document: str):
        try:
            self.__action.text_clear(self.__tag_id.search_document)
            self.__action.text_input(self.__tag_id.search_document, document, 'lazy')
            self.__action.click(self.__tag_css.search_button)
        except:
            pass
        
    def __get_text(self):
        self.__action.click(self.__tag_css.icon_expander_text)
        try:
            kyc_date = self.__action.get_content(self.__tag_xpath.text_datetime)
        except:
            kyc_date = ''
        try:
            kyc_status = self.__action.get_content(self.__tag_xpath.text_status)
        except:
            kyc_status = ''
        try:
            kyc_text = self.__action.get_content(self.__tag_xpath.text_content)
            kyc_text_split = kyc_text.split('\n')
            if len(kyc_text_split) > 0 :
                kyc_content_document = kyc_text_split[-1].split(':')
                kyc_content = kyc_content_document[0].strip()
                kyc_document = kyc_content_document[1].strip()
            else:
                kyc_content = ''
                kyc_document = ''
        except:
            kyc_content = ''
            kyc_document = ''
                
        return kyc_date, kyc_status, kyc_content, kyc_document
    
    def __save_dataframe(self, df: pd.DataFrame, df_output: pd.DataFrame):
        df_merge = pd.merge(df,
                            df_output,
                            left_on='CPF/CNPJ',
                            right_on='document',
                            how='left')
        
        return df_merge
        
    def execute(self, documents: list[str], df : pd.DataFrame) -> pd.DataFrame:
        self.__access_report()
        self.__filter_date()
        output = {'document': [], 'kyc_date' : [] , 'kyc_status' : [], 'kyc_content' : [], 'kyc_document' : []}
        for document in tqdm(documents):
            self.__click_filter_document()
            self.__search_document(document)
            kyc_date, kyc_status, kyc_content, kyc_document = self.__get_text()
            
            print(f'Document → {document}')
            output['document'].append(document)
            output['kyc_date'].append(kyc_date)
            output['kyc_status'].append(kyc_status)
            output['kyc_content'].append(kyc_content)
            output['kyc_document'].append(kyc_document)
        
        df_output  = pd.DataFrame(output)
        return self.__save_dataframe(df, df_output)