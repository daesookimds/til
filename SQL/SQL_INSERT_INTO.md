## The SQL INSERT INTO Statement

The INSERT INTO statement is used to insert new records in a table.

### INSERT INTO Syntax

It is possible to write the INSERT INTO statement in two ways.

The first way specifies both the column names and the values to be inserted:
```
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
````
- 테이블에 원하는 컬럼에 원하는 값을 집어넣을 때 사용한다.


If you are adding values for all the columns of the table, you do not need to specify the column names in the SQL query. However, make sure the order of the values is in the same order as the columns in the table. The INSERT INTO syntax would be as follows:

- 모든 컬럼에 값을 집어넣고 싶을 때에는 컬럼명을 생략해도 되지만, VALUES 파트에 컬럼명의 순서는 테이블에 있는 컬럼명의 순서와 반드시 같아야 한다.

```
INSERT INTO table_name
VALUES (value1, value2, value3, ...);
```