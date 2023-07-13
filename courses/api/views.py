from _ast import Is

from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from courses.models import Subject, Course
from courses.api.serializers import SubjectSerializer, CourseSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.decorators import action
from courses.api.permissions import IsEnrolled
from courses.api.serializers import CourseWithContentSerializer


class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetailView(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


# class CourseEnrollView(APIView):
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAuthenticated]
#
#     def post(self, request, pk, format=None):
#         course = get_object_or_404(Course, pk=pk)
#         course.students.add(request.user)
#         return Response({'enrolled': True})


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True, methods=['post'], authentication_classes=[BasicAuthentication],
            permission_classes=[IsAuthenticated])
    def enroll(self, request, *args, **kwargs):
        course = self.get_object()
        course.students.add(request.user)
        return Response({'enrolled': True})

    @action(detail=True, methods=['post'],serializer_class=CourseWithContentSerializer,
            authentication_classes=[BasicAuthentication], permission_classes=[IsAuthenticated, IsEnrolled])
    def contents(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

# Работа данного метода описывается следующим образом.
# 1. Декоратор action используется с параметром detail=True, чтобы зада-
# вать действие, которое выполняется над одним объектом.
# 2. Затем указывается, что для этого действия разрешен только метод GET.
# 3. Далее используется новый класс-сериализатор CourseWithContentsSerializer,
# который включает прорисованное содержимое курса.
# 4. Используются как разрешения IsAuthenticated, так и конкретно-при-
# кладные разрешения IsEnrolled. Тем самым обеспечивается, чтобы
# доступ к содержимому курса могли получать только те пользователи,
# которые были зачислены на курс.
# 5. В конце применяется существующее действие retrieve(), чтобы воз-
# вращать объект Course.
