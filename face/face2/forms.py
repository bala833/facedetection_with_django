
from django import forms
from face2.models import Videos
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
		# 	self.fields['countrycode'].widget.attrs['readonly'] = True
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
