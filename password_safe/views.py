from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from .models import Account, Site


class HomePageView(ListView):
    model = Site
    template_name = "home.html"

    def get_queryset(self):
        try:
            return Site.objects.filter(author=self.request.user)
        except:
            return HttpResponse("Login please!")


class SiteDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Site
    template_name = "site_detail.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class SiteDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Site
    template_name = "site_delete.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class SiteEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Site
    template_name = "site_edit.html"
    fields = ("siteName",)

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class AccountDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Account
    template_name = "account_delete.html"
    slug_field = "slug_field"
    slug_url_kwarg = "slug_field"
    success_url = reverse_lazy("home")


class AccountEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Account
    template_name = "account_edit.html"
    fields = (
        "username",
        "password",
    )
    slug_field = "slug_field"
    slug_url_kwarg = "slug_field"


class SiteCreateView(LoginRequiredMixin, CreateView):
    model = Site
    template_name = "site_new.html"
    fields = ("siteName",)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AccountCreateView(LoginRequiredMixin, CreateView):
    model = Account
    template_name = "account_new.html"
    fields = (
        "site_name",
        "username",
        "password",
    )
