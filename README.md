# Django_Proj_CadastroClientes

CADASTRO DE CLIENTES + CRUD

<iREGISTER AND CRUD OF CUSTOMERS</i>

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

*paths:

![image](https://user-images.githubusercontent.com/87100340/138941847-bd118ad0-c64a-4b38-b566-e0a5261ff6da.png)

-Html com código Django para a tela de exclusão:

![image](https://user-images.githubusercontent.com/87100340/138941981-7b79b196-57fe-4e0b-9164-43a03a04e8ea.png)

-Funções para as ações de list, remove, create e edit:

![image](https://user-images.githubusercontent.com/87100340/138942173-8242709b-e4a4-4bc6-95c9-930b36216999.png)
