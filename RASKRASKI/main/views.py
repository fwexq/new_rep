from django.views.generic import ListView
from pygments.unistring import cats

from .forms import *
from .models import *

from django.shortcuts import render, redirect




#
# class Home(ListView):
#     model = picture
#
#     template_name = 'main/index.html'
#     context_object_name = 'pictures'
#
#     extra_context = {'title': 'Главная страница'}
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         context['cat_selected'] = 0
#         return context






# СТАРОЕ отображение, функция
def index(request):
    pictures = picture.objects.all()
    #cats = Category.objects.all()
    context = {
        'title': 'Главная страница сайта',
        #'cats': cats,
        'pictures': pictures,
        'cat_selected': 0


    }
    return render(request, 'main/index.html', context)




def create(request):
   if request.method == 'POST':
       form = pictureForm(request.POST, request.FILES)
       if form.is_valid():
           form.save()
           return redirect('home')

   else:
        form = pictureForm()

   context = {
       'title': 'Создание поста',
       'form': form,
   }
   return render(request, 'main/create.html', context)



def show_category(request, cat_slug):
   #return HttpResponse(f"Отображение категории с id = {cat_id}")

   с = Category.objects.get(slug=cat_slug)
   posts = с.picture_set.all()

   #cats = Category.objects.all()
   # c = Category.objects.get(slug=cat_slug)

   # posts = c.picture_set.all()


   context = {
       #'cats': cats,
       'posts': posts,
       'title': 'Отображение по рубрикам',
       'cat_selected': cat_slug,

   }

   return render(request, 'main/category.html', context=context)


#                {% get_categories as categories %}
# {% for c in categories %}
# 	{% if c.pk == cat_selected %}
# 		<li class="nav-link active" aria-current="page">{{c.name}}</li>
# 	{% else %}
#           <li class="nav-item">
# 		<li><a class="nav-link active" aria-current="page" href="{{ c.get_absolute_url }}">{{c.name}}</a></li>
# 	{% endif %}
# {% endfor %}


