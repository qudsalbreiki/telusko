from django.contrib import admin

# Register your models here.
from .models import Contest
from .models import University
from .models import Coach
from .models import Team
from .models import TeamMember
from .models import Document

admin.site.register(Contest)
admin.site.register(University)
admin.site.register(Coach)
admin.site.register(Team)
admin.site.register(TeamMember)
admin.site.register(Document)
