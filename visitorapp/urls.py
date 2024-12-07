from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("", views.login_view, name="login"),
    path("dashboard/", views.dashboard_view, name="dashboard"),
    path("logout/", views.logout_view, name="logout"),
    path("request-visit/", views.request_visit, name="request_visit"),
    path("manage-visits/", views.manage_visits, name="manage_visits"),
    path("view-visits/", views.view_visits, name="view_visits"),
    path("all-users/", views.get_all_users, name="all_users"),
    path("all-visits/", views.get_all_visits, name="all_visits")
]
