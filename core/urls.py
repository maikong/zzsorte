from django.urls import path
from .views import New_Luckinumber, Show_Luckinumber, LuckiNumberRaffle, AdminDeleteAll, CampaignAll, Show_Luckinumber_Resume, Show_Luckinumber_Detail, user_login, logout_view, CampaigScore

urlpatterns = [
    path('new/', New_Luckinumber, name='luckinumber_new'),
    path('', Show_Luckinumber, name='luckinumber_all'),
    #path('', Show_Luckinumber_Resume, name='luckinumber_all'),
    path('detail/<str:email>/', Show_Luckinumber_Detail, name='luckynumber_detail'),
    path('resume/', Show_Luckinumber_Resume, name='luckinumber_resume'),
    path('raffle/', LuckiNumberRaffle, name='luckinumber_raffle'),
    path('campaign/', CampaignAll, name='campaign_all'),
    path('core_admin/', AdminDeleteAll, name='administrator'),
    path('login/', user_login, name='login'),
    path('logout/', logout_view, name='logout'),
    path('<uuid:campaign_id>/score/', CampaigScore, name='campaig_score'),
]