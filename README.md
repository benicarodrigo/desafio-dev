# Desafio programação - para vaga desenvolvedor

# Ambiente de desenvolvimento
* Python 3.6
* MySQL Server 8.0.17

# Instalação
1) Clonar o repositório 
   * https://github.com/benicarodrigo/desafio-dev.git

2) Criar venv
   * python -m venv venv `cria um diretório virtual 'venv' para as dependências do python` 
   * .\venv\Scripts\activate `executa o script de ativação do ambiente criado dentro do diretorio virtual 'venv'` 

3) Instalar as dependências do projeto.
   Se estiver utilizando linux é necessario instalar a libmysqlclient-dev:
     * $ sudo apt-get install python3-dev default-libmysqlclient-dev build-essential `Debian / Ubuntu`
     * % sudo yum install python3-devel mysql-devel `Red Hat / CentOS`   
   * pip install -r .\requirements.txt `baixa as dependências do projeto`

4) Criar base de dados.
    * create database bycoders character set utf8;
    * create user 'bycoders'@'localhost' identified by 'bycoders#123';
    * grant all privileges on bycoders.* to bycoders@'localhost';
    * grant all privileges on test_bycoders.* to bycoders@'localhost'; `aplicar o privilégio na base de testes automatizados`

5) Configurar base de dados:

    * Configurar conexão com a base de dados no arquivo settings.py.  
        ```
        DATABASES = {
          'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'bycoders',
          'USER': 'bycoders',
          'PASSWORD': 'bycoders#123',
          'HOST': 'localhost',
          'PORT': '3306',
          }
        }
        ```
    
    * Executar os comandos para atualizar e migrar o modelo de dados do Django para o MySQL.
        ```
        * python manage.py makemigrations
        * python manage.py migrate
        ```

# Rodar o Projeto
1) Executar o comendo abaixo para rodar o projeto.    
    * python manage.py runserver


# Funcionamento do Projeto
1) Foram criadas três páginas para o projeto.
      * Página Home:
         - Link para a página upload do arquivo CNAB;
         - Link para a página lista de operações;
   
      * Página Upload de Arquivo:
          - Selecionar o arquivo CNAB.txt através do botão "Procurar..."
          - Clicar no botão "Enviar" para fazer o upload do arquivo e cadastrar os dados na base de dados.
          - Clicar no link da página lista de operações, onde serão exibidas a lista de operações e saldo por loja.
  
     * Página Lista de Operações:
         - Página com lista das operações realizadas agrupadas por loja.
         - Link para a página Home.         
         - Link para a página upload do arquivo CNAB.
 
# Teste do Projeto
1) Executar o comando abaixo para rodar os testes.
    * python manage.py test
    
---

# Referência

Este desafio foi baseado: https://github.com/ByCodersTec/desafio-dev
