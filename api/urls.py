from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from .views import FacViewset, UserViewset

router = DefaultRouter(trailing_slash=False)
router.register(r'faculty', FacViewset)

urlpatterns = router.urls

urlpatterns += [
    path("token", obtain_auth_token),
    path("register", UserViewset.as_view())
]