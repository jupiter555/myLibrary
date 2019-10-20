from django.conf.urls import url


from . import views
from .models import BookStore
urlpatterns = [

    url(r'^add_book',views.add_book),

    url(r'^add_author',views.add_author),

    url(r'^all_book',views.all_book),

    url(r'^detail/(\d+)',views.detail),

    url(r'^update_book/(\d+)',views.update_book),

    url(r'^delete_book/(\d+)',views.delete_book),
]




