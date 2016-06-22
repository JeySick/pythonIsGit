from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .models import Lista
from .forms import ListForm
from django.shortcuts import redirect

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'listaZakupow/post_list.html', {'posts':posts})

def show_listas(request):
    listas = Lista.objects.all().order_by('do_kiedy')
    return render(request, 'listaZakupow/show_listas.html', {'listas':listas})

def edit_lista(request, pk):
    lista = get_object_or_404(Lista, pk=pk)
    return render(request, 'listaZakupow/edit_lista.html', {'lista':lista, 'pk':pk})

def post_new(request):
    if request.method == "POST":
        form = ListForm(request.POST)
        if form.is_valid():
            lista = form.save(commit=False)
            lista.autor = request.user
            lista.save()
            return redirect('edit_lista', pk=lista.pk)
    else:
        form = ListForm()
    return render(request, 'listaZakupow/edycja.html', {'form': form})

def post_edit(request, pk):
    lista = get_object_or_404(Lista, pk=pk)
    if request.method == "POST":
        form = ListForm(request.POST, instance=lista)
        if form.is_valid():
            lista = form.save(commit=False)
            lista.autor = request.user
            lista.save()
            return redirect('edit_lista', pk=lista.pk)
    else:
        form = ListForm(instance=lista)
    return render(request, 'listaZakupow/edycja.html', {'form': form})
