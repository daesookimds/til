## SQL NULL Values
### What is a NULL Value?
A field with a NULL value is a field with no value.

If a field in a table is optional, it is possible to insert a new record or update a record without adding a value to this field. Then, the field will be saved with a NULL value.

- Note: It is very important to understand that a NULL value is different from a zero value or a field that contains spaces. A field with a NULL value is one that has been left blank during record creation!

### How to Test for NULL Values?
- It is not possible to test for NULL values with comparison operators, such as =, <, or <>.

- We will have to use the IS NULL and IS NOT NULL operators instead.

### IS NULL Syntax
```
SELECT column_names
FROM table_name
WHERE column_name IS NULL;
```

- 테이블에 있는 특정 컬럼이 비어있는 경우를 조회한다.

### IS NOT NULL Syntax
```
SELECT column_names
FROM table_name
WHERE column_name IS NOT NULL;
```

- 테이블에 있는 특정 컬럼이 비어있지 않은 경우를 조회한다.
