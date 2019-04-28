from django.shortcuts import render
from django.utils import timezone
from .models import Rede
from .forms import PostForm
from django.shortcuts import redirect

def rede_list(request):
    obj = Rede.objects.all()
    for abc in obj:
        obj_ids = abc.id
        obj_NomeRedes = abc.NomeRede
        obj_created_date = abc.created_date
    context = {
	    "obj":obj,
	    "obj_NomeRedes":obj_NomeRedes,
		"obj_created_date":obj_created_date
		}
    return render(request, 'topologia/rede_list.html', context)
	
def rede_new(request):
 if request.method == "POST":
	 form = PostForm(request.POST)
	 if form.is_valid():
		 rede = form.save(commit=False)
		 rede.published_date = timezone.now()
		 rede.save()
		 return render(request, 'topologia/rede_list.html', {})
 else:
	 form = PostForm()
 return render(request, 'topologia/rede_edit.html', {'form': form})
	