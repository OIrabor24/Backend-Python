from storages.backends.s3boto3 import S3Boto3Storage

class PrivateMediaStorage(S3Boto3Storage): 
    """This class allows us to customize our s3 default file storage bucket policy"""
    custom_domain = False 