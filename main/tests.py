from django.test import TestCase, Client
from main.models import Item

class mainTest(TestCase):
    # Mengecek apakah path URL /main/ dapat diakses.
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    # Mengecek apakah halaman /main/ di-render menggunakan template main.html.
    def test_main_using_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

class ItemTestCase(TestCase):
    def setUp(self):
        Item.objects.create(name="Apple iPhone 12",
                            amount="20",
                            description="""The iPhone 12 is Apple's flagship smartphone featuring a sleek design, A14 Bionic chip, 
                                        OLED Super Retina XDR display, and 5G capability, offering a visually impressive mobile experience.""",
                            price=11999000)
        
        Item.objects.create(name="Apple MacBook Air M2 (2022)",
                            amount="10",
                            description="""The MacBook Air M2 (2022) is Apple's latest iteration of the popular ultraportable laptop, 
                                        featuring the new M2 chip for enhanced performance and efficiency in a lightweight design.""",
                            price=19999000)
    
    # Mengecek apakah kedua item yang baru dibuat dapat diakses.
    def test_items_can_created(self):
        iphone_12 = Item.objects.get(name="Apple iPhone 12")
        macbook_air_m2 = Item.objects.get(name="Apple MacBook Air M2 (2022)")
        self.assertEqual(iphone_12.name, "Apple iPhone 12")
        self.assertEqual(macbook_air_m2.name, "Apple MacBook Air M2 (2022)")

# Referensi
# 1. https://docs.djangoproject.com/en/4.2/topics/testing/overview/