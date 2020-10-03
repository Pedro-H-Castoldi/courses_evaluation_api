from rest_framework import serializers

from .models import Course, Evaluation

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

class CourseSerializer(serializers.ModelSerializer):
    # Nested Relationship
    # Pega n (many) avaliações de um detarminado curso apenas para leitura
    #evaluation = EvaluationSerializer(many=True, read_only=True)

    # HyperLinked Related Fields
    evaluation = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='evaluation-detail')

    # Primary Key Related Field
    #evaluation = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Course
        fields = (
            'id',
            'title',
            'url',
            'creation',
            'active',
            'evaluation'
        )