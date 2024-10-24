from datetime import timezone
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from .models import User, Visits
from .forms import UserRegistrationForm, LoginForm, VisitRequestForm
from django.utils import timezone

def register_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserRegistrationForm()
    return render(request, "register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            try:
                user = User.objects.get(email=email)
                if check_password(password, user.password):
                    request.session["user_id"] = user.userId
                    return redirect("dashboard")
                else:
                    return render(request, "index.html", {"form": form, "error": "Invalid credentials"})
            except User.DoesNotExist:
                return render(request, "index.html", {"form": form, "error": "User does not exist"})
    else:
        form = LoginForm()
    return render(request, "index.html", {"form": form})

def dashboard_view(request):
    user_id = request.session.get("user_id")
    if not user_id:
        return redirect("login")

    user = User.objects.get(pk=user_id)
    today = timezone.now().date()

    if user.role == "ADMIN":
        visits = Visits.objects.filter(visit_date__date=today)
    elif user.role == "SECURITY":
        visits = Visits.objects.filter(visit_date__date=today, status="ACCEPTED")
    elif user.role == "VISITOR":
        visits = Visits.objects.filter(user=user)
    else:
        visits = []

    return render(request, "dashboard.html", {"visits": visits, "user": user})


def logout_view(request):
    logout(request)
    return redirect("login")

def request_visit(request):
    user_id = request.session.get("user_id")
    if not user_id:
        return redirect("login")
    user = User.objects.get(pk=user_id)
    if user.role == "VISITOR":
        if request.method == "POST":
            form = VisitRequestForm(request.POST)
            if form.is_valid():
                visit = form.save(commit=False)
                visit.user = user  
                visit.status = "PENDING" 
                visit.checked_out = False  
                visit.save()
                return redirect('dashboard')
        else:
            form = VisitRequestForm()
        return render(request, 'request_visit.html', {'form': form})
    else:
        return redirect('dashboard')

def manage_visits(request):
    user_id = request.session.get("user_id")
    if not user_id:
        return redirect("login")
    user = User.objects.get(pk=user_id)
    if user.role == "ADMIN":
        visits = Visits.objects.filter(status="PENDING")
        if request.method == "POST":
            visit_id = request.POST.get('visit_id')
            action = request.POST.get('action')
            if visit_id:
                visit = Visits.objects.get(pk=visit_id)
                if action == "accept":
                    visit.status = "ACCEPTED"
                elif action == "reject":
                    visit.status = "REJECTED"
                visit.save()
        return render(request, 'manage_visits.html', {'visits': visits})
    else:
        return redirect('dashboard')

def view_visits(request):
    if request.user.role == "SECURITY":
        today = timezone.now().date()
        visits = Visits.objects.filter(visit_date__date=today, status="ACCEPTED")
        return render(request, 'view_visits.html', {'visits': visits})
    else:
        return redirect('dashboard')

