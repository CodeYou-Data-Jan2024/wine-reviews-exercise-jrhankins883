import pandas as pd

wine_reviews = pd.read_csv("data/winemag-data-130k-v2.csv.zip", index_col=0)

reviews_count = pd.DataFrame(wine_reviews['country'].value_counts().reset_index())
reviews_count.columns = ['country', 'count']

average = pd.DataFrame(wine_reviews.groupby('country')['points'].mean().round(1).reset_index())
average.columns = ['country', 'points']  

reviews = pd.merge(reviews_count, average, on='country')
reviews.to_csv("data/reviews-per-country.csv", index=False)