use EcommerceDB

select Sum(sales) as TotalSales
from dbo.EcommerceSales_Import

select sum(Quantity) AS TotalQuantity
from dbo.EcommerceSales_Import

select count(Distinct order_id)as Totalorders
from dbo.EcommerceSales_Import

select 
     category,
     sum(sales) as totalsales
from dbo.EcommerceSales_Import
group by Category
order by totalsales desc;

select count(Distinct category) as totalcategories
from dbo.EcommerceSales_Import;

select top 5 
    product,
    sum(sales) as totalsales
from dbo.EcommerceSales_Import
group by product
order by totalsales desc;

select 
     city,
     sum(sales) as totalsales
from dbo.EcommerceSales_Import
group by city
order by totalsales desc

select
    payment,
    sum(sales) as totalsales
from dbo.EcommerceSales_Import
group by payment
order by totalsales desc

select
    payment,
    count(*) as totalorders
from dbo.EcommerceSales_Import
group by payment
order by totalorders desc

select
    Customers.Customer_id,
    Customers.Customer_name,
    Orders.Order_id,
    Orders.sales
from Customers
inner join Orders
     on Customers.Customer_id=orders.Customer_id

select table_name
from INFORMATION_SCHEMA.TABLES
where TABLE_TYPE ='Base table'

select
    Customer_id,
    Order_id,
    Sales
from dbo.EcommerceSales_Import

select
     A.Customer_id,
     A.Order_id,
     A.sales,
     B.Order_id as Another_Order_id
from dbo.EcommerceSales_import as  A
left join dbo.EcommerceSales_import as B
    on A.customer_id = B.Customer_id
    AND A.order_id <> B.order_id 

 select
      A.Order_id,
      A.Customer_id,
      A.product,
      A.Sales,
      B.Order_id as AnotherOrderid,
      B.Sales as anothersales
from dbo.EcommerceSales_import as A
inner join dbo.EcommerceSales_import as B
     on A.customer_id = B.customer_id
where A.Order_id <> B.Order_id


select
     sum(sales) as totalsales,
     count(*) as totalorders,
     count(distinct customer_id) as uniquecustomers
from dbo.EcommerceSales_Import

select 
    month,
    sum(sales) as totalsales
from dbo.EcommerceSales_Import
group by month
order by month
