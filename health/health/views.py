from django.views import generic
from django.shortcuts import render
from django.core.mail import send_mail
from health.models import user
class search(generic.View):
    template="search.html"
    def get(self,request):
        lat=request.GET['lat']
        long=request.GET['long']
        message_content="I am in danger, My location is "+"https://maps.google.com/?q="+lat+","+long+"  Please come and help me. You will be rewarded."
        send_mail(
            'Attention',
            message_content,
            'ajay18215@iiitd.ac.in',
            ['ajaycool122@gmail.com'],
            fail_silently=False,
        )
        # return render(request,self.template,{'lat':lat,'long':long})
        return 200

class help(generic.View):
    template="help.html"
    def get(self,request):
        return render(request,self.template)
    def post(self,request):
        print(request.POST)
        return redirect("search")

class signup(generic.View):
    template="help.html"
    def get(self,request):
        name=request.GET.get('name')
        email=request.GET.get('email')
        city=request.GET.get('city')
        number=request.GET.get('number')
        password=request.GET.get('password')
        user.objects.create(name=name,email=email,city=city,number=number,password=password)
        return 200
        

class login(generic.View):
    template="help.html"
    def get(self,request):
        name=request.GET.get('name')
        password=request.GET.get('password')
        user_obj=user.objects.get(name=name)
        print(user_obj.name)
        print(user_obj.password)
        if(user_obj.name==name and user_obj.password==password):
            return 200
        else:
            return 404