from google.cloud import storage


def write_to_gcs(bucket_name, blob_name, data):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_string(data)


bucket_name = 'your-bucket-name'
blob_name = 'your-blob-name'
write_to_gcs(bucket_name, blob_name, 'some-data')
