from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . models import Thread, Message
from vendor.models import Vendor
from .forms import MessageForm

# Create your views here.

@login_required
def inbox(request):

	inboxMessages = Thread.objects.filter(host=request.user)
	context = {'inboxMessages':inboxMessages}
	print(context)
	return render(request, 'messenger/inbox.html', context)


@login_required
def vendorInbox(request):

	inboxMessages = Thread.objects.filter(vendor=request.user.vendor)
	context = {

					'inboxMessages':inboxMessages
	}
	return render(request,'messenger/inbox.html',context)

@login_required
def createThread(request,pk):
	
	vendor = get_object_or_404(Vendor,pk=pk)
	print(vendor)
	thread = Thread.objects.create(host = request.user,vendor = vendor,)
	thread.save()
	print(thread)
	return redirect('thread',thread.id)


@login_required
def threadView(request,pk):

	thread = get_object_or_404(Thread,pk=pk)
	if request.method == "POST":
		form = MessageForm(request.POST)
		if form.is_valid():
			newMessage = form.save(commit=False)
			newMessage.user = request.user
			newMessage.thread = thread
			newMessage.save()
			messages.success(request,'Your message has been sent!')

	comments = thread.messages.all()
	form = MessageForm()

	context = {'comments':comments,
				'thread':thread,
				'form':form
				 }
	return render(request, 'messenger/thread.html',context)