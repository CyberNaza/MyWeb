from django import forms
from .models import Member

class MemberForm(forms.ModelForm):
	class Meta:
		model = Member
		fields = ['User_name', 'passwd', 'email']