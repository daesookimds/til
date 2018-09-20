## SQL UPDATE Statement
### The SQL UPDATE Statement

- The UPDATE statement is used to modify the existing records in a table.

### UPDATE Syntax
```
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

원하는 조건에 맞는 컬럼들의 값들을 바꿔준다. 일반적으로 사용할일 많지는 않을 것 같다.

### UPDATE Table
- The following SQL statement updates the first customer (CustomerID = 1) with a new contact person and a new city.

```
UPDATE Customers
SET ContactName = 'Alfred Schmidt', City= 'Frankfurt'
WHERE CustomerID = 1;
```

CustomerID가 1인 경우 Customers테이블의 ContactName와 City의 값을 각각 바꿔준다.


### UPDATE Multiple Records
-  It is the WHERE clause that determines how many records that will be updated.

- The following SQL statement will update the contactname to "Juan" for all records where country is "Mexico":

```
UPDATE Customers
SET ContactName='Juan'
WHERE Country='Mexico';
```

Country가 Mexico인 컬럼의 ContactName이 모두 Juan으로 변경된다.


### Update Warning!
- Be careful when updating records. If you omit the WHERE clause, ALL records will be updated!
```
UPDATE Customers
SET ContactName='Juan';
```

WHERE절 없이 업데이트 할 경우 모든레코드의 값이 바뀌므로 주의해야한다!