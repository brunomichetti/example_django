from rest_framework import serializers

from example_app.models import Example


class ExampleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Example
        fields = ('presigned_image',)


class ExampleUploadURLSerializer(serializers.Serializer):
    object_key = serializers.CharField(required=False)
    upload_url_dict = serializers.DictField(required=False)
