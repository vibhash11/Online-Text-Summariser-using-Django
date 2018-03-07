from .sumy.parsers.plaintext import PlaintextParser 
from .sumy.nlp.tokenizers import Tokenizer 
from .sumy.summarizers.lsa import LsaSummarizer 

def lsa(num_of_sentences,text):
	a = open("plain_text.txt","w").writelines(str(text))
	file = "plain_text.txt" 
	parser = PlaintextParser.from_file(file, Tokenizer("english"))
	summarizer = LsaSummarizer()
	summary = summarizer(parser.document,int(num_of_sentences))
	newsummary = []
	for sentence in summary:
		newsummary.append(sentence)
	del file
	return '\n'.join(map(str, newsummary))
