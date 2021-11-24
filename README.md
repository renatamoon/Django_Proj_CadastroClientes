# Django_Proj_CadastroClientes

CADASTRO DE CLIENTES + CRUD

<i>REGISTER AND CRUD OF CUSTOMERS</i>

<p align="center">
  <a href="#projeto">Sobre o projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#tecnologias">Tecnologias utilizadas</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#instalacao">Como Executar o projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp; 
  <a href="#imagens">Imagens</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp; 
 
</p>

## <a id="projeto"> 💻 SOBRE ESTE PROJETO </a>

Projeto com finalidade de fazer cadastro de clientes com seus respectivos dados (nome, email, sexo, profissão e observações sobre os mesmos).
Abaixo algumas funcionalidades:
  
    *Funcionalidade de cadastro usando formulários do bootstrap;
    *Listagem dos clientes cadastrados;
    *CRUD;
    *Listagem dos dados dos clientes cadastrados por ID.

> 🟩 Status do projeto: FINALIZADO <br>

<hr>
  
  ## <a id="tecnologias"> 🧪 TECNOLOGIAS UTILIZADAS NESTE PROJETO </a>

Front-End:

![HTML 5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)

Desenvolvimento da parte do Back End:

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)

Banco de Dados:

![MySQL](https://img.shields.io/badge/MySQL-00000F?style=for-the-badge&logo=mysql&logoColor=white)

Desenvolvido no:

![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)

<hr>

## <a id="instalacao"> 🔴 PASSO A PASSO DE COMO EXECUTAR A APLICAÇÃO </a> 

*No Windows

<b>-Clone o repositório com o camando:</b> `https://github.com/renatamoon/Django_Proj_CadastroClientes.git` <br>
<b>-Criando virtual environment:</b> `python -m venv venv`<br>
<b>-Ativando o virtual environment: </b>`. venv\Scripts\Activate.ps1`<br>
<b>Obs: Caso ocorra um erro na ativação:</b> entre no powershell e digite o seguinte comando: `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`<br>
<b>-Execução do arquivo requirements: </b>`pip install -r requirements.txt`<br>

*No Linux:

<b>-Baixe o repositorio<br>
<b>-Criando virtual environment:</b> `virtualenv venv`<br>
<b>-Ativando o virtual environment:</b> `. venv/bin/activate`<br>
<b>-Execução do arquivo requirements e instalar dependencias:</b> `pip install -r requirements.txt`<br>
  
 <hr> 
  
*Alterar as configurações do DataBase no arquivo <b>`settings.py`</b> <br>

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'host_bd',
        'PORT': 'porta_bd',
        'NAME': 'ediaristas',
        'USER': 'usuario_bd',
        'PASSWORD': 'senha_bd'    
    }
}
```

 *Migre o banco de dados com: `python manage.py migrate` <br>
 *Execute o servidor: `python manage.py runserver` <br>
  
------

# <a id="imagens">IMAGENS DO PROJETO</a> 
  
------

Tela inicial do projeto onde mostra todos os clientes cadastrados:

![image](https://user-images.githubusercontent.com/87100340/138941087-416f5659-8608-4813-85ba-cee03b53f66b.png)

*CAMPO DE ADICIONAR E REMOVER:

![image](https://user-images.githubusercontent.com/87100340/138941154-982e970c-2b9d-4735-9f72-1e736345486f.png)

*MOSTRANDO OS DADOS DOS CADASTROS DOS CLIENTES:

![image](https://user-images.githubusercontent.com/87100340/138941520-0efa5554-f978-4060-8be1-86217688bacd.png)

*CAMPO DE EXCLUSÃO DOS DADOS:
Duas opções são dadas caso não queira fazer a remoção ou caso realmente deseja prosseguir:

![image](https://user-images.githubusercontent.com/87100340/138941646-50b91624-716e-44ab-be0a-e5e6285fef6e.png)

*Rotas:
```  
  urlpatterns = [
    path('listar', listar_clientes, name='listar_clientes'),
    path('cadastrar', inserir_cliente, name='cadastrar_cliente'),
    path('listar/<int:id>', listar_cliente_id, name='listar_cliente_id'),
    path('editar/<int:id>', editar_cliente, name='editar_cliente'),
    path('remover/<int:id>', remover_cliente, name='remover_cliente')
]
  ```
-código para a tela de exclusão:

  ```
  def editar_cliente(request, id):
    cliente_antigo = cliente_service.listar_cliente_id(id)
    form = ClienteForm(request.POST or None, instance=cliente_antigo)
    if form.is_valid():
        nome = form.cleaned_data["nome"]
        sexo = form.cleaned_data["sexo"]
        data_nascimento = form.cleaned_data["data_nascimento"]
        email = form.cleaned_data["email"]
        profissao = form.cleaned_data["profissao"]
        observacao = form.cleaned_data["observacao"]
        cliente_novo = cliente.Cliente(nome=nome, sexo=sexo, data_nascimento=data_nascimento, email=email,
                                       profissao=profissao, observacao=observacao)
        cliente_service.editar_cliente(cliente_antigo, cliente_novo)
        return redirect('listar_clientes')
    return render(request, 'clientes/form_cliente.html', {'form': form})

def remover_cliente(request, id):
    cliente = cliente_service.listar_cliente_id(id)
    if request.method == "POST":
        cliente_service.remover_cliente(cliente)
        return redirect('listar_clientes')
    return render(request, 'clientes/confirma_exclusao.html', {'cliente': cliente})

 ```

