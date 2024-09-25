from django.urls import path, include
from rest_framework import routers
from .apiviews import Categortyapiviews,Tagapiviews,Postapiviews,Commentapiviews,Contactapiviews





router = routers.SimpleRouter()
router.register(r'categories', Categortyapiviews)
router.register(r'tags',  Tagapiviews)
router.register(r'posts', Postapiviews)
router.register(r'comments', Commentapiviews)
router.register(r'contacts', Contactapiviews)

urlpatterns = [
    # path('api/', include(router.urls)),
]
urlpatterns=router.urls