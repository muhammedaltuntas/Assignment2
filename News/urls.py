"""News URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('NewsCategory/', newscategorylist, name='categorylist'),
    path('NewsPost/', newspostlist, name='postlist'),
    path('NewsPostComment/', newspostcommentlist, name='commentlist'),

    path('NewsCategory/Detail/<int:category_id>', newscategorydetail, name='categorydetail'),
    path('NewsPost/Detail/<int:post_id>', newspostdetail, name='postdetail'),
    path('NewsPost/Detail/p/<slug:categoryname>', newspostcategorydetail, name='postcategoryname'),
    path('NewsPostComment/Detail/<int:comment_id>', newspostcommentdetail, name='commentdetail'),

    path('NewsPost/activate/<int:post_id>', activatepost, name='isactivepost'),
    path('NewsCategory/activate/<int:category_id>', activatecategory, name='isactivecategory'),
    path('NewsPostComment/activate/<int:comment_id>', activatecomment, name='isactivecomment')

]
