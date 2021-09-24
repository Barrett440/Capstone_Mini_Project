import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re
import emoji

lemmatizer = WordNetLemmatizer()

# Lemmatization
def lemmatize_text(text):
    text_clean = text_cleaner(text) 
    lemmatized_text = []
    tokens = word_tokenize(text_clean)
    for word in tokens:
        lemmatized_text.append(lemmatizer.lemmatize(word))
    return(' '.join(lemmatized_text))

def give_emoji_free_text(text):
        # Remove emojis (credit to https://stackoverflow.com/questions/51217909/removing-all-emojis-from-text)
        allchars = [str for str in text]
        emoji_list = [c for c in allchars if c in emoji.UNICODE_EMOJI]
        clean_text = ' '.join([str for str in text.split() if not any(i in str for i in emoji_list)])
        return clean_text

def text_cleaner(text):
    
    # Remove links
    text = re.sub(r'http\S+', '', text)
    
    # Remove punctuation
    text = re.sub('[,\.!?]', '', text)
    
    # Remove emojis
    text = give_emoji_free_text(text)
    
    # Remove stop words and words that are shorter than 3 characters
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    filtered_text = []
    for w in word_tokens:
        if w.lower() not in stop_words and len(w) >= 3:
            filtered_text.append(w)              
    
    return ' '.join(filtered_text) 