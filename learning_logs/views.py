from learning_logs.forms import TopicForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
from django.http import Http404


# Create your views here.

def index(request):
    return render(request, 'learning_logs/index.html')


@login_required
def topics(request):
    """ show all topics"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}

    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """ show single topic and all its entries"""

    #topic = Topic.objects.get(pk=topic_id)
    topic = get_object_or_404(Topic, pk=topic_id)

    if topic.owner != request.user:
        raise Http404
    
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}

    return render(request, 'learning_logs/topic.html', context)


@login_required
def add_topic(request):

    if request.method != 'POST':
        form = TopicForm()

    else:

        form = TopicForm(data=request.POST)

        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            form.save()

            return redirect('learning_logs:topics')

        
    
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)
            
@login_required
def add_entry(request, topic_id):

    topic = get_object_or_404(Topic, pk=topic_id)

    if request.method != 'POST':
        form = EntryForm()

    else:

        form = EntryForm(data=request.POST)

        if form.is_valid():
            new_enty = form.save(commit=False)
            new_enty.topic = topic
            new_enty.save()

            return redirect('learning_logs:topic', topic_id=topic_id)

        
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def update_entry(request, entry_id):
    
    #entry = Entry.objects.get(pk=entry_id)
    entry = get_object_or_404(Entry, pk=entry_id)
    topic = entry.topic

    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        """ filled form with pre-filled data"""
        form = EntryForm(instance=entry)

    else:
        """update form with current data and replace previous data"""
        form = EntryForm(instance=entry, data=request.POST)

        if form.is_valid():
            form.save()

            return redirect('learning_logs:topic', topic_id=topic.id)

        
    context = {'entry':entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)