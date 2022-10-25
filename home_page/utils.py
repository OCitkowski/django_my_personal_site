from home_page.models import Home
from django.contrib.auth.mixins import LoginRequiredMixin



menu = [{'title': "Home", 'url_name': ''},
        {'title': "AboutMe", 'url_name': 'aboutme'},
        {'title': "Resume", 'url_name': 'resume'},
        {'title': "Portfolio", 'url_name': 'portfolio'},
        {'title': "Blog", 'url_name': 'blogs'},
        {'title': "Contact", 'url_name': 'contact'},
]

class MixinView():
        model = Home
        # paginate_by = 3
        context_object_name = 'home_page'


        def get_user_context(self, **kwargs):

                context = kwargs

                context['menu'] = menu
                first_posts = Home.objects.filter(status='p').order_by('-date_update')[:2]
                context['first_posts'] = first_posts

                return context