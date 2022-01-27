from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic.base import View
from perfis.models import Perfil
from usuarios.forms import RegistrarUsuarioForm

class RegistrarUsuarioView(View):
    template_name = 'registrar.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):

        #preenche o from
        form = RegistrarUsuarioForm(request.POST)

        #verifica se eh valido
        if form.is_valid():

            dados_form = form.data

            #cria o usuario
            usuario = User.objects.create_user(dados_form['nome'], dados_form['email'], dados_form['senha'])            

            #cria o perfil
            perfil = Perfil(nome=dados_form['nome'],
                            telefone=dados_form['telefone'],
                            nome_empresa=dados_form['nome_empresa'],
                            usuario=usuario)

            #grava no banco
            perfil.save()

            #redireciona para index
            return redirect('index')

        #so chega aqui se nao for valido
        #vamos devolver o form para mostrar o formulario preenchido 
        return render(request, self.template_name, {'form' : form})