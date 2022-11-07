from django.shortcuts import render, redirect
from dashboard.forms import DataForm
from dashboard.models import Data
# Create your views here.


def index(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-prediction')
    else:
        form = DataForm()
    context = {'form':form}
    return render(request, 'dashboard/index.html',context)


def prediction(request):
    data = Data.objects.all()
    context = {'data':data}

    return render( request, 'dashboard/prediction.html',context)
