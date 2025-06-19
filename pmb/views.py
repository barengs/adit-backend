from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Parent, Calon_mahasiswa, BuktiBayar, BuktiIdentitas, Registration_wave, Payment
from .serializers import (ParentSerializer, ParentListSerializer, Calon_mahasiswaSerializer,
                         Calon_mahasiswaListSerializer, Calon_mahasiswaBulkInsertSerializer, BuktiBayarSerializer, 
                         BuktiIdentitasSerializer, BuktiBayarListSerializer, BuktiIdentitasListSerializer, 
                         Registration_waveSerializer, Registration_waveListSerializers, PaymentSerializer, PaymentListSerializer)

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class ParentList(APIView):

    @swagger_auto_schema(
        responses={200: ParentListSerializer(many=True)},
        tags=['Parent'],
    )
    def get(self, request, format=None):
        parents = Parent.objects.all()
        serializer = ParentListSerializer(parents, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new Parent",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=[
                'first_name', 'nik', 'kk', 
                'address', 'contact', 'job', 'income'
            ],
            properties={
                'first_name': openapi.Schema(type=openapi.TYPE_STRING, maxLength=50),
                'last_name': openapi.Schema(type=openapi.TYPE_STRING, maxLength=50, nullable=True),
                'nik': openapi.Schema(type=openapi.TYPE_STRING, maxLength=16),
                'kk': openapi.Schema(type=openapi.TYPE_STRING, maxLength=16),
                'address': openapi.Schema(type=openapi.TYPE_STRING),
                'contact': openapi.Schema(type=openapi.TYPE_STRING, maxLength=15),
                'job': openapi.Schema(type=openapi.TYPE_INTEGER),
                'income': openapi.Schema(type=openapi.TYPE_INTEGER),
            },
        ),
        security=[],
        tags=['Parent'],
    )
    def post(self, request, format=None):
        serializer = ParentListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class ParentDetail(APIView):
    def get_object(self, pk):
        try:
            return Parent.objects.get(pk=pk)
        except Parent.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        responses={200: ParentListSerializer()},
        tags=['Parent']
    )
    def get(self, request, pk, format=None):
        parent = self.get_object(pk)
        serializer = ParentListSerializer(parent)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=ParentSerializer,
        responses={200: ParentSerializer()},
        tags=['Parent']
    )
    def put(self, request, pk, format=None):
        parent = self.get_object(pk)
        serializer = ParentSerializer(parent, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        parent = self.get_object(pk)
        parent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CalonMahasiswaList(APIView):

    @swagger_auto_schema(
        responses={200: Calon_mahasiswaListSerializer(many=True)},
        tags=['CalonMahasiswa'],
    )
    def get(self, request, format=None):
        calon = Calon_mahasiswa.objects.all()
        serializer = Calon_mahasiswaListSerializer(calon, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new Calon Mahasiswa",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=[
                'code', 'first_name', 'address', 'email', 'phone', 'gender',
                'religion', 'citizen', 'province', 'regency', 'subdistrict',
                'village', 'registrationpath', 'faculty', 'studyprogram',
                'registrationperiod', 'school', 'parent'
            ],
            properties={
                'code': openapi.Schema(type=openapi.TYPE_STRING, maxLength=10),
                'first_name': openapi.Schema(type=openapi.TYPE_STRING, maxLength=50),
                'last_name': openapi.Schema(type=openapi.TYPE_STRING, maxLength=50, nullable=True),
                'address': openapi.Schema(type=openapi.TYPE_STRING),
                'email': openapi.Schema(type=openapi.TYPE_STRING, format='email'),
                'phone': openapi.Schema(type=openapi.TYPE_STRING, maxLength=15),
                'gender': openapi.Schema(type=openapi.TYPE_INTEGER),
                'religion': openapi.Schema(type=openapi.TYPE_INTEGER),
                'citizen': openapi.Schema(type=openapi.TYPE_INTEGER),
                'province': openapi.Schema(type=openapi.TYPE_INTEGER),
                'regency': openapi.Schema(type=openapi.TYPE_INTEGER),
                'subdistrict': openapi.Schema(type=openapi.TYPE_INTEGER),
                'village': openapi.Schema(type=openapi.TYPE_INTEGER),
                'registrationpath': openapi.Schema(type=openapi.TYPE_INTEGER),
                'faculty': openapi.Schema(type=openapi.TYPE_INTEGER),
                'studyprogram': openapi.Schema(type=openapi.TYPE_INTEGER),
                'registrationperiod': openapi.Schema(type=openapi.TYPE_INTEGER),
                'school': openapi.Schema(type=openapi.TYPE_INTEGER),
                'parent': openapi.Schema(type=openapi.TYPE_INTEGER),
            },
        ),
        security=[],
        tags=['CalonMahasiswa'],
    )
    def post(self, request, format=None):
        serializer = Calon_mahasiswaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CalonMahasiswaDetail(APIView):

    def get_object(self, pk):
        try:
            return Calon_mahasiswa.objects.get(pk=pk)
        except Calon_mahasiswa.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        responses={200: Calon_mahasiswaListSerializer()},
        tags=['CalonMahasiswa'],
    )
    def get(self, request, pk, format=None):
        calon = self.get_object(pk)
        serializer = Calon_mahasiswaListSerializer(calon)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=Calon_mahasiswaSerializer,
        responses={200: Calon_mahasiswaSerializer()},
        tags=['CalonMahasiswa'],
    )
    def put(self, request, pk, format=None):
        calon = self.get_object(pk)
        serializer = Calon_mahasiswaSerializer(calon, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        calon = self.get_object(pk)
        calon.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CalonMahasiswaBulkInsertAPIView(APIView):
    @swagger_auto_schema(
        operation_description="Bulk insert calon mahasiswa",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['calon_mahasiswa'],
            properties={
                'calon_mahasiswa': openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'code': openapi.Schema(type=openapi.TYPE_STRING),
                            'first_name': openapi.Schema(type=openapi.TYPE_STRING),
                            'last_name': openapi.Schema(type=openapi.TYPE_STRING),
                            'email': openapi.Schema(type=openapi.TYPE_STRING),
                            'phone': openapi.Schema(type=openapi.TYPE_STRING),
                            'address': openapi.Schema(type=openapi.TYPE_STRING),
                            'gender': openapi.Schema(type=openapi.TYPE_INTEGER),
                            'religion': openapi.Schema(type=openapi.TYPE_INTEGER),
                            'citizen': openapi.Schema(type=openapi.TYPE_INTEGER),
                            'province': openapi.Schema(type=openapi.TYPE_INTEGER),
                            'regency': openapi.Schema(type=openapi.TYPE_INTEGER),
                            'subdistrict': openapi.Schema(type=openapi.TYPE_INTEGER),
                            'village': openapi.Schema(type=openapi.TYPE_INTEGER),
                            'registrationpath': openapi.Schema(type=openapi.TYPE_INTEGER),
                            'faculty': openapi.Schema(type=openapi.TYPE_INTEGER),
                            'studyprogram': openapi.Schema(type=openapi.TYPE_INTEGER),
                            'registrationperiod': openapi.Schema(type=openapi.TYPE_INTEGER),
                            'school': openapi.Schema(type=openapi.TYPE_INTEGER),
                            'parent': openapi.Schema(
                                type=openapi.TYPE_OBJECT,
                                properties={
                                    'nik': openapi.Schema(type=openapi.TYPE_STRING),
                                    'first_name': openapi.Schema(type=openapi.TYPE_STRING),
                                    'last_name': openapi.Schema(type=openapi.TYPE_STRING),
                                    'kk': openapi.Schema(type=openapi.TYPE_STRING),
                                    'address': openapi.Schema(type=openapi.TYPE_STRING),
                                    'contact': openapi.Schema(type=openapi.TYPE_STRING),
                                    'job': openapi.Schema(type=openapi.TYPE_INTEGER),
                                    'income': openapi.Schema(type=openapi.TYPE_INTEGER),
                                }
                            )
                        }
                    )
                )
            }
        ),
        responses={201: "Created", 400: "Validation Error"},
        tags=["CalonMahasiswa"]
    )
    def post(self, request, format=None):
        serializer = Calon_mahasiswaBulkInsertSerializer(data=request.data)
        if serializer.is_valid():
            inserted = serializer.save()
            return Response({
                "status": "success",
                "inserted_count": len(inserted)
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BuktiBayarList(APIView):

    @swagger_auto_schema(
        responses={200: BuktiBayarSerializer(many=True)},
        tags=['BuktiBayar']
    )
    def get(self, request, format=None):
        buktibayar = BuktiBayar.objects.all()
        serializer = BuktiBayarListSerializer(buktibayar, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Upload bukti bayar",
        request_body=BuktiBayarSerializer,
        responses={201: BuktiBayarSerializer()},
        tags=['BuktiBayar']
    )
    def post(self, request, format=None):
        serializer = BuktiBayarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BuktiBayarDetail(APIView):
    def get_object(self, pk):
        try:
            return BuktiBayar.objects.get(pk=pk)
        except BuktiBayar.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        responses={200: BuktiBayarListSerializer()},
        tags=['BuktiBayar']
    )
    def get(self, request, pk, format=None):
        buktibayar = self.get_object(pk)
        serializer = BuktiBayarListSerializer(buktibayar)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=BuktiBayarSerializer,
        responses={200: BuktiBayarSerializer()},
        tags=['BuktiBayar']
    )
    def put(self, request, pk, format=None):
        buktibayar = self.get_object(pk)
        serializer = BuktiBayarSerializer(buktibayar, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        buktibayar = self.get_object(pk)
        buktibayar.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BuktiIdentitasList(APIView):

    @swagger_auto_schema(
        responses={200: BuktiIdentitasListSerializer(many=True)},
        tags=['BuktiIdentitas']
    )
    def get(self, request, format=None):
        buktiidentitas = BuktiIdentitas.objects.all()
        serializer = BuktiIdentitasSerializer(buktiidentitas, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Upload bukti identitas",
        request_body=BuktiIdentitasSerializer,
        responses={201: BuktiIdentitasSerializer()},
        tags=['BuktiIdentitas']
    )
    def post(self, request, format=None):
        serializer = BuktiIdentitasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BuktiIdentitasDetail(APIView):
    def get_object(self, pk):
        try:
            return BuktiIdentitas.objects.get(pk=pk)
        except BuktiIdentitas.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        responses={200: BuktiIdentitasSerializer()},
        tags=['BuktiIdentitas']
    )
    def get(self, request, pk, format=None):
        buktiidentitas = self.get_object(pk)
        serializer = BuktiIdentitasSerializer(buktiidentitas)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=BuktiIdentitasSerializer,
        responses={200: BuktiIdentitasSerializer()},
        tags=['BuktiIdentitas']
    )
    def put(self, request, pk, format=None):
        buktiidentitas = self.get_object(pk)
        serializer = BuktiIdentitasSerializer(buktiidentitas, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        buktiidentitas = self.get_object(pk)
        buktiidentitas.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RegistrationWaveList(APIView):

    @swagger_auto_schema(
        query_serializer=Registration_waveListSerializers,
        responses={200: Registration_waveSerializer(many=True)},
        tags=['Registration Wave'],
    )
    def get(self, request, format=None):
        waves = Registration_wave.objects.all()
        serializer = Registration_waveSerializer(waves, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new registration wave",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['name', 'status'],
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING),
                'status': openapi.Schema(type=openapi.TYPE_STRING)
            },
        ),
        tags=['Registration Wave'],
    )
    def post(self, request, format=None):
        serializer = Registration_waveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegistrationWaveDetail(APIView):

    def get_object(self, pk):
        try:
            return Registration_wave.objects.get(pk=pk)
        except Registration_wave.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        responses={200: Registration_waveSerializer},
        tags=['Registration Wave'],
    )
    def get(self, request, pk, format=None):
        wave = self.get_object(pk)
        serializer = Registration_waveSerializer(wave)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=Registration_waveSerializer,
        responses={200: Registration_waveSerializer},
        tags=['Registration Wave']
    )
    def put(self, request, pk, format=None):
        wave = self.get_object(pk)
        serializer = Registration_waveSerializer(wave, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        wave = self.get_object(pk)
        wave.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PaymentList(APIView):
    @swagger_auto_schema(
        query_serializer=PaymentListSerializer,
        responses={200: PaymentListSerializer (many = True)},
        tags=['Payment'],
    )
    def get(self, request, format=None):
        payments = Payment.objects.all()
        serializer = PaymentListSerializer(payments, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(
        operation_description="Create a new payment",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['calon_mahasiswa', 'amount', 'payment_number', 'payment_date'],
            properties={
                'calon_mahasiswa': openapi.Schema(type=openapi.TYPE_INTEGER),
                'amount': openapi.Schema(type=openapi.TYPE_NUMBER, format='decimal'),
                'payment_number': openapi.Schema(type=openapi.TYPE_STRING),
                'payment_date': openapi.Schema(type=openapi.FORMAT_DATETIME, description='Format: YYYY-MM-DDTHH:MM:SSZ'),
            },
        ),
        responses={201: PaymentSerializer},
        tags=['Payment'],
    )
    def post(self, request, format=None):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PaymentDetail(APIView):

    def get_object(self, pk):
        try:
            return Payment.objects.get(pk=pk)
        except Payment.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        responses={200: PaymentListSerializer},
        tags=['Payment'],
    )
    def get(self, request, pk, format=None):
        payment = self.get_object(pk)
        serializer = PaymentListSerializer(payment)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=PaymentSerializer,
        responses={200: PaymentSerializer},
        tags=['Payment'],
    )
    def put(self, request, pk, format=None):
        payment = self.get_object(pk)
        serializer = PaymentSerializer(payment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a payment by ID",
        tags=['Payment'],
    )
    def delete(self, request, pk, format=None):
        payment = self.get_object(pk)
        payment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)