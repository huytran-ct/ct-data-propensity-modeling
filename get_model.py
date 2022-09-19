from  datetime import datetime, timedelta

from data_lake import cloud_storage


def get_model(bucket_name, source_blob_name, model_name):
    gcloud_storage = cloud_storage.CloudStorage(bucket_name=bucket_name)
    return gcloud_storage.download_blob(source_blob_name=source_blob_name, model_name=model_name)