from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')

            if not username or not password:
                return JsonResponse(
                    {'status': 'fail', 'message': 'Username and password required'},
                    status=400
                )

            user = authenticate(username=username, password=password)
            
            if user is not None:
                return JsonResponse({'status': 'ok', 'message': 'Login successful'})
            else:
                return JsonResponse(
                    {'status': 'fail', 'message': 'Invalid credentials'},
                    status=401
                )
        except json.JSONDecodeError:
            return JsonResponse(
                {'status': 'fail', 'message': 'Invalid JSON'},
                status=400
            )
    else:
        return JsonResponse(
            {'status': 'fail', 'message': 'Only POST method allowed'},
            status=405
        )