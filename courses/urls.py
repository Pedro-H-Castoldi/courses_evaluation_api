from django.urls import path

from .views import CourseAPIView, CoursesAPIView ,EvaluationAPIView, EvaluationsAPIView

urlpatterns = [
    path('courses/', CoursesAPIView.as_view(), name='courses'),
    path('courses/<int:pk>/', CourseAPIView.as_view(), name='course'),

    path('evaluations/', EvaluationsAPIView.as_view(), name='evaluations'),
    path('evaluations/<int:evaluation_pk>/', EvaluationAPIView.as_view(), name='evaluation'),

    # Rota q mostra um curso (com id específico) e todas as avaliações sobre esse curso.
    path('courses/<int:course_pk>/evaluations/', EvaluationsAPIView.as_view(), name='course_evaluations'),
    # Rota q mostra um curso (com id específico) e uma avaliação (com id específico).
    path('courses/<int:course_pk>/evaluations/<int:evaluation_pk>/', EvaluationAPIView.as_view(), name='course_evaluation'),

    # <int:course_pk> e <int:evaluation_pk> foram alterados já q o método das views correspondentes serão sobrescrevidos.
]