# from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
# import serializers
from .serializers import SubCategorySerializer, ActivitySerializers
# from rest_framework.viewsets import ViewSet 

class SubCategory(APIView):
    def post(self, request):

        serialized_data = SubCategorySerializer(data=request.data)

        # return Response({"hello": "world"})

        if not serialized_data.is_valid():

            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serialized_data.data)
            

    def get(self, request, user_id, main_id=-1):
        # return Response({"hello": "world"})
        
        return Response({"user_id" : user_id, "main_id" : main_id})

    # def get(self, request, user_id):
    #     pass


class ActivityView(APIView):

    def post(self, request):
        print(request)
        print(request.data)
        print(request.POST)
        serialized_data = ActivitySerializers(data=request.data)
        # return Response(serialized_data.data)
        # serialized_data = ActivitySerializers(data=request.POST)
        if not serialized_data.is_valid():
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

        else:
            print(serialized_data.data)
            # print(serialized_data.validated_data)
            return Response(serialized_data.validated_data)
            # return Response({"key":"hello"})
            # test = {"key2":serialized_data.validated_data["start_time"]}
            # return Response(test)
            

    def get(self, request):
        user_id = request.query_params.get('user_id', -1)
        start_time = request.query_params.get('start_time', -1)
        end_time = request.query_params.get('end_time', -1)
        date = request.query_params.get('date', None)
        focus_percentage = request.query_params.get('focus_percentage', -1)
        description = request.query_params.get('description', '')
        sub_category_id = request.query_params.get('sub_category_id', -1)
        main_category_id = request.query_params.get('main_category_id', -1)

        return Response(request.query_params)


        



        


# Create your views here.
