# -*- encoding: utf-8 -*-

from django import forms


class EmailForm(forms.Form):

    nombre = forms.CharField(max_length = 100)
    email  = forms.EmailField(max_length = 80)
    asunto = forms.CharField(max_length = 96)
    mensaje = forms.CharField(max_length = 50120, widget = forms.Textarea)

