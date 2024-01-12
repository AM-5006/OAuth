import json
import requests
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User

def index(requets):
    return HttpResponse("Bye, World!")

@csrf_exempt
def save_user_info(request):
    if request.method == 'POST':
        data = {}
        if request.body:
            try:
                data = json.loads(request.body.decode('utf-8'))
            except json.JSONDecodeError:
                return JsonResponse({'success': False, 'message': 'Invalid JSON data'})

        token = data.get('token', '')
        headers = {'Authorization': f'Bearer {token}'}

        response = requests.get('https://www.googleapis.com/oauth2/v2/userinfo', headers=headers)

        if response.status_code == 200:
            user_info = response.json()
            user_data = {
                'id': user_info.get('id'),
                'email': user_info.get('email'),
                'first_name': user_info.get('given_name'),
                'last_name': user_info.get('family_name'),
                'google_id': user_info.get('id')
            }

            return JsonResponse({'success': True, 'data': user_data})
        else:
            return JsonResponse({'success': False, 'message': 'Failed to fetch user information'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'})


# @csrf_exempt
# def save_user_info(request):
#     if request.method == 'POST':
#         token = request.POST.get('token', '')
#         data = json.loads(request.body.decode('utf-8'))
#         token = data.get('token', '')
#         headers = {'Authorization': f'Bearer {token}'}
#         response = requests.get('https://www.googleapis.com/oauth2/v2/userinfo', headers=headers)
#         if response.status_code == 200:
#             user_info = response.json()
#             user_data = {
#                 'id': user_info.get('id'),
#                 'email': user_info.get('email'),
#                 'first_name': user_info.get('given_name'),
#                 'last_name': user_info.get('family_name'),
#                 'token': user_info.get('token')
#             }
#             # user_profile, created = User.objects.get_or_create(**user_data)

#             return JsonResponse({'success': True, 'data': user_data})
#         else:
#             return JsonResponse({'success': False, 'message': 'Failed to fetch user information'})
#     else:
#         return JsonResponse({'success': False, 'message': 'Invalid request method'})


# def get_user(request):
#     if request.method == 'GET':
#         authorization_header = request.headers.get('Authorization', '')
#         if not authorization_header.startswith('Bearer '):
#             return JsonResponse({'success': False, 'message': 'Invalid Authorization header'}, status=401)
#         provided_token = authorization_header[len('Bearer '):]
#         try:
#             user = User.objects.get(token=provided_token)
#             if user:
#                 user_data = {
#                     'id': user.id,
#                     'email': user.email,
#                     'first_name': user.first_name,
#                     'last_name': user.last_name,
#                     'token': provided_token,
#                 }
#                 return JsonResponse({'success': True, 'data': user_data})
#             else:
#                 return JsonResponse({'success': False, 'message': 'User not authenticated'}, status=401)
#         except Exception as e:
#             return JsonResponse({'success': False, 'message': str(e)}, status=500)
#     return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=400)

#ya29.a0AfB_byDwHd3ogR0UDzTcrD8T_gQ7C-1jn3gw8i-d9Aigw5E4HXjPmTwVSKHRCp8kValS7eZ6WwZqSI5WOH0p4bVOgN0451W1jD18JZX8lOCqSAVMMEVsQ96UUlzHyFDYMkgqrva3HkqW5hDMxFdHCtSmZFNWHTHSUNAEaCgYKARsSARMSFQHGX2Mitk0p4Jpr7n2-s3GqD5brnA0171
#ya29.a0AfB_byB7KfeLuKfaFf2XWUYlj_6x7VBTRLuiylz2thE2fe02RAfvwRWASbw8eGxbzQsYxEOYYwGSMenmXyExz3poOtWwtJu1D2KEIXB7mXXLH0hU7WMnSOkqMy5NrGtGs2UJf17wXWTtzcQX5nYAEEPeXB2sXzeRxbQ0aCgYKAV4SARMSFQHGX2MiWhBzc6KaT0gGIOl0AJwV7w0171



# const { data } = await axiosInstance.post(
# 			'https://oauth2.googleapis.com/token',
# 			{
# 				client_id: configKeys.GOOGLE_CLIENT_ID,
# 				client_secret: configKeys.GOOGLE_CLIENT_SECRET,
# 				code,
# 				redirect_uri: configKeys.GOOGLE_CALLBACK_URL,
# 				grant_type: 'authorization_code',
# 			}
# 		);
