from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import CourseSerializer, EvaluationSerializer
from .models import Course, Evaluation

class CourseAPIView(APIView):
    """
    Geek Courses API
    """
    def get(self, request):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class EvaluationAPIView(APIView):
    """
    Geek rating API
    """
    def get(self, request):
        evaluation = Evaluation.objects.all()
        serializer = EvaluationSerializer(evaluation, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EvaluationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)