from django.shortcuts import render
from .forms import DocumentForm
from docx import Document
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

@csrf_exempt
def submit(request):
  form = DocumentForm()
  if request.method == 'POST':
    form = DocumentForm(request.POST,request.FILES)
    name = str(request.FILES['document']).replace(" ", "_")
    if form.is_valid():
      form.save()
      length = request.POST['length']
      choice = request.POST['algo']
      if(name.endswith('.txt')):
	      para =  open(str(settings.MEDIA_ROOT)+'/documents/'+name).read()
      elif(name.endswith('.docx') or name.endswith('.doc')):
	      para = ext(name)
      if choice == 'SB':
          from .sumbasic import summarise
          output = summarise(length,para)
      elif choice == 'LR':
          from .lex_rank import lexrank
          output = lexrank(length,para)
      elif choice == 'TR':
	      from .text_rank import textrank
	      output = textrank(length,para)
      elif choice == 'LSA':
	      from .lsa import lsa
	      output = lsa(length,para)
      return render(request, 'sumbasic/answer.html', {'output': output,})
    else:
      print("not working")
  return render(request, 'sumbasic/home.html',{'form':form})


def ext(name):
	doc = Document(str(settings.MEDIA_ROOT)+'/documents/'+name)
	fullText = []
	for para in doc.paragraphs:
		fullText.append(para.text)
	return '\n'.join(fullText)

def index(request):
	form = DocumentForm()
	return render(request, 'sumbasic/home.html',{'form':form})

def contact(request):
	return render(request, 'sumbasic/basic.html',{'content':['Email id: ','vibhashchandra2010@gmail.com']})