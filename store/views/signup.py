from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password
from django.views import View


class Signup(View):
    def get(self, request):
        if request.method == 'GET':
            return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('fname')
        last_name = postData.get('lname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None
        # object Creation of customer class
        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)

        error_message = self.validateCustomer(customer)

        if not error_message:
            print((first_name, last_name, phone, email, password))
            customer.password = make_password(customer.password)
            customer.register()  # save data to the server using register fun (register fun created in customer model)
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
        # Validation
        error_message = None
        if not customer.first_name:
            error_message = "First Name Required !!"
        elif len(customer.first_name) < 4:
            error_message = "First Name must be 4 char or more"
        elif not customer.last_name:
            error_message = "Last Name Required !!"
        elif len(customer.last_name) < 4:
            error_message = "Last Name must be 4 char or more"
        elif not customer.phone:
            error_message = "Phone Number Required !!"
        elif len(customer.phone) < 10:
            error_message = "Phone Number must be 10  or more"
        elif not customer.password:
            error_message = "Password Required!!"
        elif len(customer.password) < 8:
            error_message = "Password Should be minimum 8 char"
        elif customer.isEmailExists():
            error_message = "Email alreday Registered..."

            return error_message