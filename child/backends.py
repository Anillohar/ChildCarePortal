from django.contrib.auth.models import User
from .models import userdata

class MyBackend(object):
	def authenticate(self ,userid, password=None):
		existing_user=User.objects.get(username=userid)
		if not existing_user:
			user_data=userdata.objects.get(userid=userid)
			print("...%s...."%user_data)
			if userid ==user_data.userid:
				user=User.objects.create_user(username=userid,password=12345)
				user.save()
				return user
			else:
				return None
		else:
			return existing_user
	def get_user(self,user_id):
		try:
			return User.objects.get(username=user_id)
		except User.DoesNotExist:
			return None
		

