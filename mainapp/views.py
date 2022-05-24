from django.views.generic import TemplateView

from django.http import HttpResponse
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'mainapp/index.html'

class CoursesListView(TemplateView):
    template_name = 'mainapp/courses_list.html'

class DocSiteView(TemplateView):
    template_name = 'mainapp/doc_site.html'

class ContactsView(TemplateView):
    template_name = 'mainapp/contacts.html'

class LoginView(TemplateView):
    template_name = 'mainapp/login.html'

class NewsView(TemplateView):
    template_name = 'mainapp/news.html'


#class MainPageView (TemplateView):
#    template_name = 'mainapp/index.html'

