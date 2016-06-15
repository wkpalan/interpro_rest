from django.shortcuts import render,redirect

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from .forms import upload_url
from .models import id_desc
from .serializers import base_serializer



# Create your views here.
def redirect_parse_id(request):
    return redirect('/parse_id')

def db_list(request):
    databases = id_desc.objects.all().values_list('db',flat=True)
    return render(request, 'parse_id/db_list.html', {'databases':databases})

def add_data(request):
    if request.method == "POST":
        form = upload_url(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/parse_id/db_list',pk=post.pk)
    else:
        form = upload_url
    return render(request, 'parse_id/add_data.html',{'form':form})
20
class base_view(generics.ListAPIView):
    queryset = id_desc.objects.all()
    serializer_class = base_serializer

class base_add(generics.CreateAPIView):
    model = id_desc
    serializer_class = base_serializer
    # def post(self, request, format=None):
    #     serializer = base_serializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_201_CREATED)


class db_view(generics.ListAPIView):
    serializer_class = base_serializer

    def get_queryset(self):
        db_name = self.kwargs['db_name']
        records = id_desc.objects.filter(db=db_name)
        return records


class db_id_view(generics.ListAPIView):
    serializer_class = base_serializer

    def get_queryset(self):
        db_name = self.kwargs['db_name']
        db_id = self.kwargs['db_id']
        records = id_desc.objects.filter(db=db_name).filter(db_id=db_id)
        return records
'''
    def get(self, request, db_name, db_id, format=None):
        records = id_desc.objects.filter(db=db_name).filter(db_id=db_id)
        serializer = base_serializer(records, many=True)
        return Response(serializer.data)

class db_view(viewsets.ModelViewSet):
    queryset = id_desc.objects.all()
    serializer_class = base_serializer


    def get_queryset(self):
        db_name = self.kwargs['db_name']
        return id_desc.objects.filter(db = db_name)

'''
