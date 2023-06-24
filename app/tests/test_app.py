# from moto import mock_s3
# import boto3
# from pytest import fixture
from src.CopiarArquivos import download_file_from_s3_client, process_file, upload_file_to_s3_client

BUCKET_ORIGEM = 'bucket-dados-hub'
KEY_ORIGEM = 'dbo/tb_acao/dados.csv'
BUCKET_DESTINO = 'bucket-dados-sor'
KEY_DESTINO = 'dados-hub/tb_acao/arquivo_tratado.csv'
CAMINHO_DESTINO = 'app/tests/tmp/dados.csv'
ARQUIVO_TRATADO = 'app/tests/arquivos_tratados/dados_tratados.csv'

# @fixture
# def s3_client():
#     s3 = boto3.client("s3", region_name="us-east-1")
#     s3_client.create_bucket(Bucket=BUCKET_ORIGEM)
#     s3_client.create_bucket(Bucket=BUCKET_DESTINO)
#     s3_client.put_object(Bucket=BUCKET_ORIGEM, Key=KEY_ORIGEM, Body='teste')
#     return s3_client

def test_download_file_sucesso():
    download_file_from_s3_client(BUCKET_ORIGEM, KEY_ORIGEM, CAMINHO_DESTINO)
    process_file(CAMINHO_DESTINO)
    upload_file_to_s3_client(BUCKET_DESTINO, KEY_DESTINO, ARQUIVO_TRATADO)

# def test_process_file():
#     # Define o caminho do arquivo de teste
#     file_path = 'test_file.csv'
    
#     # Cria um arquivo de teste com aspas duplas
#     with open(file_path, 'w', encoding="utf-8") as file:
#         file.write('"Hello", "World"\n')

#     # Chama a função a ser testada
#     process_file(file_path)

#     # Lê o arquivo tratado e verifica se as aspas duplas foram removidas
#     with open(file_path, 'r', encoding="utf-8") as file:
#         content = file.read()
#         assert '"' not in content

#     # Remove o arquivo de teste
#     os.remove(file_path)
