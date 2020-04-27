from django.urls import path
from . import views

# here we are creating the appropriate links from the url to the actual views and 
# we give names also to these views
urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("<int:pk>/", views.blog_detail, name="blog_detail"),
    path("<category>/", views.blog_category, name="blog_category"),
]