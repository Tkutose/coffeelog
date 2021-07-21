from django.test import TestCase
from .models import Log, Store
from django.contrib.auth.models import User
# Create your tests here.


def add_test_data():
    User.objects.create()
    Store.objects.create(store='test')
    Log.objects.create(
        author=User(id=1), product='sample', price=0, hot=False,
        bitter=0, acidity=0, smell=0, after=0, likely=0,
        note='test data', store=Store(id=1)
    )

# 関数名はtestで始める必要あり。
class LogModelTest(TestCase):

    def test_no_get_store_other_log(self):
        """
        同じStoreの商品が存在しないとき正確に取得できているかのテスト
        """
        # 外部キーはアンダースコア２つを使う
        list = Log.objects.filter(store__store='')
        self.assertEqual((len(list)), 0)



    def test_get_store_other_log(self):
        """
        同じStoreの商品が存在するとき正確に取得できているかのテスト
        """
        # テスト用ダミーデータ作成
        add_test_data()

        list = Log.objects.filter(store__store='test')
        self.assertEqual((len(list)), 1)

