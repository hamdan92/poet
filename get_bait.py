import sys
import re  # For preprocessing
import pandas as pd  # For data handling


import codecs
#sys.stdout = codecs.getwriter('utf8')(sys.stdout)
#sys.stderr = codecs.getwriter('utf8')(sys.stderr)




stop_words=[
    'من','إلى','عن','على','في',
    'بن','التي','الذي','الذين','له','لها','هذه','هذا'
    ,'به','بها','عبر','وإن','ليست','حول'
    ,'أين','بل','بين','ما','أو','لا','لو'
    ,'إذ','أن','لو','كمن','ليس','وليس','وليسوا','ليسو','ليسوا','وليسو'
    ,'أين','وأين','اين','إلا','وإلا','ولو','لنا','قد','وقد','ومن','فمن','منكم','منهم','منهن','منها','فكأن','كأنه','فكأنه','كم','ذاك','إذا','منه'
]

waw_words=['وزارة','وفاء','ولاء','ويل']
lam_words=['لين','ليت','لون','لنت']
baa_words=['برق','براك','براق','','']
faa_words=['فناء','فنى','فنائ','فضل' ,'فضلتهم','وفضلتهم' , 'وفضلت' , 'فضلت']
c_words=['مكة','الله']


sentences=[]


def clean(jomla):
    jomla = re.sub('[^ء-ي ]+', '', jomla)
    jomla = re.sub(' +', ' ', jomla)
    return jomla 



        

def is_begin_with_al(word):
    if word[0] == 'ا' and word[1] == 'ل':
        return (True,2)
    if word[1] == 'ا' and word[2] == 'ل':
        return (True,3)
    else:
        return False
    

def refine(word):
    word_history={
        'al':0,
        'fl':0,
        'bl':0,
        'wl':0,
        'll':0,
        'lee':0,
        'waa':0,
        'baa':0,
        'faa':0,
        'at':0,
        'woon':0,
        'haa':0,
        'naa':0,
        'aa':0
                }
    try:
        if word in stop_words:
            return ''
        if word in c_words:
            return word
  
            
        if word[-1] == 'ا' and len(word[:-1]) >= 3:
            word=word[:-1]
            word_history.update({'aa':1})
        
        
        if word[-2] == 'ن' and word[-1]=='ي' and len(word[:-2]) >= 3:
            if (is_begin_with_al(word) == (True,2) and len(word[2:-2]) >= 4 ) or (is_begin_with_al(word) == (True,3) and len(word[3:-2]) >= 4 ) :
                word=word[:-2]
            if is_begin_with_al(word) == False:
                word=word[:-2]
        if word[-1] == 'ي':
            word=word[:-1]
            
        if word[-1] == 'ه':
            word=word[:-1]
            word_history.update({'haa':1})
        
            
        if word[0] == 'و' and word not in waw_words:
            word=word[1:]
            word_history.update({'waa':1})
            
        if word[0] == 'ف' and word not in faa_words :
            word=word[1:]
            word_history.update({'faa':1})
            
        if word[0] == 'ب' and word not in baa_words and len(word) >=4:
            word=word[1:]
            word_history.update({'baa':1})
            
        if word[0] == 'ل' and word[1]=='ل' :
            word=word[2:]
            word_history.update({'ll':1})
        if word[0] == 'ل' and word not in lam_words and word not in stop_words:
            word=word[1:]
            word_history.update({'lee':1})
        if word[0] == 'ا' and word[1]=='ل' and word not in c_words :
            word=word[2:]
            word_history.update({'al':1})
        if word[0] == 'و' and word[1]=='ا' and word[2] =='ل':
            word=word[3:]
            word_history.update({'wl':1})
        #if word[-1] == 'ة':
        #    word=word[:-1]

        if word[-2] == 'ه' and word[-1]=='ا' :
            word=word[:-2]
            word_history.update({'haa':1})
        if word[-2] == 'ي' and word[-1]=='ن' and word not in stop_words and len(word) >=4 :
            if word[-3]=='ت':
                word=word[:-3]+'ة'
            else:
                word=word[:-2]
        if word[-2] == 'ن' and word[-1]=='ا' :
            
            if len(word[:-2] <=3 ):
                word[-1]=='ى' 
            elif word[-3]=='ت':
                word=word[:-3]+'ة'
            else:
                word=word[:-2]
        if word[-2] == 'و' and word[-1]=='ن' and len(word) > 3:
            word=word[:-2]
        if word[-2] == 'ا' and word[-1]=='ت' :
            word=word[:-2]
            

        if word[-1] == 'ئ':
            word=word[:-1] +'ء'
    except:
        return ''
    return word



data = pd.read_csv('./abbasi/abbasi_review.csv', encoding='utf-8')

for i in range(len(data)):
    if data['review'][i] == 0:
        print ('{"first":'+data[data.columns[0]][i]=',"second":'+data[data.columns[1]][i]+'}')
        
        break


#for i in range(len(data['0'])):
#    try:
#        sentence1=data['0'][i]
#        sentence2=data['1'][i]

#        sentence1=clean(sentence1)
#        sentence2=clean(sentence2)

#        sentences.append(sentence1.split(' '))
#        sentences.append(sentence2.split(' '))
#    except:
#        continue

