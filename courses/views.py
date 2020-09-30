from rest_framework import generics
from rest_framework.generics import get_object_or_404

from .serializers import CourseSerializer, EvaluationSerializer
from .models import Course, Evaluation

class CoursesAPIView(generics.ListCreateAPIView):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class EvaluationsAPIView(generics.ListCreateAPIView):

    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer

    def get_queryset(self):
        # os kwargs q irão obter o q está na uri, se na uri tiver o kwargs 'course_pk'
        if self.kwargs.get('course_pk'):
            # Retorne a queryset (é a listas de objetos q são retornados para o templete) filtrando o curso com
            #o id/pk indicado.
            return self.queryset.filter(course_id=self.kwargs.get('course_pk'))
        # senão, retorne todos, pois a requisção é a rota q n tem o 'course_pk', logo é a rota 'evaluations/'.
        return self.queryset.all()

class EvaluationAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer

    def get_object(self):
        if self.kwargs.get('course_pk'):
            # Retorna um curso específico com uma avaliação específica ou erro 404.
            return get_object_or_404(self.get_queryset(), course_id=self.kwargs.get('course_pk'),
                                     pk=self.kwargs.get('evaluation_pk'))
        # Retorna uma avaliação específica somente ou erro 404.
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('evaluation_pk'))
