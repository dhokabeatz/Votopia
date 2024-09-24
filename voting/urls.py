from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index),
    path('ballot/fetch/', views.fetch_ballot, name='fetch_ballot'),
    path('dashboard/', views.dashboard, name='voterDashboard'),
    path('ballot/vote', views.show_ballot, name='show_ballot'),
    path('ballot/vote/preview', views.preview_vote, name='preview_vote'),
    path('ballot/vote/submit', views.submit_ballot, name='submit_ballot'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

