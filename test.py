
import unittest
import json

import app

BASE_URL = 'http://127.0.0.1:5000/api'



class TestFlaskApi(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()
        self.app.testing = True

    def test_get_all(self):
        response = self.app.get(BASE_URL+"/ping")
        data = json.loads(response.get_data())
        self.assertEqual(data["Success"], True)
        self.assertEqual(response.status_code, 200)
        print("ping test successful")


    def test_get_posts(self):
        response = self.app.get(BASE_URL+"/posts?tags=tech")
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data['posts']), 28)
        print('\n')
        print("get single tag post test successful")


    def test_get_multiple_tags_posts(self):
        response = self.app.get(BASE_URL+"/posts?tags=tech,history")
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data['posts']), 46)
        print('\n')
        print("get multiple tags post test successful")

    def test_posts_tag_not_present(self):
        response = self.app.get(BASE_URL+"/posts?")
        data = json.loads(response.get_data())
        self.assertEqual(data['error'], "Tags parameter is required")
        self.assertEqual(response.status_code, 400)
        print('\n')
        print("get no tags post test successful")

    def test_posts_direction_not_valid(self):
        response = self.app.get(BASE_URL+"/posts?tags=tech&direction=notvalid")
        data = json.loads(response.get_data())
        self.assertEqual(data['error'], "direction parameter is invalid")
        self.assertEqual(response.status_code, 400)
        print('\n')
        print("get invalid direction post test successful")

    def test_posts_sortBy_not_valid(self):
        response = self.app.get(BASE_URL+"/posts?tags=tech&sortBy=notvalid")
        data = json.loads(response.get_data())
        self.assertEqual(data['error'], "sortBy parameter is invalid")
        self.assertEqual(response.status_code, 400)
        print('\n')
        print("get invalid sortBy post test successful")

    def test_posts_default_order(self):
        response = self.app.get(BASE_URL+"/posts?tags=tech")
        data = json.loads(response.get_data())
        self.assertEqual(data['posts'][0]['id'], 1)
        self.assertEqual(data['posts'][27]['id'], 99)
        self.assertEqual(response.status_code, 200)
        print('\n')
        print("get default ordering post test successful")

    def test_posts_desc_order(self):
        response = self.app.get(BASE_URL+"/posts?tags=tech&direction=desc")
        data = json.loads(response.get_data())
        self.assertEqual(data['posts'][0]['id'], 99)
        self.assertEqual(data['posts'][27]['id'], 1)
        self.assertEqual(response.status_code, 200)
        print('\n')
        print("get defalut reverse ordering post test successful")

    def test_posts_reads_default_order(self):
        response = self.app.get(BASE_URL+"/posts?tags=tech&sortBy=reads")
        data = json.loads(response.get_data())
        self.assertEqual(data['posts'][0]['reads'], 312)
        self.assertEqual(data['posts'][27]['reads'], 98798)
        self.assertEqual(response.status_code, 200)
        print('\n')
        print("get reads ascending ordering post test successful")

    def test_posts_reads_desc_order(self):
        response = self.app.get(BASE_URL+"/posts?tags=tech&sortBy=reads&direction=desc")
        data = json.loads(response.get_data())
        self.assertEqual(data['posts'][0]['reads'], 98798)
        self.assertEqual(data['posts'][27]['reads'], 312)
        self.assertEqual(response.status_code, 200)
        print('\n')
        print("get reads decending ordering post test successful")

    def test_posts_likes_default_order(self):
        response = self.app.get(BASE_URL+"/posts?tags=tech&sortBy=likes")
        data = json.loads(response.get_data())
        self.assertEqual(data['posts'][0]['likes'], 25)
        self.assertEqual(data['posts'][27]['likes'], 985)
        self.assertEqual(response.status_code, 200)
        print('\n')
        print("get likes ascending ordering post test successful")

    def test_posts_likes_desc_order(self):
        response = self.app.get(BASE_URL+"/posts?tags=tech&sortBy=likes&direction=desc")
        data = json.loads(response.get_data())
        self.assertEqual(data['posts'][0]['likes'], 985)
        self.assertEqual(data['posts'][27]['likes'], 25)
        self.assertEqual(response.status_code, 200)
        print('\n')
        print("get likes decending ordering post test successful")


    def test_posts_popularity_default_order(self):
        response = self.app.get(BASE_URL+"/posts?tags=tech&sortBy=popularity")
        data = json.loads(response.get_data())
        self.assertEqual(data['posts'][0]['popularity'], 0.01)
        self.assertEqual(data['posts'][27]['popularity'], 0.96)
        self.assertEqual(response.status_code, 200)
        print('\n')
        print("get popularity ascending ordering post test successful")

    def test_posts_popularity_desc_order(self):
        response = self.app.get(BASE_URL+"/posts?tags=tech&sortBy=popularity&direction=desc")
        data = json.loads(response.get_data())
        self.assertEqual(data['posts'][0]['popularity'], 0.96)
        self.assertEqual(data['posts'][27]['popularity'], 0.01)
        self.assertEqual(response.status_code, 200)
        print('\n')
        print("get popularity decending ordering post test successful")


if __name__ == "__main__":
    unittest.main()
