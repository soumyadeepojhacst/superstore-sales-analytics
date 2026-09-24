CREATE DATABASE SUPERSTORE_DB;

use SUPERSTORE_DB;

CREATE TABLE sales (
    Order_ID VARCHAR(20),
    Order_Date DATE,
    Ship_Date DATE,
    Ship_Mode VARCHAR(50),
    Customer_ID VARCHAR(20),
    Customer_Name VARCHAR(100),
    Segment VARCHAR(50),
    Region VARCHAR(50),
    Category VARCHAR(50),
    Sub_Category VARCHAR(50),
    Product_Name VARCHAR(255),
    Sales DECIMAL(10,2),
    Quantity INT,
    Discount DECIMAL(5,2),
    Profit DECIMAL(10,2),
    Order_Year INT,
    Order_Month INT,
    Order_Month_Name VARCHAR(20),
    Order_Quarter INT,
    Shipping_Days INT,
    Profit_Margin DECIMAL(10,2)
);


LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 26.7/Uploads/Superstore_Cleaned.csv"
INTO TABLE SALES
FIELDS TERMINATED BY ","
ENCLOSED BY '"'
LINES TERMINATED BY "\n"
IGNORE 1 ROWS
(Order_ID, Order_Date, Ship_Date, Ship_Mode, Customer_ID, Customer_Name, Segment, Region, Category, Sub_Category, Product_Name, Sales, Quantity, Discount, Profit, Order_Year, Order_Month, Order_Month_Name, Order_Quarter, Shipping_Days, Profit_Margin);


#QUERY1
SELECT Category,SUM(Profit) AS Total_Profit
FROM SALES
GROUP BY Category
ORDER BY Total_profit DESC;

SELECT Sub_Category,SUM(Profit) AS Total_Profit
FROM SALES
GROUP BY Sub_Category
ORDER BY Total_Profit DESC;

#QUERY2
SELECT Order_Year, Order_Month_Name, SUM(Sales) AS Monthly_Sales
FROM SALES
GROUP BY Order_Year, Order_Month_Name
ORDER BY Monthly_Sales DESC;

#QUERY3
SELECT Region,SUM(SALES) AS Total_Sales,
SUM(Profit) AS Total_Profit,
ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS Profit_Margin_Pct
FROM Sales
GROUP BY Region
ORDER BY Total_Profit;

#Query4
#part1
SELECT Customer_Name,
SUM(Sales) AS Total_Sales,
RANK() OVER (ORDER BY SUM(Sales) DESC) AS Sales_Rank
FROM sales
GROUP BY Customer_Name
ORDER BY Total_Sales DESC
LIMIT 10;

#part2
WITH Customer_Sales AS(
    SELECT Customer_Name, SUM(Sales) AS Total_Sales
    FROM sales
    GROUP BY Customer_Name
),
Total AS(
    SELECT SUM(Sales) AS Grand_Total
    FROM sales
)
SELECT c.Customer_Name,c.Total_Sales,
    ROUND(c.Total_Sales / t.Grand_Total*100,2) AS Pct_Of_Total
FROM Customer_Sales c,Total t 
ORDER BY c.Total_Sales DESC
LIMIT 10;

#Query5
SELECT
    CASE
        WHEN Discount <= 0.1 THEN '0-10%'
        WHEN Discount <=0.2 THEN '11-20%'
        WHEN Discount <=0.3 THEN '21-30%'
        WHEN Discount <=0.4 THEN '31-40%'
        ELSE '41-50%'
    END AS Discount_Range,
    ROUND(AVG(Profit_Margin),2) AS AVG_Profit_Margin
FROM Sales
WHERE Profit_Margin BETWEEN -100 AND 100
GROUP BY Discount_Range
ORDER BY Discount_Range;

#Query6
SELECT Segment,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    ROUND(AVG(Sales),2) AS AVG_Order_Value,
    COUNT(DISTINCT Order_Id) AS Order_Count
FROM Sales
GROUP BY Segment
ORDER BY Total_Profit DESC;






