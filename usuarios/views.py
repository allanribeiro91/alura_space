from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms

def login(request):
    form = LoginForms()
    return render(request, 'usuarios/login.html', {"form": form})

def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)
        
        #Verificar se as senhas são iguais
        if form["senha1"].value() != form["senha2"].value()
            return redirect('cadastro')
        
        

    return render(request, 'usuarios/cadastro.html', {"form": form})
