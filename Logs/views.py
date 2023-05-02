from django.shortcuts import render,redirect
from .models import Topic,Entry
from .form import TopicsForm,EntryForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import Http404


# Create your views here.
def index(request):
    """Home page for learning Logs"""
    return render(request,'index.html')
@login_required
def topic(request):
    """Home page for learning Logs"""
    topic = Topic.objects.filter(owner=request.user).order_by('date_added')

    context = {'topic':topic}
    return render(request,'topic.html',context)
@login_required
def entry(request,topic_id):
    """Home page for learning Logs"""
    topic = Topic.objects.get(id =topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic,'entries':entries }
    return render(request,'entry.html',context)
@login_required
def addtopic(request):
    if request.method == 'POST':
        form = TopicsForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
        return redirect(reverse('topic'))
    else:
        form = TopicsForm()
    context = {'form':form}
    return render(request,'addtopic.html',context)
@login_required
def addentry(request,topic_id):
    """Add entry for perticular topic"""
    topic = Topic.objects.get(id = topic_id)
    if request.method == 'POST':
        form = EntryForm(data=request.POST)
        if form.is_valid():
            add_entry = form.save(commit = False)
            add_entry.topic = topic
            add_entry.save()
        return redirect(reverse('topic'))
    else:
        form = EntryForm()
    context = {'topic':topic,'form':form}
    return render(request,'addentry.html',context)
@login_required
def editentry(request,entry_id):
    entry = Entry.objects.get(id = entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    if request.method == 'POST':
        form = EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
        return redirect(reverse('topic'))
    else:
        form = EntryForm(instance=entry)
    context = {'topic':topic,'form':form,'entry':entry}
    return render(request,'addentry.html',context)
