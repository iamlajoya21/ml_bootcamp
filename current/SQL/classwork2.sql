/*******************************************************************************
   SQL ADVANCED WORKSHOP - Chinook Database
   Topics: Subqueries, CTEs, Window Functions, Temp Tables, and Case Logic
********************************************************************************/

-- =============================================================================
-- PHASE 1: SUBQUERIES (NESTED QUERIES)
-- Goal: Using the result of one query to filter another.
-- =============================================================================

-- 1. Scalar Subquery: Find all invoices where the total is greater than the average invoice total
SELECT * FROM Invoice 
WHERE Total > (SELECT AVG(Total) FROM Invoice);

-- 2. Subquery in IN: Find all customers who have ever bought a track (Invoice exists)
SELECT FirstName, LastName FROM Customer 
WHERE CustomerId IN (SELECT DISTINCT CustomerId FROM Invoice);

-- 3. Subquery in FROM: Calculate the average of the "Total Revenue per Country"
SELECT AVG(CountryTotal) 
FROM (SELECT BillingCountry, SUM(Total) AS CountryTotal FROM Invoice GROUP BY BillingCountry);

-- 4. Correlated Subquery: Find employees who earn more than the average of their specific department
-- (Note: Using a placeholder logic as salary isn't in this specific schema, let's use Invoice counts)
SELECT FirstName, LastName 
FROM Employee e 
WHERE (SELECT COUNT(*) FROM Customer WHERE SupportRepId = e.EmployeeId) > 5;

-- 5. EXISTS: Find Artists who actually have albums in our database
SELECT Name FROM Artist ar
WHERE EXISTS (SELECT 1 FROM Album al WHERE al.ArtistId = ar.ArtistId);

-- =============================================================================
-- PHASE 2: COMMON TABLE EXPRESSIONS (CTEs)
-- Goal: Modularize complex logic to make it readable.
-- =============================================================================

-- 6. Basic CTE: Create a "Top Customers" list and then select from it
WITH TopCustomers AS (
    SELECT CustomerId, SUM(Total) as TotalSpent
    FROM Invoice
    GROUP BY CustomerId
    HAVING TotalSpent > 40
)
SELECT c.FirstName, c.LastName, tc.TotalSpent
FROM Customer c
JOIN TopCustomers tc ON c.CustomerId = tc.CustomerId;

-- 7. Multi-CTE: Find the top artist and their total sales
WITH ArtistSales AS (
    SELECT al.ArtistId, SUM(il.UnitPrice * il.Quantity) AS Revenue
    FROM InvoiceLine il
    JOIN Track t ON il.TrackId = t.TrackId
    JOIN Album al ON t.AlbumId = al.AlbumId
    GROUP BY al.ArtistId
),
TopArtist AS (
    SELECT ArtistId FROM ArtistSales ORDER BY Revenue DESC LIMIT 1
)
SELECT Name FROM Artist WHERE ArtistId = (SELECT ArtistId FROM TopArtist);

-- 8. CTE for Clean Aggregation: Average sales per year
WITH YearlySales AS (
    SELECT STRFTIME('%Y', InvoiceDate) as Year, SUM(Total) as AnnualTotal
    FROM Invoice
    GROUP BY Year
)
SELECT AVG(AnnualTotal) FROM YearlySales;

-- 9. CTE for Regional Analysis: Top city per country by revenue
WITH CityRevenue AS (
    SELECT BillingCountry, BillingCity, SUM(Total) as Revenue
    FROM Invoice
    GROUP BY BillingCountry, BillingCity
)
SELECT BillingCountry, BillingCity, MAX(Revenue)
FROM CityRevenue
GROUP BY BillingCountry;

-- 10. Recursive-Style logic (Simulated): Find all employees in the hierarchy
-- (Self-join CTE for organizational structure)
WITH RECURSIVE OrgChart AS (
    SELECT EmployeeId, FirstName, LastName, ReportsTo, 0 as Level
    FROM Employee WHERE ReportsTo IS NULL
    UNION ALL
    SELECT e.EmployeeId, e.FirstName, e.LastName, e.ReportsTo, oc.Level + 1
    FROM Employee e
    JOIN OrgChart oc ON e.ReportsTo = oc.EmployeeId
)
SELECT * FROM OrgChart;

-- =============================================================================
-- PHASE 3: WINDOW FUNCTIONS (ANALYTIC FUNCTIONS)
-- Goal: Calculate values across a set of rows related to the current row.
-- =============================================================================

-- 11. ROW_NUMBER(): Rank customers by their total spend
SELECT CustomerId, Total,
       ROW_NUMBER() OVER(PARTITION BY CustomerId ORDER BY Total DESC) as PurchaseNumber
FROM Invoice;

-- 12. RANK(): Rank countries by their total revenue
SELECT BillingCountry, SUM(Total),
       RANK() OVER(ORDER BY SUM(Total) DESC) as SalesRank
FROM Invoice
GROUP BY BillingCountry;

-- 13. Running Total: Calculate a cumulative sum of sales over time
SELECT InvoiceDate, Total,
       SUM(Total) OVER(ORDER BY InvoiceDate) as RunningTotal
FROM Invoice;

-- 14. LEAD/LAG: Compare the current invoice total to the previous one for a customer
SELECT CustomerId, InvoiceDate, Total,
       LAG(Total) OVER(PARTITION BY CustomerId ORDER BY InvoiceDate) as PreviousOrderTotal
FROM Invoice;

-- 15. Percentile: Find the top 10% of invoices by value
SELECT InvoiceId, Total,
       NTILE(10) OVER(ORDER BY Total DESC) as Decile
FROM Invoice;

-- =============================================================================
-- PHASE 4: TEMPORARY TABLES
-- Goal: Store intermediate results for multi-step procedures.
-- =============================================================================

-- 16. Create a Temp Table of High Value Customers
CREATE TEMPORARY TABLE HighValueCustomers AS
SELECT CustomerId, SUM(Total) as LifetimeValue
FROM Invoice
GROUP BY CustomerId
HAVING LifetimeValue > 45;

-- 17. Use the Temp Table for a join
SELECT c.Email, hvc.LifetimeValue
FROM Customer c
JOIN HighValueCustomers hvc ON c.CustomerId = hvc.CustomerId;

-- 18. Update logic in Temp Table (Simulated)
-- (Helpful for teaching data cleaning before final reports)
DROP TABLE IF EXISTS HighValueCustomers;

-- =============================================================================
-- PHASE 5: ADVANCED STRING & DATE MANIPULATION
-- Goal: Formatting data for business reports.
-- =============================================================================

-- 19. Concatenation: Create a full mailing address string
SELECT FirstName || ' ' || LastName || ' - ' || Address || ', ' || City as MailingLabel
FROM Customer;

-- 20. String Length: Find artists with unusually long names
SELECT Name FROM Artist WHERE LENGTH(Name) > 25;

-- 21. Date Truncation: Group sales by Month
SELECT STRFTIME('%Y-%m', InvoiceDate) as Month, SUM(Total)
FROM Invoice
GROUP BY Month;

-- 22. Case Logic: Categorize customers by their spending level
SELECT CustomerId, SUM(Total),
       CASE 
           WHEN SUM(Total) > 45 THEN 'VIP'
           WHEN SUM(Total) BETWEEN 30 AND 45 THEN 'Regular'
           ELSE 'New/Low Spend'
       END as CustomerSegment
FROM Invoice
GROUP BY CustomerId;

-- =============================================================================
-- PHASE 6: SET OPERATORS (UNION, INTERSECT, EXCEPT)
-- Goal: Combining results from different queries.
-- =============================================================================

-- 23. UNION: Create a master list of all people (Customers + Employees)
SELECT FirstName, LastName, 'Customer' as Type FROM Customer
UNION
SELECT FirstName, LastName, 'Employee' as Type FROM Employee;

-- 24. INTERSECT: Find cities that have both a customer and an employee
SELECT City FROM Customer
INTERSECT
SELECT City FROM Employee;

-- 25. EXCEPT: Find countries that have customers but NO employees
SELECT Country FROM Customer
EXCEPT
SELECT Country FROM Employee;

-- =============================================================================
-- PHASE 7: COMPLEX MULTI-TABLE JOINS
-- Goal: Deep relational data extraction.
-- =============================================================================

-- 26. The "Whole Picture": Artist -> Album -> Track -> Genre -> InvoiceLine
SELECT ar.Name as Artist, al.Title as Album, g.Name as Genre, SUM(il.Quantity) as Sold
FROM Artist ar
JOIN Album al ON ar.ArtistId = al.ArtistId
JOIN Track t ON al.AlbumId = t.AlbumId
JOIN Genre g ON t.GenreId = g.Name -- (Logic fix: g.GenreId = t.GenreId)
JOIN InvoiceLine il ON t.TrackId = il.TrackId
GROUP BY ar.Name, al.Title, g.Name
ORDER BY Sold DESC;

-- 27. Cross Join: Create a matrix of all Genres and all MediaTypes (Theoretical combinations)
SELECT g.Name as Genre, m.Name as Media
FROM Genre g
CROSS JOIN MediaType m;

-- 28. Left Join to find "Dead Data": Albums with no Tracks
SELECT al.Title 
FROM Album al
LEFT JOIN Track t ON al.AlbumId = t.AlbumId
WHERE t.TrackId IS NULL;

-- 29. Complex Case + Join: Flagging invoices as "International" or "Domestic"
SELECT i.InvoiceId, c.Country as CustomerCountry, i.BillingCountry,
       CASE WHEN c.Country = i.BillingCountry THEN 'Domestic' ELSE 'International' END as ShippingType
FROM Invoice i
JOIN Customer c ON i.CustomerId = c.CustomerId;

-- 30. Final "Master Query": Customer spend vs the Average spend in their specific country
WITH CountryAvg AS (
    SELECT BillingCountry, AVG(Total) as AvgTotal
    FROM Invoice
    GROUP BY BillingCountry
)
SELECT i.CustomerId, i.Total, ca.AvgTotal,
       (i.Total - ca.AvgTotal) as VarianceFromCountryAvg
FROM Invoice i
JOIN CountryAvg ca ON i.BillingCountry = ca.BillingCountry;