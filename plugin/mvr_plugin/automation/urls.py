from django.urls import path,re_path
from . import views

urlpatterns = [
    path("",views.homepage),
    path("heartbeat",views.heartbeat),
    path("automation/process_data",views.automate),
    path("automation/sgheartbeat",views.selheart),
    path("automation/zheartbeat",views.zelheart),
    path("automation/ajax/automate/",views.automate1),
    path("automation/result",views.result),
    # re_path(r"(automation)*/process_data",views.automate),
]