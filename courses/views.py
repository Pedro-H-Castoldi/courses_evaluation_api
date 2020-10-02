from rest_framework import generics
from rest_framework.generics import get_object_or_404

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins

from .serializers import CourseSerializer, EvaluationSerializer
from .models import Course, Evaluation

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


"""
API V2
"""

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    # Essa função irá permitir pegar um curso específico e todas as avaliações da mesma,
    #sem precisar nomear o caminho da rota junto com os kwargs.

    # Detail=True indica q é para executar isso, methods são os métodos q serão executados nessa função
    @action(detail=True, methods=['get'])
    def evaluations(self, request, pk=None):
        self.pagination_class.page_size = 1 # Página de 1 dado por vez
        evaluation = Evaluation.objects.filter(course_id=pk) # Pega as avaliações onde o atributo course_id da tabela Evaluation seja igual ao PK do Curso requerido
        page = self.paginate_queryset(evaluation) # Gera a pagina (aki verá se será necessário fazer a paginação ou n de acordo com o número de objetos

        if page: # Se existir page
            serializer = EvaluationSerializer(page, many=True) # Pega todos os dados do EvaluationSerializer onde page pertença (Evaluation.objects.filter(course_id=pk)
            return self.get_paginated_response(serializer.data) # Retorne os dados da serializer em paginas

        serializer = EvaluationSerializer(evaluation, many=True) # Senão, Retorne Evaluation.objects.filter(course_id=pk)
        return Response(serializer.data) # Como n existia paginação, logo o número de objetos era =< à quantidade de objetos por página


        """course = self.get_object() # course pegará o objeto do curso q foi deferido
        serializer = EvaluationSerializer(course.evaluation.all(), many=True) # Pegue todas as avaliações que foram dirigidas à esse curso, many=True (todos).
        return Response(serializer.data) # Retorne todos os dados obtidos."""

"""
class EvaluationViewSet(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer
 """

# Se por acaso eu querer restringir certas métodos http, bastas importar o mixins comentar as extenções
class EvaluationViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin, # Comentando aki n permitirá q liste todas as avaliações de uma vez
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet):

    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer