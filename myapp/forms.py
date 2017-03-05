from django import forms

from .models import *
#the below is a test
class LimbdiForm(forms.ModelForm):

    class Meta:
        model = Limbdi2016
        fields = ('room',)

class ProfileForm(forms.ModelForm):
    class Meta:
        model= Profile
        fields = ('roll_no','name','branch','email','course','passing_year','mobile','bank_acount_no','ifs_code','branch_address','father_name','home_address','home_phone','guardian_phone','guardian_address',)
