from django.contrib import admin
#from my_app1.models import formcontact
from my_app1.models import logindetails
from my_app1.models import signupdetails
from my_app1.models import carddetails
#admin.site.register(formcontact)
from my_app1.models import Product
from my_app1.models import Customer_orders
from my_app1.models import Customer_delivery
from my_app1.models import student
from my_app1.models import employee
admin.site.register(logindetails)
admin.site.register(signupdetails)
admin.site.register(carddetails)
admin.site.register(Product)
admin.site.register(Customer_orders)
admin.site.register(Customer_delivery)
admin.site.register(student)
admin.site.register(employee)


