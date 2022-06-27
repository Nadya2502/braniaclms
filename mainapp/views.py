from django.views.generic import TemplateView
import json
from django.http import HttpResponse
from django.views.generic import TemplateView
from datetime import datetime
from django.conf import settings
from mainapp.models import News

class IndexView(TemplateView):
    template_name = 'mainapp/index.html'

class CoursesListView(TemplateView):
    template_name = 'mainapp/courses_list.html'

class DocSiteView(TemplateView):
    template_name = 'mainapp/doc_site.html'

class ContactsView(TemplateView):
    template_name = 'mainapp/contacts.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['contacts']=[
            {
                'map':'https://yandex.ru/map-widget/v1/-/CCUAZHcrhA',
                'city': 'Санкт‑Петербург',
                'phone': '+7-999-11-11111',
                'email': 'geeklab@spb.ru',
                'adress': 'территория Петропавловская крепость, 3Ж',

            },
            {
                'map': 'https://yandex.ru/map-widget/v1/-/CCUAZHX3xB',
                'city': 'Казань',
                'phone': '+7-999-22-22222',
                'email': 'geeklab@kz.ru',
                'adress': 'территория Кремль, 11, Казань, Республика Татарстан, Россия',

            },
            {
                'map': 'https://yandex.ru/map-widget/v1/-/CCUAZHh9kD',
                'city': 'Москва',
                'phone': '+7-999-33-33333',
                'email': 'geeklab@msk.ru',
                'adress': 'Красная площадь, 7, Москва, Россия',

            }

        ]
        return context_data
class LoginView(TemplateView):
    template_name = 'mainapp/login.html'

class NewsView(TemplateView):
    template_name = 'mainapp/news.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        #with open(settings.BASE_DIR / 'news.json', encoding='utf-8') as news_file:
         #   context_data['object_list'] = json.load(news_file)
        context_data['object_list'] = News.objects.all()
        return context_data


#class MainPageView (TemplateView):
#    template_name = 'mainapp/index.html'


