from django.urls import path

from . import views

app_name = 'ninjas'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:id>/', views.detail, name='detail'),
    path('<int:id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:id>/vote/', views.vote, name='vote'),
]