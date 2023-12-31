from django.db import models

status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]


class Task(models.Model):
    description = models.CharField(max_length=60, null=False, blank=False, verbose_name="Описание")
    status = models.CharField(max_length=20, choices=status_choices, default=status_choices[0][0],
                              verbose_name="Статус")
    date_of_finish = models.DateField(null=True, blank=True, verbose_name='Дата выполнения')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата изменения")

    def __str__(self):
        return f'{self.pk}.{self.description}'
