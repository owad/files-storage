from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
    
class AbstractPerson(models.Model):
    title = models.CharField(max_length=64, blank=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    company_name = models.CharField(max_length=128, blank=True)
    email = models.EmailField(blank=True)
    address_line_1 = models.CharField(max_length=64, blank=True)
    address_line_2 = models.CharField(max_length=64, blank=True)
    city = models.CharField(max_length=64, blank=True)
    postcode = models.CharField(max_length=6, blank=True)
    date_add = models.DateTimeField(auto_now_add=True)

class Agent(AbstractPerson):
    '''
    agent object
    '''
    user = models.ForeignKey(User, unique=True)
    
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

    def find_by_user(self, User):
        self.objects.get(user=User)
        
class Client(AbstractPerson):
    '''
    client object
    '''
    agent = models.ForeignKey(Agent, blank=False)
    
    def __unicode__(self):
        if self.company_name:
            return self.company_name
        else:
            return "%s %s" % (self.first_name, self.last_name)
    
    def is_company(self):
        return bool(self.company_name)