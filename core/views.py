from django.shortcuts import render, redirect
import random
from .forms import LuckyNumberaForm
from django.contrib import messages
from .models import LuckyNumber, Campaign
from django.db.models import Count
from django.contrib.auth import authenticate, login, logout
from .forms import UserLoginForm
from django.contrib.auth.decorators import login_required

@login_required
def New_Luckinumber(request):
    if request.method == 'POST':
        form = LuckyNumberaForm(request.POST)
        if form.is_valid():
            quantity = int(request.POST.get('quantity', 1))
            email = form.cleaned_data['email']
            origin = form.cleaned_data['origin']
            campaign = form.cleaned_data['campaign']

            numbers_generated = []
            for _ in range(quantity):
                luckynumber = LuckyNumber(email=email, origin=origin, campaign=campaign)
                luckynumber.save()
                numbers_generated.append(luckynumber.number)

            messages.success(request, 'Números gerados com sucesso')
            return redirect('luckinumber_new')
    else:
        form = LuckyNumberaForm()
    
    return render(request, 'core/luckinumber_new.html', {'form': form})

@login_required
def Show_Luckinumber(request):
    if not request.user.is_authenticated:
        return redirect('login')

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

@login_required
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

@login_required
def AdminDeleteAll(request):
    LuckyNumber.objects.all().delete()
    return redirect('/')


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = UserLoginForm()
    return render(request, 'core/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def CampaignAll(request):
    campaigns = Campaign.objects.all()
    ctx = {'campaigns': campaigns}
    return render(request, 'core/campaign_all.html', ctx)

def CampaigScore(request, campaign_id ):
    user = LuckyNumber.objects.filter(campaign=campaign_id).values('email').annotate(number_count=Count('number')).order_by('-number_count')
    ctx = {'user': user}
    return render(request, 'core/campaign_score.html', ctx)