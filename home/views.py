from django.shortcuts import render
from home.lista import posts
from django.shortcuts import render
from .formulario import EmpresaForm
from email.message import EmailMessage
import smtplib
import csv

def home(request):

    context={
        'posts': posts
    }

    return render(
        request,
        'home/global/index.html',
        context,
    )

def author_profile(request):
    return render(
        request,
        'home/profile_page/index.html'
    )

def projects_created(request):

    return render(
        request,
        'home/projects_page/index.html'
    )

def programs_used(request):

    return render(
        request,
        'home/programs_page/index.html'
    )

def book_reading(request):

    return render(
        request,
        'home/book_page/index.html'
    )

def maintenance(request):

    return render(
        request,
        'home/maintenance_page/index.html'
    )

def create_empresa(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            descricao = form.cleaned_data['descricao']
            with open('avaliacao_empresa.txt', mode='a') as file:
                writer = csv.writer(file)
            writer.writerow([name,descricao])
            email_com_anexo()
            return render(request, "Sucesso")
        else:
            form = EmpresaForm()
        return render(request, 'forms.html', {'form':form})
    
def email_com_anexo():
    msg = EmailMessage()
    msg['Subject'] = 'Avaliacao da Empresa'
    msg['From'] = 'macedojunior317@gmail.com'
    msg['To'] = 'macedojunior317@gmail.com'
    msg.set_content('Senhor, avaliação da empresa chegou, verifica o anexo')
    try:
        with open('avaliacao_empresa.csv','rb') as file:
            file_data = file.read()
            msg.add_attachment(file_data, maintype='text', subtype='csv', filename= 'avaliacao_empresa.txt')
            with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
                smtp.login("macedojunior317@gmail.com","-L&!Pt'9#$l6")
                smtp.send_message(msg)
    except Exception as e:
        print(f"Ocorreu um erro ao enviar a avaliação: {e}")