from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadForm
from .operacoes import tratar_file, lista_operacoes
from .models import Loja

def index(request):
    return render(request, 'index.html')

    def get_list():
        operacao()

def upload(request):

    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            result = tratar_file(request, file)
            return HttpResponseRedirect('', {'messages': result})
    else:
        form = UploadForm()
        return render(request, 'upload.html', {'form': form})



def operacao(request):

    lojas = Loja.objects.all()
    context = lista_operacoes(lojas)

    context = {
        'context': context
    }

    return render(request, 'operacao.html', context)


