from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Eblog, EblogCategorie
from .forms import EblogReviewForm

from .utils import paginateItems, searchItems
from .forms import EblogReviewForm
# Create your views here.

def blogs(request):
    items, search_query = searchItems(request)
    custom_range, items = paginateItems(request, items, 4)

    blog_cats = EblogCategorie.objects.all()

    context = {'blog_cats': blog_cats, 'search_query': search_query, 'custom_range': custom_range, 'blogs': items}

    return render(request, 'blogs/blogs.html', context)


def blogCategory(request, pk):
    blog_cats = EblogCategorie.objects.all()
    blog_cat = EblogCategorie.objects.get(id=pk)
    
    req_cut_url =  str(request.path[22:-1])
    blogs_year = blog_cat.eblog_set.all()
    custom_range, blogs = paginateItems(request, blogs_year, 4)

    print(req_cut_url)

    context = {'blog_cats': blog_cats, 'custom_range': custom_range, 'blogs': blogs, 'req_url': req_cut_url }

    return render(request, 'blogs/blogs.html', context)


def blog(request, pk):
    blog = Eblog.objects.get(id=pk)
    blog_cat = blog.eblog_cats
    blogs = Eblog.objects.all()
    form = EblogReviewForm()

    print()

    if request.method == 'POST':
        form = EblogReviewForm(request.POST)
        review = form.save(commit=False)
        review.blog = blog
        review.owner = request.user.profile
        review.save()  

        messages.success(request, 'Your comment was successfully submitted!')
        return redirect('blog', pk=blog.id)

    context = {'blog': blog, 'blog_cat': blog_cat, 'blogs': blogs, 'form': form}

    return render(request, 'blogs/single-blog.html', context)