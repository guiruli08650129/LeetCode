# Write your MySQL query statement below

SELECT c.Name As Customers FROM Customers as c
WHERE c.Id Not In (SELECT CustomerId FROM Orders as o)

