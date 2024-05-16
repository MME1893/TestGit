from rest_framework import serializers
from .models import Activity

class SubCategorySerializer(serializers.Serializer):

    name = serializers.CharField()
    user_id = serializers.IntegerField()
    main_category_id = serializers.IntegerField()
    # is_active = serializers.BooleanField()
    # sub_category_id = serializers.IntegerField()

class ActivitySerializers(serializers.Serializer):
    # class Meta:
    #     model = Activity
    #     # fields = ('user_id','start_time','end_time', 'date', 'focus_percentage', 'description', 'sub_category_id', 'main_category_id')
    #     fields = ('start_time','end_time', 'date', 'focus_percentage', 'description', 'sub_category_id', 'main_category_id')
    #     # exclude = ('mo')
    #     # fields = '__all__'

    start_time = serializers.IntegerField(required=True)
    end_time = serializers.IntegerField(required=True)
    date = serializers.CharField(required=True)
    focus_percentage = serializers.IntegerField(required=True)
    description = serializers.CharField(required=True)
    sub_category_id = serializers.IntegerField(required=True)
    main_category_id = serializers.IntegerField(required=True)