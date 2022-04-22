from django.shortcuts import render,redirect
from .models import Customer, Reseller

# Create your views here.


def common_home(request):
    return render(request, 'commonapp/common_home.html')


def customer_login(request):

    if request.method =='POST':
        cust_name=request.POST['uname']
        cust_password=request.POST['password']
        user_data=Customer.object.get(user_name=cust_name,password=cust_password)
        if user_data:
            return redirect()
    return render(request, 'commonapp/customer_login.html')
    
        
    


def reseller_login(request):
    return render(request, 'commonapp/reseller_login.html')


def reseller_signup(request):
    if request.method == 'POST':
        rese_name = request.POST['name']
        rese_email = request.POST['email']
        rese_address = request.POST['address']
        rese_mobile = request.POST['mobile']
        rese_adhar = request.POST['adhar']
        rese_h_name = request.POST['h_name']
        rese_a_number = request.POST['a_number']
        rese_ifsc = request.POST['ifsc']
        rese_user_name = request.POST['user_name']
        rese_password = request.POST['password']
        obj = Reseller(name=rese_name, email=rese_email, address=rese_address, mobile_number=rese_mobile, adhar_num=rese_adhar,
                       bank_holder_name=rese_h_name, account_number=rese_a_number, ifsc_code=rese_ifsc, user_name=rese_user_name, password=rese_password)
        obj.save()
    return render(request, 'commonapp/reseller_signup.html')


def customer_signup(request):

    if request.method == 'POST':

        cust_name = request.POST['name']
        cust_address = request.POST['address']
        cust_email = request.POST['email']
        cust_mobile_number = request.POST['mobile']
        cust_user_name = request.POST['user_name']
        cust_password = request.POST['password']
        obj = Customer(name=cust_name, address=cust_address, email=cust_email,
                       mobile_number=cust_mobile_number, user_name=cust_user_name, password=cust_password)
        obj.save()
    return render(request, 'commonapp/customer_signup.html')


def add_product(request):
    return render(request, 'commonapp/add_product.html')
