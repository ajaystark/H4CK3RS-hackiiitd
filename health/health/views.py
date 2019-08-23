from django.views import generic
from django.shortcuts import render
from django.core.mail import send_mail

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
        return render(request,self.template,{'lat':lat,'long':long})
        # return 0

class help(generic.View):
    template="help.html"
    def get(self,request):
        return render(request,self.template)
    def post(self,request):
        print(request.POST)
        return redirect("search")