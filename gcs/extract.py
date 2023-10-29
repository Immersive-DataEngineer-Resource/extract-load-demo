from google.cloud import storage


def read_from_gcs(bucket_name, blob_name):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    return blob.download_as_text()


bucket_name = 'your-bucket-name'
blob_name = 'your-blob-name'
data = read_from_gcs(bucket_name, blob_name)
