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
        fields = ('roll_no','name','acad_fee','mess_fee','room_sec','room_no','branch','email','course','passing_year','mobile','bank_acount_no','ifs_code','branch_address','father_name','home_address','home_phone','guardian_phone','guardian_address',)


class AryabhattaF(forms.ModelForm):
    class Meta:
        model= Aryabhatta
        fields = ('roll_no','name','acad_fee','mess_fee','room_sec','room_no','branch','email','course','passing_year','mobile','bank_acount_no','ifs_code','branch_address','father_name','home_address','home_phone','guardian_phone','guardian_address',)

class CvramanF(forms.ModelForm):
    class Meta:
        model= Cvraman
        fields = ('roll_no','name','acad_fee','mess_fee','room_sec','room_no','branch','email','course','passing_year','mobile','bank_acount_no','ifs_code','branch_address','father_name','home_address','home_phone','guardian_phone','guardian_address',)

class DhanrajgiriF(forms.ModelForm):
    class Meta:
        model= Dhanrajgiri
        fields = ('roll_no','name','acad_fee','mess_fee','room_sec','room_no','branch','email','course','passing_year','mobile','bank_acount_no','ifs_code','branch_address','father_name','home_address','home_phone','guardian_phone','guardian_address',)

class GmscnewF(forms.ModelForm):
    class Meta:
        model= Gmscnew
        fields = ('roll_no','name','acad_fee','mess_fee','room_sec','room_no','branch','email','course','passing_year','mobile','bank_acount_no','ifs_code','branch_address','father_name','home_address','home_phone','guardian_phone','guardian_address',)

class GmscoldF(forms.ModelForm):
    class Meta:
        model= Gmscold
        fields = ('roll_no','name','acad_fee','mess_fee','room_sec','room_no','branch','email','course','passing_year','mobile','bank_acount_no','ifs_code','branch_address','father_name','home_address','home_phone','guardian_phone','guardian_address',)

class LimbdiF(forms.ModelForm):
    class Meta:
        model= Limbdi
        fields = ('roll_no','name','acad_fee','mess_fee','room_sec','room_no','branch','email','course','passing_year','mobile','bank_acount_no','ifs_code','branch_address','father_name','home_address','home_phone','guardian_phone','guardian_address',)

class MorviF(forms.ModelForm):
    class Meta:
        model= Morvi
        fields = ('roll_no','name','acad_fee','mess_fee','room_sec','room_no','branch','email','course','passing_year','mobile','bank_acount_no','ifs_code','branch_address','father_name','home_address','home_phone','guardian_phone','guardian_address',)

class Rajputana(forms.ModelForm):
    class Meta:
        model= Rajputana
        fields = ('roll_no','name','acad_fee','mess_fee','room_sec','room_no','branch','email','course','passing_year','mobile','bank_acount_no','ifs_code','branch_address','father_name','home_address','home_phone','guardian_phone','guardian_address',)

class RamanujanF(forms.ModelForm):
    class Meta:
        model= Ramanujan
        fields = ('roll_no','name','acad_fee','mess_fee','room_sec','room_no','branch','email','course','passing_year','mobile','bank_acount_no','ifs_code','branch_address','father_name','home_address','home_phone','guardian_phone','guardian_address',)

class SalujaF(forms.ModelForm):
    class Meta:
        model= Saluja
        fields = ('roll_no','name','acad_fee','mess_fee','room_sec','room_no','branch','email','course','passing_year','mobile','bank_acount_no','ifs_code','branch_address','father_name','home_address','home_phone','guardian_phone','guardian_address',)

class ScdeyF(forms.ModelForm):
    class Meta:
        model=  Scdey
        fields = ('roll_no','name','acad_fee','mess_fee','room_sec','room_no','branch','email','course','passing_year','mobile','bank_acount_no','ifs_code','branch_address','father_name','home_address','home_phone','guardian_phone','guardian_address',)

class SnboseF(forms.ModelForm):
    class Meta:
        model= Snbose
        fields = ('roll_no','name','acad_fee','mess_fee','room_sec','room_no','branch','email','course','passing_year','mobile','bank_acount_no','ifs_code','branch_address','father_name','home_address','home_phone','guardian_phone','guardian_address',)

class VishwakarmaF(forms.ModelForm):
    class Meta:
        model= Vishwakarma
        fields = ('roll_no','name','acad_fee','mess_fee','room_sec','room_no','branch','email','course','passing_year','mobile','bank_acount_no','ifs_code','branch_address','father_name','home_address','home_phone','guardian_phone','guardian_address',)

class VishweshvarayyaF(forms.ModelForm):
    class Meta:
        model= Vishweshvarayya
        fields = ('roll_no','name','acad_fee','mess_fee','room_sec','room_no','branch','email','course','passing_year','mobile','bank_acount_no','ifs_code','branch_address','father_name','home_address','home_phone','guardian_phone','guardian_address',)

class VivekanandaF(forms.ModelForm):
    class Meta:
        model= Vivekananda
        fields = ('roll_no','name','acad_fee','mess_fee','room_sec','room_no','branch','email','course','passing_year','mobile','bank_acount_no','ifs_code','branch_address','father_name','home_address','home_phone','guardian_phone','guardian_address',)
