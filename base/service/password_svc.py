from typing import Dict
from base.forms.password_forms import passwordForm
from base.models import SecurePassword


def create_password(data: passwordForm) -> Dict:
    created_password = SecurePassword.objects.create(name=data.name, password=data.password)
    return created_password

