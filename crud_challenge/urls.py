from django.contrib import admin
from django.urls import path, include
# ESTA LINHA É CRUCIAL
from products.views_frontend import index 

urlpatterns = [
    # ESTA LINHA É CRUCIAL
    path('', index, name='home'), 
    
    path('api/', include('products.urls')),
    
    path('admin/', admin.site.urls),
]
