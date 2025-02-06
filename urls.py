# Uncomment the imports before you add the code
from django.urls import path  # Make sure this import is uncommented
from django.conf.urls.static import static
from django.conf import settings
from . import views  # Uncomment this line so that `views.get_cars` works

app_name = 'djangoapp'

urlpatterns = [
    # path for registration
     
    # path for login
    # path(route='login', view=views.login_user, name='login'),

    # path for dealer reviews view

    # path for add a review view

    # path for getting cars
    path(route='get_cars', view=views.get_cars, name='getcars'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
