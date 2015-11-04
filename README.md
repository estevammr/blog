# Blog
Blog utilizando Framework Flask, MongoDB, Python e Materialize.

# Para rodar o projeto

1. Instalar python caso não tenha (2.7.*)

2. Instalar o MongoDB (https://www.mongodb.org/downloads)

3. Instalar o pip (Eu uso Debian e para esse caso apt-get install python-pip, outras distribuições consulte o site do python https://www.python.org/)

4. Criar uma virtualenv (opcional), pode rodar sem criar que também funciona.

5. Instalar os seguintes pacotes pelo pip (use o sudo):

    5.1. pip install flask

    5.2. pip install flask-script

    5.3. pip install WTForms

    5.4. pip install mongoengine

    5.5. pip install flask_mongoengine


# Rodando a aplicação

1. python manage.py runserver na pasta do projeto

2. Criar a pasta para o Mongo dentro do projeto (../blog/data/db/) e executar o server (mongod) indicando o --dbpath para esta pasta.
Ex.: mongod.exe --dbpath C:\caminho onde está seu projeto\blog\data\db

3. Acesse depois -> http://localhost:5000
