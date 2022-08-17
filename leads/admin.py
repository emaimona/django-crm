from django.contrib import admin
from leads.models import Lead, Agent, User

admin.site.register(User)
admin.site.register(Lead)
admin.site.register(Agent)

# Register your models here.
