# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import gettext as _

class AbstractPerson(models.Model):
    title = models.CharField(max_length=64, blank=True, verbose_name=_('tytuł'))
    first_name = models.CharField(max_length=64, verbose_name=_('imię'))
    last_name = models.CharField(max_length=64, verbose_name=_('nazwisko'))
    company_name = models.CharField(max_length=128, blank=True, verbose_name=_('firma'))
    email = models.EmailField(verbose_name=_('adres e-mail'))
    address_line_1 = models.CharField(max_length=64, blank=True, verbose_name=_('adres 1'))
    address_line_2 = models.CharField(max_length=64, blank=True, verbose_name=_('adres 2'))
    city = models.CharField(max_length=64, blank=True, verbose_name=_('miejscowość'))
    postcode = models.CharField(max_length=6, blank=True, verbose_name=_('kod pocztowy'), 
                                validators=[RegexValidator(r'^\d{2}-\d{3}$', _('Błędny format'))])
    date_add = models.DateTimeField(auto_now_add=True, verbose_name=_('data utworzenia'))

class Employee(AbstractPerson):
    '''
    employee object
    '''
    user = models.ForeignKey(User, unique=True, verbose_name=_('użytkownik'))
    
    def __unicode__(self):
        '''
        if object got company_name it's treated as company
        if not then it removes empty values from the list and than joins
        rest to give a proper salutation
        '''
        if self.company_name:
            return self.company_name
        else:
            return " ".join(filter(None, [self.title, 
                                          self.first_name, 
                                          self.last_name]))

class Client(AbstractPerson):
    '''
    client object
    '''
    employee = models.ForeignKey(Employee, blank=False, verbose_name=_('pracownik'))
    
    def __unicode__(self):
        if self.company_name:
            return self.company_name
        else:
            return "%s %s" % (self.first_name, self.last_name)
    
    def is_company(self):
        return bool(self.company_name)
    