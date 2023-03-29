from base.forms.password_forms import passwordForm
from base.services import password_svc
from django.http import JsonResponse
import json


def create_password(request):
    request_params = json.loads(request.POST.get("params"))
    form_data = passwordForm(request_params)
    created_password = password_svc.create_password(form_data)
    return JsonResponse({"password": created_password})
