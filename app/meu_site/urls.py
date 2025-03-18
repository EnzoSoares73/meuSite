from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('', include('authentication.urls'))
)
urlpatterns += [path("i18n/", include("django.conf.urls.i18n")),]
