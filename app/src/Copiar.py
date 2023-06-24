import csv
import boto3

def download_file_from_s3_client(bucket_name, key, destination_path):
    s3_client = boto3.client('s3_client')
    s3_client.download_file(bucket_name, key, destination_path)

def process_file(file_path):
    # Tratar o arquivo para remover as aspas duplas
    with open(file_path, 'r', encoding="utf-8") as file:
        reader = csv.reader(file)
        data = [row for row in reader]

    with open(file_path, 'w', encoding="utf-8", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def upload_file_to_s3_client(bucket_name, key, file_path):
    s3_client = boto3.client('s3_client')
    s3_client.upload_file(file_path, bucket_name, key)

# Defina as informações dos buckets e dos arquivos
bucket_origem = 'dados'
key_origem = 'tb_001/arquivo.csv'
bucket_destino = 'bucket-sor'
key_destino = 'arquivo_tratado.csv'

# Define o caminho de destino na pasta /tmp do Lambda
caminho_destino = '/tmp/arquivo.csv'

# Faz o download do arquivo do bucket de origem
download_file_from_s3_client(bucket_origem, key_origem, caminho_destino)

# Trata o arquivo removendo as aspas duplas
process_file(caminho_destino)

# Salva o arquivo tratado no bucket de destino
upload_file_to_s3_client(bucket_destino, key_destino, caminho_destino)
