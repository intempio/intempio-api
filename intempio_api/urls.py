from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls import re_path, include, reverse_lazy
from django.views.generic.base import RedirectView
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .events.views import (
    UpTimeView, BiogenEventModelViewSet, SunovionEventModelViewSet,
    ProjectModelViewSet, FindByProjectId)
from .users.views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
# router.register(r'users', UserCreateViewSet)
router.register(r'biogen-events', BiogenEventModelViewSet)
router.register(r'sunovion-events', SunovionEventModelViewSet)
router.register(r'projects', ProjectModelViewSet)
router.register(r'project', FindByProjectId)

admin.site.site_header = 'Intempio'
admin.site.site_title = 'Admin'
admin.site.index_title = 'Events Administration'
admin.site.site_url = None

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('ping', UpTimeView.as_view(), name='up_time'),
                  path('api/v1/', include(router.urls)),
                  path('api/v1/api-token-auth', views.obtain_auth_token),
                  path('api/v1/api-auth/', include('rest_framework.urls', namespace='rest_framework')),

                  # the 'api-root' from django rest-frameworks default router
                  # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
                  re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),
              ] \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      url(r'^__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
