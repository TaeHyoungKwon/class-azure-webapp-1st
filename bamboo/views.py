from django.shortcuts import render
from django.utils import timezone
from .models import Post,Comment,User
from django.shortcuts import render, get_object_or_404
from .forms import PostForm,CommentForm
from django.shortcuts import redirect
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView,ListView
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy,reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


#@login_required

'''
def post_list(request):
    posts = Post.objects.all().order_by('-created_date')
    
    return render(request, 'bamboo/post_list.html', {'posts': posts})
'''
'''

'''



def hit_count(request,pk):

    if request.method == 'GET':
        post = get_object_or_404(Post,pk=pk)
        post.hit += 1
        post.save()

    return render(request,post_detail,{'post':post})



#post_list = login_required(ListView.as_view(model=Post,queryset=Post.objects.all().order_by('-created_date'),paginate_by=5))

'''
class PostDetailView(DetailView):
    model=Post

    def get(self,request,pk):
        post = get_object_or_404(Post,pk=self.pk)
        post.hit +=1
        post.save()

        return render(request,post_detail,{'post':post})



post_detail = login_required(DetailView.as_view(model=Post))
'''



def post_list(request):
    queryset_list =Post.objects.all().order_by('-created_date')
    query=request.GET.get("q")

    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query)|
            Q(text__icontains=query)
                ).distinct()
    paginator = Paginator(queryset_list, 5)
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
    
    return render(request,"bamboo/post_list.html",context)


def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    post.hit += 1
    post.save()
    return render(request, 'bamboo/post_detail.html',{'post':post})

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'bamboo/add_post.html'

    def form_valid(self, form):
        posts = form.save(commit=False)
        posts.author = self.request.user
        posts.save()
        return super(PostCreateView, self).form_valid(form)


post_new = login_required(PostCreateView.as_view(model=Post, form_class=PostForm,template_name='bamboo/add_post.html'))
post_edit = login_required(UpdateView.as_view(model=Post, form_class=PostForm,template_name = 'bamboo/post_edit.html'))
post_delete = login_required(DeleteView.as_view(model=Post,success_url=reverse_lazy('bamboo:post_list')))



class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'bamboo/form2_add_comment.html'

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = get_object_or_404(Post, pk=self.kwargs['post_pk'])
        comment.author = self.request.user
        comment.save()
        return super(CommentCreateView, self).form_valid(form)


comment_new = login_required(CommentCreateView.as_view(model=Comment,form_class=CommentForm,template_name = 'bamboo/add_comment.html'))

comment_edit = login_required(UpdateView.as_view(model=Comment, form_class=CommentForm,template_name = 'bamboo/edit_comment.html'))

comment_delete = login_required(DeleteView.as_view(model=Comment,success_url=reverse_lazy('bamboo:post_list')))

