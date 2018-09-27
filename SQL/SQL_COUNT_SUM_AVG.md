## SQL COUNT(), AVG() and SUM() Functions

### The SQL COUNT(), AVG() and SUM() Functions

- The COUNT() function returns the number of rows that matches a specified criteria.

- The AVG() function returns the average value of a numeric column.

- The SUM() function returns the total sum of a numeric column.

### COUNT() Syntax
```
SELECT COUNT(column_name)
FROM table_name
WHERE condition;
```

테이블내 WHERE 조건에 해당하는 column_name의 갯수 검색

### AVG() Syntax
```
SELECT AVG(column_name)
FROM table_name
WHERE condition;
```

테이블내 WHERE 조건에 해당하는 column_name의 평균 검색

### SUM() Syntax
```
SELECT SUM(column_name)
FROM table_name
WHERE condition;
```

테이블내 WHERE 조건에 해당하는 column_name의 합계 검색


### COUNT() Example

- The following SQL statement finds the number of products:

```
SELECT COUNT(ProductID)
FROM Products;
```

### AVG() Example
- The following SQL statement finds the average price of all products:

```
SELECT AVG(Price)
FROM Products;
```


### SUM() Example
- The following SQL statement finds the sum of the "Quantity" fields in the "OrderDetails" table:

```
SELECT SUM(Quantity)
FROM OrderDetails;
```