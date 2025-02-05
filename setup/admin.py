from profile.models import Profile

from django.contrib import admin

from branch.models import Branch
from branch_location.models import BranchLocation
from contact.models import Contact
from entity_relation.models import EntityRelation
from item.models import Item
from menu.models import QRMenu
from restaurant.models import Restaurant
from user.models import User
from menu_file.models import MenuFile
from social_contact.models import SocialContact
from subscription.models import Subscription
from plan.models import Plan
from transaction.models import Transaction
from email_config.models import BlockedEmail

# Register your models here.

admin.site.register(Restaurant)
admin.site.register(Branch)
admin.site.register(BranchLocation)
admin.site.register(Profile)
admin.site.register(Item)
admin.site.register(Contact)
admin.site.register(QRMenu)
admin.site.register(EntityRelation)
admin.site.register(User)
admin.site.register(MenuFile)
admin.site.register(SocialContact)
admin.site.register(Subscription)
admin.site.register(Plan)
admin.site.register(Transaction)
admin.site.register(BlockedEmail)
