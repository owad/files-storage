from django.contrib import admin
from person.models import Client, Agent

class ClientAdmin(admin.ModelAdmin):
    model = Client
#    list_display = ('id', 'first_name', 'last_name', 'company_name', 'city', 'email', 'phone_number')
#    search_fields = ('first_name', 'last_name', 'company_name', 'city', 'email', 'phone_number')
#    list_filter = ('company_name', 'city', 'postcode')
#    date_hierarchy = 'created'
#    list_display_links = ('id', 'first_name', 'last_name', 'company_name')
    
#    actions_on_bottom = True

class AgentAdmin(admin.ModelAdmin):
    model = Agent

admin.site.register(Client, ClientAdmin)
admin.site.register(Agent, AgentAdmin)