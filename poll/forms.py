from django import forms

class ElvtNumber(forms.Form):
    elvtNumber = forms.CharField(label="승강기 번호 ", required=False)

class ElvtAddress(forms.Form):
    elvtAddress = forms.CharField(label="승강기 주소/건물명", required=False)

class ElvtLogin(forms.Form):
    ID = forms.CharField(label="ID")
    password = forms.CharField(label="Password", widget=forms.PasswordInput())

class ElvtAddresList(forms.Form):
    address = forms.CharField()