from django.views.generic import FormView as GenericFormView, \
    ListView as GenericListView
from django.core.urlresolvers import reverse
from case.models import Case
from case.forms import CaseForm
from person.models import Agent

class ListView(GenericListView):
    template_name = 'case/list.html'
    model = Case
    
class FormView(GenericFormView):
    template_name = 'case/form.html'
    form_class = CaseForm
    success_url = 'case_list'
    
    def get_initial(self):
        self.initial = {'agent': Agent.objects.get(user=self.request.user)}
        return self.initial