# -*- coding: GB2312 -*-

import sqlite3
import random
import json

def get_random_element(data_list):
    if data_list:
        return random.choice(data_list)
    return None
class PoemRandom : #��������
    #Ԥ����public����
    def __init__(self):
        self.question=["","","",""]
        self.ans=0
        self.poemlist=[]
    def poemra(self,modes) : #���������ʫ
        conn = sqlite3.connect("poem.db")
        cursor = conn.cursor()
        if modes:
             id=int(get_random_element(self.poemlist))
        else:
             id=random.randint(1,240000)
        cursor.execute("select * from poem where _id="+str(id))
        i=1
        for item in cursor:
            #��ȡԭ��
           return(item[13])
           item[13]
        cursor.close()
        conn.close()
    def broken(self):#���ɻ�����
        str=self.poemra(0)
        parts=str.split(",")
        parts=[item.strip()for part in parts for item in part.split("\n")]#�ָ��ֶ�
        a=random.randint(0,len(parts)-1)
        return parts[a]
    def core (self,modes) :#�������
        str=self.poemra(modes)
        parts=str.split(",")
        parts=[item.strip()for part in parts for item in part.split("\n")]#�ָ��ֶ�
        a=random.randint(0,len(parts)-1)
        self.question[0]=parts[a] # type: ignore #��������
        self.ans=random.randint(1,3)
        for i in range(1,4):#���ɻ�����
            self.question[i]=self.broken() # type: ignore
        if a==len(parts)-1:#���Ǵ�
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

        # ��ȡ��ǰ�ĵ��������ݣ�������ת��Ϊ�б�
        cursor.execute("SELECT poem FROM Users WHERE id = ?", (uid,))
        result = cursor.fetchone()
        current_pids = []
        
        if result and result[0]:
            try:
                current_pids = json.loads(result[0])
            except json.JSONDecodeError:
                pass  # ��� JSON ����ʧ�ܣ�����Ϊ���б�

        # ���µ� pid ��ӵ��б���
        current_pids.append(pid)
        
        # �����º���б�ת��Ϊ JSON �ַ���
        updated_pids_json = json.dumps(current_pids)

        # �������ݿ�
        cursor.execute("UPDATE Users SET poem = ? WHERE id = ?", (updated_pids_json, uid))
        conn.commit()
        conn.close()      
    def get_data_as_list(self, uid):
        conn = self._connect()
        cursor = conn.cursor()

        # �滻 'data_column' Ϊʵ�ʵ�����
        column_name = 'poem'

        # ��ȡ����
        cursor.execute(f"SELECT {column_name} FROM Users WHERE id = ?", (uid,))
        result = cursor.fetchone()
        data_list = []

        if result and result[0]:
            try:
                data_list = json.loads(result[0])
            except json.JSONDecodeError:
                pass  # ��� JSON ����ʧ�ܣ�����Ϊ���б�

        conn.close()
        return data_list   


        

       
        
#����
if __name__=="__main__":

      a=users()
      db = love('user.db')
      db.update_pid(1, '11514')
      poemlist=db.get_data_as_list(1)
      
      
      

    






