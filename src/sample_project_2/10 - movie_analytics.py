movies = [
    ("Inception", "Sci-Fi", 148, 8.8),
    ("Titanic", "Romance", 195, 7.8),
    ("Avatar", "Sci-Fi", 162, 7.9),
    ("The Notebook", "Romance", 123, 7.9),
    ("Interstellar", "Sci-Fi", 169, 8.6),
]


"""Task:

Define a Movie dataclass with title, genre, length, rating.

Add property hours = length / 60.

Use Counter to count movies per genre.

Use defaultdict to group movies by genre.

Use namedtuple (GenreSummary) for storing genre, count, avg_rating.

Print summaries of all genres."""