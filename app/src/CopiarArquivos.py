import csv
import boto3


def download_file_from_s3_client(bucket_name, key, destination_path):
    s3_client = boto3.client('s3')
    s3_client.download_file(bucket_name, key, destination_path)


def process_file(file_path):
    data = []

    with open(file_path, 'r', encoding="utf-8") as arquivo_csv:
        reader = csv.reader(arquivo_csv, delimiter=';')
        for row in reader:
            linhas_tratadas = []
            for item in row:
                item_tratado = item \
                    .replace("\n", " ").strip() \
                    .replace('"', '')
                linhas_tratadas.append(item_tratado)
            data.append(linhas_tratadas)

    arquivo_tratado = 'app/tests/arquivos_tratados/dados_tratados.csv'
    with open(arquivo_tratado, 'w', encoding="utf-8", newline='') as arquivo_csv:
        writer = csv.writer(arquivo_csv, delimiter='|')
        writer.writerows(data)


def upload_file_to_s3_client(bucket_name, key, file_path):
    s3_client = boto3.client('s3')
    s3_client.upload_file(file_path, bucket_name, key)

# # Defina as informações dos buckets e dos arquivos
# bucket_origem = 'dados'
# key_origem = 'tb_001/arquivo.csv'
# bucket_destino = 'bucket-sor'
# key_destino = 'arquivo_tratado.csv'

# # Define o caminho de destino na pasta /tmp do Lambda
# caminho_destino = '/tmp/arquivo.csv'

# # Faz o download do arquivo do bucket de origem
# download_file_from_s3_client(bucket_origem, key_origem, caminho_destino)

# # Trata o arquivo removendo as aspas duplas
# process_file(caminho_destino)

# # Salva o arquivo tratado no bucket de destino
# upload_file_to_s3_client(bucket_destino, key_destino, caminho_destino)
