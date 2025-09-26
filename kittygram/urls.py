from django.urls import include, path

from rest_framework.routers import DefaultRouter

# from cats.views import cat_detail, cat_list
# from cats.views import APICat, APICatDetail
# from cats.views import CatDetail, CatList
from cats.views import CatViewSet

router = DefaultRouter()
router.register(prefix='cats', viewset=CatViewSet)

urlpatterns = [
    # path('cats/', cat_list),
    # path('cats/<int:pk>/', cat_detail),
    # path('cats/', APICat.as_view()),
    # path('cats/<int:pk>/', APICatDetail.as_view()),
    # path('cats/', CatList.as_view()),
    # path('cats/<int:pk>/', CatDetail.as_view()),
    path('', include(router.urls))
]
