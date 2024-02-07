from django.shortcuts import render,redirect, HttpResponse 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

from userApp.models import *
from adminApp.views import *
from media import *
from adminApp.models import *



# after the admin Registations submited message page ------start
@login_required
def admin_register_message(request):
    return render(request, 'admin_file/register_message.html')
# after the admin Registations submited message page-------end

# user Registrations Page --------Start


def user_signup_page(request):
    if request.method == "POST":
        user_fullName = request.POST.get('fullname')
        user_userName = request.POST.get('username')
        user_mail = request.POST.get('email')
        user_phoneNumber = request.POST.get('phone_number')
        user_pass = request.POST.get('password')
        user_confirmPass = request.POST.get('confirm_password')

        # Create a new instance of User_Model and save it to the database
        user = User_Model.objects.create(
            users_full_name=user_fullName,
            user_username=user_userName,
            user_email=user_mail,
            user_phone_number=user_phoneNumber,
            user_password=user_pass,
            user_confirm_password=user_confirmPass,
        )

        # Optional: You might want to save the instance again if you have overridden the save method in your model.
        user.save()

        return redirect("user_login_page")

    return render(request, "user_file/signup.html")

# user Registrations Page -------end



# user Login Page -------Start
def user_login_page(request):
    if request.method =="POST":
        myusername = request.POST.get('username')
        mypassword = request.POST.get('password')
        
        user = authenticate(username=myusername,password=mypassword)
        print(user)
        print(myusername)
        print(mypassword)
        
        if user:
            login(request, user)
        return redirect('home_page')
        
    return render(request, "user_file/login.html")
# user Login Page -------End
def user_profile(request,id):
    prof = User_Model.objects.get(id =id)
    context ={
        'prof':prof,
    }
    return render(request,'user_file/user_prof.html',context)


def user_logout(request):
    logout(request)
    return redirect('home_page')


# Home page Start 
def home_page(request):
    med = Add_Medicine_Info.objects.all()
    blog = Add_Blog.objects.all()
    context = {
        'medicine': med , 
        'blog' : blog
    }
    
    return render(request, "user_file/index.html", context)
# Home page end 


# About page Start 
def about_page(request):
    return render(request, 'user_file/about.html')
# About page end 


# About page Start 
def category_page(request):
    return render(request, 'user_file/category.html')
# About page end 


# blog page Start 
def blog_page(request):
    blog = Add_Blog.objects.all()
    context = {
        'blog': blog
    }
    return render(request, 'user_file/blog.html', context)
# blog page end 


# contact page Start 
def contact_page(request):
    if request.method == "POST":
        contact_name = request.POST.get('name')
        contact_mail = request.POST.get('email')
        contact_message = request.POST.get('message')

        contact = Contact_Model.objects.create(
            contact_full_name = contact_name,
            contact_email = contact_mail,
            contact_message = contact_message,
        )
        contact.save()
        return redirect("contact_page")
    return render(request, 'user_file/contactUs.html')
# contact page end 


# medicine page Start 
def medicine_page(request):
    med = Add_Medicine_Info.objects.all()
    context = {
        'medicine': med
    }
    return render(request, 'user_file/medicine.html', context)
# medicine page end 


# Add this view in your views.py file


def search_results(request):
    search_query = request.GET.get('search', '')

    # Perform the search based on your model and fields
    if search_query:
        # Assuming you have a 'name' field in your Medicine model
        results = Add_Medicine_Info.objects.filter(medicine_title__icontains=search_query)
        results_2 = Add_Blog.objects.filter(blog_title__icontains=search_query)

    else:
        results = []
        results_2= []

    context = {
        'search_query': search_query,
        'results': results,
        'results_2': results_2,
    }

    return render(request, 'user_file/search_results.html', context)











def product_order_page(request, myid):
    order_med=Add_Medicine_Info.objects.filter(id=myid)
    context={
        "om": order_med
    }
    if request.method == "POST":
        order_fullName = request.POST.get('fullName')
        order_phoneNumber = request.POST.get('phoneNumber')
        order_mail = request.POST.get('email')
        order_address = request.POST.get('address')
        order_address2 = request.POST.get('address2')
        order_location = request.POST.get('location')
        order_receivedQuantity = request.POST.get('receivedQuantity')
        order_remarks = request.POST.get('remarks')

        try:
            order = Order_Model.objects.create(
                order_full_name=order_fullName,
                order_phone_number=order_phoneNumber,
                order_email=order_mail,
                order_address=order_address,
                order_address2=order_address2,
                order_location=order_location,
                order_quantity=order_receivedQuantity,
                order_remark=order_remarks,
            )
            messages.success(request, 'Order submitted successfully.')
        except Exception as e:
            print(f"Error creating/saving order: {e}")
            messages.error(request, 'Error submitting order. Please try again.')

        return redirect("admin_register_message")
    
    return render(request, 'user_file/order.html',context)



def add_to_cart(request, myid):
    addcart=Add_Medicine_Info.objects.filter(id=myid)
    context={
        "ac": addcart,
    }
    return render(request, 'user_file/add-to-cart.html', context)
