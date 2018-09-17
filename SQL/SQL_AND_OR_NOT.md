## The SQL AND, OR and NOT Operators

The WHERE clause can be combined with AND, OR, and NOT operators.

The AND and OR operators are used to filter records based on more than one condition:

- The AND operator displays a record if all the conditions separated by AND is TRUE.
- The OR operator displays a record if any of the conditions separated by OR is TRUE.

The NOT operator displays a record if the condition(s) is NOT TRUE.

### AND Syntax
```
SELECT column1, column2, ...
FROM table_name
WHERE condition1 AND condition2 AND condition3 ...;
```
- WHERE절에 있는 조건 모두의 해당하는 선택된 컬럼을 테이블에서 불러온다.


### OR Syntax
```
SELECT column1, column2, ...
FROM table_name
WHERE condition1 OR condition2 OR condition3 ...;
```
- WHERE절에 있는 조건 중 하나라도 해당하는 선택된 컬럼을 테이블에서 불러온다.


### NOT Syntax
```
SELECT column1, column2, ...
FROM table_name
WHERE NOT condition;
```

- WHERE절에 있는 조건에 해당하지 않는 선택된 컬럼을 테이블에서 불러온다.
