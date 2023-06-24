import os
import boto3
from pytest import fixture
from app.src.Copiar import process_file

@fixture
def s3 ():
    s3 = boto3.client('s3')
    s3.cr
    return s3

def test_process_file():
    # Define o caminho do arquivo de teste
    file_path = 'test_file.csv'
    
    # Cria um arquivo de teste com aspas duplas
    with open(file_path, 'w', encoding="utf-8") as file:
        file.write('"Hello", "World"\n')

    # Chama a função a ser testada
    process_file(file_path)

    # Lê o arquivo tratado e verifica se as aspas duplas foram removidas
    with open(file_path, 'r', encoding="utf-8") as file:
        content = file.read()
        assert '"' not in content

    # Remove o arquivo de teste
    os.remove(file_path)
