from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication
from .models import *
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.decorators import api_view
from rest_framework.authentication import get_user_model
from rest_framework.response import Response
from django.contrib.auth.models import Group
from users.models import UserProfile
import os
from rest_framework.status import (
     HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

# Create your views here.

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def create(request,user):
    data = request.data
    try:
        print(type(user))
        User=get_user_model()
        user = User.objects.get(username=user)
        print(type(user))
        blog_profile = blogs()
        blog_profile.name = data["name"]
        blog_profile.description = data["description"]
        blog_profile.detail = data["detail"]
        blog_profile.image = data["image"]
        blog_profile.creator = user
        blog_profile.save()
        blog_profile.users.add(User.objects.get(username=user))
        # blog_profile.users = user
        blog_profile.save()
    except Exception as e:
        print("Exception is ",e)
        return Response({"status": str(e)})

    return Response({"status": "success"},status=HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def getblogs(request,user):
    User = get_user_model()
    user = User.objects.get(username=user)
    blog = blogs.objects.filter(users = user)
    resp = {}
    for i in blog:
        print(i.name)
        # try:
        resp[i.name] = {}
        # except Exception as e:
        #     print(e)
        temp = {}
        temp["name"] = i.name
        temp["description"] = i.description
        temp["detail"] = i.detail
        temp["image"] = i.image
        temp["creator"] = i.creator
        print(temp)
        resp[i.name] = temp
    return Response(resp)


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def updateblog(request,user,blogname):
    data = request.data
    user = get_user_model().objects.get(username=user)
    blogdata = blogs.objects.filter(name = blogname,users = user)
    # print(blogdata.description)
    for i in blogdata:
        i.description = data["description"]
        i.detail = data["detail"]
        # blogdata.image = data["image"]
        i.save()

    return Response({"status":"success"})


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def deleteblog(request, user, blogname):
    data = request.data
    user = get_user_model().objects.get(username=user)
    blogdata = blogs.objects.filter(name = blogname,users = user)
    blogdata.delete()


    return Response({"status": "success"})


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def comment(request, user, blogname):
    data = request.data
    User = get_user_model().objects.get(username=user)
    blogdata = blogs.objects.get(name=blogname)
    comment_data = blogcomments()
    comment_data.name = blogdata
    comment_data.comment= data["comment"]
    comment_data.creator = user
    comment_data.save()
    comment_data.users.add(User)
    comment_data.save()
    return Response({"status":"success"})

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def delete_comment(request,id):
    comment = blogcomments.objects.get(id=id)
    comment.delete()
    return Response({"status":"deleted"})


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_comment(request, user, blogname):
    blogdata = blogs.objects.get(name=blogname)
    allcomment = blogcomments.objects.filter(name = blogdata)
    print(allcomment)
    resp = {}
    for i in allcomment:
        print(i.id)
        resp[i.id] = {}
        temp = {}
        temp["name"] = blogname
        temp["comment"] = i.comment
        # temp["date"] = i.created_date
        temp["creator"] = i.creator
        resp[i.id] = temp
        print(resp)
    return Response(resp)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def getallblogs(request):
    # User = get_user_model()
    # user = User.objects.get(username=user)
    blog = blogs.objects.all()
    resp = {}
    for i in blog:
        print(i.name)
        # try:
        resp[i.name] = {}
        # except Exception as e:
        #     print(e)
        temp = {}
        temp["name"] = i.name
        temp["description"] = i.description
        temp["detail"] = i.detail
        temp["image"] = i.image
        temp["creator"] = i.creator
        temp["comments"] = {}
        blogdata = blogs.objects.get(name=i.name)
        allcomment = blogcomments.objects.filter(name=blogdata)
        for k in allcomment:
            print(k.id)
            temp["comments"][k.id] = {}
            t = {}
            t["name"] = i.name
            t["comment"] = k.comment
            # temp["date"] = i.created_date
            t["creator"] = k.creator
            temp["comments"][k.id] = t


        print(temp)
        resp[i.name] = temp
    return Response(resp)