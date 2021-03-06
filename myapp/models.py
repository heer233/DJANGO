from django.db import models
from django.utils import timezone

# Create your models here.
class Contact(models.Model):
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	subject=models.CharField(max_length=100)
	message=models.TextField()

	def __str__(self):
		return self.fname

class User(models.Model):
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	mobile=models.CharField(max_length=100)
	address=models.TextField()
	password=models.CharField(max_length=100)
	usertype=models.CharField(max_length=100,default="user")

	def __str__(self):
		return self.fname

class Product(models.Model):
	CHOICE1=(
			('men','men'),
			('women','women'),
			('kids','kids'),
		)
	CHOICE2=(
			('shirt','shirt'),
			('tshirt','tshirt'),
			('jeans','jeans'),
		)
	CHOICE3=(
			('s','s'),
			('m','m'),
			('l','l'),
		)
	CHOICE4=(
			('blue','blue'),
			('black','black'),
			('white','white'),
			('pink','pink'),
			('green','green'),
			('red','red'),
			('yellow','yellow'),
		)
	product_seller=models.ForeignKey(User,on_delete=models.CASCADE)
	product_collection=models.CharField(max_length=100,choices=CHOICE1)
	product_category=models.CharField(max_length=100,choices=CHOICE2)
	product_size=models.CharField(max_length=100,choices=CHOICE3)
	product_color=models.CharField(max_length=100,choices=CHOICE4)
	product_price=models.PositiveIntegerField()
	product_desc=models.TextField()
	product_image=models.ImageField(upload_to="product_image/")

	def __str__(self):
		return self.product_seller.fname+" - "+self.product_collection+" - "+self.product_category


class Wishlist(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	product=models.ForeignKey(Product,on_delete=models.CASCADE)
	date=models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.user.fname+ " - "+self.product.product_collection

class Cart(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	product=models.ForeignKey(Product,on_delete=models.CASCADE)
	date=models.DateTimeField(default=timezone.now)
	product_price=models.PositiveIntegerField()
	product_qty=models.PositiveIntegerField()
	total_price=models.PositiveIntegerField()
	payment_status=models.CharField(max_length=100,default="pending")

	def __str__(self):
		return self.user.fname+ " - "+self.product.product_collection

class Transaction(models.Model):
    made_by = models.ForeignKey(User, related_name='transactions', 
                                 on_delete=models.CASCADE)
    made_on = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True)
    checksum = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.order_id is None and self.made_on and self.id:
            self.order_id = self.made_on.strftime('PAY2ME%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)