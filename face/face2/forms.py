
from django import forms
from face2.models import Videos,Face
from crispy_forms.helper import FormHelper
from django.forms.models import inlineformset_factory
from crispy_forms.layout import Layout,Field, Fieldset, ButtonHolder, Submit,Button, Div
 
# class VideoForm(forms.ModelForm):
#     class Meta:
#         model= Videos
#         fields= ["title", "video"]



class VideoForm(forms.ModelForm):

    def __init__(self,*args, **kwargs):
        super(VideoForm, self).__init__(*args, **kwargs)
        self.fields['title'].required = True
        self.helper = FormHelper()
        # instance = getattr(self, 'instance', None)
        # if instance and instance.pk:
        #   self.fields['countrycode'].widget.attrs['readonly'] = True
        self.helper.from_tag = False
        self.helper.disable_csrf = True
        self.helper.layout =Layout(
            Div(
                Div(Field('title'), css_class="col-md-6"),
                Div(Field('video'), css_class="col-md-6"),
                css_class='row'
            ),
        )
    class Meta:
        model = Videos
        fields =('title', 'video')
    def clean(self):
        video = self.cleaned_data.get("video")
        print(video,"kkkkkkkkkkkkkkkkkkkkkkkkkkk")

        return self.cleaned_data





class FaceForm(forms.ModelForm):

    def __init__(self,*args, **kwargs):
        super(FaceForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['user_id'].required = True
        self.helper = FormHelper()
        # instance = getattr(self, 'instance', None)
        # if instance and instance.pk:
        #   self.fields['countrycode'].widget.attrs['readonly'] = True
        self.helper.from_tag = False
        self.helper.disable_csrf = True
        self.helper.layout =Layout(
            Div(
                Div(Field('name'), css_class="col-md-6"),
                Div(Field('user_id'), css_class="col-md-6"),
                css_class='row'
            ),
        )
    class Meta:
        model = Face
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
           }
        fields =('name','user_id')

    def clean_name(self):
        name_valid = self.cleaned_data.get('name')
        if name_valid:
            name_model = Face.objects.all()
            for names in name_model:
                if names.name == name_valid:
                    raise forms.ValidationError("With This name Already User is Register")
        return name_valid
    def clean_user_id(self):
        id_valid = self.cleaned_data.get('user_id')
        if id_valid:
            id_model     = Face.objects.all()
            for names in id_model   :
                if names.user_id == id_valid:
                    raise forms.ValidationError("With This Id Already User is Register")
        return id_valid



