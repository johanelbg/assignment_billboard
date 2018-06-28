from django.shortcuts import render
from .models import AddBoard
import time


def index(request):
    date_created = time.strftime("%Y/%m/%d")
    title = request.POST.get("title")
    description = request.POST.get("description")
    author = request.POST.get("author")
    if title and description and author:
        get_board = AddBoard(title=title, text=description, author=author)
        get_board.save()
    get_all = AddBoard.objects.all()
    context = {
        "display_board": get_all,
        "date": date_created
    }
    return render(request, 'board.html', context)