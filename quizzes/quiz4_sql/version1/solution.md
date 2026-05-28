Solution 1: Hidden Hits
SQL
SELECT 
    t.Name AS TrackName, 
    g.Name AS GenreName, 
    t.Milliseconds,
    RANK() OVER (PARTITION BY g.Name ORDER BY t.Milliseconds DESC) as DurationRank
FROM Track t
JOIN Genre g ON t.GenreId = g.GenreId
JOIN PlaylistTrack pt ON t.TrackId = pt.TrackId
WHERE t.TrackId NOT IN (SELECT DISTINCT TrackId FROM InvoiceLine)
GROUP BY t.TrackId, g.Name
HAVING COUNT(pt.PlaylistId) > 3;
Solution 2: Spending Deviation
SQL
WITH CustomerMovingAvg AS (
    SELECT 
        c.FirstName, 
        c.LastName, 
        i.InvoiceId,
        i.Total,
        AVG(i.Total) OVER (
            PARTITION BY i.CustomerId 
            ORDER BY i.InvoiceDate 
            ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
        ) AS RollingAvg
    FROM Customer c
    JOIN Invoice i ON c.CustomerId = i.CustomerId
)
SELECT * 
FROM CustomerMovingAvg
WHERE Total > (RollingAvg * 1.5);