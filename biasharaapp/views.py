from django.shortcuts import render,redirect
from biasharaapp.models import Member
from biasharaapp.forms import ProductsForm
from biasharaapp.models import Products
# Create your views here.
def register(request):
    if request.method == 'POST':
        member = Member(firstname=request.POST['firstname'], lastname=request.POST['lastname'],
                        email=request.POST['email'],
                        username=request.POST['username'],
                        password=request.POST['password'])
        member.save()
        return redirect('/')
    else:
        return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')

def index(request):
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'],
                                 password=request.POST['password']).exists():
            member = Member.objects.get(username=request.POST['username'],
                                        password=request.POST['password'])
            return render(request, 'index.html',{'member': member})
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')
def inner(request):
    return render(request, 'inner-page.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request,'services.html')

def departments(request):
    return render(request,'departments.html')

def doctors(request):
    return render(request,'Doctors.html')
def contacts(request):
    return render(request,'Contacts.html')

def home(request):
    return render(request, 'home.html')
    
def add(request):
    if request.method == "POST":
        form = ProductsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = ProductsForm()
        return render(request,'addproducts.html', {'form': form})

def show(reuqest):
    products = Products.objects.all()
    return render(reuqest, 'show.html', {'products': products})

def delete(request, id):
    product = Products.objects.get(id=id)
    product.delete()
    return redirect('/show')

def edit(request, id):
    product =Products.objects.get(id=id)
    return render(request, 'edit.html', {'product': product})

def update(request, id):
    product = Products.objects.get(id=id)
    form = ProductsForm(request.POST, instance=Products)
    if form.is_valid():
        form.save()
        return redirect('/show')
    else:
        return render(request, 'edit.html', {'product': product})


