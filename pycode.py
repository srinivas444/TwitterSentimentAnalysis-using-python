import csv

terms=[]
scores={}
count=0

with open('AFINN-111.txt','r') as affinefile:
		for line in affinefile:
			term,score=line.split('\t')
			scores[term]=int(score)
			terms.append(term)
def words(StringIterable):
	linestream=iter(StringIterable)
	for line in linestream:
		for word in line.split():
			yield word
									   

with open('tweet.csv','r+') as op:
	for word in words(op):
		for term in terms:
			if term==word:
#                                op.write( scores[term] )
				print (word)
				print(scores[term])
				if scores[term]>=0:
					count =count+scores[term]
				if scores[term]<=0:
					count =count-scores[term]
#op.write(str(scores[term]))

if count>=0:
        
	print('responding positively')                                          
if count<0:
	print('we need to develop our product')                         
									   
									   

affinefile.close()
op.close()
