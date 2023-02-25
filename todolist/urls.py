from django.contrib import admin
from django.urls import include, path
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def health_check(request):
    return Response({'status': 'OK'})


urlpatterns = [
    path('core/', include(('core.urls', 'core'))),
    path('goals/', include('goals.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('ping/', health_check, name='health-check'),
    path('admin/', admin.site.urls),
]
