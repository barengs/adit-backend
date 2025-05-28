from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Religion, Gender, Citizen, Province, Regency, Subdistrict, Village, RegistrationPath, Faculty, StudyProgram, RegistrationPeriod, School, Job, Income
from .serializers import ReligionSerializer, ReligionListSerializer, GenderSerializer, GenderListSerializer, CitizenSerializer, CitizenListSerializer, ProvinceSerializer, ProvinceListSerializer, RegencySerializer, RegencyListSerializer, SubdistrictSerializer, SubdistrictListSerializer, VillageSerializer, VillageListSerializer, RegistrationPathSerializer, RegistrationPathListSerializer, FacultySerializer, FacultyListSerializer, StudyProgramSerializer, StudyProgramListSerializer, RegistrationPeriodSerializer, RegistrationPeriodListSerializer, SchoolSerializer, SchoolListSerializer, JobSerializer, JobListSerializer, IncomeSerializer, IncomeListSerializer

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
# Create your views here.

# ini class untuk metode GET dan POST
class ReligionList(APIView):
    
    @swagger_auto_schema(
        query_serializer=ReligionListSerializer,
        responses={200: ReligionSerializer(many=True)},
        tags=['Religion'],
    )
        
    def get(self, request, format=None):
        religions = Religion.objects.all()
        serializer = ReligionSerializer(religions, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(
        operation_description="apiview post description override",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['name','code'],
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING),
                'code': openapi.Schema(type=openapi.TYPE_STRING)
            },
        ),
        security=[],
        tags=['Religion'],
    )
    def post(self, request, format=None):
        serializer = ReligionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ini class untuk metode GET, PUT, dan DELETE
class ReligionDetail(APIView):
    def get_object(self, pk):
        try:
            return Religion.objects.get(pk=pk)
        except Religion.DoesNotExist:
            raise Http404
    
    @swagger_auto_schema(
        query_serializer=ReligionSerializer,
        responses={200: ReligionSerializer},
        tags=['Religion'],
    )
    def get(self, request, pk, format=None):
        religion = self.get_object(pk)
        serializer = ReligionSerializer(religion)
        return Response(serializer.data)
    
    @swagger_auto_schema(
        query_serializer=ReligionSerializer,
        request_body=ReligionSerializer,
        responses={200: ReligionSerializer},
        tags=['Religion']
    )
    def put(self, request, pk, format=None):
        religion = self.get_object(pk)
        serializer = ReligionSerializer(religion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        religion = self.get_object(pk)
        religion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GenderList(APIView):

    @swagger_auto_schema(
        query_serializer=GenderListSerializer,
        responses={200: GenderSerializer(many=True)},
        tags=['Gender'],
    )
        
    def get(self, request, format=None):
        genders = Gender.objects.all()
        serializer = GenderSerializer(genders, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(
        operation_description="apiview post description override",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['name','code'],
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING),
                'code': openapi.Schema(type=openapi.TYPE_STRING)
            },
        ),
        security=[],
        tags=['Gender'],
    )
    def post(self, request, format=None):
        serializer = GenderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GenderDetail(APIView):
    def get_object(self, pk):
        try:
            return Gender.objects.get(pk=pk)
        except Gender.DoesNotExist:
            raise Http404
    
    @swagger_auto_schema(
        query_serializer=GenderSerializer,
        responses={200: GenderSerializer},
        tags=['Gender'],
    )
    def get(self, request, pk, format=None):
        gender = self.get_object(pk)
        serializer = GenderSerializer(gender)
        return Response(serializer.data)
    
    @swagger_auto_schema(
        query_serializer=GenderSerializer,
        request_body=GenderSerializer,
        responses={200: GenderSerializer},
        tags=['Gender']
    )
    def put(self, request, pk, format=None):
        gender = self.get_object(pk)
        serializer = GenderSerializer(gender, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        gender = self.get_object(pk)
        gender.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CitizenList(APIView):

    @swagger_auto_schema(
        query_serializer=CitizenListSerializer,
        responses={200: CitizenSerializer(many=True)},
        tags=['Citizen'],
    )
        
    def get(self, request, format=None):
        citizens = Citizen.objects.all()
        serializer = CitizenSerializer(citizens, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(
        operation_description="apiview post description override",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['name','code'],
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING),
                'code': openapi.Schema(type=openapi.TYPE_STRING)
            },
        ),
        security=[],
        tags=['Citizen'],
    )
    def post(self, request, format=None):
        serializer = CitizenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CitizenDetail(APIView):
    def get_object(self, pk):
        try:
            return Citizen.objects.get(pk=pk)
        except Citizen.DoesNotExist:
            raise Http404
    
    @swagger_auto_schema(
        query_serializer=CitizenSerializer,
        responses={200: CitizenSerializer},
        tags=['Citizen'],
    )
    def get(self, request, pk, format=None):
        citizen = self.get_object(pk)
        serializer = CitizenSerializer(citizen)
        return Response(serializer.data)
    
    @swagger_auto_schema(
        query_serializer=CitizenSerializer,
        request_body=CitizenSerializer,
        responses={200: CitizenSerializer},
        tags=['Citizen']
    )
    def put(self, request, pk, format=None):
        citizen = self.get_object(pk)
        serializer = CitizenSerializer(citizen, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        citizen = self.get_object(pk)
        citizen.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ProvinceList(APIView):

    @swagger_auto_schema(
        query_serializer=ProvinceListSerializer,
        responses={200: ProvinceSerializer(many=True)},
        tags=['Province'],
    )
    def get(self, request, format=None):
        provinces = Province.objects.all()
        serializer = ProvinceSerializer(provinces, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(
        operation_description="Create a new province",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['name', 'code', 'meta'],
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING),
                'code': openapi.Schema(type=openapi.TYPE_STRING),
                'meta': openapi.Schema(type=openapi.TYPE_OBJECT)
            },
        ),
        security=[],
        tags=['Province'],
    )
    def post(self, request, format=None):
        serializer = ProvinceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProvinceDetail(APIView):
    def get_object(self, pk):
        try:
            return Province.objects.get(pk=pk)
        except Province.DoesNotExist:
            raise Http404
    
    @swagger_auto_schema(
        query_serializer=ProvinceSerializer,
        responses={200: ProvinceSerializer},
        tags=['Province'],
    )
    def get(self, request, pk, format=None):
        province = self.get_object(pk)
        serializer = ProvinceSerializer(province)
        return Response(serializer.data)
    
    @swagger_auto_schema(
        query_serializer=ProvinceSerializer,
        request_body=ProvinceSerializer,
        responses={200: ProvinceSerializer},
        tags=['Province']
    )
    def put(self, request, pk, format=None):
        province = self.get_object(pk)
        serializer = ProvinceSerializer(province, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        province = self.get_object(pk)
        province.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class RegencyList(APIView):

    @swagger_auto_schema(
        query_serializer=RegencyListSerializer,
        responses={200: RegencySerializer(many=True)},
        tags=['Regency'],
    )
    def get(self, request, format=None):
        regencies = Regency.objects.all()
        serializer = RegencySerializer(regencies, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(
        operation_description="Create a new regency",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['name', 'code', 'province', 'meta'],
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING),
                'code': openapi.Schema(type=openapi.TYPE_STRING),
                'province': openapi.Schema(type=openapi.TYPE_INTEGER),
                'meta': openapi.Schema(type=openapi.TYPE_OBJECT)
            },
        ),
        security=[],
        tags=['Regency'],
    )
    def post(self, request, format=None):
        serializer = RegencySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RegencyDetail(APIView):
    def get_object(self, pk):
        try:
            return Regency.objects.get(pk=pk)
        except Regency.DoesNotExist:
            raise Http404
    
    @swagger_auto_schema(
        query_serializer=RegencySerializer,
        responses={200: RegencySerializer},
        tags=['Regency'],
    )
    def get(self, request, pk, format=None):
        regency = self.get_object(pk)
        serializer = RegencySerializer(regency)
        return Response(serializer.data)
    
    @swagger_auto_schema(
        query_serializer=RegencySerializer,
        request_body=RegencySerializer,
        responses={200: RegencySerializer},
        tags=['Regency']
    )
    def put(self, request, pk, format=None):
        regency = self.get_object(pk)
        serializer = RegencySerializer(regency, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        regency = self.get_object(pk)
        regency.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class SubdistrictList(APIView):
    
    @swagger_auto_schema(
        query_serializer=SubdistrictListSerializer,
        responses={200: SubdistrictSerializer(many=True)},
        tags=['Subdistrict'],
    )
    def get(self, request, format=None):
        subdistricts = Subdistrict.objects.all()
        serializer = SubdistrictSerializer(subdistricts, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(
        operation_description="Create a new subdistrict",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['name', 'code', 'regency', 'meta'],
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING),
                'code': openapi.Schema(type=openapi.TYPE_STRING),
                'regency': openapi.Schema(type=openapi.TYPE_INTEGER),
                'meta': openapi.Schema(type=openapi.TYPE_OBJECT),
            },
        ),
        security=[],
        tags=['Subdistrict'],
    )
    def post(self, request, format=None):
        serializer = SubdistrictSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubdistrictDetail(APIView):
    def get_object(self, pk):
        try:
            return Subdistrict.objects.get(pk=pk)
        except Subdistrict.DoesNotExist:
            raise Http404
        
    @swagger_auto_schema(
        query_serializer=SubdistrictSerializer,
        responses={200: SubdistrictSerializer()},
        tags=['Subdistrict']
    )
    def get(self, request, pk, format=None):
        subdistrict = self.get_object(pk)
        serializer = SubdistrictSerializer(subdistrict)
        return Response(serializer.data)
    
    @swagger_auto_schema(
        query_serializer=SubdistrictSerializer,
        request_body=SubdistrictSerializer,
        responses={200: SubdistrictSerializer()},
        tags=['Subdistrict']
    )
    def put(self, request, pk, format=None):
        subdistrict = self.get_object(pk)
        serializer = SubdistrictSerializer(subdistrict, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        subdistrict = self.get_object(pk)
        subdistrict.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class VillageList(APIView):
    
    @swagger_auto_schema(
        query_serializer=VillageListSerializer,
        responses={200: VillageSerializer(many=True)},
        tags=['Village'],
    )
    def get(self, request, format=None):
        villages = Village.objects.all()
        serializer = VillageSerializer(villages, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(
        operation_description="Create a new village",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['name', 'code', 'subdistrict', 'meta'],
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING),
                'code': openapi.Schema(type=openapi.TYPE_STRING),
                'subdistrict': openapi.Schema(type=openapi.TYPE_INTEGER),
                'meta': openapi.Schema(type=openapi.TYPE_OBJECT),
            },
        ),
        security=[],
        tags=['Village'],
    )
    def post(self, request, format=None):
        serializer = VillageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class VillageDetail(APIView):

    def get_object(self, pk):
        try:
            return Village.objects.get(pk=pk)
        except Village.DoesNotExist:
            raise Http404
        
    @swagger_auto_schema(
        query_serializer=VillageSerializer,
        responses={200: VillageSerializer()},
        tags=['Village']
    )
    def get(self, request, pk, format=None):
        village = self.get_object(pk)
        serializer = VillageSerializer(village)
        return Response(serializer.data)
    
    @swagger_auto_schema(
        query_serializer=VillageSerializer,
        request_body=VillageSerializer,
        responses={200: VillageSerializer()},
        tags=['Village']
    )
    def put(self, request, pk, format=None):
        village = self.get_object(pk)
        serializer = VillageSerializer(village, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        village = self.get_object(pk)
        village.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RegistrationPathList(APIView):

    @swagger_auto_schema(
        query_serializer=RegistrationPathListSerializer,
        responses={200: RegistrationPathSerializer(many=True)},
        tags=['RegistrationPath'],
    )
        
    def get(self, request, format=None):
        registrationpaths = RegistrationPath.objects.all()
        serializer = RegistrationPathSerializer(registrationpaths, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(
        operation_description="apiview post description override",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['name','code'],
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING),
                'code': openapi.Schema(type=openapi.TYPE_STRING)
            },
        ),
        security=[],
        tags=['RegistrationPath'],
    )
    def post(self, request, format=None):
        serializer = RegistrationPathSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegistrationPathDetail(APIView):
    def get_object(self, pk):
        try:
            return RegistrationPath.objects.get(pk=pk)
        except RegistrationPath.DoesNotExist:
            raise Http404
    
    @swagger_auto_schema(
        query_serializer=RegistrationPathSerializer,
        responses={200: RegistrationPathSerializer},
        tags=['RegistrationPath'],
    )
    def get(self, request, pk, format=None):
        registrationpath = self.get_object(pk)
        serializer = RegistrationPathSerializer(registrationpath)
        return Response(serializer.data)
    
    @swagger_auto_schema(
        query_serializer=RegistrationPathSerializer,
        request_body=RegistrationPathSerializer,
        responses={200: RegistrationPathSerializer},
        tags=['RegistrationPath']
    )
    def put(self, request, pk, format=None):
        registrationpath = self.get_object(pk)
        serializer = RegistrationPathSerializer(registrationpath, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        registrationpath = self.get_object(pk)
        registrationpath.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class FacultyList(APIView):

    @swagger_auto_schema(
        query_serializer=FacultyListSerializer,
        responses={200: FacultySerializer(many=True)},
        tags=['Faculty'],
    )
        
    def get(self, request, format=None):
        Faculties = Faculty.objects.all()
        serializer = FacultySerializer(Faculties, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(
        operation_description="apiview post description override",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['name','code'],
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING),
                'code': openapi.Schema(type=openapi.TYPE_STRING)
            },
        ),
        security=[],
        tags=['Faculty'],
    )
    def post(self, request, format=None):
        serializer = FacultySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FacultyDetail(APIView):
    def get_object(self, pk):
        try:
            return Faculty.objects.get(pk=pk)
        except Faculty.DoesNotExist:
            raise Http404
    
    @swagger_auto_schema(
        query_serializer=FacultySerializer,
        responses={200: FacultySerializer},
        tags=['Faculty'],
    )
    def get(self, request, pk, format=None):
        faculty = self.get_object(pk)
        serializer = FacultySerializer(faculty)
        return Response(serializer.data)
    
    @swagger_auto_schema(
        query_serializer=FacultySerializer,
        request_body=FacultySerializer,
        responses={200: FacultySerializer},
        tags=['Faculty']
    )
    def put(self, request, pk, format=None):
        faculty = self.get_object(pk)
        serializer = FacultySerializer(faculty, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        faculty = self.get_object(pk)
        faculty.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class StudyProgramList(APIView):

    @swagger_auto_schema(
        query_serializer=StudyProgramListSerializer,
        responses={200: StudyProgramSerializer(many=True)},
        tags=['StudyProgram'],
    )

    def get(self, request, format=None):
        Studyprograms = StudyProgram.objects.all()
        serializer = StudyProgramSerializer(Studyprograms, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(
        operation_description="Create a new Study Program",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['name', 'faculty', 'code'],
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING),
                'faculty': openapi.Schema(type=openapi.TYPE_INTEGER),
                'code': openapi.Schema(type=openapi.TYPE_STRING)
            },
        ),
        security=[],
        tags=['StudyProgram'],
    )

    def post(self, request, format=None):
        serializer = StudyProgramSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class StudyProgramDetail(APIView):
    def get_object(self, pk):
        try:
            return StudyProgram.objects.get(pk=pk)
        except StudyProgram.DoesNotExist:
            raise Http404
        
    @swagger_auto_schema(
        responses={200: StudyProgramSerializer},
        tags=['StudyProgram'],
    )

    def get(self, request, pk, format=None):
        studyprogram = self.get_object(pk)
        serializer = StudyProgramSerializer(studyprogram)
        return Response(serializer.data)
    
    @swagger_auto_schema(
        query_serializer=FacultySerializer,
        responses={200: FacultySerializer},
        tags=['Faculty'],
    )
    def get(self, request, pk, format=None):
        faculty = self.get_object(pk)
        serializer = FacultySerializer(faculty)
        return Response(serializer.data)
    
    @swagger_auto_schema(
        query_serializer=StudyProgramSerializer,
        request_body=StudyProgramSerializer,
        responses={200: StudyProgramSerializer},
        tags=['StudyProgram']
    )
    def put(self, request, pk, format=None):
        studyprogram = self.get_object(pk)
        serializer = StudyProgramSerializer(studyprogram, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        studyprogram = self.get_object(pk)
        studyprogram.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class RegistrationPeriodList(APIView):

    @swagger_auto_schema(
        responses={200: RegistrationPeriodListSerializer(many=True)},
        tags=['RegistrationPeriod'],
    )
    def get(self, request, format=None):
        periods = RegistrationPeriod.objects.all()
        serializer = RegistrationPeriodSerializer(periods, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new Registration Period",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['period'],
            properties={
                'period': openapi.Schema(type=openapi.TYPE_STRING, description="Format YYYY/YYYY"),
            },
        ),
        security=[],
        tags=['RegistrationPeriod'],
    )
    def post(self, request, format=None):
        serializer = RegistrationPeriodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegistrationPeriodDetail(APIView):
    
    def get_object(self, pk):
        try:
            return RegistrationPeriod.objects.get(pk=pk)
        except RegistrationPeriod.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        responses={200: RegistrationPeriodSerializer},
        tags=['RegistrationPeriod'],
    )
    def get(self, request, pk, format=None):
        period = self.get_object(pk)
        serializer = RegistrationPeriodSerializer(period)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=RegistrationPeriodSerializer,
        responses={200: RegistrationPeriodSerializer},
        tags=['RegistrationPeriod'],
    )
    def put(self, request, pk, format=None):
        period = self.get_object(pk)
        serializer = RegistrationPeriodSerializer(period, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        period = self.get_object(pk)
        period.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SchoolList(APIView):

    @swagger_auto_schema(
        responses={200: SchoolListSerializer(many=True)},
        tags=['School'],
    )
    def get(self, request, format=None):
        schools = School.objects.all()
        serializer = SchoolSerializer(schools, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new School",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['name', 'code', 'address', 'phone'],
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING),
                'code': openapi.Schema(type=openapi.TYPE_STRING),
                'address': openapi.Schema(type=openapi.TYPE_STRING),
                'phone': openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        security=[],
        tags=['School'],
    )
    def post(self, request, format=None):
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SchoolDetail(APIView):
    def get_object(self, pk):
        try:
            return School.objects.get(pk=pk)
        except School.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        responses={200: SchoolSerializer()},
        tags=['School'],
    )
    def get(self, request, pk, format=None):
        school = self.get_object(pk)
        serializer = SchoolSerializer(school)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=SchoolSerializer,
        responses={200: SchoolSerializer},
        tags=['School'],
    )
    def put(self, request, pk, format=None):
        school = self.get_object(pk)
        serializer = SchoolSerializer(school, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        school = self.get_object(pk)
        school.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class JobList(APIView):
    @swagger_auto_schema(
        responses={200: JobListSerializer(many=True)},
        tags=['Job'],
    )
    def get(self, request, format=None):
        jobs = Job.objects.all()
        serializer = JobListSerializer(jobs, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new Job",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['job'],
            properties={
                'job': openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        security=[],
        tags=['Job'],
    )

    def post(self, request, format=None):
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JobDetail(APIView):
    def get_object(self, pk):
        try:
            return Job.objects.get(pk=pk)
        except Job.DoesNotExist:
            raise Http404
        
    @swagger_auto_schema(
        responses={200: JobSerializer()},
        tags=['Job'],
    )
    def get(self, request, pk, format=None):
        job = self.get_object(pk)
        serializer = JobSerializer(job)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=JobSerializer,
        responses={200: JobSerializer},
        tags=['Job'],
    )
    def put(self, request, pk, format=None):
        job = self.get_object(pk)
        serializer = JobSerializer(job, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        job = self.get_object(pk)
        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class IncomeList(APIView):
    @swagger_auto_schema(
        responses={200: IncomeListSerializer(many=True)},
        tags=['Income'],
    )

    def get(self, request, format=None):
        incomes = Income.objects.all()
        serializer = IncomeSerializer(incomes, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new income",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['income'],
            properties={
                'income': openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        security=[],
        tags=['Income'],
    )

    def post(self, request, format=None):
        serializer = IncomeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class IncomeDetail(APIView):
    def get_object(self, pk):
        try:
            return Income.objects.get(pk=pk)
        except Income.DoesNotExist:
            raise Http404
        
    @swagger_auto_schema(
        responses={200: IncomeSerializer()},
        tags=['Income'],
    )
    def get(self, request, pk, format=None):
        income = self.get_object(pk)
        serializer = IncomeSerializer(income)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=IncomeSerializer,
        responses={200: IncomeSerializer},
        tags=['Income'],
    )
    def put(self, request, pk, format=None):
        income = self.get_object(pk)
        serializer = IncomeSerializer(income, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        income = self.get_object(pk)
        income.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)