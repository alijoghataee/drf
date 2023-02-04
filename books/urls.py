from django.urls import path

from .views import *


urlpatterns = [
    path('get-all-data/', GetAllDate.as_view(), name='get_all_data'),
    path('detail-data/<int:pk>/', DetailApi.as_view(), name='get_fav_data'),
    path('create-model-data/', PostModelDate.as_view(), name='create_model_data'),
    path('create-data/', PostData.as_view(), name='create_data'),
    path('search/', SearchData.as_view(), name='search'),
    path('change/<int:pk>/', ChangeData.as_view(), name='change'),
    path('all-api/', all_api, name='all_data'),
    path('change-api/<int:pk>/', change_api, name='change_api'),
    path('create-api/', create_api, name='create_api'),
    path('list-create-data/', ListAndCreateData.as_view()),
    path('retrieve-create/<int:pk>/', RetrieveApi.as_view())

]
