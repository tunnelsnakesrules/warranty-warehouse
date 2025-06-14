from django.shortcuts import render, redirect
from .models import Part
from .forms import PartForm
from django.db.models import Q

def parts_list(request):
    query = request.GET.get('q')
    parts = Part.objects.all()
    if query:
        parts = parts.filter(
            Q(order__number__icontains=query) |
            Q(storage_location__code__icontains=query)
        )
    return render(request, 'warehouse/parts_list.html', {'parts': parts})


def add_part(request):
    if request.method == 'POST':
        form = PartForm(request.POST)
        if form.is_valid():
            part = form.save()
            return redirect('parts_list')
    else:
        form = PartForm()
    return render(request, 'warehouse/add_part.html', {'form': form})
