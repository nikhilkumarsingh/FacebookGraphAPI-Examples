from PIL import Image
import numpy as np
import re
from wordcloud import WordCloud, STOPWORDS

def clean_text(text):
     text = re.sub(r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+','',text)  #remove urls
     text = re.sub(r'[^A-Za-z\s]+','',text)    #remove everything except alphabets/words
     text = text.replace("check",'python')
     text = text.replace("using",'')
     return text
     

def wcloud(text):
     mask = np.array(Image.open("face_mask.png"))   #choose mask
     stopwords = set(STOPWORDS)
     wc = WordCloud(background_color="white",
                    mask=mask,
                    max_words=80,
                    stopwords=stopwords,
                    width=800,
                    height=400,
                    mode="RGB",
                    relative_scaling=0.5,
                    )

     text = clean_text(text)
     wc.generate(text)

     #save image
     file_name = raw_input("Enter any name for the Word Cloud image:") +'.png'    
     wc.to_file(file_name)

     return
