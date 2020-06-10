from rest_framework import  status,generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django_filters import rest_framework as filters
from .models import Page
from .serializers import landingPageSerializer
from .views import add_page


class PageList(generics.ListAPIView):
    serializer_class = landingPageSerializer
    queryset = Page.objects.all()
    # filter_backends = [filters.DjangoFilterBackend]
    # filterset_fields = ['url']

    def get_queryset(self):
        url=self.kwargs['url']
        url = url.split("=")[1]
        pre_set = Page.objects.filter(page_url=url)
        # try:
        #     queryset.filter(page_url=url)
        # except:
        #     print("none")
        return pre_set
       
class AllPagesList(generics.ListAPIView):
    queryset = Page.objects.all()
    serializer_class = landingPageSerializer

# class Alexa(APIView):

#     def alexa(request, url):
#         add_page()

