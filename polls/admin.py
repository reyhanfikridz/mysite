"""
Import:
1. Django library
2. Models
"""
from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    """
    Class agar Choice dapat ditambah oleh admin
    dengan tampilan tabular
    """
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    """
    Class agar Question dapat ditambah oleh admin dengan adanya:
    1. fieldsets: Field Question yang dipisah dengan fieldsets
    2. inlines: Menampilkan Choice sesuai Class yang ditentukan
    3. list_display: Menampilkan tabel Question dengan kolom yang ditentukan
    4. list_filter: Menampilkan filter dengan atribut yang ditentukan
    5. search_fields: Menampilkan search berdasarkan atribut yang ditentukan
    """
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'],
                              'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
