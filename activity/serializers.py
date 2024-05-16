from rest_framework import serializers
from .models import Activity

class SubCategorySerializer(serializers.Serializer):

    name = serializers.CharField()
    user_id = serializers.IntegerField()
    main_category_id = serializers.IntegerField()
    # is_active = serializers.BooleanField()
    # sub_category_id = serializers.IntegerField()

class ActivitySerializers(serializers.Serializer):
    class Meta:
        model = Activity
        fields = ('start_time','end_time', 'date', 'focus_percentage', 'description', 'sub_category_id', 'main_category_id')
        # exclude = ('mo')
        # fields = '__all__'