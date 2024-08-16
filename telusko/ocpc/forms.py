from django import forms
from .models import Coach, Team, TeamMember, Document, University, Contest

class UniversityForm(forms.ModelForm):
    class Meta:
        model = University
        fields = ['name', 'contest']

class CoachForm(forms.ModelForm):
    class Meta:
        model = Coach
        fields = ['name', 'gender',  'email', 'tshirt_size', 'official_phone_number']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'The coach name',
                'required': 'required'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'email@gmail.com',
                'required': 'required'
            }),
            'tshirt_size': forms.Select(attrs={
                'required': 'required'
            }),
            'gender': forms.Select(choices=[('Female', 'Female'), ('Male', 'Male')], attrs={
                'required': 'required'
            }),
            'official_phone_number': forms.TextInput(attrs={
                'placeholder': '+968 00000000',
                'required': 'required'
            })
        }

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'university', 'contest', 'coach']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your team name',
                'required': 'required'
            }),
            'university': forms.Select(attrs={
                'required': 'required'
            }),
            'contest': forms.Select(attrs={
                'required': 'required'
            }),
            'coach': forms.Select(attrs={
                'required': 'required'
            }),
        }

class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = ['full_name', 'family_name', 'birth_date', 'gender', 'specialization', 'email', 'tshirt_size']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Your first, second and third name'}),
            'family_name': forms.TextInput(attrs={'placeholder': 'Your family name'}),
            'birth_date': forms.TextInput(attrs={'placeholder': '00/0/0000'}),
            'gender': forms.Select(choices=[('Female', 'Female'), ('Male', 'Male')], attrs={'class': 'selection'}),
            'specialization': forms.TextInput(attrs={'placeholder': 'Your specialization/major'}),
            'email': forms.EmailInput(attrs={'placeholder': 'email@gmail.com'}),
            'tshirt_size': forms.Select(choices=[
                ('XS', 'XS'), 
                ('S', 'S'), 
                ('M', 'M'), 
                ('L', 'L'), 
                ('XL', 'XL'), 
                ('XXL', 'XXL'), 
                ('not required', 'T-Shirt is not required')
            ], attrs={'class': 'selection'}),
        }

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['file']

class GeneralInfoForm(forms.Form):
    general_info = forms.CharField(widget=forms.Textarea)

class ContestSelectionForm(forms.Form):
    contest = forms.ModelChoiceField(queryset=Contest.objects.all(), empty_label=None, widget=forms.RadioSelect)

    def __init__(self, *args, contests=None, **kwargs):
        super().__init__(*args, **kwargs)
        if contests:
            self.fields['contest'].queryset = contests
