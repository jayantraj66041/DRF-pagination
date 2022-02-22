# from django.shortcuts import render
from api.serializers import StudentSerializer
from api.models import Student
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from rest_framework.pagination import PageNumberPagination

from django.core.paginator import Paginator

# Create your views here.
class StudentView(APIView):
    def get(self, request):
        student = Student.objects.all()

        p = Paginator(student, 2)   # It creates an object of 2 dataset
        page_number = request.GET.get('page')
        try:
            page_obj = p.get_page(page_number)  # returns the desired page object
        except PageNotAnInteger:
            # if page_number is not an integer then assign the first page
            page_obj = p.page(1)
        except EmptyPage:
            # if page is empty then return last page
            page_obj = p.page(p.num_pages)
        serializer = StudentSerializer(page_obj, many=True) # serialized out data in json
        # print(request.get_host())
        return Response({
            'count': student.count(),
            'next': "https://" + request.get_host() + "/api/student/?page=" + str(page_obj.next_page_number()) if page_obj.has_next() else None,
            'prev': "https://" + request.get_host() + "/api/student/?page=" + str(page_obj.previous_page_number()) if page_obj.has_previous() else None,
            'results': serializer.data
        }, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)