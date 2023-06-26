import os
from src.CopiarArquivos import download_file_from_s3_client, process_file, upload_file_to_s3_client

BUCKET_ORIGEM   = 'bucket-dados-hub'
KEY_ORIGEM      = 'dbo/tb_acao/dados.csv'
BUCKET_DESTINO  = 'bucket-dados-sor'
KEY_DESTINO     = 'dados-hub/tb_acao/arquivo_tratado.csv'
CAMINHO_DESTINO = 'app/tests/tmp/dados.csv'
ARQUIVO_TRATADO = 'app/tests/arquivos_tratados/dados_tratados.csv'
ARQUIVOS        = [CAMINHO_DESTINO, ARQUIVO_TRATADO]

def test_download_file_sucesso():
    download_file_from_s3_client(BUCKET_ORIGEM, KEY_ORIGEM, CAMINHO_DESTINO)
    process_file(CAMINHO_DESTINO)
    upload_file_to_s3_client(BUCKET_DESTINO, KEY_DESTINO, ARQUIVO_TRATADO)

    # Remover todos os arquivos
    for arquivo in ARQUIVOS:
        os.remove(arquivo)
