from django.shortcuts import render, redirect
from . import forms
from django.core.mail import send_mail
from emailPro.settings import EMAIL_HOST_USER
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .utils import render_to_pdf
from django.template.loader import get_template
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from . import models
# Create your views here

# Fetches the data from a post request and passes it to the get pdf function in utils.py
def get_my_pdf(request, pk):
    myobj = models.CVTemplate.objects.get(id=pk)
    temp = str(myobj.template) + '.html'
    template = get_template(temp)
    if request.method=='POST':
        print('request method is post')
        form = forms.CVForm(request.POST)
        if form.is_valid():
            print('form is valid')
            context = {
                "name":form.cleaned_data['name'],
                "title":form.cleaned_data['title'],
                "email":form.cleaned_data['email'],
                "website_url":form.cleaned_data['website_url'],
                "phone":form.cleaned_data['phone'],
                "description":form.cleaned_data['description'],
                "title_exp1":form.cleaned_data['title_exp1'],
                "duration_exp1":form.cleaned_data['duration_exp1'],
                "description_exp1":form.cleaned_data['description_exp1'],
                "title_exp2":form.cleaned_data['title_exp2'],
                "duration_exp2":form.cleaned_data['duration_exp2'],
                "description_exp2":form.cleaned_data['description_exp2'],
                "title_exp3":form.cleaned_data['title_exp3'],
                "duration_exp3":form.cleaned_data['duration_exp3'],
                "description_exp3":form.cleaned_data['description_exp3'],
                "skill1":form.cleaned_data['skill1'],
                "skill2":form.cleaned_data['skill2'],
                "skill3":form.cleaned_data['skill3'],
                "skill4":form.cleaned_data['skill4'],
                "skill5":form.cleaned_data['skill5'],
                "skill6":form.cleaned_data['skill6'],
                "title_pro1":form.cleaned_data['title_pro1'],
                "description_pro1":form.cleaned_data['description_pro1'],
                "title_pro2":form.cleaned_data['title_pro2'],
                "description_pro2":form.cleaned_data['description_pro2'],
                "title_pro3":form.cleaned_data['title_pro3'],
                "description_pro3":form.cleaned_data['description_pro3'],
                "title_edu1":form.cleaned_data['title_edu1'],
                "duration_edu1":form.cleaned_data['duration_edu1'],
                "title_edu2":form.cleaned_data['title_edu2'],
                "duration_edu2":form.cleaned_data['duration_edu2'],
                "title_edu3":form.cleaned_data['title_edu3'],
                "duration_edu3":form.cleaned_data['duration_edu3'],
            }
            html = template.render(context)
            pdf = render_to_pdf(myobj.template, context)
            # return HttpResponse(html)  # we can simply return the html page, if we want to add a html builder in the end.
            if pdf:
                print('pdf formed')
                response = HttpResponse(pdf, content_type='application/pdf')
                name = form.cleaned_data['name']
                filename = "%s_CV.pdf" %(name)
                content = "inline; filename='%s'" %(filename)
                download = request.GET.get("download")
                if download:
                    content = "attachment; filename='%s'" %(filename)
                response['Content-Disposition'] = content
                return response
    return HttpResponse("Not found")


# List view for all the designs saved
class CVListView(ListView):
    model = models.CVTemplate
    template_name = 'CVList.html'


# Once a CV is selected you go to the form and get the selected CV Downloaded
class CVDetailView(DetailView):
    model=models.CVTemplate
    template_name='index.html'