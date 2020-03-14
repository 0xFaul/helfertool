from django.utils.translation import ugettext_lazy as _

# This is the central file that defines and manages the different permissions for events, jobs and users!

# There are different administrator roles for an event. These roles are assigned to the different users:
ROLE_ADMIN = 'ADMIN'
ROLE_FRONTDESK = 'FRONTDESK'
ROLE_INVENTORY = 'INVENTORY'
ROLE_BADGES = 'BADGES'

ROLE_CHOICES = (
    (ROLE_ADMIN, _('Administrator')),
    (ROLE_FRONTDESK, _('Front desk')),
    (ROLE_INVENTORY, _('Inventory')),
    (ROLE_BADGES, _('Badges')),
)

# In the views, a certain permission is requested.
