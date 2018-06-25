
def go():
    tag1 = nltk.pos_tag(text1)
    text1POS = [tag for (word,tag) in tag1]
    return text1POS
    
