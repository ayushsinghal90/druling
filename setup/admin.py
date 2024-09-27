from profile.models import Profile

from django.contrib import admin

from branch.models import Branch
from branch_location.models import BranchLocation
from contact.models import Contact
from item.models import Item
from menu.models import QRMenu
from restaurant.models import Restaurant

# Register your models here.

admin.site.register(Restaurant)
admin.site.register(Branch)
admin.site.register(BranchLocation)
admin.site.register(Profile)
admin.site.register(Item)
admin.site.register(Contact)
admin.site.register(QRMenu)
