from django.urls import path

from .views import signin, signout, signup


app_name = 'accounts'
urlpatterns = [
    path('signup', signup, name='signup'),
    path('signin', signin, name='signin'),
    path('signout', signout, name='signout'),
]
