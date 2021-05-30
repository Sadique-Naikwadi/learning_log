from learning_logs.forms import TopicForm
from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm, EntryForm


# Create your views here.

def index(request):
    return render(request, 'learning_logs/index.html')



def topics(request):
    """ show all topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}

    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """ show single topic and all its entries"""

    topic = Topic.objects.get(pk=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}

    return render(request, 'learning_logs/topic.html', context)



def add_topic(request):

    if request.method != 'POST':
        form = TopicForm()

    else:

        form = TopicForm(data=request.POST)

        if form.is_valid():
            form.save()

            return redirect('learning_logs:topics')

        
    
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)
            

def add_entrty(request, topic_id):

    topic = Topic.objects.get(pk=topic_id)

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

