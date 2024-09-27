from django.contrib.auth.models import User
user1 = User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")


