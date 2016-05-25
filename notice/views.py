from django.shortcuts import render,get_object_or_404,render_to_response
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from .models import Post, Comment
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.http import HttpResponseRedirect
from .forms import CommentForm
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


def post_list(request):
    queryset_list =Post.objects.all().order_by('-created_at')
    query=request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query)|
            Q(content__icontains=query)|
            Q(name__icontains=query)
                ).distinct()
    paginator = Paginator(queryset_list, 10)
    page = request.GET.get('page') 

    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
    # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)  
    
    context ={
        "object_list":queryset,
        "title":"List"
    }
    
    return render(request,"notice/post_list.html",context)

def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    post.hit += 1
    post.save()
    return render(request, 'notice/post_detail.html',{'post':post,})	


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'notice/add_comment.html'

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = get_object_or_404(Post, pk=self.kwargs['post_pk'])
        comment.author = self.request.user
        comment.save()
        return super(CommentCreateView, self).form_valid(form)


comment_new = login_required(CommentCreateView.as_view(model=Comment,form_class=CommentForm,template_name = 'notice/add_comment.html'))
comment_edit = login_required(UpdateView.as_view(model=Comment, form_class=CommentForm,template_name = 'notice/edit_comment.html'))
comment_delete = login_required(DeleteView.as_view(model=Comment,success_url=reverse_lazy('notice:post_list')))