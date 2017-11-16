from __future__ import unicode_literals

from django.db import models

class UserManager(models.Manager):
	def printout(self):
		print("yas ----------------------")
		# User.objects.create(first_name = "ethan", last_name = "TU", email = "ethan@agh.com")
		# User.objects.create(first_name = "David", last_name = "TU", email = "david@agh.com")
		# User.objects.create(first_name = "Lucio", last_name = "TU", email = "lucio@agh.com")
		# User.objects.create(name="The Beast", desc="This book is very scary", user=User.objects.get(id=1))
		# User.objects.create(name="Ninja Manual", desc="Learn to hidde like a boss", user=User.objects.get(id=1))
		# User.objects.create(name="PHP CookBook", desc="Recipes for a delicious source code", user=User.objects.get(id=2))
		# User.objects.create(name="Drinking Java", desc="Toast it, Grind it, Code it", user=User.objects.get(id=2))
		# User.objects.create(name="Hacking The Web", desc="This book will get you in trouble, fool!", user=User.objects.get(id=3))
		# User.objects.create(name="Syntax", desc="Forma your writing...", user=User.objects.get(id=3))
		# Book.objects.get(id=1).likes = User.objects.get(id=1)
		# Book.objects.get(id=6).likes = User.objects.get(id=1)
		# Book.objects.get(id=1).likes = User.objects.get(id=2)
		# Book.objects.get(id=3).likes = User.objects.get(id=2)
		# User.objects.get(id=3).likes = Books.objects.all()
		# User.objects.get(likes = Books.objects.get(id=1))
		# User.objects.get(id == Books.objects.get(id=1))
		# User.objects.get(likes = Books.objects.get(id=2))
		# User.objects.get(id == Books.objects.get(id=2))
		return {'success': user}


class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()

class Books(models.Model):
	name = models.CharField(max_length=255)
	desc = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(User, related_name="books")
	likes = models.ManyToManyField(User, related_name="users")