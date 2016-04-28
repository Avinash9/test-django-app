from django.test import TestCase

from models import Logs,LogUser
from views import create_entry


class LogTestCase(TestCase):

    def setUp(self):
        pass

    def test_create_entry(self):
        records = Logs.objects.all()
        counter = records.count()
        data = {
            "message":"hello21",
            "time_stamp":"2020-05-20T00:43:38",
            "is_sent":True
        }
        test = create_entry(data,9)
        records = Logs.objects.all()
        new_counter = records.count()
        self.assertEqual(counter+1, new_counter)


