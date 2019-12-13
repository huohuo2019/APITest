from django import forms
from .. import models


class BookForm(forms.Form):
    title = forms.CharField(max_length=4)

    def one(self, instance = None, *args, **kwargs):
        self.instance = instance
        super(BookForm, self).__init__(*args, **kwargs)

    def one_save(self,):
        if self.instance is not None:
            for key, value in self.cleaned_data.items():
                setattr(self.instance,key,value)

            self.instance.save()
            return self.instance

        return models.Book.objects.create(**self.cleaned_data)

    def save(self, ):
        return models.Book.objects.create(**self.cleaned_data)

class IdCardForm(forms.Form):
    name = forms.CharField(max_length=20)
    nation = forms.CharField(max_length=10)
    sex = forms.CharField(max_length=1)
    idnum = forms.CharField(max_length=18)
    address = forms.CharField(max_length=50)
    session = forms.CharField(max_length=10)

    def save(self):
        return models.IDCard.objects.create(**self.cleaned_data)


