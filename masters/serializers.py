from rest_framework import serializers
from .models import Religion, Gender, Citizen, Province, Regency, Subdistrict, Village, RegistrationPath, Faculty, StudyProgram, RegistrationPeriod, School, Job, Income
from rest_framework.validators import UniqueValidator


class ReligionSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(max_length=100)
    # code = serializers.CharField(max_length=10)
    
    # def create(self, validated_data):
    #     return super().create(validated_data)
    
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.code = validated_data.get('code', instance.code)
    #     instance.save()
    #     return instance
    
    class Meta:
        model = Religion
        fields = '__all__'

class ReligionListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    code = serializers.CharField(max_length=10)

class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields ='__all__'

class GenderListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    code = serializers.CharField(max_length=10)

class CitizenSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    code = serializers.CharField(max_length=10)

class CitizenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citizen
        fields = '__all__'

class CitizenListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    code = serializers.CharField(max_length=10)

class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = '__all__'

class ProvinceListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    code = serializers.CharField(max_length=10)
    meta = serializers.JSONField(default=dict)
    
class RegencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Regency
        fields = '__all__'

class RegencyListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    code = serializers.CharField(max_length=10)
    province = serializers.PrimaryKeyRelatedField(queryset=Province.objects.all())
    meta = serializers.JSONField(default=dict)

class SubdistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subdistrict
        fields = '__all__'

class SubdistrictListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    code = serializers.CharField(max_length=10)
    regency = serializers.PrimaryKeyRelatedField(queryset=Regency.objects.all())
    meta = serializers.JSONField(default=dict)

class VillageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Village
        fields = '__all__'

class VillageListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    code = serializers.CharField(max_length=10)
    subdistrict = serializers.PrimaryKeyRelatedField(queryset=Subdistrict.objects.all())
    meta = serializers.JSONField(default=dict)

class RegistrationPathSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrationPath
        fields = '__all__'

class RegistrationPathListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    code = serializers.CharField(max_length=10)

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'

class FacultyListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    code = serializers.CharField(max_length=10)

class StudyProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyProgram
        fields = '__all__'

class StudyProgramListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    code = serializers.CharField(max_length=10)
    faculty = serializers.PrimaryKeyRelatedField(queryset=Faculty.objects.all())

class RegistrationPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrationPeriod
        fields = '__all__'

class RegistrationPeriodListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    period = serializers.CharField(max_length=9)

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

class SchoolListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    code = serializers.CharField(max_length=50, 
                                 validators = [UniqueValidator(queryset=School.objects.all())])
    address = serializers.CharField(max_length=255)
    phone = serializers.CharField(max_length=15, 
                                  validators = [UniqueValidator(queryset=School.objects.all())])

    class Meta:
        model = School
        fields = ['id, name, code, address, phone']


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

class JobListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'

class IncomeListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    amount = serializers.CharField(max_length=50)