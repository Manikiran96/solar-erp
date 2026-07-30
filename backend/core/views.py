from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render


def login_view(request):

    error_message = None

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect("role_dashboard")

        error_message = "Invalid username or password"

    return render(
        request,
        "core/login.html",
        {
            "error_message": error_message
        }
    )


@login_required
def logout_view(request):

    logout(request)

    return redirect("login")


@login_required
def role_dashboard(request):

    user = request.user

    if user.is_superuser:
        return redirect("admin_dashboard")

    if user.groups.filter(name="ADMIN").exists():
        return redirect("admin_dashboard")

    if user.groups.filter(name="SALES").exists():
        return redirect("sales_dashboard_page")

    if user.groups.filter(name="FINANCE").exists():
        return redirect("finance_dashboard_page")

    if user.groups.filter(name="TECHNICIAN").exists():
        return redirect("technician_dashboard_page")

    if user.groups.filter(name="MANAGEMENT").exists():
        return redirect("management_dashboard_page")

    return render(
        request,
        "core/no_access.html"
    )


@login_required
def admin_dashboard_page(request):

    return render(
        request,
        "core/admin_dashboard.html"
    )


@login_required
def sales_dashboard_page(request):

    return render(
        request,
        "core/sales_dashboard.html"
    )


@login_required
def finance_dashboard_page(request):

    return render(
        request,
        "core/finance_dashboard.html"
    )


@login_required
def technician_dashboard_page(request):

    return render(
        request,
        "core/technician_dashboard.html"
    )


@login_required
def management_dashboard_page(request):

    return render(
        request,
        "core/management_dashboard.html"
    )
