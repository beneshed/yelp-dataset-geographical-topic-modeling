# Create your views here.
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext, loader
from mining.models import Review, Restaurant
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def research_paper(request):
    return render(request, 'research_paper.html')

def reviews(request):
    review_list = Review.objects.all()
    paginator = Paginator(review_list, 25)
    page = request.GET.get('page')
    try:
        reviews = paginator.page(page)
    except PageNotAnInteger:
        reviews = paginator.page(1)
    except EmptyPage:
        reviews = paginator.page(paginator.num_pages)

    return render_to_response('reviews.html', {"reviews": reviews})

def restaurants(request):
    restaurant_list = Restaurant.objects.all()
    paginator = Paginator(restaurant_list, 25)
    page = request.GET.get('page')
    try:
        rests = paginator.page(page)
    except PageNotAnInteger:
        rests = paginator.page(1)
    except EmptyPage:
        rests = paginator.page(paginator.num_pages)

    return render_to_response('restaurants.html', {"rests": rests})

def research_map(request):
    return render(request, 'map.html')

def legal(request):
    return render(request, 'legal.html')

def contact_me(request):
    return render(request, 'contact_me.html')

def contact_form(request):
    name = request.POST.get('name', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('email', '')

    if subject and message and from_email:
        try:
	    send_mail(name, message, from_email, ['bsawyerwaters@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/')
    else:
        return render_to_response('contact_me.html', {'form': ContactForm()})
    return render_to_response('contact_me.html', {'form': ContactForm()},
        RequestContext(request))
