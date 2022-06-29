from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request

from example_app.models import Example
from example_app.serializers import ExampleSerializer, ExampleUploadURLSerializer
from example_app.s3_files import get_presigned_url_dict_to_upload_file


class ExampleViewSet(viewsets.ModelViewSet):
    serializer_class = ExampleSerializer
    queryset = Example.objects.all()

    @action(detail=False, methods=('post',), url_path='upload-url')
    def grouped_by_category(self, request: Request) -> Response:
        serializer = ExampleUploadURLSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        object_key = serializer.validated_data['object_key']

        upload_url_dict = get_presigned_url_dict_to_upload_file(object_key)

        return_serializer = ExampleUploadURLSerializer(
            data={'object_key': object_key, 'upload_url_dict': upload_url_dict,}
        )
        return_serializer.is_valid(raise_exception=True)

        return Response(return_serializer.validated_data, status=status.HTTP_200_OK)

