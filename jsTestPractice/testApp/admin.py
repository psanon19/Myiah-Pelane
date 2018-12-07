from django.contrib import admin
from .models import TestModel, UserSetup , VocabularyModel
from .models import QuestionModel
# Register your models here.


admin.site.register(TestModel)

admin.site.register(QuestionModel)

admin.site.register(UserSetup)


admin.site.register(VocabularyModel)