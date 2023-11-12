# Docker pull latest mysql server

```cmd
docker pull mysql/mysql-server
docker run --name=LocalMysql -p3306:3306 -e MYSQL_ROOT_PASSWORD=password -e MYSQL_ROOT_HOST:"%" -d mysql/mysql-server:latest

```
---

### Create database ang grant privilage
```cmd
docker exec -it LocalMysql sh
```


```bash
mysql -uroot -p


mysql> CREATE USER 'it'@'%' IDENTIFIED WITH mysql_native_password BY 'password';

# check is %
mysql> SELECT host, user FROM mysql.user;
```

---

# Install sqlalchemy with pip:
```python
pip install


```


from sqlalchemy import create_engine



engine = create_engine('mysql://root:password@127.0.0.1/mysql')
# Write records stored in a DataFrame to a SQL database
df.to_sql("characters", con = engine)




----------------------------------------------



from sqlalchemy import create_engine, insert

import pandas as pd
require_cols = [1, 2, 3, 4, 5]
df = pd.read_excel("mainRep.xls", sheet_name = "Page 1", usecols = require_cols, skiprows=[0, 44, 45, 88, 89])

# print(df)

engine = create_engine('mysql://root:password@localhost/araz')
df.to_sql("test", con=engine, index=False)



-------------------------------------------------
Pandas

https://www.geeksforgeeks.org/creating-a-dataframe-using-excel-files/
