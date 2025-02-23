from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from .config import Config

class PerfumeRecommender:
    """Main recommendation system class"""
    
    def __init__(self, df, tfidf_matrix, preprocessor):
        self.df = df
        self.tfidf_matrix = tfidf_matrix
        self.preprocessor = preprocessor
        
    def get_recommendations(self, user_input, n_recommendations=None):
        """Get perfume recommendations based on user input"""
        if n_recommendations is None:
            n_recommendations = Config.N_RECOMMENDATIONS
            
        # Transform user input
        user_vector = self.preprocessor.transform_user_input(user_input)
        
        # Calculate similarity scores
        similarity_scores = cosine_similarity(user_vector, self.tfidf_matrix)
        
        # Get top recommendations
        top_indices = similarity_scores[0].argsort()[::-1][:n_recommendations]
        
        # Prepare recommendations
        recommendations = []
        for idx in top_indices:
            recommendations.append({
                'name': self.df.iloc[idx]['Name'],
                'brand': self.df.iloc[idx]['Brand'],
                'similarity_score': similarity_scores[0][idx],
                'description': self.df.iloc[idx]['Description'],
                'notes': self.df.iloc[idx]['Notes']
            })

            
        return recommendations