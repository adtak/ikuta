import boto3
import os


class ImageStorage(object):
    def __init__(self) -> None:
        self.s3 = boto3.resource("s3")
        self.bucket_name = os.environ["AWS_S3_BUCKET"]

    def push_images(self):
        file_name = "./result/000001.jpg"
        key = "000001.jpg"
        self.s3.meta.client.upload_file(file_name, self.bucket_name, key)


if __name__ == "__main__":
    ImageStorage().push_images()
