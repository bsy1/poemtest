# -*- coding: GB2312 -*-

import sqlite3
import random

class PoemRandom : #生成问题
    #预定义public变量
    question=["","","",""]
    ans=0
    def poemra(self) : #生成随机古诗
        conn = sqlite3.connect("poem.db")
        cursor = conn.cursor()
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
        str=self.poemra()
        parts=str.split(",")
        parts=[item.strip()for part in parts for item in part.split("\n")]#分割字段
        a=random.randint(0,len(parts)-1)
        return parts[a]
    def core (self) :#组成问题
        str=self.poemra()
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
    def init(self):
        self.core()
        return self.question
    def check(self,b):
        return b==self.ans
class FindData:
    def ff(self, query_text):
        """生成随机古诗"""
        conn = sqlite3.connect("poem.db")
        cursor = conn.cursor()
        try:
            id = random.randint(1, 240000)
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
class users:
    def __init__(self):
        userdb=sqlite3.connect("User.db")


        

       
        
#测试
if __name__=="__main__":
      a=PoemRandom()
      
      print(a.init())
      print(a.check(int(input())))
      cursor = conn.cursor()
      cursor.execute("select * from poem where mingcheng=\"静夜思\"")
      for item in cursor:
          print(item)
      cursor.close()

    






