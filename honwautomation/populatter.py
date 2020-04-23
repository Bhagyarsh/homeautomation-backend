import os 
import csv
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mogambo.settings')
import django
django.setup()


from django.contrib.auth import get_user_model
user = get_user_model()

# d = user.objects.create_superuser("bhagyarsh@gmail.com","bhagyarsh","dhumal","bhagyarsh31")
# print(d)