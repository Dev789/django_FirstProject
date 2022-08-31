from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from Validation_messages import api_success_msg, api_error_message
from firstapp.models import SystemUser
from firstapp.serializers import InsertUserSerializer, ListUserSerializer
from firstproject.settings import APP_VERSION, ACCEPT_DEVICE_TYPE


def hello_world1(request, lang):
    return HttpResponse('api_success_msg.HELLO_WORLD')


def hello_world(request):
    return HttpResponse(api_success_msg.HELLO_WORLD)


class ApiHelloWorld(APIView):

    @extend_schema(responses=None,
                   tags=['Demo'],
                   parameters=[
                       OpenApiParameter(name='accept-version',
                                        required=True,
                                        type=OpenApiTypes.STR,
                                        default=APP_VERSION,
                                        location=OpenApiParameter.HEADER),
                       OpenApiParameter(name='accept-device-type',
                                        required=True,
                                        type=OpenApiTypes.INT,
                                        default=ACCEPT_DEVICE_TYPE,
                                        location=OpenApiParameter.HEADER),
                       OpenApiParameter(name='accept-language',
                                        required=True,
                                        type=OpenApiTypes.STR,

                                        location=OpenApiParameter.HEADER),
                   ])
    # @api_view(['GET'])
    def get(self, request, version):
        try:
            print(request.META.get('HTTP_ACCEPT_LANGUAGE'))
            return Response({'message': api_success_msg.HELLO_WORLD}, status=status.HTTP_200_OK)
        except Exception as ex:
            return Response({'message': 'fail'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_data(request, version):
    try:
        print(request.META.get('HTTP_ACCEPT_LANGUAGE'))
        return Response({'message': api_success_msg.HELLO_WORLD}, status=status.HTTP_200_OK)
    except Exception as ex:
        return Response({'message': 'fail'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def user_insert(request, version):
    try:
        serializer = InsertUserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'message': serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({'message': 'success'}, status=status.HTTP_200_OK)
    except ArithmeticError as ex:
        return Response({'message': 'Failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_user(request, version):
    try:
        return Response(ListUserSerializer(SystemUser.objects.all(), many=True).data, status=status.HTTP_200_OK)
    except Exception as ex:
        return Response({'message': 'Fail'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def user_update(request, version, pk):
    try:
        get_user = get_object_or_404(SystemUser, pk=pk)
        serializer = InsertUserSerializer(instance=get_user, data=request.data)
        if not serializer.is_valid():
            return Response({'message': serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({'message': 'success'}, status=status.HTTP_200_OK)
    except ArithmeticError as ex:
        return Response({'message': 'Failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
