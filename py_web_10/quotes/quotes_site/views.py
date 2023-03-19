from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .forms import AuthorForm, QuoteForm
from .models import Quote, Tag, Author


def get_top10tags():
    tags = Tag.objects.all()
    topTenTags: list = sorted(tags, key=lambda tag: (tag.quotes.all().count(), tag.name), reverse=True)[:10]
    return topTenTags


def index(request):
    quotes = Quote.objects.all().order_by("-id")
    topTenTags = get_top10tags()

    tag_name = request.GET.get('tag_name')
    if tag_name:
        try:
            tag_id = Tag.objects.get(name=tag_name.capitalize()).id
            quotes = quotes.filter(tags__in=[tag_id])
        except Tag.DoesNotExist as e:
            quotes = []

    paginator = Paginator(quotes, 4)
    page = request.GET.get('page')
    quotes = paginator.get_page(page)

    return render(request, "quotes_site/index.html", {"quotes": quotes, "topTenTags": topTenTags})


def author_details(request, id):
    author = Author.objects.get(pk=id)

    return render(request, "quotes_site/author_details.html", {"author": author})


@login_required
def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quotes_site:index')

        return render(request, 'quotes_site/add_author.html', {'form': form})

    return render(request, "quotes_site/add_author.html", {'form': AuthorForm()})


@login_required
def add_quote(request):
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quotes_site:index')

        return render(request, 'quotes_site/add_quote.html', {'form': form})

    return render(request, "quotes_site/add_quote.html", {'form': QuoteForm()})

