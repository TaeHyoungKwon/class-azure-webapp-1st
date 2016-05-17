from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .forms import SignupForm
from django.contrib.auth.forms import UserCreationForm
from django import forms

# Create your views here.
def home(request):

	return render(request, 'home/home.html', {})


def rule(request):

	return render(request, 'home/rule.html', {})	



def tree(request):

	return render(request, 'home/tree.html', {})	



class UserCreateView(CreateView):
	model = User
	form_class = SignupForm
	template_name = 'registration/signup.html'

	def form_valid(self, form):
		user = form.save(commit=False)
		user.save()
		return super(UserCreateView, self).form_valid(form)

user_new = UserCreateView.as_view(model=User,success_url=reverse_lazy('home:signup_ok'))


