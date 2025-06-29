import re

def clean_text(text):
    text=re.sub(r'<[^>]*?>','',text) #remove html tags
    text=re.sub(r'https?://(?:[a-zA-Z]|[0-9]|[$-_@,&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+','',text) #remove URLs
    text=re.sub(r'[^a-zA-Z0-9\s]',' ',text) #replace special characters with space
    text=re.sub(r'\s+',' ',text) #replace multiple spaces with single space
    text=text.strip()
    return text
