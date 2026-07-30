from django.contrib import admin
from .models import *

# Register your models here.
for model in list(globals().values()):
    try:
        if hasattr(model, "_meta"):
            admin.site.register(model)
    except Exception:
        pass
