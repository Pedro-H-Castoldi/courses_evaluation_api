from rest_framework import generics
from rest_framework.generics import get_object_or_404

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import permissions

from .serializers import CourseSerializer, EvaluationSerializer
from .models import Course, Evaluation
from .permissions import IsSuperUser

"""
API V1
"""

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
        if self.kwargs.get('course_pk'):
            return self.queryset.filter(course_id=self.kwargs.get('course_pk'))
        return self.queryset.all()

class EvaluationAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer

    def get_object(self):
        if self.kwargs.get('course_pk'):
            return get_object_or_404(self.get_queryset(), course_id=self.kwargs.get('course_pk'),
                                     pk=self.kwargs.get('evaluation_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('evaluation_pk'))


"""
API V2
"""

class CourseViewSet(viewsets.ModelViewSet):
    permission_classes = (
        IsSuperUser,
        permissions.DjangoModelPermissions,
    )
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True, methods=['get'])
    def evaluations(self, request, pk=None):
        self.pagination_class.page_size = 1
        evaluation = Evaluation.objects.filter(course_id=pk)
        page = self.paginate_queryset(evaluation)

        if page:
            serializer = EvaluationSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = EvaluationSerializer(evaluation, many=True)
        return Response(serializer.data)

class EvaluationViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet):

    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer