from django.contrib import admin
from django.db import models

class Advertisements(models.Model):
    title = models.CharField('Заголовок', max_length=128)
    description = models.TextField('Содержание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Отметьте, если будет уместен торг')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self): 
        return f'Advertisements(id={self.id}, title={self.title}, price={self.price})'
    
    @admin.display(description='Дата создания')
    def created_date(self):
        from django.utils import timezone
        from django.utils.html import format_html
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: green; font-weight: bold">Сегодня в {}</span>', created_time
            )
        return self.created_at.strftime('%d:%m:%Y в %H:%M:%S')
    
    class Meta:
        db_table = 'advertisements'
