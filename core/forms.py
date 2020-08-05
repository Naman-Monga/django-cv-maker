from django import forms

class CVForm(forms.Form):
# intro
    name = forms.CharField(max_length=100)
    title = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    website_url = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
# work experience
    title_exp1 = forms.CharField(max_length=150)
    duration_exp1 = forms.CharField(max_length=150)
    description_exp1 = forms.CharField(widget=forms.Textarea)

    title_exp2 = forms.CharField(max_length=150, required = False)
    duration_exp2 = forms.CharField(max_length=150, required = False)
    description_exp2 = forms.CharField(widget=forms.Textarea, required = False)

    title_exp3 = forms.CharField(max_length=150, required = False)
    duration_exp3 = forms.CharField(max_length=150, required = False)
    description_exp3 = forms.CharField(widget=forms.Textarea, required = False)
# skills
    skill1 = forms.CharField(max_length=100)
    skill2 = forms.CharField(max_length=100)
    skill3 = forms.CharField(max_length=100)
    skill4 = forms.CharField(max_length=100)
    skill5 = forms.CharField(max_length=100)
    skill6 = forms.CharField(max_length=100)
# projects
    title_pro1 = forms.CharField(max_length=200)
    description_pro1 = forms.CharField(max_length=200)
    title_pro2 = forms.CharField(max_length=200)
    description_pro2 = forms.CharField(max_length=200)
    title_pro3 = forms.CharField(max_length=200)
    description_pro3 = forms.CharField(max_length=200)
# Education and certification
    title_edu1 = forms.CharField(max_length=200)
    duration_edu1 = forms.CharField(max_length=200)
    title_edu2 = forms.CharField(max_length=200)
    duration_edu2 = forms.CharField(max_length=200)
    title_edu3 = forms.CharField(max_length=200)
    duration_edu3 = forms.CharField(max_length=200)
 
    def __str__(self):
        return self.Email