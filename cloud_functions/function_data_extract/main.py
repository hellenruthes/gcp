import functions_framework
from google.cloud import storage
import requests


bucket_name = 'dataeng-bronze'
folder_name = 'world_bank'
file_name = 'example.json'



def save_data(json_file):
    storage_client = storage.Client.from_service_account_json('/Users/hellenruthes/dev/gcp/credentials.json')
    # Define the destination blob (file) in GCS
    destination_blob_name = f'{folder_name}/{file_name}'

    # Create a bucket object
    bucket = storage_client.bucket(bucket_name)

    # Define the blob object
    blob = bucket.blob(destination_blob_name)

    # Upload the CSV data to the blob
    blob.upload_from_string(json_file)


@functions_framework.http
def download_data():

    url = 'http://api.worldbank.org/v2/countries/br;cn;us;de/indicators/SP.POP.TOTL/?format=json&per_page=1000'
    r = requests.get(url)
    json_file = r.text
    save_data(json_file)


#if __name__ == '__main__':
   #download_data()
