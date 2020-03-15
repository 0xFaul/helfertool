from django import template
from django.conf import settings

from ..permissions import has_access, ACCESS_INVOLVED, _check_job_role


register = template.Library()


@register.simple_tag(takes_context=True)
def is_involved(context, event):
    if not event:
        return False

    return has_access(context["user"], event, ACCESS_INVOLVED)


@register.simple_tag(takes_context=True)
def is_job_admin(context, job):
    if not job:
        return False

    # FIXME: change after job admin roles are implemented
    return _check_job_role(context["user"], job, None)