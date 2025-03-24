from django.shortcuts import render

def home(request):
    context = {'numbers': range(1, 15)}
    return render(request, 'riskapp/home.html', context)


def risk_page(request, page_id):
    return render(request, 'riskapp/risk_page.html', {'page_id': page_id})

def entry_page(request, page_id):
    return render(request, 'riskapp/Entery.html', {'page_id': page_id})

def user_guide(request):
    return render(request, 'riskapp/userguide.html')

def Definitions(request):
    return render(request, 'riskapp/Definitions.html')

def Frameworks(request):
    return render(request, 'riskapp/Frameworks.html')

def Formula(request):
    return render(request, 'riskapp/Formula.html')


def Flowchart(request):
    return render(request, 'riskapp/Flowchart.html')

def RTQ(request):
    return render(request, 'riskapp/RTQ.html')

def PII(request):
    return render(request, 'riskapp/PII.html')

def RIQ(request):
    return render(request, 'riskapp/RIQ.html')

def ai_score(request):
    return render(request, 'riskapp/ai_score.html')
def cmatrix(request):
    return render(request, 'riskapp/cmatrix.html')
def RCM(request):
    return render(request, 'riskapp/RCM.html')
def rescore(request):
    return render(request, 'riskapp/rescore.html')

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


rtq_data = "/Users/nirbhaysedha/Desktop/AI-Assess-Tool/ai_risk_assessment/riskapp/templates/riskapp/data/rtq.json"
@csrf_exempt
def rtq_save(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            final_data = {"RTQ": data}
            with open(rtq_data, 'w') as file:
                json.dump(data, file, indent=2)
                
            return JsonResponse({"message": "Responses saved successfully"})
        except Exception as e:
            return JsonResponse({"message": "Error saving data", "error": str(e)}, status=500) 
    return JsonResponse({"message": "Invalid request"}, status=400)




pii_data = "/Users/nirbhaysedha/Desktop/AI-Assess-Tool/ai_risk_assessment/riskapp/templates/riskapp/data/pii.json"
@csrf_exempt
def pii_save(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            final_data = {"PII": data}
            with open(pii_data, 'w') as file:
                json.dump(data, file, indent=2)
                
            return JsonResponse({"message": "Responses saved successfully"})
        except Exception as e:
            return JsonResponse({"message": "Error saving data", "error": str(e)}, status=500) 
    return JsonResponse({"message": "Invalid request"}, status=400)

import json
import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

riq_data = "/Users/nirbhaysedha/Desktop/AI-Assess-Tool/ai_risk_assessment/riskapp/templates/riskapp/data/riq.json"

@csrf_exempt
def riq_save(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))

            if "responses" not in data:
                return JsonResponse({"message": "Invalid data format"}, status=400)

            responses = data["responses"]

            if not responses:
                return JsonResponse({"message": "No data received"}, status=400)

            # Debugging: Print received data
            print("Received Data:", responses)

            with open(riq_data,'w',encoding='utf-8') as file:
                json.dump({"RIQ": responses}, file, indent=2)

            return JsonResponse({"message": "Responses saved successfully"})

        except json.JSONDecodeError:
            return JsonResponse({"message": "Invalid JSON format"}, status=400)
        except Exception as e:
            print(f"Error saving data: {str(e)}")  
            return JsonResponse({"message": "Error saving data", "error": str(e)}, status=500)

    return JsonResponse({"message": "Invalid request"}, status=400)


matrix= "/Users/nirbhaysedha/Desktop/AI-Assess-Tool/ai_risk_assessment/riskapp/templates/riskapp/data/matrix.json"
@csrf_exempt
def matrix_save(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            final_data = {"MATRIX": data}
            print("d",data)
            with open(matrix, 'w') as file:
                json.dump(data, file, indent=2)
                
            return JsonResponse({"message": "Responses saved successfully"})
        except Exception as e:
            return JsonResponse({"message": "Error saving data", "error": str(e)}, status=500) 
    return JsonResponse({"message": "Invalid request"}, status=400)



rcm= "/Users/nirbhaysedha/Desktop/AI-Assess-Tool/ai_risk_assessment/riskapp/templates/riskapp/data/rcm.json"
@csrf_exempt
def rcm_save(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            final_data = {"RCM": data}
            print("d",data)
            with open(rcm, 'w') as file:
                json.dump(data, file, indent=2)
                
            return JsonResponse({"message": "Responses saved successfully"})
        except Exception as e:
            return JsonResponse({"message": "Error saving data", "error": str(e)}, status=500) 
    return JsonResponse({"message": "Invalid request"}, status=400)







from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os

# Path to JSON file for storing entries
entry="/Users/nirbhaysedha/Desktop/AI-Assess-Tool/ai_risk_assessment/riskapp/templates/riskapp/data/entery.json"

@csrf_exempt  # Disable CSRF for simplicity (consider using proper authentication in production)
def save_entry(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from request
            entry = json.loads(request.body)

            # Load existing data
            if os.path.exists(entry):
                with open(entry, 'r') as file:
                    data = json.load(file)
            else:
                data = []

            # Append new entry
            data.append(entry)

            # Save back to file
            with open(entry, 'w') as file:
                json.dump(data, file, indent=4)

            return JsonResponse({"status": "success", "message": "Data saved successfully!"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method."})
