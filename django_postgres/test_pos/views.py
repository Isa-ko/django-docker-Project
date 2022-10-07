from django.shortcuts import render
from test_pos.models import Members
from datetime import datetime
from django.template import loader
from django.http import HttpResponse, JsonResponse
#DRF
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from test_pos.serializers import MemberSerializer


# Create your views here.

def index(request):
    
    members=Members.objects.all().values()
    template = loader.get_template('index.html')
    context={
        'current_time': str(datetime.now()),
        "obj":members,
    }

    return HttpResponse(template.render(context, request))
    #return render(request,"index.html",{
    #    'current_time': str(datetime.now())
    #})


@api_view(['GET', 'POST','PUT'])
def member_list(request):
    #get all the members
    #serialize them
    #return json
    if request.method == 'GET':
        members= Members.objects.all()
        serializer= MemberSerializer(members, many=True)
        return Response(serializer.data)
        
    if request.method =='POST':
        serializer= MemberSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        serializer = MemberSerializer(Members, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def member_detail(request, id):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        member = Members.objects.get(pk=id)
    except Members.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MemberSerializer(member)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MemberSerializer(member, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)