from django.views.generic import ListView, DetailView
from .models import SnackModel

# Create your views here.
class SnackModelListView(ListView):
  template_name = 'snack_list.html'
  model = SnackModel
  
class SnackModelDetailView(DetailView):
  template_name = 'snack_detail.html'
  model = SnackModel