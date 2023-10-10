from django.contrib import admin
from django.urls import path

import revieWs.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', revieWs.views.index),
    path('book-search', revieWs.views.book_search)
]
