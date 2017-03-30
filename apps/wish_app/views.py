from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import MyWishlist, Biglist
from ..login_and_reg_app.models import User

# Create your views here.
def index(request):
    if not 'user_id' in request.session:
        messages.error(request, 'must be logged in to continue')
        return redirect(reverse('login_stuff:my_index'))
    request.session['user_name']
    context= {
        'myitems': MyWishlist.objects.filter(owner=request.session['user_name']),
        'othersitems': Biglist.objects.exclude(added_by=request.session['user_name'])
    }
    return render(request, 'wish_app/dashboard.html', context)

def create(request):
    return render(request, 'wish_app/create_item.html')

def add(request):
    if len(request.POST['new_item']) < 3:
        messages.error(request, 'Item/Product name has to be at least 3 chars!')
        return redirect(reverse('wishlist_stuff:create'))
    else:
        MyWishlist.objects.create(item_name=request.POST['new_item'], added_by=request.session['user_name'], owner=request.session['user_name'])
        Biglist.objects.create(item_name=request.POST['new_item'], added_by=request.session['user_name'])
        return redirect(reverse('wishlist_stuff:index'))

def delete(request, id):
    MyWishlist.objects.filter(id=id).delete()
    Biglist.objects.filter(id=id).delete()
    return redirect('/dashboard')

def add_to_my_list(request, item_name, added_by):
    MyWishlist.objects.create(item_name=item_name, added_by=added_by, owner=request.session['user_name'])
    Biglist.objects.filter(item_name=item_name).delete()
    return redirect('/dashboard')

def remove(request, id, item_name, added_by):
    MyWishlist.objects.filter(id=id).delete()
    Biglist.objects.create(item_name=item_name, added_by=added_by)
    return redirect('/dashboard')

def show(request, id):
    item = MyWishlist.objects.get(id=id)
    # User.objects.filter(mywishlist__id=id)
    print "************************"
    context = {
        'show': User.objects.filter(id=id)
    }
    print item.added_by
    return render('wish_app/show.html', context)
