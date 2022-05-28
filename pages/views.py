from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Book
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect


class HomeView(generic.ListView):
    model = Book
    paginate_by = 4
    template_name = 'pages/home.html'
    context_object_name = 'books'

    # def get_queryset(self):
    #     return Book.objects.all().order_by('price')


# @login_required()
def detail_page(request, pk):
    book = get_object_or_404(Book, pk=pk)
    is_favorite = False
    is_like = False
    if book.favorite.filter(id=request.user.id).exists():
        is_favorite = True
        is_like = True
    comment_book = book.comments.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.book = book
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()
    return render(request, 'pages/detail_page.html',
                  context={'book': book, 'comment_form': comment_form, 'comments': comment_book,
                           'is_favorite': is_favorite, 'is_like': is_like})


def favorite_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if book.favorite.filter(id=request.user.id).exists():
        book.favorite.remove(request.user)
    else:
        book.favorite.add(request.user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required()
def favorite_list(request):
    user = request.user
    favorite_books = user.favorite.all()
    context = {'favorite_books': favorite_books}
    return render(request, 'pages/favorite.html', context)


def search_bar(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        book = Book.objects.filter(title__contains=searched)
        return render(request, 'search_result.html', {'searched': searched, 'books': book})
    else:
        return render(request, 'search_result.html')


def like_book(request, pk):
    book = get_object_or_404(Book, id=request.POST.get('book_id'))
    book.likes.add(request.user)
    return HttpResponseRedirect(reverse('detail_page', args=[str(pk)]))
