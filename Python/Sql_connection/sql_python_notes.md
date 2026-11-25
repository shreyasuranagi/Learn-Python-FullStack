# SQL Connection

module - sqlite3 module

1. connect() -is used to establish the connection between the python file and the database

```
import sqlite3
var1=sqlite3.connect('database.db')
```

2. cursor() - It helps to get the pointer pointing to the particular position in the databse and execute sql queries
```
var2 = var1.cursor()
```

3. execute() - It is used to write the SQL query
```
var2.execute("query")
```

4. commit() - to save the changes
```
var1.commit()
```

5. close() - to close the connection
```
var1.close()
```

**Example**


