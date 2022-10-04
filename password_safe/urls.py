from django.urls import path
from .views import (
    AccountCreateView,
    HomePageView,
    SiteDetailView,
    SiteDeleteView,
    SiteEditView,
    SiteCreateView,
    AccountDeleteView,
    AccountEditView,
    AccountCreateView,
)

urlpatterns = [
    path("<slug:slug>/new_account/", AccountCreateView.as_view(), name="account_new"),
    path(
        "<slug:slug>/<slug:slug_field>/edit/",
        AccountEditView.as_view(),
        name="account_edit",
    ),
    path(
        "<slug:slug>/<slug:slug_field>/delete/",
        AccountDeleteView.as_view(),
        name="account_delete",
    ),
    path("new_site/", SiteCreateView.as_view(), name="site_new"),
    path("<slug:slug>/edit/", SiteEditView.as_view(), name="site_edit"),
    path("<slug:slug>/delete/", SiteDeleteView.as_view(), name="site_delete"),
    path("<slug:slug>/", SiteDetailView.as_view(), name="site_detail"),
    path("", HomePageView.as_view(), name="home"),
]
