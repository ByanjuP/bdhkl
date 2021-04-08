from django import forms
from .models import Post,Destinations,Gallery,Thingstodo
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django.core import validators
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import User,AuthenticationForm,UsernameField,PasswordResetForm,SetPasswordForm



#============================= USER LOGIN FORM ===================

class UserLoginForm(AuthenticationForm):
    username = UsernameField(label = 'Enter Username',widget=forms.TextInput(attrs={'autofocus': True,
                                                           'class': 'form-control'}))

    password = forms.CharField(label=('Password'), strip=False,
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'autofocus': True,
                                                                 'autocomplete': True}))


#============================= PASSWORD RESET FORM ===================
class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label="Email",widget=forms.EmailInput(attrs={'class':'form-control',
                                                                            'autofocus':True,
                                                                            }))


def address_validator(a):
   if a.isalpha == True and a.isnum == False:
       raise  ValidationError('The address should consist of the number and characters')

def min_length_validation(a):
    if len(a)<8:
        raise ValidationError('The number should be more than 8 characters')
def student_validator(a):
    mylist = []
    mylist2 = []
    mylist3 = []
    special_chars=['@','#','$','!','%','^','&','*','-']
    for i in a:
        if i.isupper() == True:
            mylist.append(i)
        elif i.isnumeric() == True:
            mylist2.append(i)
        elif i in special_chars:
            mylist3.append(i)

    if len(mylist) < 1:
        raise forms.ValidationError('The password must contain atleast one Uppercase')
    elif len(mylist2) < 1:
        raise forms.ValidationError('The password must containt atleast one Number')
    elif len(mylist3) == 0:
        raise forms.ValidationError('The password must containt at least one special character')


class PostCreateForm(forms.ModelForm):
    title = forms.CharField()
    body = forms.CharField(initial='Your name',widget=SummernoteWidget())
    featured_image = forms.ImageField(label='Upload  Featured Image')
    class Meta:
        model = Post
        fields = ['title','body','featured_image']

class DestinationForm(forms.ModelForm):
    body = forms.CharField(widget = SummernoteWidget())
    featured_image = forms.ImageField(label='Upload  Featured Image')

    class Meta:
        model = Destinations
        fields = ['title', 'body', 'featured_image']

class GalleyForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['img','caption','taken_by']


'''class TestForm(forms.ModelForm):
    student = forms.CharField(validators=[min_length_validation])
    address = forms.CharField(validators=[address_validator],required=False)
    email = forms.EmailField(validators=[validators.EmailValidator()])
    class Meta:
        model = TestModel
        fields = ['student','grade','address','gender','email']
        labels = {'gender':'Gender'}

    def __init__(self, *args, **kwargs):
        super(TestForm, self).__init__(*args, **kwargs)
        self.fields['grade'].empty_label = 'Select Grade'''''
class ThingstodoForm(forms.ModelForm):
    class Meta:
        model = Thingstodo
        fields = '__all__'
        exclude = ('author',)


