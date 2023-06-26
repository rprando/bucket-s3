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
