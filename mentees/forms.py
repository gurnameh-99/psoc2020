from django.forms import ModelForm, CharField, PasswordInput 

from .models import Mentee, Proposal

class MenteeForm(ModelForm):
    class Meta():
        model = Mentee
        fields = ['name', 'phone', 'organization']

class ApplyForm(ModelForm):
    class Meta():
        model = Proposal
        fields = ['proposal_link']