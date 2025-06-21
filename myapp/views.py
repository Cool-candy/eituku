from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import subprocess
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def ranning(request):
    user_input1 =  request.POST.get('url') # 'url' is the name attribute of your textbox
    user_input2 =  request.POST.get('short')
    user_choice =  request.POST.get('todo')
    result = subprocess.run(['python', 'myapp/scripts/only.py', user_choice, user_input1, user_input2], capture_output=True, text=True)
    data = {'output': result.stdout, 'error': result.stderr}
    if result.returncode == 0:
        return JsonResponse(data)
    else:
        return HttpResponse(f"Error: {result.stderr}")
