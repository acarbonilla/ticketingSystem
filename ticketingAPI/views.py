from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

from baseApp.models import INCTicket, SRTicket
from baseApp.viewsCall.cal import skeleton
from .serializers import PostSerializer, IncidentSerializer, SRSerializer
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse

skeletons = skeleton()


@api_view(['GET'])
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = User.objects.all()
        serializer = PostSerializer(snippets, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def posting(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PostSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# This is for all tickets within the month.

@api_view(['GET'])
def incidentTicket(request):
    if request.method == 'GET':
        snippets = INCTicket.objects.filter(
            created__month=skeletons,
            status="Closed"
        )
        serializer = IncidentSerializer(snippets, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def inc_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = INCTicket.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = IncidentSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = IncidentSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# This is for all tickets within the month.


@api_view(['GET'])
def serviceTicket(request):
    if request.method == 'GET':
        snippets = SRTicket.objects.filter(
            created__month=skeletons,
            status="Closed"
        )
        serializer = SRSerializer(snippets, many=True)
        return Response(serializer.data)
