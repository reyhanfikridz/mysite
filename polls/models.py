"""
Import:
1. Built-in Python Library
2. Django Library
"""
import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    """
    Class untuk model Question
    Atribut:
    1. question_text: Pertanyaan untuk voting
    2. pub_date: Tanggal pertanyaan dipublikasikan
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        """
        Fungsi untuk menentukan apakah pertanyaan baru saja dipublikasi.
        Fungsi ini ditampilkan pada model Question dengan:
        1. Berurutan sesuai pub_date
        2. Lambang boolean
        3. Deskripsi singkat
        """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def __str__(self):
        return str(self.question_text)


class Choice(models.Model):
    """
    Class untuk model Choice
    Atribut:
    1. question: Pertanyaan yang berhubungan dengan pilihan (choice)
    2. choice_text: Teks pilihan
    3. votes: Banyak vote
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.choice_text)
