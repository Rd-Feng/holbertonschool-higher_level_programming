-- list all shows that have at least one genre linked
SELECT shows.title, show_genres.genre_id
FROM tv_shows AS shows
LEFT JOIN tv_show_genres AS show_genres
ON shows.id = show_genres.show_id
where show_genres.show_id IS NULL
ORDER BY shows.title;
