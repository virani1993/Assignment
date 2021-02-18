from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .forms import StudentForm
from .models import StudentModel
# Create your views here.
def index(request):
    return HttpResponse("Hello")
def form_view(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,'BLOG_POSTS/POST_FORM.html',context)

def list_view(request):
    dataset = StudentModel.objects.all()
    return render(request, 'BLOG_POSTS/POST_LIST.html', {'dataset': dataset})

def delete_view(request,_Id):
    try:
        data = get_object_or_404(StudentModel, Id=_Id)
    except Exception:
        raise Http404('No Data')
    if request.method == 'POST':
        data.delete()
    else:
        return render(request, 'POST_DELETE.html')