from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import HomeForm
from MyCalculator.models import Calculations



# Create your views here.

class HomePage(TemplateView):
    template_name= 'MyCalculator/home.html'
    model = Calculations
    
    def get(self,request,*args,**kwargs):
        form = HomeForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self,request):
        form = HomeForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['num1']
            text2 = form.cleaned_data['num2']
            answer = text + text2

            calc = Calculations(calc1=text, calc2 = text2, result= answer)
            calc.save()
            form = HomeForm()
        history = self.history_list(request)
        return render (request, self.template_name, {'form':form, 'result': answer, 'hist': history})

    def history_list(self,request):
        history = Calculations.objects.all()
        return history