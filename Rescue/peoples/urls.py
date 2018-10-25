from django.conf.urls import url
from . import views

app_name = 'peoples'
urlpatterns = [
    url(r'^main_page/$',views.main_page,name='main_page'),
    url(r'^all_shelters/$',views.all_shelters,name='all_shelters'),
    url(r'^add_shelter/$', views.add_shelter, name='add_shelter'),

    url(r'^add_group/$',views.add_group,name='add_group'),
    url(r'^get_group/$',views.get_group,name='get_group'),
    url(r'^volunteering/$',views.volunteering,name='volunteering'),
    url(r'^volunteer_regist/$', views.volunteer_regist, name='volunteer_regist'),
    url(r'^all_volunteers/$',views.all_volunteers,name='all_volunteers'),
    url(r'^ngo_regist/$',views.ngo_regist,name='ngo_regist'),
    url(r'^all_ngos/$',views.all_ngos,name='all_ngos'),
    url(r'^print_POST_request/$',views.print_POST_request,name='print_POST_request'),
    url(r'^all_request/$',views.all_request,name='all_request'),
    url(r'^make_request/$', views.make_request, name='make_request'),
    url(r'^person_finder/$',views.person_finder,name='person_finder'),
    url(r'^missing_person_request/$',views.missing_person_request,name='missing_person_request'),
    url(r'^search_missing_person/$',views.search_missing_person,name='search_missing_person'),

    url(r'^search_missing_person_app/$',views.search_missing_person_app,name='search_missing_person_app'),
    url(r'^battery_stat/$',views.battery_stat,name='battery_stat'),
    url(r'^is_active/$',views.is_active,name='is_active'),
]

