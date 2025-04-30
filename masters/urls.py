from django.urls import path
from .views import ReligionList, ReligionDetail, GenderList, GenderDetail, CitizenList, CitizenDetail, ProvinceList, ProvinceDetail, RegencyList, RegencyDetail, SubdistrictList, SubdistrictDetail, VillageList, VillageDetail, RegistrationPathList, RegistrationPathDetail, FacultyList, FacultyDetail, StudyProgramList, StudyProgramDetail, RegistrationPeriodList, RegistrationPeriodDetail, SchoolList, SchoolDetail, JobList, JobDetail, IncomeList, IncomeDetail
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('religions/', ReligionList.as_view(), name='Religions'),
    path('religions/<int:pk>/', ReligionDetail.as_view(), name='Religion'),
    path('genders/', GenderList.as_view(), name='Genders'),
    path('genders/<int:pk>/', GenderDetail.as_view(), name='Genders'),
    path('citizens/', CitizenList.as_view(), name='Citizens'),
    path('citizens/<int:pk>/', CitizenDetail.as_view(), name='Citizens'),
    path('provinces/', ProvinceList.as_view(), name='Provinces'),
    path('provinces/<int:pk>/', ProvinceDetail.as_view(), name='Provinces'),
    path('regencies/', RegencyList.as_view(), name='Regencies'),
    path('regencies/<int:pk>/', RegencyDetail.as_view(), name='Regencies'),
    path('subdistricts/', SubdistrictList.as_view(), name='Subdistricts'),
    path('subdistricts/<int:pk>/', SubdistrictDetail.as_view(), name='Subdistricts'),
    path('villages/', VillageList.as_view(), name='villages'),
    path('villages/<int:pk>/', VillageDetail.as_view(), name='villages'),
    path('registrationpaths/', RegistrationPathList.as_view(), name='registrationpathlist'),
    path('registrationpaths/<int:pk>/', RegistrationPathDetail.as_view(), name='registrationpathdetail'),
    path('faculties/', FacultyList.as_view(), name='facultylist'),
    path('faculties/<int:pk>/', FacultyDetail.as_view(), name='facultydetail'),
    path('studyprograms/', StudyProgramList.as_view(), name='studyprograms'),
    path('studyprograms/<int:pk>/', StudyProgramDetail.as_view(), name='studyprograms'),
    path('periods/', RegistrationPeriodList.as_view(), name='periods'),
    path('periods/<int:pk>/', RegistrationPeriodDetail.as_view(), name='periods'),
    path('schools/', SchoolList.as_view(), name='Schools'),
    path('schools/<int:pk>/', SchoolDetail.as_view(), name='Schools'),
    path('jobs/', JobList.as_view(), name='Jobs'),
    path('jobs/<int:pk>/', JobDetail.as_view(), name='Jobs'),
    path('incomes/', IncomeList.as_view(), name='Incomes'),
    path('incomes/<int:pk>/', IncomeDetail.as_view(), name='Jobs'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
