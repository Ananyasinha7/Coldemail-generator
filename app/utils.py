import re

def clean_text(text):
    text=re.sub(r'<[^>]*?>','',text) #removed html tags
    text=re.sub(r'https?://(?:[a-zA-Z]|[0-9]|[$-_@,&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+','',text) #removed URLs
    text=re.sub(r'[^a-zA-Z0-9\s]',' ',text) #removed special characters
    text=re.sub(r'\s+',' ',text) #removed multiple spaces
    text=text.strip()
    return text
