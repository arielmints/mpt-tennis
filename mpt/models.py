from django.db import models
from ckeditor.fields import RichTextField


class HomePage(models.Model):
    main_text = RichTextField()
    contact_text = RichTextField(default=None)
