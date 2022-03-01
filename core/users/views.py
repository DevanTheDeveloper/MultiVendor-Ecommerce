from django.shortcuts import render, redirect
from django.contrib import messages 
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, UserShippingForm
from django.contrib.auth.decorators import login_required




def register(request):
	if request.method == 'POST':
		form = UserRegisterForm (request.POST)
		if form.is_valid():
			form.save() 
			username=form.cleaned_data.get('username')
			
			messages.success(request, f'Your account {username} has been created! You can now log in!')
			return redirect('cx_login')

	else:
		form = UserRegisterForm()
	return render (request, 'users/register.html', {'form':form})


@login_required
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm( request.POST, 
									request.FILES,
									instance=request.user.profile)
		shipping = UserShippingForm(request.POST, instance = request.user.shipping)
		if u_form.is_valid() and p_form.is_valid() and shipping.is_valid():
			u_form.save()
			p_form.save()
			shipping.save()
			messages.success(request, f'Your account has been updated!')
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)
		shipping_form = UserShippingForm(instance=request.user.shipping) 


	context = { 'u_form':u_form,

				'p_form':p_form,

				'shipping_form':shipping_form}


	return render (request, 'users/profile.html', context )

