from django.contrib import admin
from django.urls import path, include # new
from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    # Local Apps
    path('', include('users.urls')), # new

]


if settings.DEBUG: # new
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns