"""
URL configuration for ai_risk_assessment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""




from django.urls import path
from riskapp import views  # Ensure correct app name here
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from riskapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('page<int:page_id>/', views.risk_page, name='risk_page'),
    path('userguide/', views.user_guide, name='userguide'),
    path('Definitions/', views.Definitions, name='Definitions'),
    path('Frameworks/', views.Frameworks, name='Frameworks'),
    path('Formula/', views.Formula, name='Formula'),
    path('Flowchart/', views.Flowchart, name='Flowchart'),
    path('RTQ/', views.RTQ, name='RTQ'),
    path('PII/', views.PII, name='PII'),
    path('RIQ/', views.RIQ, name='RIQ'),
    path('ai_score/', views.ai_score, name='ai_score'),
    path('cmatrix/', views.cmatrix, name='cmatrix'),
    path('RCM/', views.RCM, name='RCM'),
    path('rescore/', views.rescore, name='rescore'),
    path('rtq_save', views.rtq_save, name='rtq_save'),
    path('pii_save', views.pii_save, name='pii_save'),
    path('riq_save', views.riq_save, name='riq_save'),
    path('matrix_save', views.matrix_save, name='matrix_save'),
    path('rcm_save', views.rcm_save, name='rcm_save'),
    path('save_entry', views.save_entry, name='save_entry'),
    path('admin/', admin.site.urls),
    path('riskapp/', include('riskapp.urls')),
]



