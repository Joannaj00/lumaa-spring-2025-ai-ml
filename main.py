from perfume_recommender.data_loader import DataLoader
from perfume_recommender.preprocessor import TextPreprocessor
from perfume_recommender.recommender import PerfumeRecommender
import sys 

def main():
    # Load data
    df = DataLoader.load_perfume_data()
    
    # Initialize preprocessor and prepare features
    preprocessor = TextPreprocessor()
    tfidf_matrix = preprocessor.prepare_features(df)
    
    # Initialize recommender
    recommender = PerfumeRecommender(df, tfidf_matrix, preprocessor)
    
    # Get user input
    try:
        user_input = input("Describe the type of perfume you're looking for:\n> ")
        N = input("How many recommendations do you want?:\n> ")
    except EOFError:
        print("\n[Error] No input detected. Exiting...")
        sys.exit(1)

    
    # Get recommendations
    recommendations = recommender.get_recommendations(user_input, N)
    
    # Display recommendations
    output = "\n\nTop Perfume Recommendations:\n"
    output += "-" * 80 + "\n"

    for i, rec in enumerate(recommendations, 1):
        output += f"\n{i}. {rec['name']} by {rec['brand']}\n\n"
        output += f"Description: {rec['description']}\n\n"
        output += f"Notes: {rec['notes']}\n\n"
        output += "-" * 80 + "\n"
    
    
    sys.stdout.reconfigure(encoding='utf-8')  # Ensure UTF-8 encoding for terminal output
    print(output)


if __name__ == "__main__":
    main()
