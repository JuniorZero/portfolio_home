python -m venv venv
. venv/bin/activate
pip install django
django-admin startproject project home

git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main
#No caso de fazer alterações
git init
git add .
git commit -m 'Mensagem'
#Comando usado apenas uma unica vez
git remote add origin URL_DO_GIT