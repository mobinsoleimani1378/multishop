from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, logout, authenticate
from random import randint
import ghasedakpack
import requests
from uuid import uuid4
from account.forms import LoginForm, EnterPhoneForm, EnterCodeForm, RegisterForm, AddressForm
from account.models import Code, User

SMS = ghasedakpack.Ghasedak('d38322b3ed7402143c6d40d3789e726d150755998e256f94b9529df86146846f')


def login_user(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['phone'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('home:home')
            else:
                form.add_error('phone', 'is not valid')
        else:
            form.add_error('phone', 'is not valid')
    return render(request, 'account/login.html', {'form': form})


def enter_phone(request):
    form = EnterPhoneForm()
    if request.method == "POST":
        form = EnterPhoneForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            code = randint(1000, 9999)
            print(code)
            SMS.verification({'receptor': cd["phone"], 'type': '1', 'template': 'multishop', 'param1': code})
            token = str(uuid4())
            Code.objects.create(phone=cd['phone'], code=code, token=token)
            return redirect(reverse('account:check') + f'?token={token}')
        else:
            form.add_error('phone', 'invalid data')

    return render(request, 'account/enter_phone.html', {'form': form})


def enter_code(request):
    form = EnterCodeForm()
    token = request.GET.get('token')
    code = Code.objects.get(token=token)
    if request.method == "POST":
        form = EnterCodeForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if Code.objects.filter(code=cd['code'], token=token).exists:
                code = Code.objects.get(token=token)
                user, is_created = User.objects.get_or_create(phone=code.phone)
                login(request, user)
                code.delete()
                return redirect('account:register')

    return render(request, 'account/check_code.html', {'form': form, 'code': code.code})


def register(request):
    user = request.user
    form = RegisterForm(instance=user)
    if request.method == 'POST':
        form = RegisterForm(data=request.POST, instance=user)
        if form.is_valid():
            form.save()
            login(request, user)
            return redirect('home:home')
    return render(request, 'account/register.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('home:home')


def address(request):
    form = AddressForm()
    if request.method == 'POST':
        form = AddressForm(data=request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            next = request.GET.get('next')
            if next:
                return redirect(next)
            else:
                return redirect('account:address')

    return render(request, 'account/add_address.html', {'form': form})
