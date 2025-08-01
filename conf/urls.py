"""
URL configuration for conf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
   openapi.Info(
      title="Chocolate shop",
      default_version='v1',
      description="""
          Sh's team loyihasi orqali siz o'zingizga xos shokolad turlarini yaratishingiz, tarkibini belgilashingiz va buyurtma qilishingiz mumkin. 🍫
    
          📌 API funksiyalari:
          - Shokolad turlarini ko‘rish va izlash
          - Yangi shokolad retseptini yaratish
          - Foydalanuvchi buyurtmalari bilan ishlash
          - O‘zingizning shokolad kolleksiyangizni boshqarish
    
          🔐 Ba'zi endpointlar autentifikatsiyani talab qiladi.
          🔄 JSON formatida so‘rovlar yuboring va natijalarni qulay interfeysda oling.
    
            API dasturchilar uchun qulay va kengaytiriladigan qilib ishlab chiqilgan.
        
            Enjoy crafting your own chocolate with ❤️!
            """,
       terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="shaxzodaavalboyeva14@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('products.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
