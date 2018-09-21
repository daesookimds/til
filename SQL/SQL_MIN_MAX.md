## SQL MIN() and MAX() Functions

### The SQL MIN() and MAX() Functions
- The MIN() function returns the smallest value of the selected column.

- The MAX() function returns the largest value of the selected column.

### MIN() Syntax
```
SELECT MIN(column_name)
FROM table_name
WHERE condition;
```

조건에 맞는 컬럼의 최소값을 검색하기.

### MAX() Syntax
```
SELECT MAX(column_name)
FROM table_name
WHERE condition;
```

조건에 맞는 컬럼의 최대값을 검색하기.

### MIN() Example
- The following SQL statement finds the price of the cheapest product:

```
SELECT MIN(Price) AS SmallestPrice
FROM Products;
```
Products 테이블 내 Price가 가장 작은 값을 SmallestPrice이라는 컬럼명으로 검색하기


### MAX() Example
- The following SQL statement finds the price of the most expensive product:

```
SELECT MAX(Price) AS LargestPrice
FROM Products;
```
Products 테이블 내 Price가 가장 큰 값을 LargestPrice이라는 컬럼명으로 검색하기