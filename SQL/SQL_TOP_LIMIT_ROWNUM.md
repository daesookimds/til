## SQL TOP, LIMIT or ROWNUM Clause
### The SQL SELECT TOP Clause

- The SELECT TOP clause is used to specify the number of records to return.

- The SELECT TOP clause is useful on large tables with thousands of records. Returning a large number of records can impact on performance.

Note: Not all database systems support the SELECT TOP clause. MySQL supports the LIMIT clause to select a limited number of records, while Oracle uses ROWNUM.

### SQL Server / MS Access Syntax:

```
SELECT TOP number|percent column_name(s)
FROM table_name
WHERE condition;
```

### MySQL Syntax:

```
SELECT column_name(s)
FROM table_name
WHERE condition
LIMIT number;
```

### Oracle Syntax:

```
SELECT column_name(s)
FROM table_name
WHERE ROWNUM <= number;
```

### SQL TOP, LIMIT and ROWNUM Examples
- The following SQL statement selects the first three records from the "Customers" table:
```
SELECT TOP 3 * FROM Customers;
````

- The following SQL statement shows the equivalent example using the LIMIT clause:

```
SELECT * FROM Customers
LIMIT 3;
```

- The following SQL statement shows the equivalent example using ROWNUM:

```
SELECT * FROM Customers
WHERE ROWNUM <= 3;
```

Customers테이블 가장 위에 있는 3개 레코드를 보여주는 구문


### SQL TOP PERCENT Example
- The following SQL statement selects the first 50% of the records from the "Customers" table:
```
SELECT TOP 50 PERCENT * FROM Customers;
```

### ADD a WHERE CLAUSE
- The following SQL statement selects the first three records from the "Customers" table, where the country is "Germany":

```
SELECT TOP 3 * FROM Customers
WHERE Country='Germany';
```

- The following SQL statement shows the equivalent example using the LIMIT clause:

```
SELECT * FROM Customers
WHERE Country='Germany'
LIMIT 3;
```

- The following SQL statement shows the equivalent example using ROWNUM:

```
SELECT * FROM Customers
WHERE Country='Germany' AND ROWNUM <= 3;
```
Customers 테이블에서 Country가 'Germany'인 데이터 중 가장 위에(테이블에 표시된 순서) 있는 3개 데이터를 불러온다.
