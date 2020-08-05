from django.urls import path
from . import views
urlpatterns = [
    path('',views.CVListView.as_view(), name="home"),
    path('pdf/<int:pk>', views.get_my_pdf, name="pdf"),
    path('cv/<int:pk>', views.CVDetailView.as_view(), name='cv-detail'),
]
