from django.db import models
from s3direct.fields import S3DirectField

from example_app.s3_files import get_object_key_from_url, get_presigned_url

class Example(models.Model):
    image = S3DirectField(dest='example_destination')

    @property
    def presigned_image(self):
        return get_presigned_url(get_object_key_from_url(self.image))
