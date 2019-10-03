from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # path('', views.index, name='index'),
    # # 查看指定id的问卷
    # path('<int:question_id>/', views.details, name='detail'),
    # path('<int:question_id>/results/', views.results, name='results'),
    # 函数视图转换为通用视图(generic view systems)
    path('', views.IndexView.as_view(), name='index'),
    # 查看指定id的问卷
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote')
]
