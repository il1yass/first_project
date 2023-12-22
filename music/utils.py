import logging
from django.contrib import messages
from django.db.models import Count
from .models import *


logger = logging.getLogger(__name__)

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
]

class DataMixin:
    paginate_by = 20

    def get_user_context(self,**kwargs):
        try:
            context = kwargs
            cats = Category.objects.annotate(Count('music'))

            user_menu = menu.copy()


            context['menu'] = user_menu

            context['cats'] = cats
            if 'cat_selected' not in context:
                context['cat_selected'] = 0
            return context
        except Exception as e:
            messages.error(f"An error occurred: {e}", 'Something is wrong!')
            logger.error(f'An error occurred: {e}')


