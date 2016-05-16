from django.conf.urls import url

from . import views

app_name = 'gifts'
urlpatterns = [
    #
    # list
    #
    url(r'^(?P<event_url_name>[a-zA-Z0-9]+)/gifts/$',
        views.list,
        name='list'),

    #
    # edit gifts
    #
    url(r'^(?P<event_url_name>[a-zA-Z0-9]+)/gifts/gift/add/$',
        views.edit_gift,
        name='add_gift'),

    url(r'^(?P<event_url_name>[a-zA-Z0-9]+)/gifts/gift/(?P<gift_pk>[0-9]+)/$',
        views.edit_gift,
        name='edit_gift'),

    url(r'^(?P<event_url_name>[a-zA-Z0-9]+)/gifts/gift/(?P<gift_pk>[0-9]+)/'
         'delete/$',
        views.delete_gift,
        name='delete_gift'),

    #
    # edit gift sets
    #
    url(r'^(?P<event_url_name>[a-zA-Z0-9]+)/gifts/giftset/add/$',
        views.edit_gift_set,
        name='add_gift_set'),

    url(r'^(?P<event_url_name>[a-zA-Z0-9]+)/gifts/giftset/'
         '(?P<gift_set_pk>[0-9]+)/$',
        views.edit_gift_set,
        name='edit_gift_set'),

    url(r'^(?P<event_url_name>[a-zA-Z0-9]+)/gifts/giftset/'
         '(?P<gift_set_pk>[0-9]+)/delete/$',
        views.delete_gift_set,
        name='delete_gift_set'),
]