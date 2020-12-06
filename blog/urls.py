
from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('create/<slug:user>',views.create,name="create blog"),
    path('getallblogs/',views.getallblogs,name="all blog"),
    path('getblogs/<slug:user>',views.getblogs,name="get user specific blogs"),
    url('^updateblogs/(?P<user>[\w-]+)/(?P<blogname>[\w-]+)$',views.updateblog,name="update specific blogs"),
    # path('updateblogs/<slug:user>/<slug:blogname>',views.updateblog,name="update specific blogs"),
    path('deleteblog/<slug:user>/<slug:blogname>',views.deleteblog,name="delete specific blogs"),
    path('comment/<slug:user>/<slug:blogname>',views.comment,name="comments for specific blogs"),
    path('get_comment/<slug:user>/<slug:blogname>',views.get_comment,name="get_comment"),
    path('deletecomment/<slug:id>',views.delete_comment,name="delete comments"),

    ]