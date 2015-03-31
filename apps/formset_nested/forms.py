__author__ = 'christian'

from django import forms
from .models import Contact, CellPhone, Email
from django.forms import modelformset_factory, inlineformset_factory, BaseInlineFormSet, BaseModelFormSet


class MasterFormSet(BaseModelFormSet):

    def total_form_count(self):
        """Returns the total number of forms in this FormSet."""
        if self.data or self.files:
            return self.management_form.cleaned_data['TOTAL_FORMS']
        else:
            if self.initial_form_count() > 0:
                total_forms = self.initial_form_count()
            else:
                total_forms = self.initial_form_count() + self.extra
            if total_forms > self.max_num > 0:
                total_forms = self.max_num
            return total_forms

    pass


class MasterInlineFormSet(BaseInlineFormSet):
    def total_form_count(self):
        """Returns the total number of forms in this FormSet."""
        if self.data or self.files:
            return self.management_form.cleaned_data['TOTAL_FORMS']
        else:
            if self.initial_form_count() > 0:
                total_forms = self.initial_form_count()
            else:
                total_forms = self.initial_form_count() + self.extra
            if total_forms > self.max_num > 0:
                total_forms = self.max_num
            return total_forms

    pass


class CellPhoneForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CellPhoneForm, self).__init__(**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    class Meta:
        model = CellPhone
        fields = 'number',

CellPhoneFormSet = inlineformset_factory(Contact, CellPhone, form=CellPhoneForm, can_delete=False, extra=1,
                                         formset=MasterInlineFormSet)


class EmailForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EmailForm, self).__init__(**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Email
        fields = 'mail',

EmailFormSet = inlineformset_factory(Contact, Email, form=EmailForm, can_delete=False, extra=1,
                                         max_num=1)


class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(**kwargs)
        self.cellphone_formset = CellPhoneFormSet(instance=self.instance, data=self.data or None, prefix=self.prefix)
        self.email_formset = EmailFormSet(instance=self.instance, data=self.data or None, prefix=self.prefix)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def is_valid(self):
        return super(ContactForm, self).is_valid() and self.cellphone_formset.is_valid() and self.email_formset.is_valid()

    def save(self, commit=True):
        res = super(ContactForm, self).save(commit=commit)
        if commit:
            self.cellphone_formset.save()
            self.email_formset.save()
        return res

    class Meta:
        model = Contact
        fields = 'first_name', 'last_name'

ContactFormSet = modelformset_factory(Contact, form=ContactForm, can_delete=False, extra=3, formset=MasterFormSet)





