# Docker pull latest mysql server

```cmd
docker pull mysql/mysql-server

docker run --name=mysql1 -d mysql/mysql-server 
# Windows
docker logs mysql1

# linux
docker logs mysql1 2>&1 | grep GENERATED
GENERATED ROOT PASSWORD: seJ_c2hC:y37o525VG/K=@7Zf*T^_k2p

docker exec -it mysql1 mysql -uroot -p
ALTER USER 'root'@'localhost' IDENTIFIED BY 'password';
```
---

 # 👆 OR 👇

---

```cmd
docker pull mysql/mysql-server
docker container run --name=LocalMysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=password -e MYSQL_ROOT_HOST:"%" mysql -d mysql/mysql-server

docker run --name=LocalMysql -p3306:3306 -v mysql-volume:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=my-password -e MYSQL_ROOT_HOST:"%" -d mysql/mysql-server:latest

docker exec -it LocalMysql mysql -uroot -p
# OR
docker exec -it LocalMysql
mysql -h localhost -uroot -P 3306 -ppassword
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
