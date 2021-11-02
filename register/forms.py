from django import forms
from jalali_date.fields import JalaliDateField
from jalali_date.widgets import AdminJalaliDateWidget

from .models import CustomerRegistration


class SearchForm(forms.Form):
    SearchText = forms.CharField(max_length=100, label=" مشتری را جستجو کنید", required=False)


class CustomerForm(forms.ModelForm):
    class Meta:
        model = CustomerRegistration
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super(CustomerForm,self).__init__(*args, **kwargs)

        self.fields["startdatetime"]=JalaliDateField(label=("تاریخ"),
            widget=AdminJalaliDateWidget)





