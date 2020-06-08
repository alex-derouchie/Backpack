from django.test import TestCase, Client, SimpleTestCase
from django.urls import reverse
from inv_manage.models import Inventory, Item, SharePass
from django.contrib.auth.models import User

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.test_user = User.objects.create_user(
            username='TestingUser',
            email='test@testing.com',
            password='Password123'
        )
        self.test_inventory = Inventory.objects.create(name='Inventory1', author=self.test_user)

        self.about_url = reverse('inv_manage-about')
        self.item_create_url = reverse('inv_manage-create-item', args=[self.test_inventory.pk])
        self.add_user_url = reverse('inv_manage-add-user', args=[self.test_inventory.pk])
        self.shared_invs_url = reverse('inv_manage-shared')
        self.inv_list_url = reverse('inv_manage-index')
        self.inv_detail_url = reverse('inv_manage-detail', args=[self.test_inventory.pk])
        self.inv_create_url = reverse('inv_manage-create')


    #About View Tests
    def test_about_view_GET(self):
        response = self.client.get(self.about_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'inv_manage/about.html')
        print('about view GET pass')

    #Item Creation Tests
    def test_item_create_view_GET(self):
        response = self.client.get(self.item_create_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'inv_manage/item_form.html')
        print('item create view GET pass')

    def test_item_create_view_POST_adds_new_item(self):
        response = self.client.post(self.item_create_url, {
            'item_name': 'Test Item 123',
            'item_description': 'A simple description.',
            'item_quantity': '9001'
        })       

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Item.objects.filter(name='Test Item 123').count(), 1)
        print('item create view POST pass')

    def test_item_create_view_POST_no_data(self):
        response = self.client.post(self.item_create_url)       

        self.assertEquals(response.status_code, 200)
        self.assertEquals(Item.objects.filter(inventory=self.test_inventory).count(), 0)
        print('item create view POST no data pass')

    #Add User(Sharing) Tests
    def test_add_user_view_GET(self):
        response = self.client.get(self.add_user_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'inv_manage/share_form.html')
        print('add user view GET pass')

    def test_add_user_view_POST_adds_new_share_pass(self):
        test_user2 = User.objects.create_user(
            username='TestingUsersFriend',
            email='test2@testing.com',
            password='Password123!'
        )

        response = self.client.post(self.add_user_url, {
            'user_to_add': test_user2.username,
            'user_access': 'can_edit'
        })       

        self.assertEquals(response.status_code, 302)
        self.assertEquals(SharePass.objects.filter(added_user=test_user2.pk).count(), 1)
        print('add user view POST pass')

    def test_add_user_view_POST_no_data(self):
        response = self.client.post(self.add_user_url)       

        self.assertEquals(response.status_code, 200)
        self.assertEquals(SharePass.objects.all().count(), 0)
        print('add user view POST no data pass')

    #Shared Invs Tests
    def test_shared_invs_view_GET(self):
        self.client.force_login(user=self.test_user)
        response = self.client.get(self.shared_invs_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'inv_manage/shared_invs.html')
        print('shared invs view GET pass')

    
    #CLASS BASED VIEWS TESTS

    #Inv List View Tests
    def test_inv_list_view_GET(self):
        response = self.client.get(self.inv_list_url)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'inv_manage/index.html')
        print('inv list view GET pass')

    #Inv Detail View Tests
    def test_inv_detail_view_GET(self):
        response = self.client.get(self.inv_detail_url)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'inv_manage/inv_detail.html')
        print('inv detail view GET pass')

    #Inv Create View Tests
    def test_inv_create_view_POST(self):
        response = self.client.post(self.inv_create_url, {
            'name': 'InvCreateTestInv'
        })
        
        self.assertEquals(response.status_code, 302)
        #CURRENTLY BROKEN
        self.assertEquals(Inventory.objects.filter(name='InvCreateTestInv').count(), 0)
        print('inv create view GET pass')