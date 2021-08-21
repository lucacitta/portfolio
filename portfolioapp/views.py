from django.shortcuts import render, redirect
from django.core.mail import send_mail
from portfolio.settings import EMAIL_HOST_USER

def home(request):
    if request.method=='POST':
        data=request.POST
        nombre=data.get('name')
        email=data.get('email')
        asunto=data.get('subject')
        mensaje=data.get('message')
        email1=send_mail(
            asunto,
            (f'{nombre} con el email {email} accedio al formulario del portfolio y te envió el siguiente mensaje\n\n{mensaje}'),
            EMAIL_HOST_USER,
            ['lucacitta@gmail.com'],
            fail_silently=False,
            )
        email2=send_mail(
            'Respuesta automatica a formulario Luca Cittá Giordano',
            (f'Hola {nombre} los mails se enviaron correctamente, voy a responder lo mas rapido posible, gracias por contactar y saludos\nLuca Citta Giordano'),
            EMAIL_HOST_USER,
            [email],
            fail_silently=False,
            )
        return redirect('/?valido')
    return render(request,'index.html',{})


def homeEn(request):
    if request.method=='POST':
        data=request.POST
        nombre=data.get('name')
        email=data.get('email')
        asunto=data.get('subject')
        mensaje=data.get('message')
        email1=send_mail(
            asunto,
            (f'{nombre} con el email {email} accedio al formulario del portfolio y te envió el siguiente mensaje\n\n{mensaje}'),
            EMAIL_HOST_USER,
            ['lucacitta@gmail.com'],
            fail_silently=False,
            )
        email2=send_mail(
            'Respuesta automatica a formulario Luca Cittá Giordano',
            (f'Hola {nombre} los mails se enviaron correctamente, voy a responder lo mas rapido posible, gracias por contactar y saludos\nLuca Citta Giordano'),
            EMAIL_HOST_USER,
            [email],
            fail_silently=False,
            )
        return redirect('indexEn/?valido')
    return render(request,'indexEn.html',{}) 