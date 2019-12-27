from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Store
from rest_framework.views import APIView
from .serializers import StoreDataViewSerializer
from rest_framework import status
from datetime import datetime 
# Create your views here.


def index(request):
    #logging.getLogger("error_logger").error("Hi I am here")
    return HttpResponse("Hello World. First Django Project. ThePythonDjango.Com")

class StoreDataView(APIView):
    def get_object(self, pk):
        try:
            return Store.objects.get(pk=pk)
        except Store.DoesNotExist:
            raise Http404
    def get(self, request, *args, **kwargs):
        keys = request.query_params.get('keys')
        dic = {}
        flag = 1
        if keys:
            for key in keys.split(','):
                val = [item for item in Store.objects.filter(key=key).values_list('key','value','id')]
                for item in val:
                    dic[item[0]] = item[1]
                    t = Store.objects.get(id=item[2])
                    t.posting_date = datetime.now() 
                    t.save() #
            return Response(dic,status=status.HTTP_200_OK)
                                        
        else:
            stores = Store.objects.all()
            for val in stores:
                dic[val.key] = val.value
                t = Store.objects.get(id=val.id)
                t.posting_date = datetime.now() 
                t.save()
            return Response(dic,status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = request.data
        arr = []
        flag = 1
        for key in data:
            temp_data = {'key':key, 'value':data[key], 'posting_date' : datetime.now()}
            serializer = StoreDataViewSerializer(data=temp_data)
            if serializer.is_valid():
                serializer.save()
                arr.append(serializer.data)
            else:
                flag = 0
                print(serializer.errors)

        if flag == 1:
            return Response(arr, status=status.HTTP_201_CREATED)
        else:
           return Response(arr, status=status.HTTP_204_NO_CONTENT) 

    def patch(self, request, *args, **kwargs):
        key_id = []
        flag = 1
        arr = []
        data = request.data
        for key in data:
            try:
                pk = Store.objects.filter(key=key).values_list('id',flat = True)[0]
                print("aaaaaaaaaaaaaaaaa = ",pk)
                store = self.get_object(pk)
                temp_data = {'key':key, 'value':data[key],'posting_date' : datetime.now()}
                serializer = StoreDataViewSerializer(store, data=temp_data)
                if serializer.is_valid():
                    serializer.save()
                    arr.append(serializer.data)
                else:
                    flag = 0
            except:
                continue

        if flag == 1:
            return Response(arr, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        


