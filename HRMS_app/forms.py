from django import forms
from .models import *


def getAll():
    list=[]
    skill=Skillset.objects.all()
    for s in skill:
        a=(s.id,s.skill_name)
        list.append(a)

    return list


class SkillForm(forms.Form):
    name=forms.MultipleChoiceField(label='Skills',choices=getAll())


class EmpForms(forms.Form):
    eid =forms.CharField()
    fname =forms.CharField()
    mname =forms.CharField()
    lname =forms.CharField()
    dob =forms.CharField()
    gender =forms.CharField()
    pcontac=forms.IntegerField()
    scontac=forms.IntegerField()
    photo = forms.CharField()
    pemail =forms.CharField()
    semail =forms.CharField()
    skills =forms.CharField()


