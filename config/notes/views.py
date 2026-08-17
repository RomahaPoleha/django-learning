from django.shortcuts import render, get_object_or_404,redirect
from .models import Note
from .forms import NoteForm


def note_list(request):
    notes = Note.objects.all()
    return render(request, 'notes/note_list.html', {'notes': notes})


def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'notes/note_detail.html', {'note': note})

def note_created(request):
    if request.method == "POST": # Какой запрос пришел
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save()
            return redirect('note_detail', note.pk)
    else:
        form = NoteForm
    return render(request, 'notes/note_form.html', {'form': form})

