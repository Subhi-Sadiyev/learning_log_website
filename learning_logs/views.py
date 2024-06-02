from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic, Entry
from .forms import TopicForm, EntryForm


def index(request):
    """Learning log uchun esas sehife"""
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """butun movzulari goster"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """tek movzu ve onun mezmununu goster"""
    topic = Topic.objects.get(id=topic_id)
    #istifadechiler movzu id url yazmaq ile acha bilmesinler deye:
    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """istifadechilerin yeni movzu yaratmasi"""
    if request.method != 'POST':
        # Melumat elave edilmeyib, bosh form yarat
        form = TopicForm()
    else:
        #POST request edilib, data process et
        form = TopicForm(data = request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')

    #Bosh ve ya duzgun olmayan form goster???
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """mueyyen movzu uchun yeni mezmun"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        #melumat POST edilmeyib, blank form yarat
        form = EntryForm()
    else:
        # POST edilib, process data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_topic.owner = request.user
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    # Display a blank or invalid form???
    # question to self. everyfunction here in view must have context and render
    # why does the book specify this part as when blank or invalid form segment??

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Movcud mezmunu redakte et"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # intial reques, form hazirki mezmun ile doldur
        form = EntryForm(instance=entry)
    else:
        # POST edilib, melumati emal ele
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)