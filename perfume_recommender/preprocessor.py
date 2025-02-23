import re
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer, ENGLISH_STOP_WORDS
from .config import Config

class TextPreprocessor:
    """Handle text preprocessing and vectorization"""
    
    def __init__(self):
        self.stop_words = set(ENGLISH_STOP_WORDS)
        self.vectorizer = TfidfVectorizer(
            stop_words='english',
            min_df=Config.MIN_DF,
            max_features=Config.MAX_FEATURES
        )
        
    def clean_text(self, text):
        """Clean and normalize text data"""
        if not isinstance(text, str):
            return ""
            
        # Convert to lowercase
        text = text.lower()
        
        # Remove special characters and numbers
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        
        # Remove extra whitespace
        text = ' '.join(text.split())
        
        # Remove stopwords
        text = ' '.join([word for word in text.split() if word not in self.stop_words])
        
        return text
        
    def prepare_features(self, df):
        """Prepare text features for the recommender"""
        # Combine relevant text features
        df['combined_features'] = df['Description'].fillna('') + ' ' + \
                                df['Notes'].fillna('')
        
        # Clean text
        df['combined_features'] = df['combined_features'].apply(self.clean_text)
        
        # Create TF-IDF matrix
        tfidf_matrix = self.vectorizer.fit_transform(df['combined_features'])
        
        return tfidf_matrix
        
    def transform_user_input(self, user_input):
        """Transform user input for recommendation"""
        cleaned_input = self.clean_text(user_input)
        return self.vectorizer.transform([cleaned_input])