from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import subprocess
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def ranning(request):
    data=json.loads(request.body)
    user_input1 =  data.get('url') # 'url' is the name attribute of your textbox
    user_input2 =  data.get('short')
    user_choice =  data.get('todo')
    #print(user_input1)
    result = subprocess.run(['python', 'myapp/scripts/only.py', user_choice, user_input1, user_input2], capture_output=True, text=True)
    data = {'output': result.stdout, 'status': 'success', 'error': result.stderr}
    if result.returncode == 0:
        return JsonResponse(data)
    else:
        return JsonResponse(f"Error: {result.stderr}")
