from django import forms

from .models import lostchild,childinfo,parent,doner
from .models import Post ,Comment,Question

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
class LostForm(forms.ModelForm):

    class Meta:
        model = lostchild
        fields = ('name', 'cityfound',"Detail",'age')
class ChildForm(forms.ModelForm):
	class Meta:
		model= childinfo
		fields =('name','currentcity','age','cci','guardian','aadhar','dob')
class ParentForm(forms.ModelForm):
	class Meta:
		model=parent
		fields=('__all__')
class DonorForm(forms.ModelForm):

	class Meta:
		model=doner

		fields=('__all__')