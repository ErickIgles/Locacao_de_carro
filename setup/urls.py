from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Cars.views import error404, error500
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('', include('Cars.urls')),
    path('', include('Users.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = error404
handler500 = error500
