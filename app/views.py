from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.generic import FormView

from app.models import *

def newscategorylist(request):
    try:
        categoryall = NewsCategory.objects.all()
    except NewsCategory.DoesNotExist:
        raise Http404("News Category does not exist")
    return render(request, 'NewsCategory/index.html', {'categoryall': categoryall })
def newscategorydetail(request,category_id):
    try:
        newscategory = NewsCategory.objects.get(pk=category_id)
    except NewsCategory.DoesNotExist:
        raise Http404("News Category does not exist")
    return render(request, 'NewsCategory/detail.html', {'newscategory': newscategory })

def newspostlist(request):
    try:
        newspost = NewsPost.objects.all()
    except NewsPost.DoesNotExist:
        raise Http404("News Post does not exist")
    return render(request, 'NewsPost/index.html', {'newspost': newspost })

def newspostdetail(request,post_id):
    try:
        postdetail = NewsPost.objects.get(pk=post_id)
    except NewsPost.DoesNotExist:
        raise Http404("Post does not exist")
    return render(request, 'NewsPost/detail.html', {'postdetail': postdetail})

def newspostcategorydetail(request,categoryname):
    try:
        postdetail = NewsPost.objects.filter(category=categoryname)
    except NewsPost.DoesNotExist:
        raise Http404("Post does not exist")
    return render(request, 'NewsPost/detail.html', {'postdetail': postdetail})


def newspostcommentlist(request):
    try:
        if request.method=='POST':
            pass
        postcommentlist = NewsPostComment.objects.all()
    except NewsPostComment.DoesNotExist:
        raise Http404("Post Comment does not exist")
    return render(request, 'NewsPostComment/index.html', {'postcommentlist': postcommentlist})
def newspostcommentdetail(request,comment_id):
    try:
        postcomment = NewsPostComment.objects.get(pk=comment_id)
    except NewsPostComment.DoesNotExist:
        raise Http404("Post Comment does not exist")
    return render(request, 'NewsPostComment/detail.html', {'postcomment': postcomment})


def activatepost(request, post_id):
    post = NewsPost.objects.get(pk=post_id)
    try:
        selected_post = NewsPost.objects.get(pk=request.POST['post'])
    except(KeyError, NewsPost.DoesNotExist):
        return render(request, "NewsPost/detail.html", {"postdetail":post})
    else:
        selected_post.isactive= True
        selected_post.save()
        return render(request, "NewsPost/detail.html", {"postdetail":post})

def activatecategory(request, category_id):
    cat = NewsCategory.objects.get(pk=category_id)
    try:
        selected_cat = NewsCategory.objects.get(pk=request.POST['post'])
    except(KeyError, NewsCategory.DoesNotExist):
        return render(request, "NewsCategoryexit"
                               "/detail.html", {"category":cat})
    else:
        selected_cat.isactive= True
        selected_cat.save()
        return render(request, "NewsCategory/detail.html", {"category":cat})

def activatecomment(request, comment_id):
    postcomment = NewsPostComment.objects.get(pk=comment_id)
    try:
        selected_postcomment = NewsPostComment.objects.get(pk=request.POST['post'])
    except(KeyError, NewsPostComment.DoesNotExist):
        return render(request, "NewsPostComment/detail.html", {"postcomment":postcomment})
    else:
        selected_postcomment.isactive= True
        selected_postcomment.save()
        return render(request, "NewsPostComment/detail.html", {"postcomment":postcomment})
