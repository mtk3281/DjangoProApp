from django.urls import path
from .views import *

urlpatterns = [
    path('add-post/', add_post_view, name='add_post'),
    path('post/<int:year>/<int:month>/<int:day>/<slug:post>', blog_post_detail_view, name='blog_post_detail'),

]
