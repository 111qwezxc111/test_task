from rest_framework.serializers import ModelSerializer, SerializerMethodField
from kitten_show.models import Kitten, Grade


class KittenSerializer(ModelSerializer):
    avg_grade = SerializerMethodField()
    user_grade = SerializerMethodField()

    def get_avg_grade(self, obj):
        summ = sum([grade.value for grade in obj.grade_set.all()])
        count = len(obj.grade_set.all())
        return summ/count if count else 0

    def get_user_grade(self, obj):
        grade = Grade.objects.filter(user=self.context['request'].user, kitten=obj).first()
        return grade.value if grade else grade

    class Meta:
        model = Kitten
        fields = ('id', 'name', 'color', 'age', 'breed', 'description', 'avg_grade', 'user_grade')


class BreedsSerializer(ModelSerializer):

    class Meta:
        model = Kitten
        fields = ('id', 'name', 'breed',)
