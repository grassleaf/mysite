#coding:utf-8
from django import forms

class RegisterForm(forms.Form):
	email = forms.EmailField(label=(u"邮件"),max_length=30,widget=forms.TextInput(attrs={'size': 30,}))	
	password = forms.CharField(label=(u"密码"),max_length=30,widget=forms.PasswordInput(attrs={'size': 20,}))
	username = forms.CharField(label=(u"昵称"),max_length=30,widget=forms.TextInput(attrs={'size': 20,}))
	
	def clean_username(self):
		'''验证重复昵称'''
		users = User.objects.filter(username__iexact=self.cleaned_data["username"])
		if not users:
			return self.cleaned_data["username"]
		raise forms.ValidationError(u"该昵称已经被使用")
		
	def clean_email(self):
		'''验证重复email'''
		emails = User.objects.filter(email__iexact=self.cleaned_data["email"])
		if not emails:
			return self.cleaned_data["email"]
		raise forms.ValidationError(u"该邮箱已经被使用")
