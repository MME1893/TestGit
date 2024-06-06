from rest_framework import serializers
from .models import Activity,SubCategory, MainCategory

class MainCategorySerializer(serializers.ModelSerializer):
    class Meta:
       model = MainCategory
       fields = '__all__'

class SubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SubCategory
        fields = '__all__'
    # name = serializers.CharField()
    # user_id = serializers.IntegerField()
    # main_category_id = serializers.IntegerField()
    # is_active = serializers.BooleanField()
    # sub_category_id = serializers.IntegerField()

class ActivitySerializers(serializers.ModelSerializer):

    main_category_name = serializers.CharField(source='main_category_id.name', read_only=True)
    sub_category_name = serializers.CharField(source='sub_category_id.name', read_only=True)

    class Meta:
        model = Activity
        fields = ('user_id','start_time','end_time', 'date', 'focus_percentage', 'description', 'sub_category_id', 'main_category_id', 'main_category_name', 'sub_category_name')
        # fields = ('start_time','end_time', 'date', 'focus_percentage', 'description', 'sub_category_id', 'main_category_id')
    #     # exclude = ('mo')
    #     # fields = '__all__'
    # user_id = serializers.IntegerField(required=True)
    # start_time = serializers.IntegerField(required=True)
    # end_time = serializers.IntegerField(required=True)
    # date = serializers.CharField(required=True)
    # focus_percentage = serializers.IntegerField(required=True)
    # description = serializers.CharField(required=True)
    # sub_category_id = serializers.IntegerField(required=True)
    # main_category_id = serializers.IntegerField(required=True)
        
class ActivityResponseSerlializer(serializers.Serializer):

    # main_category_name = serializers.CharField(source='')

    user_id = serializers.IntegerField(required=True)
    start_time = serializers.IntegerField(required=True)
    end_time = serializers.IntegerField(required=True)
    date = serializers.CharField(required=True)
    focus_percentage = serializers.IntegerField(required=True)
    description = serializers.CharField(required=True)
    sub_category_id = serializers.IntegerField(required=True)
    main_category_id = serializers.IntegerField(required=True)
    # sub_category_name = serializers.CharField()
    main_category_name = serializers.CharField()

    # def get_main_category_name(self, obj):
    #     return obj.MainCategory.name
    # def get_user_id(self, obj):
    #     return obj.user_id.user_id

