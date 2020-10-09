from django.test import TestCase, Client

# Create your tests here.
class BlogTest(TestCase):

    def setUp(self):
        self.c = Client()

    def test_index_access(self):
        res = self.c.get('/')

        # status code=> 200 OK
        # stauts code => 302 Redirct
        # status code => 404 Not Found
        self.assertEqual(200, res.status_code)

    def test_fail_access(self):
        res = self.c.get('/unkonwn')
        print(res.status_code)
        self.assertEqual(404, res.status_code)