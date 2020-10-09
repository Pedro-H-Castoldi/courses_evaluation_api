from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import (
    CourseAPIView,
    CoursesAPIView,
    EvaluationAPIView,
    EvaluationsAPIView,
    EvaluationViewSet,
    CourseViewSet
)

router = SimpleRouter()
router.register('courses', CourseViewSet)
router.register('evaluations', EvaluationViewSet)

urlpatterns = [
    path('courses/', CoursesAPIView.as_view(), name='courses'),
    path('courses/<int:pk>/', CourseAPIView.as_view(), name='course'),

    path('evaluations/', EvaluationsAPIView.as_view(), name='evaluations'),
    path('evaluations/<int:evaluation_pk>/', EvaluationAPIView.as_view(), name='evaluation'),


    path('courses/<int:course_pk>/evaluations/', EvaluationsAPIView.as_view(), name='course_evaluations'),
    path('courses/<int:course_pk>/evaluations/<int:evaluation_pk>/', EvaluationAPIView.as_view(), name='course_evaluation'),
]