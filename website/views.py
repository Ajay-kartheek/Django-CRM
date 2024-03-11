from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .forms import SignUpForm,DOBRangeForm
from .models import Person




def home(request):
    


    #check to see if logging in 
    if request.method == "POST":
        if 'username' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            #Authenticate
            user = authenticate(request, username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request, "You Have Been Logged In!")
                return redirect('home')
            else:    
                messages.success(request, "There Was An Error Logging In , Please Try Again...")
                return redirect('home')
        else:
            if 'show_all' in request.POST:  # Check for separate button click
                records = Person.objects.all()  # Retrieve all records
                form = DOBRangeForm()  # Reset the form
            else:
              # Check for DOB range filter submission
                form = DOBRangeForm(request.POST)  # Pass POST data to the form
                if form.is_valid():
                    start_date = form.cleaned_data['start_date']
                    end_date = form.cleaned_data['end_date']
                    records = Person.objects.filter(DOB__range=(start_date, end_date))
                else:
                    # Handle potential form validation errors (optional)
                    messages.error(request, 'Please enter valid dates for the DOB range.')
    else:
        form = DOBRangeForm()  # Initialize form
        records = Person.objects.all()  # Retrieve all records initially
    
    # Check if user is logged in
    if request.user.is_authenticated:
        return render(request, 'home.html', {'records': records, 'form': form})
    else:
        return render(request, 'home.html')  # Redirect to login page if not authenticated



def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out!")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate and login
            username =  form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,"You have been successfully registerd! Welcome!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request,'register.html',{'form':form})
        
    return render(request,'register.html',{'form':form})


