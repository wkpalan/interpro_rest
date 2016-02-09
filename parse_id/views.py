from django.shortcuts import render,redirect
from .forms import upload_url
from .models import id_desc

# Create your views here.
def db_list(request):
    databases = id_desc.objects.all().values_list('db',flat=True)
    return render(request, 'parse_id/db_list.html', {'databases':databases})

def add_data(request):
    if request.method == "POST":
        form = upload_url(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/parse_id/db_list',pk=post.pk)
    else:
        form = upload_url
    return render(request, 'parse_id/add_data.html',{'form':form})
