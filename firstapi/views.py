from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# from Validation_messages.api_error_message import FILE_VIEW_ERROR_MSG
# from Validation_messages.api_success_msg import FILE_VIEW_MSG
from Validation_messages import api_success_msg, api_error_message
from firstapi.serializers import FileInputSerializer


@api_view(['POST'])
def file_view(request, version):
    try:
        serializer = FileInputSerializer(data=request.data, )
        if not serializer.is_valid():
            return Response(
                {'message': serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer.save()
        return Response({'message': api_success_msg.FILE_VIEW_MSG}, status=status.HTTP_200_OK)
    except ArithmeticError as ex:
        return Response({'message': api_error_message.FILE_VIEW_ERROR_MSG}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
