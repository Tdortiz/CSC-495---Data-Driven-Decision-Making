from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

app_name = 'hospitalRanking'

urlpatterns = [
    # .com/hospitalRanking/
    url(r'^$', TemplateView.as_view(template_name='hospitalRanking/index.html'), name='hospitalForm'),
]
