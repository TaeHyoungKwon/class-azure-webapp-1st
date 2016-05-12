from django.shortcuts import render

# Create your views here.
def home(request):

	return render(request, 'home/home.html', {})


def rule(request):

	return render(request, 'home/rule.html', {})	



def tree(request):

	return render(request, 'home/tree.html', {})	

