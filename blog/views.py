from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from .models import Publicacion
from .forms import FormPub

def listar_pub(request):
    pubs = Publicacion.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/listar_pub.html', {'pubs': pubs})

def detalle_pub(request, pk):
    pub = get_object_or_404(Publicacion, pk=pk)
    return render(request, 'blog/detalle_pub.html', {'pub': pub})

def nueva_pub(request):
    if request.method == "POST":
        form = FormPub(request.POST)
        if form.is_valid():
            pub = form.save(commit=False)
            pub.autor = request.user
            pub.fecha_publicacion = timezone.now()
            pub.save()
            return redirect('detalle_pub', pk=pub.pk)
    else:
        form = FormPub()
    return render(request, 'blog/nueva_pub.html', {'formulario': form})

def editar_pub(request, pk):
    pub = get_object_or_404(Publicacion, pk=pk)
    if request.method == "POST":
        form = FormPub(request.POST, instance=pub)
        if form.is_valid():
            pub = form.save(commit=False)
            pub.autor = request.user
            pub.fecha_publicacion = timezone.now()
            pub.save()
            return redirect('detalle_pub', pk=pub.pk)
    else:
        form = FormPub(instance=pub)
    return render(request, 'blog/editar_pub.html', {'formulario': form})
