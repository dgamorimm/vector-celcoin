from datetime import datetime
import os
import pandas as pd

def save_dataframe(df : pd.DataFrame):
    """Função para escrever o arquivo na saida"""
    folder = os.path.join(os.getcwd(),'data', 'output')
    datetime_str = datetime.now().strftime('%d_%m_%Y_%H_%M_%S')
    df.to_excel(os.path.join(folder, f'output_{datetime_str}.xlsx'), index=False, header=True)