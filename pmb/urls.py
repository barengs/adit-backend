from django.urls import path
from .views import (ParentList, ParentDetail, CalonMahasiswaList,
                    CalonMahasiswaDetail, CalonMahasiswaBulkInsertAPIView, BuktiBayarList, BuktiBayarDetail,
                      BuktiIdentitasDetail, BuktiIdentitasList, RegistrationWaveList, RegistrationWaveDetail)

urlpatterns = [
    path('parent/', ParentList.as_view(), name='parentlist'),
    path('parent/<int:pk>/', ParentDetail.as_view(), name='parentdetail'),
    path('calon/', CalonMahasiswaList.as_view(), name='calonmahasiswalist'),
    path('calon/<int:pk>/', CalonMahasiswaList.as_view(), name='calonmahasiswadetail'),
    path('calon/bulk/', CalonMahasiswaBulkInsertAPIView.as_view(), name='calonmahasiswabulkinsert'),
    path('bukti-bayar/', BuktiBayarList.as_view(), name='buktibayarlist'),
    path('bukti-bayar/<int:pk>/', BuktiBayarDetail.as_view(), name='buktibayardetail'),
    path('bukti-identitas/', BuktiIdentitasList.as_view(), name='buktiidentitaslist'),
    path('bukti-identitas/<int:pk>/', BuktiIdentitasDetail.as_view(), name='buktiidentitasdetail'),
    path('gelombang/', RegistrationWaveList.as_view(), name='gelombangmahasiswalist'),
    path('gelombang/<int:pk>/', RegistrationWaveDetail.as_view(), name='gelombangmahasiswadetail'),
]