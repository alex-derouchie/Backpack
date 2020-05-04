from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Inventory, Item


def about(request):
    return render(request, 'inv_manage/about.html', {'title': 'About'})


def IndexView(request):
    return render(request, 'inv_manage/index.html')

###########################################
#           CLASS BASED VIEWS             #
###########################################

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


class UserInvListView(ListView):
    model = Inventory
    template_name = 'inv_manage/user_invs.html'
    context_object_name = 'Inventories'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Inventory.objects.filter(author=user).order_by('-date_created')


class InvDetailView(DetailView):
    model = Inventory
    template_name = 'inv_manage/inv_detail.html'
    context_object_name = 'inv'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        inv = get_object_or_404(Inventory, pk=self.kwargs.get('pk'))
        context['item_list'] = Item.objects.filter(inventory = inv)
        print(self.kwargs)
        return context

    #def get_queryset(self):
        #pk = self.kwargs.get('pk')
        #print(self.kwargs)
        #return Item.objects.filter(pk=pk).order_by('name')


class InvCreateView(LoginRequiredMixin, CreateView):
    model = Inventory
    fields = ['name']
    template_name = 'inv_manage/inv_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    fields = ['name', 'description', 'quantity', 'inventory']
    template_name = 'inv_manage/item_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


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

