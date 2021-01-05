from django.shortcuts import render,get_object_or_404,redirect
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import ImageForm, PostForm
from .models import Images
from .models import Post
import boto3
import os




def post(request):
 
    ImageFormSet = modelformset_factory(Images,
                                        form=ImageForm, extra=3)
    #'extra' means the number of photos that you can upload   ^
    if request.method == 'POST':
    
        postForm = PostForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=Images.objects.none())
    
    
        if postForm.is_valid() and formset.is_valid():
            post_form = postForm.save(commit=False)
            post_form.user = request.user
            post_form.save()
    
            for form in formset.cleaned_data:
                #this helps to not crash if the user   
                #do not upload all the photos
                if form:
                    image = form['image']
                    photo = Images(post=post_form, image=image)
                    photo.save()
            return HttpResponseRedirect("/uploads")
        else:
            print(postForm.errors, formset.errors)
    else:
        postForm = PostForm()
        formset = ImageFormSet(queryset=Images.objects.none())
    return render(request, 'uploads/index.html',
                  {'postForm': postForm, 'formset': formset,'public_posts': Post.objects.filter(public=True)})


def delete(request,id):
    deletedobj=Images.objects.get(pk=id)
    s3 = boto3.resource("s3")
    obj = s3.Object(os.environ.get('BUCKET_NAME'),str(deletedobj.image))
    deletedobj.delete()
    obj.delete()
    return redirect("/uploads")

def deleteall(request):
    s3 = boto3.resource("s3")
    for i in Post.objects.filter(user=request.user):
        for im in Images.objects.filter(post=i.id):
            obj = s3.Object(os.environ.get('BUCKET_NAME'),str(im.image))
            im.delete()
            obj.delete()
        i.delete()
    return redirect("/uploads")  


#
#def getfilename(url):
     #return (url.split("https://notitelligence.s3.amazonaws.com/")[1])


# Create your views here.
