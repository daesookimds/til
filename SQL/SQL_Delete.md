## SQL DELETE Statement

### The SQL DELETE Statement
- The DELETE statement is used to delete existing records in a table.

### DELETE Syntax
```
DELETE FROM table_name
WHERE condition;
```
조건에 해당하는 컬럼을 삭제한다.

### SQL DELETE Example
- The following SQL statement deletes the customer "Alfreds Futterkiste" from the "Customers" table:

```
DELETE FROM Customers
WHERE CustomerName='Alfreds Futterkiste';
```
CustomerName이 Alfreds Futterkiste인 레코드를 삭제한다.

### Delete All Records
- It is possible to delete all rows in a table without deleting the table. This means that the table structure, attributes, and indexes will be intact:
```
DELETE FROM table_name;
```
or:

```
DELETE * FROM table_name;
```

테이블에 모든 데이터를 삭제하고 싶을 경우 위 두가지 방법을 사용할 수 있다.