from django import forms

from .models import Rede

class PostForm(forms.ModelForm):


    class Meta:
        model = Rede
        fields = ('NomeRede','RoteadorIP1', 'RoteadorNetmask1', 'RoteadorIP2', 'RoteadorNetmask2', 'HostIP1' , 'HostNetmask1', 'HostGateway1',
		'HostIP2', 'HostNetmask2', 'HostGateway2',
		'HostIP3', 'HostNetmask3', 'HostGateway3',
		'HostIP4', 'HostNetmask4', 'HostGateway4')
        widgets = { 'NomeRede': forms.TextInput(attrs={'size':'50'}),}
		