from rest_framework import serializers
from .models import Parent, Calon_mahasiswa
from rest_framework.validators import UniqueValidator

class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = '__all__'

class ParentListSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50, allow_blank=True, required=False)
    nik = serializers.CharField(max_length=16)
    kk = serializers.CharField(max_length=16)
    address = serializers.CharField()
    contact = serializers.CharField(max_length=15)
    job = serializers.CharField(source='job.__str__', read_only=True)
    income = serializers.CharField(source='income.__str__', read_only=True)

    class Meta:
        model = Parent
        fields = [
            'id', 'first_name', 'last_name', 'nik', 'kk', 
            'address', 'contact', 'job', 'income'
        ]

class Calon_mahasiswaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calon_mahasiswa
        fields = '__all__'

class Calon_mahasiswaListSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    code = serializers.CharField(max_length=10)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50, allow_blank=True, required=False)
    email = serializers.EmailField(validators=[UniqueValidator(queryset=Calon_mahasiswa.objects.all())])
    phone = serializers.CharField(max_length=15)
    address = serializers.CharField()

    gender = serializers.CharField(source='gender.__str__', read_only=True)
    religion = serializers.CharField(source='religion.__str__', read_only=True)
    citizen = serializers.CharField(source='citizen.__str__', read_only=True)

    province = serializers.CharField(source='province.__str__', read_only=True)
    regency = serializers.CharField(source='regency.__str__', read_only=True)
    subdistrict = serializers.CharField(source='subdistrict.__str__', read_only=True)
    village = serializers.CharField(source='village.__str__', read_only=True)
    
    registrationpath = serializers.CharField(source='registrationpath.__str__', read_only=True)
    faculty = serializers.CharField(source='faculty.__str__', read_only=True)
    studyprogram = serializers.CharField(source='studyprogram.__str__', read_only=True)
    registrationperiod = serializers.CharField(source='registrationperiod.__str__', read_only=True)
    school = serializers.CharField(source='school.__str__', read_only=True)
    parent = serializers.CharField(source='parent.__str__', read_only=True)

    class Meta:
        model = Calon_mahasiswa
        fields = [
            'id', 'code', 'first_name', 'last_name', 'email', 'phone', 'address',
            'gender', 'religion', 'citizen',
            'province', 'regency', 'subdistrict', 'village',
            'registrationpath', 'faculty', 'studyprogram', 'registrationperiod',
            'school', 'parent'
        ]