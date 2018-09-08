## SQL SELECT Statement

- The SELECT statement is used to select data from database.
- The data returned is stored in a result table, called the result-set.

SELECT 구문은 데이터베이스에서 데이터를 선택할 때 사용한다.
SELECT 구문을 사용할 경우 result-set으로 불리는 테이블 형태로 데이터가 반환된다.

### SELECT Syntax

```
SELECT columns1, columns2, ...
FROM table_name;
```

- Here, "column1, column2, ..." are the field names of the table you want to select data from. 

여기서 "열1, 열2, ..." 는 데이터베이스에서 SELECT 하는 데이터의 필드 이름이다.

- If you want to select all the fields available in the table, use the following syntax:

만약 테이블에서 선택할 수 있는 모든 필드 이름을 SELECT 하고 싶다면, 아래 문법 처럼 * 을 사용하면 된다.


```
SELECT * FROM table_name;
````

### Demo Database

- Below is a selection from the "Customers" table in the Northwind sample database:
아래 Customers 테이블을 가지고 SELECT 구문을 연습해보자.


CustomerID | CustomerName | ContactName | Address | City | PostalCod | Country
----------|---------------|-------------|----------|------|-----------|-----
1|Alfreds Futterkiste|Maria Anders|Obere Str. 57|Berlin|12209|Germany|
2|Ana Trujillo Emparedados y helados|Ana Trujillo|Avda. de la Constitución 2222|México D.F.|05021|Mexico|
3|Antonio Moreno Taquería|Antonio Moreno|Mataderos 2312|México D.F.|05023|Mexico|
4|Around the Horn|Thomas Hardy|120 Hanover Sq.|London|WA1 1DP|UK|
5|Berglunds snabbköp|Christina Berglund|Berguvsvägen 8|Luleå|S-958 22|Sweden|


### SELECT Column Example
- To select CustomerName and City field from Customers table. 
Customers 테이블에서 CustomerName필드와 City필드 SELECT 하기.
```
SELECT CustomberName, City FROM Customers;
```

- To select all fields from Customers table.
Customers 테이블에서 모든 필드 SELECT 하기.
```
SELECT * FROM Customers;