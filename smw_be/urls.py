from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# To display React view here
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('StillMinutePhotographs.urls')),
    # This path will render our react app in djnago
    path('', TemplateView.as_view(template_name='index.html')),
    # Use HashRouter in React to render the react app instad of django URLs
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)