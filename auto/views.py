from datetime import datetime

from django.shortcuts import render
from django.utils.timezone import now
from django.views.generic import DetailView, ListView
from django.db.models import Q
from auto.models import Review, Khabar, DailyPageView


# Create your views here.


def home(request):
    latest_posts = Review.objects.all().order_by("-date")[:2]
    last_posts = Review.objects.all().order_by("-date")[2:6]
    khabars = Khabar.objects.all().order_by("-date")[:9]
    today = now().date()
    page_view, created = DailyPageView.objects.get_or_create(
        page_name="home",
        date=today
    )
    page_view.views_count += 1
    page_view.save()
    return render(request, "auto/home.html", {
        "lposts": latest_posts,
        "posts": last_posts,
        "khabars": khabars,
        "views_count": page_view.views_count,
    })


def search(request):
    query = None
    results = []
    today = now().date()
    page_view, created = DailyPageView.objects.get_or_create(
        page_name="search",
        date=today
    )
    page_view.views_count += 1
    page_view.save()
    if 'query' in request.GET and 'query' != '':
        query = request.GET['query']
        results = Khabar.objects.filter(Q(title__icontains=query) |
                                        Q(titr__icontains=query) |
                                        Q(hashtag1__icontains=query) |
                                        Q(hashtag2__icontains=query))
    return render(request, 'auto/search.html', {
        'query': query,
        'results': results,
        'views_count': page_view.views_count,
    })


class SingleReviewView(DetailView):
    template_name = "auto/moarefi_detail.html"
    model = Review

    def get_context_data(self, **kwargs):
        five_last = Review.objects.all().order_by("-date")[:6]
        context = super().get_context_data(**kwargs)
        context['five_last'] = five_last
        context['car_details'] = self.object.specs
        return context


class SingleKhabarView(DetailView):
    template_name = "auto/khabar_detail.html"
    model = Khabar

    def get_context_data(self, **kwargs):
        five_last = Khabar.objects.all().order_by("-date")[2:6]
        context = super().get_context_data(**kwargs)
        context['five_last'] = five_last
        return context


class AllKhabarsView(ListView):
    template_name = "auto/all-khabars.html"
    model = Khabar
    context_object_name = "khabars"
    paginate_by = 9
    ordering = ['-date']


class AllReviewView(ListView):
    template_name = "auto/all-review.html"
    model = Review
    context_object_name = "reviews"
    paginate_by = 9


def about(request):
    return render(request, 'auto/about-us.html')

