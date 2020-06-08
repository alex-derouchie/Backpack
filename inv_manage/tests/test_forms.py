from django.test import SimpleTestCase
from inv_manage.forms import ShareForm, ItemForm

class TestForms(SimpleTestCase):

    #Item Form Tests
    def test_item_form_valid_data(self):
        form = ItemForm(data={
            'item_name': 'TestItem',
            'item_description': 'Test Description',
            'item_quantity': 23
        })

        self.assertTrue(form.is_valid())
        print('item form valid data pass')

    def test_item_form_no_data(self):
        form = ItemForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)
        print('item form no data pass')

    #Share Form Tests  
    def test_share_form_valid_data(self):
        form = ShareForm(data={
            'user_to_add': 'TestUser1',
            'user_access': 'can_edit'
        })

        self.assertTrue(form.is_valid())
        print('share form valid data pass')

    def test_share_form_no_data(self):
        form = ShareForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)
        print('share form no data pass')