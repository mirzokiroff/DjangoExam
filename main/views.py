from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from .forms import UpdateForm, RegisterForm
from .models import User
from django.core.checks import messages


#
# class EditProfile(LoginRequiredMixin, UpdateView):
#     model = User
#     fields = ['image', 'first_name', 'last_name', 'company', 'email']
#     template_name = 'update.html'
#     success_url = reverse_lazy('customer')
#
#     def get_object(self, queryset=None):
#         return self.request.user


def customers(request):
    if request.GET:
        key = request.GET.get('q')
        users = User.objects.filter(
            Q(first_name__contains=key) | Q(last_name__contains=key) | Q(username__contains=key))
    else:
        users = User.objects.all()
    return render(request, 'main.html', {'users': users})


def loginfunc(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('update')
    return render(request, 'login.html')


def register(request):
    if request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'register.html')


@login_required
def update_userfunc(request):
    user = User.objects.filter(id=request.user.id).first()
    if request.POST:
        form = UpdateForm(request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
        if form.errors:
            print(form.errors.as_json(escape_html=True))
    return render(request, 'update.html', {'user': user})


@login_required
def delete_user(request, pk):
    user = User.objects.filter(id=pk).first()
    if request.user.id != user.id:
        return redirect('home')
    if user:
        User.objects.filter(id=pk).delete()
        return redirect('register')


def update_user(request, pk):
    user = User.objects.filter(id=pk).first()
    if request.user.id != pk:
        if request.POST:
            form = UpdateForm(request.POST, files=request.FILES, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('customer')
        return render(request, 'update.html', {'user': user})
    else:
        return render(request, 'update.html', {'user': user})
