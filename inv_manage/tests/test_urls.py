from django.test import SimpleTestCase
from django.urls import reverse, resolve
from inv_manage.views import ( AboutView, ItemCreateView,
    AddUserView, SharedInvs, InvListView, InvDeleteView,
    InvDetailView, InvCreateView, InvUpdateView, ItemDetailView)

class TestUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url = reverse('inv_manage-index')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, InvListView) 

    def test_inv_shared_url_is_resolved(self):
        url = reverse('inv_manage-shared')
        print(resolve(url))
        self.assertEquals(resolve(url).func, SharedInvs) 

    def test_inv_detail_url_is_resolved(self):
        url = reverse('inv_manage-detail', args=['1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, InvDetailView) 

    def test_inv_update_url_is_resolved(self):
        url = reverse('inv_manage-update', args=['1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, InvUpdateView) 

    def test_inv_delete_url_is_resolved(self):
        url = reverse('inv_manage-delete', args=['1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, InvDeleteView) 

    def test_create_item_url_is_resolved(self):
        url = reverse('inv_manage-create-item', args=['1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, ItemCreateView) 

    def test_add_user_url_is_resolved(self):
        url = reverse('inv_manage-add-user', args=['1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, AddUserView) 

    def test_item_detail_url_is_resolved(self):
        url = reverse('inv_manage-item-detail', args=['1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, ItemDetailView) 

    def test_inv_create_url_is_resolved(self):
        url = reverse('inv_manage-create')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, InvCreateView) 

    def test_about_url_is_resolved(self):
        url = reverse('inv_manage-about')
        print(resolve(url))
        self.assertEquals(resolve(url).func, AboutView) 

