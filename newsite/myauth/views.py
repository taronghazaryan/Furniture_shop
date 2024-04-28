from django.shortcuts import render, redirect, reverse

from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, HttpRequest

from django.views.generic import TemplateView, CreateView, UpdateView

from django.urls import reverse_lazy

from .models import Profile, ProfileImages

from .forms import EditUserForm, AddAvatarForm

from django.utils.translation import gettext_lazy as _, ngettext

from shop.models import Basket
from blog.models import Blog

from django.db import transaction

import os

# Create your views here.


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('myauth:user_page')
        else:
            # User.objects.create(username=username, password1=password, password2=password)
            error = _('Invalid login or password!')
            return render(request, 'myauth/login.html', {'error': error})
    else:
        if request.user.is_authenticated:
            return redirect('myauth:user_page')
        return render(request, 'myauth/login.html')

# User information page
# def user_page(request, pk):
#
#     user = User.objects.get(pk=pk)
#
#     context = {
#         'context': user,
#     }
#
#     return render(request, 'myauth/user_page.html', context=context)


class AboutMeView(TemplateView):
    template_name = 'myauth/user_page.html'

    def get_context_data(self, instance=User, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user  # Set the user from the request

        data = ProfileImages.objects.filter(user=user)
        data_2 = Basket.objects.filter(user=user)
        data_3 = Blog.objects.select_related('user').filter(user=user)

        for item in data_2:
            item.total_price = item.product.price * item.quantity
            item.save()
        context['data'] = data
        context['data_2'] = data_2
        context['data_3'] = data_3

        return context


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'myauth/register.html'
    success_url = reverse_lazy('myauth:user_page')

    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(
            self.request,
            username=username,
            password=password
        )
        login(request=self.request, user=user)
        return response


# don't work
# class MyLogoutViw(LogoutView):
#     next_page = reverse_lazy('/myauth/login/')


def logout_view(request: HttpRequest):
    logout(request)
    return redirect(reverse("myauth:login"))


@transaction.atomic()
@login_required
def edit_user(request):
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=request.user)
        profile, created = Profile.objects.get_or_create(user=request.user)
        form_av = AddAvatarForm(request.POST, request.FILES, instance=profile)
        # form_img = AddMoreImagesForm(request.POST, request.FILES, instance=profile)
        if form.is_valid() and form_av.is_valid():
            form_av.save()
            form.save()

        for image in request.FILES.getlist('images'):
            # form_img = AddMoreImagesForm(request.POST, {'image': file}, instance=profile)
            ProfileImages.objects.get_or_create(images=image, user=request.user)

        # if form_img.is_valid():
        #     images = form_img.save(commit=False)
        #     images.user = profile  # Associate the image with the current user
        #     images.save()
        return redirect('myauth:user_page')
    else:
        form = EditUserForm(instance=request.user)
        profile, created = Profile.objects.get_or_create(user=request.user)
        form_av = AddAvatarForm(instance=profile)
        # form_img = AddMoreImagesForm(instance=profile)

    return render(request, 'myauth/edit_user.html', {'form': form, 'form_av': form_av})


def edit_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()

    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'myauth/edit_password.html', {'form': form})


# def reset_password(request):
#     if request.method == 'POST':
#         form = PasswordResetForm(None, request.POST)
#         if form.is_valid():
#             email = request.POST.get('email', '')
#             user = request.user
#
#     else:
#         form = PasswordResetForm(None)
#
#     return render(request, 'myauth/password_reset.html', {'form': form})

# def password_reset(request):
#     return render(request, 'myauth/password_reset.html')


# class EditProfileView(UpdateView):
#     form_class = UserChangeForm
#     template_name = 'myauth/edit_user.html'
#     success_url = reverse_lazy('myauth:user_page')

