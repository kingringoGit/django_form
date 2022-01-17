from django.urls import path
from .import views
urlpatterns = [
    path('',views.save_fun),
    path('savedata',views.save_fun),
    path('dispdata',views.fetch_all),
    path('edit/<int:id>',views.edit_fun),
    path('update/<int:id>',views.update_fun),
    path('delete/<int:id>',views.delete_fun),
    # path('detail<ename>',views.detail)
]