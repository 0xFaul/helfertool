from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from multiselectfield import MultiSelectField

from .event import Event
from ..permissions import ROLE_CHOICES, ROLE_ADMIN


class EventAdminRoles(models.Model):
    class Meta:
        unique_together = ['event', 'user', ]
        
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    roles = MultiSelectField(
        choices=ROLE_CHOICES,
        default=ROLE_ADMIN,
        max_length=250,
        blank=False,
        verbose_name=_("Role"),
    )

    def __str__(self):
        return "{} - {} ({})".format(self.event.name, self.user, ", ".join(self.roles))