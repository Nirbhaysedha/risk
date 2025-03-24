from django.urls import path
from . import views
from django.urls import path
from riskapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('page<int:page_id>/', views.risk_page, name='risk_page'),
    path('userguide/', views.user_guide, name='userguide'),  # Added this line
    path('Definitions/', views.Definitions, name='Definitions'), 
    path('Frameworks/', views.Frameworks, name='Frameworks'),
    path('Formula/', views.Formula, name='Formula'),  
    path('Flowchart/', views.Flowchart, name='Flowchart'),  
    path('RTQ/', views.RTQ, name='RTQ'),
    path('PII/', views.PII, name='PII'),
    path('RIQ/', views.RIQ, name='RIQ'),  
    path('ai_score/', views.ai_score, name='ai_score'),  
    path('cmatrix/', views.cmatrix, name='cmatrix'), 
    path('rescore/', views.rescore, name='rescore'),
    path('RCM/', views.RCM, name='RCM'),   
    path('rtq_save', views.rtq_save, name='rtq_save'),
    path('pii_save', views.pii_save, name='pii_save'),
    path('riq_save', views.riq_save, name='riq_save'),
    path('matrix_save', views.matrix_save, name='matrix_save'),
    path('rcm_save', views.rcm_save, name='rcm_save'),
    path('save_entry', views.save_entry, name='save_entry'),
]

