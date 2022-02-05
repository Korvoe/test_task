from django.urls import path, re_path
from vpsHandler import views

urlpatterns = [
    path("vpslist/", views.vpsShow.as_view(),name="vps_list"),
    path("<int:pk>/", views.vpsRetrieve.as_view(),name="vps_retrieve"),
    path("create/", views.vpsCreate.as_view(),name="vps_create"),
    path("update/<int:pk>/",views.vpsUpdate.as_view(),name="vps_update"),
]
