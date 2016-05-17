from django.shortcuts import render
from django.shortcuts import render,get_object_or_404,render_to_response
from .models import Post,Comment
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import CommentForm
from django.core.urlresolvers import reverse_lazy,reverse


# Create your views here.
def post_list(request):
	post_list = Post.objects.all().order_by('-created_at')
	return render(request, 'notice/post_list.html', {'post_list': post_list})


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


comment_new = CommentCreateView.as_view(model=Comment,form_class=CommentForm,template_name = 'notice/add_comment.html')
comment_edit = UpdateView.as_view(model=Comment, form_class=CommentForm,template_name = 'notice/edit_comment.html')
comment_delete = DeleteView.as_view(model=Comment,success_url=reverse_lazy('notice:post_list'))