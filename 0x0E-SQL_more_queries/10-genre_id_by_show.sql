-- list all shows that have at least one genre linked
SELECT shows.title, show_genres.genre_id
FROM tv_show_genres AS show_genres
INNER JOIN tv_shows AS shows
ON shows.id = show_genres.show_id AND genre_id IS NOT NULL
ORDER BY shows.title, show_genres.genre_id;
