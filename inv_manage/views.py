from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from .models import Inventory, Item, SharePass
from .forms import ItemForm, ShareForm
from django.contrib import messages

#######################################################################
# This file defines the views for the inv_manage app. In Django, views
# define the data and functionality associated to each HTML template
# in the system.
#######################################################################

#Renders the about page
def AboutView(request):
    print(request)
    return render(request, 'inv_manage/about.html', {'title': 'About'})

# Item creation view - renders the custom form and processes it into
# an Item object upon form submission
def ItemCreateView(request, pk):
    print(request)
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            inv = Inventory.objects.get(pk=pk)
            item = Item()
            item.name = form.cleaned_data['item_name']
            item.description = form.cleaned_data['item_description']
            item.quantity = form.cleaned_data['item_quantity']
            item.inventory = inv
            item.save()
            inv.inv_size = Item.objects.filter(inventory=inv).count()
            inv.save()
            return HttpResponseRedirect(f'/inv/{pk}')
    else:
        form = ItemForm()
    return render(request, 'inv_manage/item_form.html', {'form': form})

# Add User View - Handles adding other users to the current user's inventories
# (sharing). creates a new ShareForm object based on the custom form submission.
def AddUserView(request, pk):
    print(request)
    if request.method == "POST":
        form = ShareForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['user_to_add']
            access = form.cleaned_data['user_access']
            if (User.objects.filter(username=username).count() > 0 and username != request.user.username):
                new_pass = SharePass()
                new_pass.added_user = User.objects.get(username = username)
                new_pass.inventory = Inventory.objects.get(pk=pk)
                if(access == "can_edit"):
                    new_pass.can_edit = True
                else:
                    new_pass.can_edit = False
                new_pass.save()
                messages.success(request, f'Inventory shared with user')
                return HttpResponseRedirect(f'/inv/{pk}')
            elif (username == request.user.username):
                messages.warning(request, "You can't share Inventories with yourself!")
            else:
                messages.warning(request, "User could not be found")
    else:
        form = ShareForm()
    return render(request, 'inv_manage/share_form.html', {'form': form})
        
# Renders list of inventories that have been shared with the current user
def SharedInvs(request):
    print(request)
    context = {
        'shared': SharePass.objects.filter(added_user=request.user)
    }
    return render(request, 'inv_manage/shared_invs.html', context)

###########################################
#           CLASS BASED VIEWS             #
###########################################

#Lists the current user's inventories -- HOME PAGE
class InvListView(ListView):
    model = Inventory
    template_name = 'inv_manage/index.html'
    context_object_name = 'Inventories'
    ordering = ['-date_created']
    paginate_by = 5

    # This takes all the Inventories in the DB and filters out Inventories
    # from other users.
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Inventory.objects.filter(author=self.request.user)
        else:
            return Inventory.objects.all()


#Provides details into a specific inventory
class InvDetailView(DetailView):
    model = Inventory
    template_name = 'inv_manage/inv_detail.html'
    context_object_name = 'inv'

    #Passes list of items associated with this inventory to the template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        inv = get_object_or_404(Inventory, pk=self.kwargs.get('pk'))
        context['item_list'] = Item.objects.filter(inventory = inv)
        return context

#Provides inventory creation functionality
class InvCreateView(LoginRequiredMixin, CreateView):
    model = Inventory
    fields = ['name']
    template_name = 'inv_manage/inv_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

#Provides details into a specific item
class ItemDetailView(DetailView):
    model = Item
    template_name = 'inv_manage/item_detail.html'
    context_object_name = 'item'

#Allows user to update inventory information
class InvUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Inventory
    fields = ['name']
    template_name = 'inv_manage/inv_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        inv = self.get_object()
        if self.request.user == inv.author:
            return True
        else:
            return False

#Allows user to delete inventories
class InvDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Inventory
    template_name = 'inv_manage/confirm_delete.html'
    context_object_name = 'inv'
    success_url = '/'

    def test_func(self):
        inv = self.get_object()
        if self.request.user == inv.author:
            return True
        else:
            return False

