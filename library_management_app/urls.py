from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter, DefaultRouter

# router = SimpleRouter()
router = DefaultRouter()
router.register('authors', views.AuthorViewSet)
router.register('books', views.BookViewSet)

# urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    path('send_mail/', views.send_mail_function)
]

# urlpatterns = [
# path('authors/', views.AuthorView.as_view(), name='authors'),
# path('', include(router.urls)),
# path('authors/<pk>', views.AuthorDetail.as_view(), name='author-detail')

# path('welcome/', views.welcome),
# path('welcome-you/', views.welcome_you),
# path('books/', views.list_books),
# path('books/<pk>', views.book_detail)
# ]
