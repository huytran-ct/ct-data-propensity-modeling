import os, json
import sys

from google.cloud import storage


class CloudStorage():
    def __init__(self, bucket_name):
        self.storage_client = storage.Client(project="chotot-dwh")
        self.bucket_name = bucket_name

    def download_blob(self, source_blob_name, model_name):
        bucket = self.storage_client.bucket(self.bucket_name)

        blobs = list(bucket.list_blobs(prefix=source_blob_name))
        if blobs == [] or blobs is None:
            return False
        blobs.sort(key=lambda x: x.name, reverse=True)
        model_blobs = [blob for blob in blobs if blob.name.endswith(model_name)]
        blob = model_blobs[0]
        return blob.download_as_string()
