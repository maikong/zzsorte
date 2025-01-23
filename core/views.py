from django.shortcuts import render, redirect
import random
from .forms import LuckyNumberaForm
from django.contrib import messages
from .models import LuckyNumber
from django.db.models import Count

def New_Luckinumber(request):
    if request.method == 'POST':
        form = LuckyNumberaForm(request.POST)
        if form.is_valid():
            quantity = int(request.POST.get('quantity', 1))
            email = form.cleaned_data['email']
            origin = form.cleaned_data['origin']

            numbers_generated = []
            for _ in range(quantity):
                luckynumber = LuckyNumber(email=email, origin=origin)
                luckynumber.save()
                numbers_generated.append(luckynumber.number)

            messages.success(request, 'Números gerados com sucesso')
            return redirect('luckinumber_new')
    else:
        form = LuckyNumberaForm()
    
    return render(request, 'core/luckinumber_new.html', {'form': form})

def Show_Luckinumber(request):
    if request.GET.get('email'):
            #numbers = LuckyNumber.objects.all()
            numbers = LuckyNumber.objects.filter(email__icontains=request.GET.get('email'))
    else:
        numbers = LuckyNumber.objects.all()
    return render(request, 'core/luckinumber_all.html', {'pessoas': numbers})

def Show_Luckinumber_Resume(request):
    resume = LuckyNumber.objects.values('email').annotate(number_count=Count('number')).order_by('-number_count')
    return render(request, 'core/luckinumber_resume.html', {'resume': resume})

def Show_Luckinumber_Detail(request, email):
    numbers = LuckyNumber.objects.filter(email=email).values('email', 'number')
    email = numbers.first()
    return render(request, 'core/luckinumber_detail.html', {'numbers': numbers, 'email': email})

def LuckiNumberRaffle(request):
    if request.method == 'POST':
        try:
            quantity = int(request.POST.get('quantity', 1))
            if quantity <= 0:
                raise ValueError("A quantidade deve ser maior que 0.")
            
        except (ValueError, TypeError) as e:
            return render(request, 'core/luckinumber_raffle.html')
       
        luckinumbers = list(LuckyNumber.objects.all())
        numbers_generated = []
        for i in range(quantity):
            numbers_generated.append(random.choice(luckinumbers))

        return render(request, 'core/luckinumber_raffle.html', {'raffles': numbers_generated, 'quantity': quantity})
    
    return render(request, 'core/luckinumber_raffle.html')

def AdminDeleteAll(request):
    LuckyNumber.objects.all().delete()
    return redirect('/')
