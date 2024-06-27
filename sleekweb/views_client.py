from .models import *

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_list_or_404, get_object_or_404
from django.core.paginator import Paginator


from django.http import HttpResponse
import requests
import time

from django.db import models
from django.utils import timezone

import os

from datetime import datetime

from django.shortcuts import redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout

from django.contrib.postgres.search import TrigramSimilarity
from django.db.models import Q
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from datetime import datetime
from django.contrib import messages
import random
import string
from django.contrib.auth import update_session_auth_hash
from datetime import datetime, timedelta
from django.utils.timezone import make_aware

# from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

import random
import string

import base64

import time
from django.http import JsonResponse

import re
import json

from django.conf import settings
from .models import *
from django.db.models import Q

def set_Page_S():
	Page = 8
	return Page

def home_page(request):
    if request.method == 'GET':
        context = {}
        search_query = request.GET.get('s', '')  # Lấy dữ liệu tìm kiếm từ query parameter 'q'
        if search_query:
            context['search_query'] = search_query
            List_product = Product.objects.filter(Q(Name__icontains=search_query) | Q(Describe__icontains=search_query))
            context['List_product'] = List_product
        else:
            List_product = Product.objects.all()
            context = {'List_product':List_product}
        print('context',context)
        return render(request, 'sleekweb/client/home_page.html', context, status=200)

def detail_page(request,pk):
    if request.method == 'GET':
        product = Product.objects.get(pk=pk)
        context = {'product':product}
        print('context',context)
        return render(request, 'sleekweb/client/detail_page.html', context, status=200)
    
def import_data(request):
    if request.method == 'GET':
        # Đọc file JSON từ cùng thư mục
        file_path = os.path.join(os.path.dirname(__file__), 'data.json')
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        for i in data:
            obj = Product.objects.create(Name=i['Name'],
                                   Price=i['Price'],
                                   Promotion_percentage=i['Promotion_percentage'],
                                   Price_Promotion = int(i['Price'])-(int(i['Price'])*(int(i['Promotion_percentage'])/100)),
                                   Describe=i['Describe'],
                                   )
            for j in i['List_image']:
                Image_Product.objects.create(Avatar_url=j,Belong_product=obj)
        return JsonResponse({'status': 'success', 'message': 'Data imported successfully'}, status=201)
            

        