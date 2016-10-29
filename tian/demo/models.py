#coding=utf-8
from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class goodKinds(models.Model):
	'''
	'''	
	kinds = models.CharField(max_length=20)
	def __str__(self):
		return self.kinds.encode('utf8')

class goodsInfo(models.Model):
	'''
	'''	
	name = models.CharField(max_length=20)
	pic = models.ImageField(upload_to='demo/media')		#no img
	price = models.FloatField(default=0.0)
	intro = models.TextField()	
	describe = 	HTMLField() 
	kucunliang = models.IntegerField(default=100)
	goodKinds = models.ForeignKey('goodKinds')

	def __str__(self):
		return self.name.encode('utf8')

class user(models.Model):
	'''
	'''	
	name = models.CharField(max_length=20)
	passwd = models.CharField(max_length=20)
	mail = models.CharField(max_length=20)
	phone =	models.CharField(max_length=20)
	# history = models.CharField(max_length=20) 
	'''
	history should create a single table not a field
	history should be a list, not know if is a charfield
	'''

	def __str__(self):
		return self.name.encode('utf8')

class user_history(models.Model):

	goods_id = models.ForeignKey('goodsInfo')
	user_id = models.ForeignKey('user')

	def __str__(self):
		return self.user_id.encode('utf8')

class user_addr(models.Model):
	'''
	'''	
	name = models.CharField(max_length=20)
	addr = models.CharField(max_length=45)
	postcode = models.CharField(max_length=20)
	phone =	models.CharField(max_length=20)
	user_id = models.ForeignKey('user')
	'''
	history shoud be a list, not know if is a charfield
	'''

	def __str__(self):
		return self.name.encode('utf8')


class shoppingCart(models.Model):
	'''
	'''	
	goods_id = models.ForeignKey('goodsInfo')
	user_id = models.ForeignKey('user')
	goods_num = models.IntegerField()
	totalprice = models.FloatField(default=0.0)

	def __str__(self):
		return self.goods_num.encode('utf8')

class order(models.Model):
	date = models.DateTimeField(auto_now_add=True)
	user_id = models.ForeignKey('user')
	state = models.BooleanField(default=False)
	totalprice = models.FloatField(default=0.0)


	def __str__(self):
		return self.date.encode('utf8')


class order_goods(models.Model):
	'''
	'''	
	goods_id = models.ForeignKey('goodsInfo')
	order_id = models.ForeignKey('order')
	goods_num = models.IntegerField()
	cur_price = models.IntegerField()

	def __str__(self):
		return self.goods_num.encode('utf8')