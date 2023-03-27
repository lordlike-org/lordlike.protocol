from django.urls import path
from . import views

app_name = 'protocol'

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('create_text_trans/', views.create_text_trans, name='create_text_trans'),
    path('ipfs_trans/', views.ipfs_trans, name='ipfs_trans'),
    path('about/', views.about, name='about'),
    path('update/hash/transaction/', views.UpdateHashTransaction.as_view()),
    path('create/user/wallet/address/', views.CreateUserWalletAddress.as_view()),
    path('create/data/', views.Data.as_view()),
    path('create/ipfs/data/', views.IPFSData.as_view()),

]
