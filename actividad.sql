1
SELECT LastName, FirstName FROM employees
ORDER by  LastName, FirstName ASC 
2
SELECT  tracks.name, tracks.Milliseconds FROM tracks
JOIN albums on tracks.AlbumId = albums.AlbumId
WHERE albums.AlbumId = 5
ORDER by tracks.Milliseconds DESC;
3
SELECT UnitPrice, name FROM tracks
ORDER by UnitPrice ASC
LIMIT 10;
4
SELECT * FROM artists
JOIN albums ON artists.ArtistId = albums.ArtistId
JOIN tracks ON albums.AlbumId = tracks.AlbumId
JOIN genres ON tracks.GenreId = genres.GenreId
WHERE UnitPrice = 0.99;
5
SELECT * FROM tracks
JOIN albums ON artists.ArtistId = albums.ArtistId
JOIN tracks ON albums.AlbumId = tracks.AlbumId
JOIN genres ON tracks.GenreId = genres.GenreId
WHERE UnitPrice = 0.99;