from django.test import TestCase,Client

# Create your tests here.
class ApiTest(TestCase):
    def login(self,username='acer',password='shax'):
        c=Client()
        resp=c.get('/show/',{'username':'acer','password':'shax'})
        print(resp.status_code)


def decrypt():
    key=input().encode()
    