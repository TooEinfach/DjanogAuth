from django.shortcuts import render

from .models import Files
import os
import json
import logging


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.conf import settings

from django.core.files.storage import FileSystemStorage

# Create your views here.

class DemoView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello! This is a Demo!'}
        return Response(content)

    def post(self, request):
        success = {'message': 'Post was successful'}
        failure = {'message': 'Save failed'}
        if request.method == 'POST':
            print('Raw Data: "%s"' % request.body)
            # received_json_date=json.loads(request.body)
            # logging.info('Post is ' + str(received_json_date))
            # newdoc = Files(json_file=request.FILES.get('myfile'))
            # newdoc.save()                
            return Response(success)
            
