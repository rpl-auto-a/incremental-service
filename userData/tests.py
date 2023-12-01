from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import PostProperti, UserData

class FavoriteTests(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        # Create a test post
        self.post = PostProperti.objects.create(
            user=self.user,
            nama_properti='Test Property',
            deskripsi_properti='Test description',
            foto_properti='path/to/test/image.jpg',
            kota_properti='Test City',
            negara_properti='Test Country',
            kode_pos_properti='12345'
        )

        # Create UserData for the test user
        self.user_data = UserData.objects.create(user=self.user)

        # Log the user in
        self.client.login(username='testuser', password='testpassword')

    def test_add_favorite_view(self):
        response = self.client.post(reverse('userData:add_favorite', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(self.post in self.user_data.postFavorit.all())

    def test_delete_favorite_view(self):
        # Add the post to favorites first
        self.user_data.postFavorit.add(self.post)
        response = self.client.post(reverse('userData:delete_favorite', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertFalse(self.post in self.user_data.postFavorit.all())

    def test_favorites_json_view(self):
        # Add a post to favorites
        self.user_data.postFavorit.add(self.post)
        response = self.client.get(reverse('userData:favorites_json'))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['fields']['nama_properti'], 'Test Property')

    def test_add_favorite_view_invalid_post_id(self):
        # Try to add a favorite with an invalid post_id
        response = self.client.post(reverse('userData:add_favorite', args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_delete_favorite_view_invalid_post_id(self):
        # Try to delete a favorite with an invalid post_id
        response = self.client.post(reverse('userData:delete_favorite', args=[999]))
        self.assertEqual(response.status_code, 404)
