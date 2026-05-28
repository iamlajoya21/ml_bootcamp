# Quiz 4 Gradebook and Feedback

## Gradebook

| Student | Q1 Score | Q2 Score | Total Score |
| :--- | :--- | :--- | :--- |
| Nona Zakoyan | 20/50 | 0/50 | **20/100** |
| Astghik Saghyan | 25/50 | 0/50 | **25/100** |
| Areg Ayvazyan | 20/50 | 45/50 | **65/100** |
| Arsen Sirunyan | 50/50 | 35/50 | **85/100** |
| Armen Gasparyan | 50/50 | 0/50 | **50/100** |
| Karen Poghosyan | 40/50 | 0/50 | **40/100** |
| Nonna Parsyan | 30/50 | 35/50 | **65/100** |
| Mels Tadevosyan | 15/50 | 35/50 | **50/100** |
| Harutyun Khachatryan | 50/50 | 0/50 | **50/100** |
| Yulya Sargsyan | 50/50 | 0/50 | **50/100** |

## Detailed Feedback

### 1. Nona Zakoyan (20/100)
**Question 1: 20/50**
- **Feedback:** You correctly joined the tables and used `RANK()`, but you missed the filter for tracks in more than 3 playlists (`HAVING COUNT(pt.PlaylistId) > 3`). Also, the join to `Playlist` was unnecessary.
**Question 2: 0/50**
- **Feedback:** No submission provided.

### 2. Astghik Saghyan (25/100)
**Question 1: 25/50**
- **Feedback:** Your `GROUP BY p.PlaylistId HAVING Count > 3` filters for playlists that have more than 3 tracks, not tracks that are in more than 3 playlists. This changes the logic completely. The window function logic was mostly correct.
**Question 2: 0/50**
- **Feedback:** No submission provided.

### 3. Areg Ayvazyan (65/100)
**Question 1: 20/50**
- **Feedback:** You incorrectly filtered for unsold tracks by checking `TrackId NOT IN (SELECT i.InvoiceId FROM Invoice i)` which compares a TrackId to an InvoiceId. Also, the `RANK` function was partitioned by track name instead of genre name.
**Question 2: 45/50**
- **Feedback:** Good approach using `AVG() OVER()`. However, `GROUP BY i.InvoiceId` is unnecessary here and can cause unexpected grouping behavior when you're selecting non-aggregated columns.

### 4. Arsen Sirunyan (85/100)
**Question 1: 50/50**
- **Feedback:** Perfect logic. You properly isolated the unsold popular tracks in a CTE and ranked them over the Genre partition correctly.
**Question 2: 35/50**
- **Feedback:** You calculated the 3-invoice moving average perfectly, but you forgot to add the final `WHERE` clause to filter for invoices where the total is strictly greater than 1.5 times the moving average!

### 5. Armen Gasparyan (50/100)
**Question 1: 50/50**
- **Feedback:** Excellent work. The joins, the `NOT IN` subquery, and the `RANK()` window function partitioned by Genre were all executed correctly.
**Question 2: 0/50**
- **Feedback:** No submission provided.

### 6. Karen Poghosyan (40/100)
**Question 1: 40/50**
- **Feedback:** You successfully used `LEFT JOIN` to find unsold tracks and counted playlists. However, you forgot to partition your `DENSE_RANK()` by Genre as requested.
**Question 2: 0/50**
- **Feedback:** No submission provided.

### 7. Nonna Parsyan (65/100)
**Question 1: 30/50**
- **Feedback:** Good use of `LEFT JOIN` for unsold tracks. However, you completely forgot to include the `RANK()` window function to rank the tracks by duration within their genres.
**Question 2: 35/50**
- **Feedback:** Your moving average window function is missing an `ORDER BY InvoiceDate`. Without the `ORDER BY`, `ROWS BETWEEN 2 PRECEDING` is non-deterministic. Additionally, you filtered by a ratio of `> 2` instead of `> 1.5`.

### 8. Mels Tadevosyan (50/100)
**Question 1: 15/50**
- **Feedback:** You incorrectly used `TrackId not in (SELECT TrackId FROM PlaylistTrack)`. This filters for tracks that are NOT in any playlist, which completely contradicts the `HAVING count(t.TrackId)>3` requirement. You should have filtered against `InvoiceLine` for unsold tracks.
**Question 2: 35/50**
- **Feedback:** You correctly formulated the moving average over the customer partition, but you forgot the `ROWS BETWEEN 2 PRECEDING AND CURRENT ROW` frame clause to limit it to the last 3 invoices.

### 9. Harutyun Khachatryan (50/100)
**Question 1: 50/50**
- **Feedback:** Perfect logic. Extracting the "Hidden Hits" in a CTE made the code very readable, and your `RANK()` window function was fully correct.
**Question 2: 0/50**
- **Feedback:** No submission provided.

### 10. Yulya Sargsyan (50/100)
**Question 1: 50/50**
- **Feedback:** Well done. The logic for filtering unsold tracks and the `RANK()` window function over Genre were both correctly implemented.
**Question 2: 0/50**
- **Feedback:** No submission provided.
