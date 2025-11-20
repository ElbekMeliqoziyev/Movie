from django.urls import path
from .views import *

urlpatterns = [
    path("",view_list, name='home'),
    path("create",add_movie, name="create"),
    path("detail/<int:pk>/", view_detail, name="detail"),
    path("edit/<int:pk>/", edit_movie, name='edit'),
    path("delete/<int:pk>/", remove_movie, name='delete'),
]