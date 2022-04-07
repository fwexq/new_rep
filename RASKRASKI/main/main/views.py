from .models import *

from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

#menu = [{'title': "Главная", 'url_name': 'home'},
#        {'title': "Фильм", 'url_name': 'film'},
#        {'title': "Мультсериал", 'url_name': 'mult'},
#        {'title': "Создать", 'url_name': 'create'}]




def index(request):
    pictures = picture.objects.all()
    cats = Category.objects.all()
    context = {
        'title': 'Главная страница сайта',
        'cats': cats,
        'pictures': pictures,
        'cat_selected': 0


    }
    return render(request, 'main/index.html', context)


#def film(request):
#    return render(request, 'main/film.html')
#
#
#def mult(request):
#    return render(request, 'main/mult.html')

#def create(request):
#    error = ''
#    if request.method == 'POST':
#        form = pictureForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('home')
#
#        else:
#            error = 'Форма была неверной'
#    form = pictureForm()
#    context = {
#        'form': form,
#        'error': error
#    }
#    return render(request, 'main/create.html', context)



def show_category(request, cat_id):
    return HttpResponse(f"Отображение категории с id = {cat_id}")



#    posts = picture.objects.filter(cat__cat_id=id)
#    cats = Category.objects.all()
#
#    if len(posts) == 0:
#        raise Http404()
#
#    context = {
#        'posts': posts,
#        'cats': cats,
#        'title': 'Отображение по рубрикам',
#        'cat_selected': cat_id,
#    }
#
#    return render(request, 'women/index.html', context=context)




#{% block content%} <br><br><br>Текст</br></br></br>
#    {% for el in pictures %}
#        <div class="alert alert-warning mt-2">
#                <h3>{{el.title}}</h3>
#            {% if el.photo %}
#                <p><img class="img-article-left thumb" src="{{el.photo}}"></p>
#            {% endif %}
#        </div>
#    {% endfor %}
#{% endblock%}

#ятебялюблююююююююююююююююююююююююююююююююююююююююю




#{% for m in menu %}
#	{% if not forloop.last %}
#			<li><a href="{% url m.url_name %}">{{m.title}}</a></li>
#	{% else %}
#			<li class="last"><a href="{% url m.url_name %}">{{m.title}}</a></li>
#	{% endif %}
#{% endfor %}
#
#
#{% if cat_selected == 0 %}
#		<li class="selected">Все категории</li>
#{% else %}
#		<li><a href="{% url 'home' %}">Все категории</a></li>
#{% endif %}
#
#{% for c in cats %}
#	{% if c.pk == cat_selected %}
#		<li class="selected">{{c.name}}</li>
#	{% else %}
#		<li><a href="{{ c.get_absolute_url }}">{{c.name}}</a></li>
#	{% endif %}
#{% endfor %}