from django.urls import path
from . import views # imports from same root level

app_name = 'polls' # {% url 'polls:detail' question.id %} usando de manera dinámica, hay que indicar el parámetro al lado de polls:detail
urlpatterns = [
    #ex: /polls/5/
    path('', views.IndexView.as_view(), name='index'), # views -> llamo el nombre de la clase view -> llamo el método iterno asView()
    #ex: /polls/5/
    path('<int:pk>/detail/estaeslamejorpagina', views.DetailView.as_view(), name='detail'), # Para gneric views no se puede usar question_id para el id, u otra variable. Hay que usar pk para que entienda que se refiere a la primary key.
    #ex: /polls/5/results
    path('<int:pk>/results', views.ResultView.as_view(), name='results'), 
    #ex: /polls/5/vote
    path('<int:question_id>/vote', views.vote, name='vote') # Vote no usa generic views
]