from django.shortcuts import render,redirect, HttpResponse 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from adminApp.models import *


# Create your views here.
# Create your views here.
print("hi")

# after the admin Registations submited message page ------start
@login_required
def admin_register_message(request):
    return render(request, 'admin_file/register_message.html')
# after the admin Registations submited message page-------end


# Admin Registrations Page --------Start
def admin_signup_page(request):
    if request.method == "POST":
        admin_fullName = request.POST.get('fullname')
        admin_userName = request.POST.get('username')
        admin_mail = request.POST.get('email')
        admin_phoneNumber = request.POST.get('phone_number')
        admin_pass = request.POST.get('password')
        admin_confirmPass = request.POST.get('confirm_password')

        adminUser = Admin_Panel.objects.create_user(
            username=admin_userName, 
            password=admin_confirmPass,
            email=admin_mail,
        )
        adminUser.display_name = admin_fullName
        adminUser.admin_phone_number = admin_phoneNumber
        adminUser.save()

        return redirect("admin_register_message")

    return render(request, "admin_file/signup.html")
# Admin Registrations Page -------end


# Admin Login Page -------Start
def admin_login_page(request):
    if request.method == "POST":
        ad_userName = request.POST.get('username')
        ad_logPass = request.POST.get('password')
        adminUser_log = authenticate(username = ad_userName, password = ad_logPass)

        if adminUser_log is not None:
            login(request, adminUser_log)
            return redirect("admin_home_page")
        else:
            return render(request, 'admin_file/login.html')
        
    return render(request, "admin_file/login.html")
# Admin Login Page -------End


# Admin LogOut Page -------Start
@login_required
def admin_logout(request):
    return redirect("admin_login_page")
# Admin LogOut Page -------End


# Admin Home Page -------Start
@login_required
def admin_home_page(request):
    return render(request, 'admin_file/adminhome.html')
# Admin Home Page -------End


# Add Medicine Information Page -------Start
@login_required
def add_medicine(request):
    if request.method == "POST":
        med_Name = request.POST.get('medicine_name')
        med_Company_Name = request.POST.get('company_name')
        med_Price = request.POST.get('med_price')
        med_Description = request.POST.get('med_descriptions')
        med_Image = request.FILES.get('medicine_image')  # Use FILES for file uploads

        # Validate form data
        if med_Name and med_Company_Name and med_Price and med_Description and med_Image:
            medicine = Add_Medicine_Info(
                medicine_title=med_Name,
                medicine_company_name=med_Company_Name,
                medicine_price=med_Price,
                medicine_discription=med_Description,
                medicine_image=med_Image
            )
            medicine.save()
            return redirect("add_medicine")

    return render(request, 'admin_file/addmed.html')
# Add Medicine Information Page -------end




# Add Blog Page -------Start
@login_required
def add_blog(request):
    if request.method == "POST":
        blog_Title = request.POST.get('blog_title')
        blog_Article = request.POST.get('blog_article')
        blog_Image = request.FILES.get('blog_image')  # Use FILES for file uploads

        # Validate form data
        if blog_Title and blog_Article and blog_Image:
            blog = Add_Blog(
                blog_title=blog_Title,
                blog_article=blog_Article,
                blog_image=blog_Image,
            )
            blog.save()
            return redirect("add_blog")

    return render(request, 'admin_file/addblog.html')
# Add Blog Page -------End



@login_required
def admin_profile(request,id):
    prof = Admin_Panel.objects.get(id =id)
    context ={
        'prof':prof,
    }

    return render(request, 'admin_file/adminprofile.html',context)

@login_required
def view_medicine_info(request):
    med = Add_Medicine_Info.objects.all()
    context = {
        'medicine': med
    }
    return render(request, 'admin_file/view_med_info.html', context)


@login_required
def update_med_info(request, myid):
    medicine=Add_Medicine_Info.objects.filter(id=myid)
    context={
        "um": medicine
    }
    if request.method == "POST":
        med_Name = request.POST.get('medicine_name')
        med_Company_Name = request.POST.get('company_name')
        med_Price = request.POST.get('med_price')
        med_Description = request.POST.get('med_descriptions')
        med_Image = request.FILES.get('medicine_image')  # Use FILES for file uploads

        # Validate form data
        if med_Name and med_Company_Name and med_Price and med_Description and med_Image:
            medicine = Add_Medicine_Info(
                medicine_title=med_Name,
                medicine_company_name=med_Company_Name,
                medicine_price=med_Price,
                medicine_discription=med_Description,
                medicine_image=med_Image
            )
            medicine.save()
            return redirect("view_medicine_info")
    return render(request, 'admin_file/updateMed.html', context)



def delete_med_info(request, myid):
    medicine=Add_Medicine_Info.objects.filter(id=myid)
    medicine.delete()
    return redirect("view_medicine_info")



@login_required
def view_blog(request):
    blog = Add_Blog.objects.all()
    context = {
        'blog': blog
    }
    return render(request, 'admin_file/view_blog.html',context)


@login_required
def update_blog(request, myid):
    blog=Add_Blog.objects.filter(id=myid)
    context={
        "ub": blog
    }
    return render(request, 'admin_file/update_blog.html', context)


def delete_blog(request, myid):
    blog=Add_Blog.objects.filter(id=myid)
    blog.delete()
    return redirect("view_blog")