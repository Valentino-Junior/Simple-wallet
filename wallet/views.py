from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .forms import UserRegistrationForm,DepositForm,WithdrawForm
from .models import User,Wallet

def home(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'register.html', context)

def wallet(request):
    wallet = Wallet.objects.all()
    context = {
        'wallet': wallet,
    }
    return render(request, "wallet.html",context)

def deposit(request):
    wallet = Wallet.objects.get(user=request.user)
    if request.method == 'POST':
        form = DepositForm(request.POST, instance=wallet)
        if form.is_valid():
            wallet = form.save(commit=False)
            wallet.balance = wallet.balance + int(request.POST['balance'])
            wallet.save()
            return redirect('wallet')
    else:
        form = DepositForm(instance=wallet)
    return render(request, 'deposit.html', {'form': form})

def withdraw(request):
    wallet = Wallet.objects.get(user=request.user)
    if request.method == 'POST':
        form = WithdrawForm(request.POST, instance=wallet)
        if form.is_valid():
            wallet = form.save(commit=False)
            wallet.balance = wallet.balance - int(request.POST['balance'])
            wallet.save()
            return redirect('wallet')
    else:
        form = WithdrawForm(instance=wallet)
    return render(request, 'withdraw.html', {'form': form})
