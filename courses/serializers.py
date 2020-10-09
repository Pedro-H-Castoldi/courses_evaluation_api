from rest_framework import serializers

from .models import Course, Evaluation
from django.db.models import Avg

class EvaluationSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Evaluation
        fields = (
            'id',
            'course',
            'name',
            'email',
            'commentary',
            'grade',
            'creation',
            'active',
        )

    def validate_grade(self, value):
        if value in range(1, 6):
            return value
        raise serializers.ValidationError('The grade must be 1 to 5.')

class CourseSerializer(serializers.ModelSerializer):
    # Nested Relationship
    #evaluation = EvaluationSerializer(many=True, read_only=True)

    # HyperLinked Related Fields
    evaluation = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='evaluation-detail')

    # Primary Key Related Field
    #evaluation = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    average_evaluation = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = (
            'id',
            'title',
            'url',
            'creation',
            'active',
            'evaluation',
            'average_evaluation'
        )

    def get_average_evaluation(self, obj):
        average = obj.evaluation.aggregate(Avg('grade')).get('grade__avg')

        if average is None:
            return 0
        return round(average * 2) / 2