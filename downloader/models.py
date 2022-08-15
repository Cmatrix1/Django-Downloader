from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()

class DlModel(models.Model):
    users = models.ManyToManyField(user, related_name="dls")
    dl_file = models.FileField(upload_to="files")