from django.contrib import admin
from api import models


admin.site.register([
    models.Student,
    models.Institute
])