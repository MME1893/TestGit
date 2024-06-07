# from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
# import serializers
from .serializers import SubCategorySerializer, ActivitySerializers, ActivityResponseSerlializer, MainCategorySerializer
from rest_framework import permissions
import datetime

from .models import Activity, SubCategory, MainCategory
# from rest_framework.viewsets import ViewSet 

class SubCategoryController(APIView):
    """
    Yasin Style \Coding :(
    """
    # permission_classes = (permissions.IsAuthenticated,)
    def post(self, request):

        serialized_data = SubCategorySerializer(data=request.data)

        # return Response({"hello": "world"})

        if not serialized_data.is_valid():

            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            # return Response(serialized_data.data)
            SubCategory.objects.create(
                name=serialized_data.validated_data['name'],
                user_id=serialized_data.validated_data['user_id'],
                main_id=serialized_data.validated_data['main_id'],
                is_active=True,
            )

            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
            
            

    def get(self, request, user_id=None, main_id=None):
        result = SubCategory.objects.all()
        if user_id:
            result = result.filter(user_id=user_id)
        if main_id:
            result = result.filter(main_id=main_id)

        # serialized_response = SubCategorySerializer(instance=SubCategory.objects.all() , many = True )
        serialized_response = SubCategorySerializer(instance=result, many=True)
        return Response(serialized_response.data)

    # def get(self, request, user_id):
    #     pass


class MainCategoryController(APIView):
    
    def get(self, request):
        response_data = MainCategorySerializer(instance=MainCategory.objects.all(), many=True)
        return Response(response_data.data)
        

class ActivityView(APIView):

    # permission_classes = (permissions.IsAuthenticated,)

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
            # print("hello")
            Activity.objects.create(user_id=serialized_data.validated_data['user_id'],
                                    start_time=serialized_data.validated_data['start_time'],
                                    end_time=serialized_data.validated_data['end_time'],
                                    date=serialized_data.validated_data['date'],
                                    modified_time=datetime.datetime.now(),
                                    focus_percentage=serialized_data.validated_data['focus_percentage'],
                                    description=serialized_data.validated_data['description'],
                                    main_category_id=serialized_data.validated_data['main_category_id'],
                                    sub_category_id=serialized_data.validated_data['sub_category_id']
                                    )
            # return Response(serialized_data.validated_data)
            # return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(serialized_data.validated_data, status=status.HTTP_201_CREATED)
            
            

    def get(self, request):
        # permission_classes = (permissions.IsAuthenticated,)
        user_id = request.query_params.get('user_id', -1)
        start_time = request.query_params.get('start_time', -1)
        end_time = request.query_params.get('end_time', -1)
        date = request.query_params.get('date', None)
        start_date = request.query_params.get('start_date', None)
        end_date = request.query_params.get('end_date', None)
        focus_percentage = request.query_params.get('focus_percentage', -1)
        description = request.query_params.get('description', '')
        sub_category_id = request.query_params.get('sub_category_id', -1)
        main_category_id = request.query_params.get('main_category_id', -1)
           
        resultQuerySet = Activity.objects.all()
        
        if user_id != -1:
            resultQuerySet = resultQuerySet.filter(user_id=user_id)

        if start_time != -1:
            resultQuerySet = resultQuerySet.filter(start_time__gte=start_time)

        if end_time != -1:
            resultQuerySet = resultQuerySet.filter(end_time__lte=end_time)

        if date:
            resultQuerySet = resultQuerySet.filter(date=date)

        if start_date:
            resultQuerySet = resultQuerySet.filter(date__gte=start_date)
        
        if end_date:
            resultQuerySet = resultQuerySet.filter(date__lte=end_date)

        if focus_percentage != -1:
            resultQuerySet = resultQuerySet.filter(focus_percentage=focus_percentage)

        if sub_category_id != -1:
            resultQuerySet = resultQuerySet.filter(sub_category_id=sub_category_id)
        
        if main_category_id != -1:
            resultQuerySet = resultQuerySet.filter(main_category_id=main_category_id)
        
        
        file = ActivitySerializers(instance=resultQuerySet, many=True)
        return Response(file.data)


        



        


# Create your views here.
