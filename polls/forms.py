from django import forms
from polls.models import Choice

class VotingForm(forms.Form):
    choiceID = forms.IntegerField()
    # class Meta:
    #     model = Choice
    #     fields = "__all__"
    #     exclude = ['vote']
    #
    #     widgets = {
    #         'question' :forms.RadioSelect(attrs={'text':Choice.choiceText})
    #
    #     }

        # widgets = {
        #     'bio': forms.Textarea(attrs={
        #         'placeholder': 'biography...',
        #     }),
        #     'birthday': forms.DateInput(attrs={
        #         'type': 'date'
        #
        #     }),
        #     'gender': forms.Select(choices=genders),
        #     'profile_photo': forms.FileInput(attrs={
        #         'accept': 'image/*'
        #     })
        # }

