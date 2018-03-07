from django import forms
from .models import Document

class tosum(forms.Form):
	length = forms.IntegerField(label='Length(Number of Sentences)')
	algos=[('SB','Sum-Basic'),
         ('LR','Lex-Rank'),
	 ('TR','Text-Rank'),
	 ('LSA','LSA')]
	algo = forms.ChoiceField(label='Choose Algo',choices=algos, widget=forms.RadioSelect())

class DocumentForm(forms.ModelForm,tosum):
    class Meta:
        model = Document
        fields = ('document', )
