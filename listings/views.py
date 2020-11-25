from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from . models import Listing
from . choices import bedroom_choices, price_choices, state_choices


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = { 'listings': paged_listings }
    return render(request, 'listings/listings.html', context)

def listing(request, id):
    listing = get_object_or_404(Listing, pk=id)

    context = { 'listing': listing }
    return render(request, 'listings/listing.html', context)

def search(request):
    listings = Listing.objects.order_by('-list_date')
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            listings = listings.filter(description__icontains=keywords)
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            listings = listings.filter(city__iexact=city)
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            listings = listings.filter(state__iexact=state)
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            listings = listings.filter(bedrooms__lte=bedrooms)
    if 'bathrooms' in request.GET:
        bathrooms = request.GET['bathrooms']
        if bathrooms:
            listings = listings.filter(bathrooms__lte=bathrooms)
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            listings = listings.filter(price__lte=price)

    context = {
        'listings': listings,
        'bedrooms': bedroom_choices,
        'prices': price_choices,
        'states': state_choices,
    }
    return render(request, 'listings/search.html', context)
