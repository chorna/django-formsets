from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from extra_views import ModelFormSetView

from .models import Contact, CellPhone
from .forms import ContactForm, CellPhoneForm, ContactFormSet

# Create your views here.


class CreateContactView(ModelFormSetView):
    form_class = ContactForm
    model = Contact
    formset_class = ContactFormSet
    template_name = 'example1.html'
    seccion_inline = CellPhoneForm

    def get_success_url(self):
        return reverse('example1')

    def get_context_data(self, **kwargs):
        context = super(CreateContactView, self).get_context_data(**kwargs)

        if self.request.POST:
            context['formset'] = self.formset_class(self.request.POST)
        else:
            context['formset'] = self.formset_class()

        return context

    def formset_valid(self, formset):
        for form in formset:
            if form.is_valid() and form not in formset.deleted_forms:
                form.save()
            else:
                print form.errors
        return HttpResponseRedirect(self.get_success_url())