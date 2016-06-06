from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Post, Comment
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, CreateView,UpdateView,DeleteView,ListView
from .forms import CommentForm
from django.core.urlresolvers import reverse_lazy,reverse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse


'''
@login_required # must need to do 'login'

#Showing 'monthlypy' list function
def list(request):
	list = Post.objects.all().order_by('-created_date')
	return render(request, 'monthlypy/list.html', {'list': list})
'''
#post_list = login_required(ListView.as_view(model=Post,queryset=Post.objects.all().order_by('-created_date'),paginate_by=5))


#detail = login_required(DetailView.as_view(model=Post))
@login_required
def post_list(request):
    queryset_list =Post.objects.all().order_by('-created_date')
    query=request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query)|
            Q(message__icontains=query)|
            Q(user__username__icontains=query)
                ).distinct()
    paginator = Paginator(queryset_list, 8)
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
    
    return render(request,"monthlypy/post_list.html",context)


@login_required
def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)

    post_id=post.pk
    liked=False

    if request.session.get('has_liked_'+str(post_id), liked):
        liked =True

    post.hit += 1
    post.save()

    return render(request, 'monthlypy/post_detail.html',{'post':post,'liked':liked})

def like_count_blog(request):
    liked = False
    if request.method == 'GET':
        post_id = request.GET['post_id']
        post = Post.objects.get(id=int(post_id))
        if request.session.get('has_liked_'+post_id, liked):
            print("unlike")
            if post.likes > 0:
                likes = post.likes - 1
                try:
                    del request.session['has_liked_'+post_id]
                except KeyError:
                    print("keyerror")
        else:
            print("like")
            request.session['has_liked_'+post_id] = True
            likes = post.likes + 1
    post.likes = likes
    post.save()
    return HttpResponse(likes, liked)





class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'monthlypy/add_comment.html'

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = get_object_or_404(Post, pk=self.kwargs['post_pk'])
        comment.comment_user = self.request.user
        comment.save()
        return super(CommentCreateView, self).form_valid(form)


comment_new = login_required(CommentCreateView.as_view(model=Comment,form_class=CommentForm,template_name = 'monthlypy/add_comment.html'))

comment_edit = login_required(UpdateView.as_view(model=Comment, form_class=CommentForm,template_name = 'monthlypy/edit_comment.html'))

comment_delete = login_required(DeleteView.as_view(model=Comment,success_url=reverse_lazy('monthlypy:post_list')))