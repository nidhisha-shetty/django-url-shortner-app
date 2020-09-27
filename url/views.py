from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import urlForm
from .shortner import shortner
from .models import short_urls

def base(request):
    return render(request, 'base.html');

def home(request,tok):
    long_url=short_urls.objects.filter(short_url=tok)[0]
    return redirect(long_url.long_url)

def short_url(request):
    obj=short_urls.objects.all()
    form=urlForm(request.POST)
    a=''
    if request.method=='POST':       
        if form.is_valid():
            NewURL=form.save()
            a=shortner().issue_token()
            NewURL.short_url=a
            NewURL.save()
        else:
            form=urlForm()
            a="Invalid url"
    return render(request, "short_url.html", {"context_obj":obj,"form":form,"a":a})

def post_view(request):
    form=urlForm(request.POST or None)
    a=''
    if request.method=='POST':     
        if form.is_valid():
            NewURL=form.save()
            a=shortner().issue_token()
            NewURL.short_url=a
            NewURL.save()
        else:
            form=urlForm()
            a="invalid_url"
    return render(request, 'post.html', {"form":form,"a":a});

def delete(requests):
    obj=short_urls.objects.all()
    context={
        'context_obj':obj
    }
    return render(requests, "delete.html", context)

def delete_view(requests, id):
	obj=short_urls.objects.get(id=id)
	if requests.method=="POST":
		obj.delete()
		return HttpResponseRedirect("/api/delete")
	context={'context_obj':obj}
	return render(requests, "deleteurl.html", context)