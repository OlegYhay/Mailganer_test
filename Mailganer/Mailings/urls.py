from django.conf.urls import url
import views

urlpatterns = [
    url('^$', views.home_page, name='home_page'),
    url(r'^subscribers/$', views.SubsribersListView.as_view(), name='subsribers_page'),
    url(r'^subscribers/add/$', views.SubsribersAddView.as_view(), name='subsribers_add'),
    url(r'^subscribers/update/(?P<pk>\d+)/$', views.SubsribersUpdateView.as_view(), name='subscribers_update'),
    url(r'^subscribers/delete/(?P<pk>\d+)/$', views.SubscribersDeleteView.as_view(), name='subscribers_delete'),
    url(r'^mailings/$', views.MailingsListView.as_view(), name='mailings_page'),
    url(r'^mailings/add/$', views.MailingsCreateView.as_view(), name='mailings_add'),
    url(r'^mailings/delete/(?P<pk>\d+)/$', views.MailingsDeleteView.as_view(), name='mailings_delete'),
    url(r'^mailings/update/(?P<pk>\d+)/$', views.MailingsUpdateView.as_view(), name='mailings_update'),
    url(r'^mailings/(?P<pk>\d+)/statistic/$', views.Message_mailings.as_view(), name='message_mailings'),
    url(r"^email/(?P<key>\d+)/(?P<key2>\d+).png$", views.email_seen, name="email_seen"),
]
