from django.shortcuts import render, HttpResponse, redirect
from .models import NameDetails


def launch_form(request):
    html_templates = 'fill_form.html'
    return render(request, html_templates)


def create_data(request):
    message = "Data not Saved."
    if request.method == 'POST':
        # html form data
        html_id = request.POST['id']
        html_person_name = request.POST['pname']
        html_country_name = request.POST['cname']

        # save into database(db)
        NameDetails(person_name=html_person_name,
                    country_name=html_country_name).save()
        message = "Data Saved."

    html_templates = 'fill_form.html'
    context = {'message': message}
    return render(request, html_templates, context)


def show_details(request):
    data = NameDetails.objects.all().values()
    # "select id, person_name, country_name from NameDetails"
    #
    # print("\n\n\n")
    # id_list = [i['id'] for i in data]
    # print(id_list)
    # print("\n\n\n")
    html_templates = 'show.html'
    context = {'data': data}
    return render(request, html_templates, context)


def update_form(request, num):
    name_details = NameDetails.objects.get(id=num)
    if request.method == 'POST':
        name_details.id = request.POST.get('id')
        name_details.person_name = request.POST.get('pname')
        name_details.country_name = request.POST.get('cname')
        name_details.save()
        return redirect('show_url')

    context = {"id": name_details.id,
               "person_name": name_details.person_name,
               "country_name": name_details.country_name}
    html_templates = 'update_form.html'
    return render(request, html_templates, context)


def update_data(request, num):
    data = NameDetails.objects.get(id=num)
    if request.method == 'POST':
        data.id = request.POST['id']
        data.person_name = request.POST['pname']
        data.country_name = request.POST['cname']
        data.save()
        return redirect('show_url')
    html_templates = 'update_form_2.html'
    context = {'id': data.id,
               'person_name': data.person_name,
               "country_name": data.country_name}
    return render(request, html_templates, context)


def delete_data(request, num):
    NameDetails.objects.get(id=num).delete()
    return redirect('show_url')
