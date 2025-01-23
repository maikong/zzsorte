from django.urls import path
from .views import New_Luckinumber, Show_Luckinumber, LuckiNumberRaffle, AdminDeleteAll, Show_Luckinumber_Resume, Show_Luckinumber_Detail

urlpatterns = [
    path('new/', New_Luckinumber, name='luckinumber_new'),
    path('', Show_Luckinumber, name='luckinumber_all'),
    path('detail/<str:email>/', Show_Luckinumber_Detail, name='luckynumber_detail'),
    path('resume/', Show_Luckinumber_Resume, name='luckinumber_resume'),
    path('raffle/', LuckiNumberRaffle, name='luckinumber_raffle'),
    path('core_admin/', AdminDeleteAll, name='administrator'),
]