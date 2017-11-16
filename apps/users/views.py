from django.shortcuts import render, redirect
from models import *
# Create your views here.
def index(request):
	User.objects.create(first_name = "ethan", last_name = "TU", email = "ethan@agh.com")
	User.objects.create(first_name = "David", last_name = "TU", email = "david@agh.com")
	User.objects.create(first_name = "Lucio", last_name = "TU", email = "lucio@agh.com")
	# Books.objects.create(name="The Beast", desc="This book is very scary", user=User.objects.get(id=1))
	# Books.objects.create(name="Ninja Manual", desc="Learn to hidde like a boss", user=User.objects.get(id=1))
	# Books.objects.create(name="PHP CookBook", desc="Recipes for a delicious source code", user=User.objects.get(id=2))
	# Books.objects.create(name="Drinking Java", desc="Toast it, Grind it, Code it", user=User.objects.get(id=2))
	# Books.objects.create(name="Hacking The Web", desc="This book will get you in trouble, fool!", user=User.objects.get(id=3))
	# Books.objects.create(name="Syntax", desc="Forma your writing...", user=User.objects.get(id=3))
	# Book.objects.get(id=1).likes = User.objects.get(id=1)
	# Book.objects.get(id=6).likes = User.objects.get(id=1)
	# Book.objects.get(id=1).likes = User.objects.get(id=2)
	# Book.objects.get(id=3).likes = User.objects.get(id=2)
	# User.objects.get(id=3).likes = Books.objects.all()
	# User.objects.get(likes = Books.objects.get(id=1))
	# User.objects.get(id == Books.objects.get(id=1))
	# User.objects.get(likes = Books.objects.get(id=2))
	# User.objects.get(id == Books.objects.get(id=2))
	context = {
		"user": User.objects.all(),
		"book": Book.objects.all(),
	}
	return render(request, 'users/index.html', context)

def printout(request):

	return redirect('/')

def printall(request):
	context = {
		"user": User.objects.all(),
		"book": Book.objects.all(),
	}
	return render(request, "users/index.html", context)

