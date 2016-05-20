# -*- encoding: utf-8 -*-
import sys
sys.path.append(r"../comm")
from sqlite3worker import Sqlite3Worker

sql_worker = Sqlite3Worker("../config/spiderurls.db")


results = sql_worker.execute("SELECT method,url,param from spiderurls")
for method,url,param in results:
    print method,url,param

sql_worker.close()
