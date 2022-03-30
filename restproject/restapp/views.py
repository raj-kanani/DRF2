import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Student

# class based view packages
from django.utils.decorators import method_decorator
from django.views import View


# CLASS BASED VIEW ... CRUD OPERATION

@method_decorator(csrf_exempt, name='dispatch')
class StudentApi(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type="application/json")
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type="application/json")

    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': "Data Created"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type="application/json")
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type="application/json")

    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=pythondata, partial=True)  # partial update for specific update field
        if serializer.is_valid():
            serializer.save()
            res = {'msg': ' data update '}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg': 'data delete'}
        return JsonResponse(res, safe=False)


#  serializer and serialization..
# def detail(request, pk):
#     stu = Student.objects.get(pk=pk)  # create queryset
#     se = StudentSerializer(stu)  # convert queryset into python dict / serializing queryset
#     json_data = JSONRenderer().render(se.data)  # convert  serializing data into JSON
#     return HttpResponse(json_data, content_type='application/json')  # send user data
#
#
# # queryset with all data
# def list(request):
#     stu = Student.objects.all()
#     se = StudentSerializer(stu, many=True)
#     # return JSONResponse(se.data)
#     j = JSONRenderer().render(se.data)
#     return HttpResponse(j)


# deserialization data

# create student data


# FUNCTION BASED VIEW ... CRUD OPERATION
#
# @csrf_exempt
# def student_create(request):
#     if request.method == "POST":
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         serializer = StudentSerializer(data=pythondata)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': "Data Created"}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type="application/json")
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type="application/json")
#
#
# @csrf_exempt
# def student_api(request):
#     # get student data with id or get all data
#     if request.method == "GET":
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id', None)
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             serializer = StudentSerializer(stu)
#             json_data = JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data, content_type="application/json")
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu, many=True)
#         json_data = JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data, content_type="application/json")
#
#     # update data for student
#     if request.method == 'PUT':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id')
#         stu = Student.objects.get(id=id)
#         serializer = StudentSerializer(stu, data=pythondata, partial=True)  # partial update for specific update field
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': ' data update '}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
#
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')
#
#     if request.method == 'DELETE':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id')
#         stu = Student.objects.get(id=id)
#         stu.delete()
#         res = {'msg': 'data delete'}
#         # json_data = JSONRenderer().render(res)
#         # return HttpResponse(json_data, content_type='application/json')
#         # data is not in dict then use safe=false
#         return JsonResponse(res, safe=False)
