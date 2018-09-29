## SQL Wildcards
### SQL Wildcard Characters
A wildcard character is used to substitute any other character(s) in a string.

Wildcard characters are used with the SQL LIKE operator. The LIKE operator is used in a WHERE clause to search for a specified pattern in a column. 

There are two wildcards used in conjunction with the LIKE operator:

- % - The percent sign represents zero, one, or multiple characters
- _ - The underscore represents a single character
Note: MS Access uses a question mark (?) instead of the underscore (_).

In MS Access and SQL Server you can also use:

- [charlist] - Defines sets and ranges of characters to match
- [^charlist] or [!charlist] - Defines sets and ranges of characters NOT to match
The wildcards can also be used in combinations!


### Using the % Wildcard
The following SQL statement selects all customers with a City starting with "ber":

```
SELECT * FROM Customers
WHERE City LIKE 'ber%';
```

The following SQL statement selects all customers with a City containing the pattern "es": 

```
SELECT * FROM Customers
WHERE City LIKE '%es%';
```

### Using the _ Wildcard
The following SQL statement selects all customers with a City starting with any character, followed by "erlin":

```
SELECT * FROM Customers
WHERE City LIKE '_erlin';
```

The following SQL statement selects all customers with a City starting with "L", followed by any character, followed by "n", followed by any character, followed by "on":

```
SELECT * FROM Customers
WHERE City LIKE 'L_n_on';
```

### Using the [charlist] Wildcard
The following SQL statement selects all customers with a City starting with "b", "s", or "p":

```
SELECT * FROM Customers
WHERE City LIKE '[bsp]%';
```

The following SQL statement selects all customers with a City starting with "a", "b", or "c":

```
SELECT * FROM Customers
WHERE City LIKE '[a-c]%';
```

### Using the [!charlist] Wildcard
The two following SQL statements select all customers with a City NOT starting with "b", "s", or "p":

```
SELECT * FROM Customers
WHERE City LIKE '[!bsp]%';
```
Or:
```
SELECT * FROM Customers
WHERE City NOT LIKE '[bsp]%';
```