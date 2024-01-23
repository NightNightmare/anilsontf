from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Livro, Autor
from .serializers import LivroSerializer, AutorSerializer

import json


@api_view(['GET'])
def get_livros(request):
    if request.method== "GET":
        livro = Livro.objects.all()
        serializer = LivroSerializer(livro, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_autores(request):
    if request.method== "GET":
        autor = Autor.objects.all()
        serializer = AutorSerializer(autor, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def get_livro_by_id(request, id):
    try: 
        livro = Livro.objects.get(pk=id)
    except Livro.DoesNotExist:
        return Response(status =status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LivroSerializer(livro)
        return Response(serializer.data)

    
    if request.method == 'PUT':
        serializer = LivroSerializer(livro, data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST', 'DELETE'])
def livro_manager(request):

    if request.method == 'GET':
        try:
            if request.GET['livro']:
                id = request.GET['livro']
                try:
                    livro = Livro.objects.get(pk=id)
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                serializer = LivroSerializer(livro)
                return Response(serializer.data)
            else:
                return Response(status = status.HTTP_400_BAD_REQUEST)
        except:
                return Response(status = status.HTTP_400_BAD_REQUEST)

    if request.method == 'POST':
            novo_livro = request.data
            serializer = LivroSerializer(data = novo_livro)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            return Response(status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
def delete_livro(request, livro_id):
    try:
        livro = Livro.objects.get(pk=livro_id)
    except Livro.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        livro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # Se o método não for DELETE, retornar um erro de método não permitido
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

        

@api_view(['GET', 'PUT'])
def get_autor_by_id(request, id):
    try: 
        autor = Autor.objects.get(pk=id)
    except Autor.DoesNotExist:
        return Response(status =status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AutorSerializer(autor)
        return Response(serializer.data)

    
    if request.method == 'PUT':
        serializer = AutorSerializer(autor, data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)



@api_view(['GET','POST', 'DELETE'])
def autor_manager(request):

    if request.method == 'GET':
        try:
            if request.GET['autor']:
                id = request.GET['autor']
                try:
                    autor = Autor.objects.get(pk=id)
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                serializer = AutorSerializer(autor)
                return Response(serializer.data)
            else:
                return Response(status = status.HTTP_400_BAD_REQUEST)
        except:
                return Response(status = status.HTTP_400_BAD_REQUEST)

    if request.method == 'POST':
            novo_autor = request.data
            serializer = AutorSerializer(data = novo_autor)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            return Response(status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def delete_autor(request, autor_id):
    try:
        autor = Autor.objects.get(pk=autor_id)
    except Autor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        autor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # Se o método não for DELETE, retornar um erro de método não permitido
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)




