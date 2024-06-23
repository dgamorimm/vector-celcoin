from utils.logger import logger

import pandas as pd
import os

logger = logger()

def __read_file() -> pd.DataFrame:
    """Função para ler o arquivo de entrada"""
    folder = os.path.join(os.getcwd(),'data', 'input')

    # Listar todos os arquivos na pasta
    files = os.listdir(folder)

    # Filtrar apenas os arquivos CSV
    csv_files = [file for file in files if file.endswith('.csv')]

    for file in csv_files:
        try:
            df = pd.read_csv(os.path.join(folder, file), sep=';', dtype=str)
            logger.success(f"O arquivo {file} foi lido com sucesso.")
            return df
        except pd.errors.EmptyDataError:
            logger.error(f"O arquivo {file} está vazio e foi ignorado.")
            raise pd.errors.EmptyDataError(f"O arquivo {file} está vazio e foi ignorado.")
        except pd.errors.ParserError:
            logger.error(f"O arquivo {file} não pôde ser analisado e foi ignorado.")
            raise pd.errors.ParserError(f"O arquivo {file} não pôde ser analisado e foi ignorado.")
        except Exception as error:
            logger.error(f"Ocorreu um erro ao ler o arquivo {file}: {error}")
            raise Exception(f"Ocorreu um erro ao ler o arquivo {file}: {error}")

def __transform_lpad_documents(row: str) -> str:
    if row['Tipo Conta'] == 'PF':
        return row['CPF/CNPJ'].zfill(11)
    else:
        return row['CPF/CNPJ'].zfill(14)
        
def __transform_documents(df : pd.DataFrame) -> pd.DataFrame:
    if df is not None:
        df['CPF/CNPJ'] = df.apply(__transform_lpad_documents, axis=1)
    return df

def get_inputs() -> list[pd.DataFrame , list[str]]:
    try:
        df = __read_file()
        df = __transform_documents(df)
        return df, df['CPF/CNPJ'].tolist()
    except Exception as error:
        logger.error(f"Ocorreu um erro ao ler os arquivos: {error}")
        raise Exception(f"Ocorreu um erro ao ler os arquivos: {error}")