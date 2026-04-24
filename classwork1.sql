-- 1. Select everything from the Artist table
SELECT * FROM Artist;

-- 2. Select only the names of the Artists
SELECT Name FROM Artist;

-- 3. Find all unique countries where customers live (Removing duplicates)
SELECT DISTINCT Country FROM Customer;

-- 4. Using an Alias (AS) to rename a column for a report
SELECT Title AS Album_Title FROM Album a ;


-- 5. Basic Arithmetic: Show the total invoice amount and a calculated 10% tax column
SELECT Total, Total * 0.1 AS Tax  FROM Invoice;




-- 6. Filter by exact match: All customers living in Brazil
SELECT * FROM Customer WHERE Country = 'Brazil';

-- 7. Filter by numeric comparison: Invoices where the total spent is greater than $10
SELECT * FROM Invoice WHERE Total > 10;

-- 8. Using AND: Customers from the USA who also live in California (CA)
SELECT * FROM Customer WHERE Country = 'USA' AND State = 'CA';

-- 9. Using OR: Finding customers in either Berlin or London
SELECT * FROM Customer WHERE City = 'Berlin' OR City = 'London';

-- 10. Using IN: A cleaner way to write multiple OR conditions
SELECT * FROM Customer WHERE Country IN ('USA', 'Canada', 'Brazil');

-- 11. Finding ranges: All invoices between $5 and $15
SELECT * FROM Invoice WHERE Total BETWEEN 5.94 AND 13.86;

-- 12. Pattern Matching (Wildcards): Artists whose names start with 'A'
SELECT * FROM Artist WHERE Name LIKE '%A%';

-- 13. Pattern Matching: Customers using a Gmail address
SELECT * FROM Customer WHERE Email LIKE '%@gmail.com';

-- 14. Finding NULLs: Customers who do not have a company name listed
SELECT * FROM Customer WHERE Company IS NULL;

SELECT * FROM Customer WHERE Company IS NOT NULL;






-- Solution 1: Easy (Basic WHERE)
SELECT FirstName, LastName, Email 
FROM Customer 
WHERE Country = 'Canada';

-- Solution 2: Medium-Easy (Logical AND + Numeric Comparison)
SELECT * FROM Invoice 
WHERE BillingCountry = 'Germany' 
  AND Total > 15;

-- Solution 3: Medium (Wildcard Pattern Matching)
SELECT * FROM Artist 
WHERE Name LIKE '%Black%';

-- Solution 4: Medium-Hard (Handling NULLs and Set Membership)
-- Note: 'IN' is the most efficient way to handle multiple countries
SELECT * FROM Customer 
WHERE Company IS NULL 
  AND Country IN ('USA', 'Canada', 'Brazil');

-- Solution 5: Hard (Date Filtering + Negation)
-- Note: We use <> or != for 'NOT EQUAL'
SELECT * FROM Employee 
WHERE HireDate >= '2003-01-01' 
  AND Country <> 'USA';
  
 
 
 
 
 
 -- 15. Sort Artists alphabetically (A-Z)
SELECT Name FROM Artist ORDER BY Name asc

-- 16. Sort Invoices by price (Most expensive first)
SELECT * FROM Invoice ORDER BY Total desc

-- 17. Multi-level Sort: Sort by Country first, then City within each country
SELECT * FROM Customer ORDER BY Country ASC, City ASC;

-- 18. Top 5: Find the 5 most expensive invoices ever generated
SELECT * FROM Invoice order by BillingAddress LIMIT 200;


-- =============================================================================
-- PHASE 4: AGGREGATE FUNCTIONS
-- Goal: Performing math across multiple rows.
-- =============================================================================

-- 19. Count the total number of customers in the database
SELECT COUNT(*) AS Total_Customers FROM Customer;

SELECT COUNT(CustomerId) AS Total_Customers FROM Customer;

SELECT COUNT(Fax) AS Total_Customers FROM Customer;

-- 20. Find the total revenue (SUM) of all invoices
SELECT SUM(Total) AS Grand_Total_Revenue FROM Invoice;

-- 21. Find the average (AVG) amount spent on an invoice
SELECT AVG(Total) AS Average_Invoice_Value FROM Invoice;

-- 22. Find the highest (MAX) and lowest (MIN) invoice totals in one query
SELECT MAX(Total) AS Highest_Sale, MIN(Total) AS Lowest_Sale, 
round(max(total)/avg(total), 2) as ratio FROM Invoice;


select 
billingCountry as country,
sum(Total)  as total_revenue,
count(*) as num_invoices, 
round(avg(Total),2) as avg_revenue
from Invoice i 
group by billingCountry
having count(*) > 10
order by sum(total) desc ;




   

-- Solution 1: Medium (Basic Grouping + Sorting)
-- Teaches: COUNT and ORDER BY on an aggregate
SELECT Country, COUNT(CustomerId) AS Customer_Count
FROM Customer
GROUP BY Country
ORDER BY Customer_Count DESC;

-- Solution 2: Medium-Hard (Multiple Aggregates)
-- Teaches: Using multiple math functions in one Group By
SELECT BillingCity, 
       SUM(Total) AS Total_Revenue, 
       AVG(Total) AS Avg_Invoice_Value
FROM Invoice
GROUP BY BillingCity;

-- Solution 3: Hard (The HAVING Clause)
-- Teaches: Filtering groups based on a calculation

SELECT BillingCountry, SUM(Total) AS Total_Revenue
FROM Invoice
GROUP BY BillingCountry
HAVING SUM(Total) > 100
ORDER BY Total_Revenue DESC;

-- Solution 4: Hard (Aggregating specific transaction data)
-- Teaches: Grouping by ID and using HAVING for volume
SELECT TrackId, SUM(Quantity) AS Total_Sold
FROM InvoiceLine
GROUP BY TrackId


-- Solution 5: Extra Hard (Calculated Aggregates + Multiple Constraints)
-- Teaches: Arithmetic inside SELECT and complex HAVING logic
SELECT 
    BillingCountry, 
    SUM(Total) / COUNT(InvoiceId) AS Avg_Spend_Per_Invoice,
    COUNT(InvoiceId) AS Total_Invoices
FROM Invoice
GROUP BY BillingCountry
HAVING COUNT(InvoiceId) > 30
ORDER BY Avg_Spend_Per_Invoice DESC;


 
 
 
 
 