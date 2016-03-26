from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    url(r'^' + settings.ADMIN_PATH + r'/', admin.site.urls),
    url(r'^nested_admin/', include('nested_admin.urls')),
]
