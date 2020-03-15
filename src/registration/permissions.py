from .models import Event, EventAdminRoles, Job, Helper

from django.utils.translation import ugettext_lazy as _


# This is the central file that defines and manages the different permissions for events, jobs and users.
# Global permissions like creating events, users or sending newsletters are managed in the accounts app.

# There are different roles, defined in registration.models.EventAdminRoles

# In the views, a certain access is requested.
ACCESS_INVOLVED = "INVOLVED"  # basically just the main page (user is somehow involved, necessary for all roles)
ACCESS_EVENT_EDIT = "EVENT_EDIT"  # edit/archive/delete the event
ACCESS_EVENT_EDIT_LINKS = "EVENT_EDIT_LINKS"  # edit links of an event
ACCESS_EVENT_EDIT_JOBS = "EVENT_EDIT_JOBS"  # add/delete/duplicate/sort jobs
ACCESS_EVENT_EXPORT_HELPERS = "EVENT_EXPORT_HELPERS"  # export data as pdf/excel
ACCESS_EVENT_EDIT_DUPLICATES = "EVENT_EDIT_DUPLICATES"  # manage duplicated helpers

ACCESS_JOB_EDIT = "JOB_EDIT"  # edit an existing job
ACCESS_JOB_EDIT_HELPERS = "JOB_EDIT_HELPERS"  # add/remove helpers of job
ACCESS_JOB_VIEW_HELPERS = "JOB_VIEW_HELPERS"  # view helpers of job
ACCESS_JOB_SEND_MAILS = "JOB_SEND_MAILS"  # send mails for job
ACCESS_JOB_VIEW_MAILS = "JOB_VIEW_MAILS"  # view sent mails for job
ACCESS_JOB_VIEW_STATISTICS = "JOB_VIEW_STATISTICS"  # view statistics for job (currently for t-shirts)

ACCESS_HELPER_EDIT = "HELPER_EDIT"  # edit the personal data of a helper
ACCESS_HELPER_VIEW = "HELPER_VIEW"  # view the personal data of a helper

ACCESS_INVENTORY_EDIT = "INVENTORY_EDIT"  # edit inventory settings for an event
ACCESS_INVENTORY_HANDLE = "INVENTORY_HANDLE"  # register and take back inventory

ACCESS_BADGES_EDIT = "BADGES_EDIT"  # edit badge settings for an event
ACCESS_BADGES_EDIT_HELPER = "BADGES_EDIT_HELPER"  # edit badges of single helpers
ACCESS_BADGES_GENERATE = "BADGES_GENERATE"  # generate and register badges

ACCESS_MAILS_SEND = "MAILS_SEND"  # can send all mails of an event
ACCESS_MAILS_VIEW = "MAILS_VIEW"  # can view all mails of an event

ACCESS_STATISTICS_VIEW = "STATISTICS_VIEW"  # can view statistics

ACCESS_GIFTS_EDIT = "GIFTS_EDIT"  # edit gift settings for an event
ACCESS_GIFTS_HANDLE = "GIFTS_HANDLE"  # give gifts to helpers and note presence

# Based on requested access and role, we can decide whether we grant access or not.
# Here, for each access type, the allowed/required roles are listed.
_rbac_matrix = {
    ACCESS_INVOLVED: [
        EventAdminRoles.ROLE_ADMIN,
        EventAdminRoles.ROLE_RESTRICTED_ADMIN,
        EventAdminRoles.ROLE_FRONTDESK,
        EventAdminRoles.ROLE_INVENTORY,
        EventAdminRoles.ROLE_BADGES,
    ],

    ACCESS_EVENT_EDIT: [
        EventAdminRoles.ROLE_ADMIN,
    ],

    ACCESS_EVENT_EDIT_LINKS: [
        EventAdminRoles.ROLE_ADMIN,
    ],

    ACCESS_EVENT_EDIT_JOBS: [
        EventAdminRoles.ROLE_ADMIN,
    ],

    ACCESS_EVENT_EXPORT_HELPERS: [
        EventAdminRoles.ROLE_ADMIN,
        EventAdminRoles.ROLE_RESTRICTED_ADMIN,
    ],

    ACCESS_EVENT_EDIT_DUPLICATES: [
        EventAdminRoles.ROLE_ADMIN,
        EventAdminRoles.ROLE_RESTRICTED_ADMIN,
    ],

    ACCESS_JOB_EDIT: [
        EventAdminRoles.ROLE_ADMIN,
    ],

    ACCESS_JOB_EDIT_HELPERS: [
        EventAdminRoles.ROLE_ADMIN,
        EventAdminRoles.ROLE_RESTRICTED_ADMIN,
    ],

    ACCESS_JOB_VIEW_HELPERS: [
        EventAdminRoles.ROLE_ADMIN,
        EventAdminRoles.ROLE_RESTRICTED_ADMIN,
        EventAdminRoles.ROLE_FRONTDESK,
        EventAdminRoles.ROLE_INVENTORY,
    ],

    ACCESS_JOB_SEND_MAILS: [
        EventAdminRoles.ROLE_ADMIN,
        EventAdminRoles.ROLE_RESTRICTED_ADMIN,
    ],

    ACCESS_JOB_VIEW_MAILS: [
        EventAdminRoles.ROLE_ADMIN,
        EventAdminRoles.ROLE_RESTRICTED_ADMIN,
    ],

    ACCESS_JOB_VIEW_STATISTICS: [
        EventAdminRoles.ROLE_ADMIN,
        EventAdminRoles.ROLE_RESTRICTED_ADMIN,
    ],

    ACCESS_HELPER_EDIT: [
        EventAdminRoles.ROLE_ADMIN,
        EventAdminRoles.ROLE_RESTRICTED_ADMIN,
    ],

    ACCESS_HELPER_VIEW: [
        EventAdminRoles.ROLE_ADMIN,
        EventAdminRoles.ROLE_RESTRICTED_ADMIN,
        EventAdminRoles.ROLE_FRONTDESK,
        EventAdminRoles.ROLE_INVENTORY,
    ],

    ACCESS_INVENTORY_EDIT: [
        EventAdminRoles.ROLE_ADMIN,
    ],

    ACCESS_INVENTORY_HANDLE: [
        EventAdminRoles.ROLE_ADMIN,
        EventAdminRoles.ROLE_RESTRICTED_ADMIN,
        EventAdminRoles.ROLE_INVENTORY,
    ],

    ACCESS_BADGES_EDIT: [
        EventAdminRoles.ROLE_ADMIN,
    ],

    ACCESS_BADGES_EDIT_HELPER: [
        EventAdminRoles.ROLE_ADMIN,
        EventAdminRoles.ROLE_RESTRICTED_ADMIN,
    ],

    ACCESS_BADGES_GENERATE: [
        EventAdminRoles.ROLE_ADMIN,
        EventAdminRoles.ROLE_RESTRICTED_ADMIN,
        EventAdminRoles.ROLE_BADGES,
    ],

    ACCESS_MAILS_SEND: [
        EventAdminRoles.ROLE_ADMIN,
        EventAdminRoles.ROLE_RESTRICTED_ADMIN,
    ],

    ACCESS_MAILS_VIEW: [
        EventAdminRoles.ROLE_ADMIN,
        EventAdminRoles.ROLE_RESTRICTED_ADMIN,
    ],

    ACCESS_STATISTICS_VIEW: [
        EventAdminRoles.ROLE_ADMIN,
        EventAdminRoles.ROLE_RESTRICTED_ADMIN,
    ],

    ACCESS_GIFTS_EDIT: [
        EventAdminRoles.ROLE_ADMIN,
        EventAdminRoles.ROLE_RESTRICTED_ADMIN,
    ],

    ACCESS_GIFTS_HANDLE: [
        EventAdminRoles.ROLE_ADMIN,
        EventAdminRoles.ROLE_RESTRICTED_ADMIN,
        EventAdminRoles.ROLE_FRONTDESK,
    ],
}


def has_access(user, resource, access):
    """
    Checks whether the user has access to the resource with the requested access type.
    """
    # superuser can do anything
    if user.is_superuser:
        return True

    # check type of accessed resource
    if isinstance(resource, Event):
        return _has_access_event(user, resource, access)
    elif isinstance(resource, Job):
        return _has_access_job(user, resource, access)
    elif isinstance(resource, Helper):
        return _has_access_helper(user, resource, access)
    else:
        raise ValueError("Invalid resource type")
    
    return False


def has_access_event_or_job(user, event, access_event, access_job):
    # check event
    if has_access(user, event, access_event):
        return True

    # check jobs
    for job in event.job_set.all():
        if has_access(user, job, access_job):
            return True
    
    return False


def _has_access_event(user, event, access):
    # check role
    if _check_event_role(user, event, access):
        return True
    
    # special cases
    if access == ACCESS_INVOLVED:
        for job in event.job_set.all():
            if _check_event_role(user, job.event, access):
                return True

    # nothing worked, no access
    return False


def _has_access_job(user, job, access):
    # check role
    if _check_event_role(user, job.event, access):
        return True
    
    # handle job admins
    if _check_job_role(user, job, access):
        return True
    
    return False


def _has_access_helper(user, helper, access):
    # check role
    if _check_event_role(user, helper.event, access):
        return True

    # handle job admins for helpers
    for shift in helper.shifts.all():
        if _check_job_role(user, shift.job, access):
            return True

    # handle job admins for coordinators
    for job in helper.job_set.all():
        if _check_job_role(user, job, access):
            return True
    
    return False


def _check_event_role(user, event, access):
    """
    Check whether the user has a required role for this access
    """
    # get admin roles of user
    try:
        admin_roles = EventAdminRoles.objects.get(event=event, user=user).roles
    except EventAdminRoles.DoesNotExist:
        return FalseEvent

    # get required roles for this access type
    try:
        required_roles = _rbac_matrix[access]
    except KeyError:
        raise ValueError("Invalid access tself.job_admins.filter(pk=user.pk).exists()ype")

    # check if we have one of the required roles. then we are done
    for role in admin_roles:
        if role in required_roles:
            return True

    return False

def _check_job_role(user, job, access):
    # user is job admin or not, nothing more
    return job.job_admins.filter(pk=user.pk).exists()