## SQL WHERE Clause

### The SQL WHERE Clause

- The WHERE clause is used to filter records.

- The WHERE clause is used to extract only those records that fulfill a specified condition.

WHERE절은 필터 용도로 사용한다.

WHERE절은 특정한 조건의 값들을 추출해 내는데 사용한다.

### WHERE syntax

```
SELECT column1, column2, ...
FROM table_name
WHERE condition;
````


### WHERE Clause example

- The following SQL statement selects all the customers from the country "Mexico", in the "Customers" table:

아래 SQL문은 Customers테이블에서 Country가 Mexico인 고객의 정보를 모두 보여준다.

````
SELECT * FROM Customers
WHERE Country='Mexico';
````
