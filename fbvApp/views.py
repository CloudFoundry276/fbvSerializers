from django.shortcuts import render
from fbvApp.models import Student
from fbvApp.serializers import StudentSerializer
from rest_framework.response import Response


# Create your views here.
def student_list(request):

    if request.method == "GET":
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
