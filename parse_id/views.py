from django.shortcuts import render

# Create your views here.
def db_list(request):
    return render(request, 'parse_id/db_list.html', {})
