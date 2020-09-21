from django.shortcuts import render
from okay_app.models import Contacts,Upload_Image
from django.views.generic import ListView,DetailView
from okay_app.models import Upload_Image


# Create your views here.
class HomeView(ListView):
    model = Upload_Image
    # paginate_by = 10
    template_name = 'pages/page.html'

class ProductView(DetailView):
    model = Upload_Image
    # paginate_by = 10
    template_name = 'pages/product/product.html'



# def home(request):

#     obj = Upload_Image.objects.all()

#     if request.method == "POST":
#         contactName = request.POST['contactName']
#         contactEmail = request.POST['contactEmail']
#         contactSubject = request.POST['contactSubject']
#         contactMessage = request.POST['contactMessage']
#         # print(contactEmail,contactName,contactMessage)
#         inc = Contacts(contactName=contactName,contactEmail=contactEmail,contactSubject=contactSubject,contactMessage=contactMessage)
#         inc.save()
#     return render(request, 'pages/page.html', {'Images' : obj})

# def product(request):
#     obj = Upload_Image.objects.all()
#     return render(request,'pages/product/product.html',{'Image':obj})
    

# def tea(request):
#     return render(request,'pages/product/tea.html')
# def bowl(request):
#     return render(request,'pages/product/bowl.html')
# def juice(request):
#     return render(request,'pages/product/Juice.html')
# def whisky(request):
#     return render(request,'pages/product/whisky.html')
# def giftset(request):
#     return render(request,'pages/product/giftset.html')

# class ContactHomeView(ListView):
#     template_name = 'pages/service.html'

class ProductListView(ListView):
    model = Upload_Image
    # paginate_by = 10
    template_name = 'pages/service.html'
     
def quality(request):

    return render(request,'pages/product/quality.html')
 



# class AboutView(ListView):
#     template_name = 'pages/about.html'
def contact_form_submit(request):

    # contact =  request.method == "POST":
    contactName = request.POST['contactName']
    contactEmail = request.POST['contactEmail']
    contactSubject = request.POST['contactSubject']
    contactMessage = request.POST['contactMessage']
    print(contactEmail,contactName,contactMessage)
    inc = Contacts(contactName=contactName,contactEmail=contactEmail,contactSubject=contactSubject,contactMessage=contactMessage)
    inc.save()
    return render(request, 'pages/contact.html')
    

def about(request):
    return render(request,'pages/about.html')
        
def contact(request):
    if request.method == "POST":
        contactName = request.POST['contactName']
        contactEmail = request.POST['contactEmail']
        contactSubject = request.POST['contactSubject']
        contactMessage = request.POST['contactMessage']
        print(contactEmail,contactName,contactMessage)
        inc = Contacts(contactName=contactName,contactEmail=contactEmail,contactSubject=contactSubject,contactMessage=contactMessage)
        inc.save()

    return render(request,'pages/contact.html')