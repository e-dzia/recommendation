import os
import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings("ignore", category=RuntimeWarning)
DATA_PATH = "/home/marta/Documents/PyCharm/Semestr 3/SR_Z1/Github repo/input_data/movie_dataset"


def load_csv(filename, data_path=DATA_PATH):
    file_path = os.path.join(data_path, filename)
    df = pd.read_csv(file_path)
    return df


def load_data():
    ratings_df = load_csv('ratings_small.csv')
    movies_csv = load_csv('movies.csv')
    df = pd.merge(ratings_df, movies_csv, on='movieId')
    return df


def load_movie_user_matrix():
    df = load_data()
    movie_user_matrix = df.pivot_table(index='movieId', columns='userId', values='rating')
    return movie_user_matrix


def get_movie_title(movie_id):
    df = load_csv('movies.csv')
    movie_title = df[df['movieId'] == movie_id]['title'].values[0]
    return movie_title


def count_no_of_ratings(df):
    ratings = pd.DataFrame(df.groupby('title')['rating'].mean())
    ratings['number_of_ratings'] = df.groupby('title')['rating'].count()
    return ratings


def count_correlations_for_user(df, user_id):
    user_all_ratings = df[user_id]
    user_similarities = df.corrwith(user_all_ratings)

    user_similar_users = pd.DataFrame(user_similarities, columns=['correlation'])
    user_similar_users.dropna(inplace=True)
    user_similar_users = user_similar_users.sort_values('correlation', ascending=False)
    return user_similar_users


def get_correlations_for_users_that_have_seen_the_movie(df, correlations, user_id, movie_id):
    users_that_have_seen_movie = list(df.iloc[movie_id - 1, :].dropna(inplace=False).index)
    users_that_have_seen_movie.remove(user_id)
    correlations_for_movie = correlations[correlations.index.isin(users_that_have_seen_movie)]
    return correlations_for_movie


def get_users_with_best_correlations(correlations, threshold):
    users_with_best_correlation = correlations[correlations['correlation'] >= threshold]
    users_with_best_correlation = users_with_best_correlation.sort_index()
    return users_with_best_correlation


def get_top_n_correlated_users(correlations, n):
    top_users = correlations.sort_values('correlation', ascending=False).head(n)
    top_users = top_users.sort_index()
    return top_users


def count_average(ratings, weights=None):
    return np.average(ratings, weights=weights)


def get_most_correlated_users_for_user_and_movie(df, user_id, movie_id, threshold=0.75, n=50):
    user_correlations = count_correlations_for_user(df, user_id)
    correlations = get_correlations_for_users_that_have_seen_the_movie(df, user_correlations, user_id, movie_id)
    if correlations.shape[0] > 0:
        best_correlated_users = get_users_with_best_correlations(correlations, threshold)
        top_correlated_users = get_top_n_correlated_users(correlations, n)
        return best_correlated_users, top_correlated_users


def print_ratings(movie_ratings, best_correlated_users, top_correlated_users, user_id, movie_id):
    best_ratings = movie_ratings[movie_ratings.index.isin(list(best_correlated_users.index))].values
    top_ratings = movie_ratings[movie_ratings.index.isin(list(top_correlated_users.index))].values

    avg_best = np.average(best_ratings)
    avg_weighted_best = np.average(best_ratings, weights=best_correlated_users.values.reshape(-1, ))
    avg_top = np.average(top_ratings)
    avg_weighted_top = np.average(top_ratings, weights=top_correlated_users.values.reshape(-1, ))

    print(f"\nPredicted rating of '{get_movie_title(movie_id)}'om movie for user {user_id}\n")

    print(f"Average for best correlated users: {round(avg_best, 2)} | {round(avg_weighted_best, 2)} "
          f"({best_ratings.shape[0]} most similar users)\n"
          f"Average for top correlated users:  {round(avg_top, 2)} | {round(avg_weighted_top, 2)} "
          f"({top_correlated_users.shape[0]} most similar users)")

    return avg_best, avg_weighted_best, avg_top, avg_weighted_top


def count_users_rating_for_movie(user_id, movie_id, threshold=0.75, n=50):
    df = load_movie_user_matrix()
    try:
        best_correlated_users, top_correlated_users = get_most_correlated_users_for_user_and_movie(df, user_id, movie_id, threshold, n)
        movie_ratings = df.iloc[movie_id - 1]
        avg_best, avg_weighted_best, avg_top, avg_weighted_top = print_ratings(movie_ratings, best_correlated_users, top_correlated_users, user_id, movie_id)
    except:
        print("There aren't any similar users that have seen this movie.")
        avg_best, avg_weighted_best, avg_top, avg_weighted_top = 0, 0, 0, 0
    return avg_best, avg_weighted_best, avg_top, avg_weighted_top


if __name__ == "__main__":
    avg_best, avg_weighted_best, avg_top, avg_weighted_top = \
        count_users_rating_for_movie(user_id=1, movie_id=1)
