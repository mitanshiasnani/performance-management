from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CheckIn

@login_required
def checkin_page(request):
    if request.method == "POST":
        CheckIn.objects.create(
            user=request.user,
            accomplishments=request.POST.get("accomplishments"),
            blockers=request.POST.get("blockers"),
            next_priorities=request.POST.get("next_priorities"),
        )
        return redirect("checkin_page")

    return render(request, "checkins/checkin_form.html")


@login_required
def checkin_list(request):
    checkins = CheckIn.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "checkins/checkin_list.html", {"checkins": checkins})
