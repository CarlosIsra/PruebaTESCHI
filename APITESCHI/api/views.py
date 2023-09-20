from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.


class home (APIView):
    template_name="index.html"
    def get (self, resques):
        return render(resques, self.template_name)
class inicio (APIView):
    template_name="inicio.html"
    def get (self, resques):
        return render(resques,self.template_name )
        
            