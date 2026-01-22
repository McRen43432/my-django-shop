from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 1. Путь к панели администратора (теперь будет работать /admin/)
    path('admin/', admin.site.urls),

    # 2. Ваши приложения
    path('', include('store.urls')),
    path('reviews/', include('reviews.urls')),
    path('promotions/', include('promotions.urls')),
]

# 3. Настройка для отображения статики (CSS, картинки) во время разработки
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)