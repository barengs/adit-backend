from django.urls import path
from .views import (ParentList, ParentDetail, CalonMahasiswaList,
                    CalonMahasiswaDetail, CalonMahasiswaBulkInsertAPIView)

urlpatterns = [
    path('parent/', ParentList.as_view(), name='parentlist'),
    path('parent/<int:pk>/', ParentDetail.as_view(), name='parentdetail'),
    path('calon/', CalonMahasiswaList.as_view(), name='calonmahasiswalist'),
    path('calon/<int:pk>/', CalonMahasiswaList.as_view(), name='calonmahasiswadetail'),
    path('calon/bulk/', CalonMahasiswaBulkInsertAPIView.as_view(), name='calonmahasiswabulkinsert'),
]