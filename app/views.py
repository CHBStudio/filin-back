from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import ProductService, Lease, Company
from app.serializers import CompanySerializer, LeaseSerializer
from django.db.models import Q


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening

class NoCSRFView(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication,)

class LandingView(NoCSRFView):
    def get(self,request,*args):
        leases = Lease.objects.all().order_by('order')[:3]
        companies = Company.objects.all()
        return Response(data={
            'companies': CompanySerializer(companies,many=True).data
        })

class ProductView(NoCSRFView):

    def get(self,request):
        type_id = request.GET.get('type')
        q = Q()
        if type_id != 'all' and type_id:
            type = ProductService.objects.get(id=type_id)
            q = Q(tags__in=[type])
        data = []
        floors = sorted(list(Company.objects.all().values_list('floor',flat=True).distinct()))

        for fl in floors:
            companies = Company.objects.filter(q).order_by('floor')
            data.append({
                'floor':fl,
                'data': CompanySerializer(companies,many=True).data
            })
        return Response(data={
            'data':data
        })

class ServiceView(NoCSRFView):

    def get(self,request):
        type_id = request.GET.get('type')
        q = Q()
        if type_id != 'all':
            type = ProductService.objects.get(id=type_id)
            q = Q(tags__in=[type])
        data = []
        floors = sorted(list(Company.objects.all().values_list('floor',flat=True).distinct()))

        for fl in floors:
            companies = Company.objects.filter(q).order_by('floor')
            data.append({
                'floor':fl,
                'data': CompanySerializer(companies,many=True).data
            })
        return Response(data={
            'data':data
        })



        pass

class LeaseView(NoCSRFView):

    def get(self,request):
        leases = Lease.objects.all().order_by('order')
        return Response(data={
            'leases':LeaseSerializer(leases).data
        })
