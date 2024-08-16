from django.shortcuts import render
from django.contrib import messages
from django.views.generic import TemplateView
from django.core.files.storage import default_storage
from formtools.wizard.views import SessionWizardView
from .models import Team, Document, Coach, University, Contest, TeamMember
from .forms import GeneralInfoForm, ContestSelectionForm, CoachForm, TeamForm, TeamMemberForm, DocumentForm

class RegistrationWizard(SessionWizardView):
    form_list = [ContestSelectionForm, 
                 CoachForm, TeamForm, 
                 TeamMemberForm, 
                 TeamMemberForm, 
                 TeamMemberForm, 
                 DocumentForm
                 ]
    file_storage = default_storage
    template_name = 'ocpc/index.html'

    def get_form_kwargs(self, step=None):
        kwargs = super().get_form_kwargs(step)
        if step == '0':  # Adjust the step index as per your form list
            kwargs['contests'] = Contest.objects.all()
        return kwargs
    

    def done(self, form_list, **kwargs):
        #general_info_form = form_list[0]
        contest_selection_form = form_list[0]
        coach_form = form_list[1]
        team_form = form_list[2]
        member_forms = form_list[3:6]  # Assuming 3 members
        document_form = form_list[6]

        # Save coach and team
        coach_data = coach_form.cleaned_data
        coach = Coach.objects.create(**coach_data)

        team_data = team_form.cleaned_data
        team = Team.objects.create(
            name=team_data['name'],
            university=team_data['university'],
            contest=contest_selection_form.cleaned_data['contest'],
            coach=coach
        )

        # Save team members
        for member_form in member_forms:
            member_data = member_form.cleaned_data
            TeamMember.objects.create(team=team, **member_data)

        # Save document
        document = document_form.cleaned_data['file']
        Document.objects.create(file=document, team=team)

        return render(self.request, 'confirm_registration.html')

    def get_template_names(self):
        return ['formtools/wizard/wizard_form.html']

class ContestSelectionView(TemplateView):
    template_name = 'contest_selection.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contests'] = Contest.objects.all()
        return context

class GeneralInfoView(TemplateView):
    template_name = 'generalinfo.html'
