from django.shortcuts import render


# Create your views here.
def welcome_page(request):
    return render(request, template_name="employee.html")


def save_update_employee(request):
    pass


def edit_employee(request):
    pass


def delete_employee(request):
    pass
