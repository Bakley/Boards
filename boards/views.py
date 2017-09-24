from django.shortcuts import render, get_object_or_404
# from django.http import Http404
from .models import Board

# Create your views here.


def home(request):
    """The home view."""
    boards = Board.objects.all()
    context = {"boards": boards}
    return render(request, 'home.html', context)


def boards_topic(request, pk):
    """The Boards topic view, has a primary key attribute"""
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topic.html', {'board': board})
