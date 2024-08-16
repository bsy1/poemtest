# -*- coding: GB2312 -*-

import sqlite3
import random
import json

def get_random_element(data_list):
    if data_list:
        return random.choice(data_list)
    return None
class PoemRandom : #生成问题
    #预定义public变量
    def __init__(self):
        self.question=["","","",""]
        self.ans=0
        self.poemlist=[]
    def poemra(self,modes) : #生成随机古诗
        conn = sqlite3.connect("poem.db")
        cursor = conn.cursor()
        if modes:
             id=int(get_random_element(self.poemlist))
        else:
             id=random.randint(1,240000)
        cursor.execute("select * from poem where _id="+str(id))
        i=1
        for item in cursor:
            #获取原文
           return(item[13])
           item[13]
        cursor.close()
        conn.close()
    def broken(self):#生成混淆项
        str=self.poemra(0)
        parts=str.split(",")
        parts=[item.strip()for part in parts for item in part.split("\n")]#分割字段
        a=random.randint(0,len(parts)-1)
        return parts[a]
    def core (self,modes) :#组成问题
        str=self.poemra(modes)
        parts=str.split(",")
        parts=[item.strip()for part in parts for item in part.split("\n")]#分割字段
        a=random.randint(0,len(parts)-1)
        self.question[0]=parts[a] # type: ignore #生成问题
        self.ans=random.randint(1,3)
        for i in range(1,4):#生成混淆项
            self.question[i]=self.broken() # type: ignore
        if a==len(parts)-1:#覆盖答案
            self.question[self.ans]=parts[a-1] # type: ignore
            #return [parts[a],parts[a-1]]
            
        else:
            self.question[self.ans]=parts[a+1] # type: ignore
            #return[parts[a],parts[a+1]]
    def init(self,modes):
        self.core(modes)
        return self.question
    def check(self,b):
        return b==self.ans
class FindData:
    def ff(self, query_text):
        conn = sqlite3.connect("poem.db")
        cursor = conn.cursor()
        try:
            
            query = "SELECT * FROM poem WHERE mingcheng LIKE ?"
            cursor.execute(query, (f'%{query_text}%',))
            results = cursor.fetchall()
            return results
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []
        finally:
            cursor.close()
            conn.close()
    def idfound(self,pid):
        conn = sqlite3.connect("poem.db")
        cursor = conn.cursor()
        try:
            
            query = "SELECT * FROM poem WHERE _id LIKE ?"
            cursor.execute(query, (f'%{pid}%',))
            results = cursor.fetchall()
            return results
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []
        finally:
            cursor.close()
            conn.close()
class users:
    
        
    def login(self,user,key):
        try:
            userdb=sqlite3.connect("User.db")
            self.cursor = userdb.cursor()
            query = "SELECT * FROM Users WHERE name LIKE ?"
            self.cursor.execute(query, (f'{user}',))
            results = self.cursor.fetchall()
            
            if results :
                if results[0][2]==key:
                    return results[0][0]
                else:
                    return -1
            else:
                
                
                self.cursor.execute("INSERT INTO Users (name, passwd) VALUES (?, ?)", (user, key))
                query = "SELECT * FROM Users WHERE name LIKE ?"
                self.cursor.execute(query, (f'{user}',))
                temp = self.cursor.fetchall()
                userdb.commit()
                return temp
              
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            
            return []
        finally :
            self.cursor.close()
            userdb.close()
class love:
    def __init__(self, db_path):
        self.db_path = db_path

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def update_pid(self, uid, pid):
        conn = self._connect()
        cursor = conn.cursor()

        # 获取当前的第五列数据，并将其转换为列表
        cursor.execute("SELECT poem FROM Users WHERE id = ?", (uid,))
        result = cursor.fetchone()
        current_pids = []
        
        if result and result[0]:
            try:
                current_pids = json.loads(result[0])
            except json.JSONDecodeError:
                pass  # 如果 JSON 解析失败，保持为空列表

        # 将新的 pid 添加到列表中
        current_pids.append(pid)
        
        # 将更新后的列表转换为 JSON 字符串
        updated_pids_json = json.dumps(current_pids)

        # 更新数据库
        cursor.execute("UPDATE Users SET poem = ? WHERE id = ?", (updated_pids_json, uid))
        conn.commit()
        conn.close()      
    def get_data_as_list(self, uid):
        conn = self._connect()
        cursor = conn.cursor()

        # 替换 'data_column' 为实际的列名
        column_name = 'poem'

        # 获取数据
        cursor.execute(f"SELECT {column_name} FROM Users WHERE id = ?", (uid,))
        result = cursor.fetchone()
        data_list = []

        if result and result[0]:
            try:
                data_list = json.loads(result[0])
            except json.JSONDecodeError:
                pass  # 如果 JSON 解析失败，保持为空列表

        conn.close()
        return data_list   


        

       
        
#测试
if __name__=="__main__":

      a=users()
      db = love('user.db')
      db.update_pid(1, '11514')
      poemlist=db.get_data_as_list(1)
      
      
      

    






