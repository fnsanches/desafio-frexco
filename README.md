# Desafio Tech (Automação) Frexco

### Desafio proposto pela equipe de recrutamento para o processo seletivo de estágio

O desafio consistia em fazer uma aplicação para servir API utilizando a linguagem Python e sua framework Django.

Os principais pontos que o desafio pede são:
* Utilizar pelo menos 2 endpoints;
* Cadastrar usuário, fornecendo login, senha e data de nascimento;
* A senha deve ser opcional, caso não seja fornecida um senha aleatória deve ser gerada;
* Deve ser possível consultar os usuários cadastrados;
* Deve ser possível consultar em XLSX, CSV ou JSON;
* O aplicativo deve estar em um repositório público no GitHub ou em plataforma similar;
  
#
##  Passo a passo e considerações
#
* Instalação do ambiente de desenvolvimento e todas as suas dependências necessárias.
  
Primeiro foi necessário criar um ambiente virtual através do comando  ```$python -m venv env``` e direcionar o interpretador do python para que usasse como base com o comando ```$source env/Scripts/activate``` (usando a pasta Scripts, pois estou utilizando uma máquina Windows).

Depois instalei o Django e o Django REST Framework com os comandos:

```$pip install django```

```$pip install djangorestframework```

Outras dependências foram instaladas ao decorrer que as necessidades foram aparecendo.

Como:

```Excel Response``` que ajuda na hora de gerar um arquivo XLSX (arquivo baseado em XML comprimido).

```Django REST Framework CSV``` que ajuda na hora de renderizar um arquivo CSV (comma-separate values)

#
* Criando o projeto
  
Utilizando ```$django-admin startproject <nomedoprojeto> . ``` cria-se o projeto no formato padrão do Django.

Após o primeiro passo foi necessário criar o primeiro modelo de acordo com as especificações do projeto. Portanto no arquivo ```models.py``` é criado um modelo de banco de dados com ```$username $password $birthdate``` .

Após a criação do modelo é necessário fazer as migrações para o banco de dados.

Usa-se os comandos:
```
$python manage.py makemigrations
$python manage.py migrate
```

Com isso é criado o banco de dados em SQLite, que é o padrão do Django.

#
* Criando Serializers, Views e Paths

Para facilitar a incorporação e visualização dos dados é preciso criar um 'serializer' para fazer a transcrição entre o objeto Django(Python) e JSON e vice-versa.

Na criação do 'serializer' podemos impor diversas regras, as que eu optei foram:

1. username tem que ser único, e não maior que 200 caracteres;
2. password não pode ser maior que 50 caracteres, e se ele não for introduzido durante a criação no banco de dados, ele irá ser gerado e terá um tamanho de 12 caracteres aleatórios;

Com a criação do 'serializer' fazer o arquivo ```views.py``` foi bem simples.

Na função ```getData``` só é preciso especificar que só atende ao GET do protocolo HTTP, e nela é gerado uma lista de todos os usuários cadastrados.

Na função ```addUser``` é uma função de criar usuário utilizando o método POST, e nela só é necessário fazer a verifição dos dados passados pelo 'serializer' para fazer o retorno da Resposta.

A função ```getDataXLSX``` foi criada devido a necessidade de servir os dados em forma de um arquivo XLSX.

Na criação de rotas dentro do arquivo ```urls.py``` utilizamos a função ```path()``` para criar as rotas para os 3 endpoints necessários para concluir o desafio.

```<ip-address>:<port>/users``` serve para a consulta da lista de usuários cadastrados.

```<ip-address>:<port>/users/xlsx``` serve para o download da lista de usuário em forma de XLSX.

```<ip-address>:<port>/users/add``` é o endpoint para o cadastro de usuários, onde é necessário mandar em forma de JSON.

Exemplo:
```
<ip-address>:<port>/users/add
{
    "username": "<Login>",
    "password": "<Senha>",
    "birthdate": "YYYY-MM-DD"
}
```

Ou sem a senha:

```
<ip-address>:<port>/users/add
{
    "username": "<Login>",
    "birthdate": "YYYY-MM-DD"
}
```

#
* Considerações finais

O desafio mostrou que mesmo em uma aplicação simples, há diversas preocupações em tornar o código simples, reutilizável e claro quanto a suas funcionalidades.

Aprendi muito ao realizar o desafio, e agradeço pela oportunidade de demonstrar meu conhecimento.
