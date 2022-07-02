from django.db import models
#class formcontact(models.Model):
    #fname=models.CharField(max_length=30)
    #lname=models.CharField(max_length=30)
    #email=models.CharField(max_length=30)
    #phone=models.CharField(max_length=30)
    #def _unicode_(self):
            #return self.name

class logindetails(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    mobile=models.CharField(max_length=30)
    def _unicode_(self):
        return self.name
class carddetails(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    pincode=models.CharField(max_length=30)
    pname=models.CharField(max_length=30)
    pid=models.CharField(max_length=30)
    quantity=models.CharField(max_length=30)
    price=models.CharField(max_length=30)
    cardnum=models.CharField(max_length=30)
    cardname=models.CharField(max_length=30)
    edate=models.CharField(max_length=30)
    cvv=models.CharField(max_length=30)
    def _unicode_(self):
        return self.name
class signupdetails(models.Model):
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    def _unicode_(self):
        return self.name
class Customer_delivery(models.Model):
    dname=models.CharField(max_length=10)
    address=models.CharField(max_length=30)
    pname=models.CharField(max_length=30)
    pincode=models.CharField(max_length=30)
    rname=models.CharField(max_length=30)
    delivery_date=models.DateField()
    def _unicode_(self):
        return self.name
class Customer_orders(models.Model):
    name=models.CharField(max_length=10)
    email=models.CharField(max_length=60)
    mobile=models.CharField(max_length=60)
    pname=models.CharField(max_length=30)
    quantity=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    city=models.CharField(max_length=60)
    card_num=models.CharField(max_length=30)
    order_date=models.DateField()
class Product(models.Model):
    name=models.CharField(max_length=10)
    price=models.CharField(max_length=30)
    Customer_orders=models.ManyToManyField(Customer_orders)
    Customer_delivery=models.ForeignKey(Customer_delivery,models.CASCADE,default="")
    Expiry_date=models.DateField()
    review=models.CharField(max_length=30)
    website=models.CharField(max_length=60)
class student(models.Model):
    s_id=models.CharField(max_length=20)
    name=models.CharField(max_length=30)
    sub_mark1=models.CharField(max_length=30)
    sub_mark2=models.CharField(max_length=30)
    sub_mark3=models.CharField(max_length=30)
    Total=models.CharField(max_length=30)
    avg=models.CharField(max_length=30)
    def _unicode_(self):
        return self.name	
class employee(models.Model):
    e_id=models.CharField(max_length=20)
    name=models.CharField(max_length=30)
    age=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    salary=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    dept=models.CharField(max_length=30)
    def _unicode_(self):
        return self.name
