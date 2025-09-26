from rest_framework import generics, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Cat
from .serializers import CatSerializer


# Реализация через API функции

@api_view(['GET', 'POST'])
def cat_list(request):
    if request.method == 'POST':
        serializer = CatSerializer(
            data=request.data,
            many=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    cats = Cat.objects.all()
    serializer = CatSerializer(cats, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def cat_detail(request, pk):
    cat = Cat.objects.get(pk=pk)
    if request.method in ('PUT', 'PATCH'):
        serializer = CatSerializer(
            cat,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        cat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    serializer = CatSerializer(cat)
    return Response(data=serializer.data ,status=status.HTTP_200_OK)


# Реализация через View-классы API

class APICat(APIView):
    def get(self, request):
        cats = Cat.objects.all()
        serializer = CatSerializer(cats, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CatSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class APICatDetail(APIView):
    def get(self, request, pk):
        cat = Cat.objects.get(pk=pk)
        serializer = CatSerializer(cat)
        return Response(data=serializer.data ,status=status.HTTP_200_OK)

    def put(self, request, pk):
        cat = Cat.objects.get(pk=pk)
        serializer = CatSerializer(cat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        cat = Cat.objects.get(pk=pk)
        serializer = CatSerializer(cat, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        cat = Cat.objects.get(pk=pk)
        cat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Реализация через Generic Views

class CatList(generics.ListCreateAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class CatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


# Реализация через ViewSet

class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
