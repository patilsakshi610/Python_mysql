import mysql.connector
from tabulate import tabulate
mydb=mysql.connector.connect(host="localhost" , user="root", passwd="2620")# database="marksheet")
cursor=mydb.cursor()




def create_database():
    try:
        cursor.execute("create database marksheet")
        cursor.execute("use marksheet")
        cursor.execute("create table student_sheet(sr_no integer primary key not null auto_increment ,student_id char(10) , student_name varchar(50), middle_name varchar (50), surname varchar(50), age integer, place varchar (30), percentage double)")
        print('your database is successfully created with table student_marksheet')
    except:
        print("database exist...no need to create it again")



def delete_database():
    try:
        if(isEmpty()==True):
            print("none database created yet")
        ans=input('\nAre you sure you want to delete this database\nIt will delete your all records stored uptill now\n (y/n)')
        if (ans=="y") or (ans=="Y") :
            cursor.execute("drop database marksheet")
            print("your database is successfully deleted\n")
        elif ans=="n" or (ans=="N"):
            print('\nyour database is secure')
        else:
            print("Oops !!! something went wrong ")
    except:
        print("none database created yet")




def isEmpty():
    c=0
    cursor.execute("use marksheet")
    cursor.execute("select * from student_sheet")
    for i in cursor:
        c +=1
    return  c



def table():
    print('\n')
    print('Your Stored Data is : \n')
    cursor.execute("use marksheet")
    cursor.execute("select * from student_sheet")
    mycursor=cursor.fetchall()
    for i in mycursor:
        print(tabulate(mycursor, headers=["sr_no", "name", "middle name", "last name","age","place" ,"percentage"]))




def run():
    try:
        print('\n')
        print('Your Stored Data is : \n')
        cursor.execute("use marksheet")
        cursor.execute("select * from student_sheet")
        mycursor=cursor.fetchall()
        for i in mycursor:
            print('Sr no is : ',i[0])
            print('id is : ',i[1])
            print('name is : ',i[2])
            print('middle name is : ', i[3])
            print('last name is : ', i[4])
            print('age is : ',i[5])
            print('address : ',i[6])
            print('percentage is : ',i[7],'%\n\n')
    except:
        print("oops !!! something went wrong !!!! ")




def delete():
    ans=input('\nAre you sure you want to delete all the stored records \n(y/n)')
    if (ans=="y") or (ans=="Y") :
        cursor.execute("use marksheet")
        cursor.execute("truncate table student_sheet")
        print('all Data is cleared\n')
    elif ans=="n" or (ans=="N"):
        print('\nyour data is safe')
    else:
        print("Oops !!! something went wrong ")




while(True):
    print('\nMenu :')
    print(" 1.Create Database\n 2.Delete Database\n 3.stored data\n 4.display data\n 5.Delete all Data\n 6.exit\n\n")

    choice=int(input('\nenter your choice : '))

    if (choice==1):
        create_database()

    elif (choice==2):
        delete_database()

    elif (choice==3):
        try:
            if(isEmpty()==True):
                print("create databases first")
            else:
                print('\nenter student details : ')
                id=input('student id : ')
                name=input('first name : ')
                mname=input('middle name : ')
                sname=input('last name : ')
                age=int(input('age : '))
                place=input('place name : ')
                total = int(input('total marks of all subjects : '))
                count=int(input('enter number of subjects : '))
                sum=0
                percentage=0.0
                print('enter marks one by one : ')
                for i in range(count):
                    a=int(input())
                    sum= sum + a
                percentage=(sum*100)/total
                cursor.execute("use marksheet")
                sql="insert into student_sheet (student_id , student_name ,middle_name,surname,age,place,percentage )values(%s,%s,%s,%s,%s,%s,%s)"
                val=(id,name,mname,sname,age,place,percentage)
                cursor.execute(sql,val)
                mydb.commit()
        except:
            print("Oops!!!something went wrong")


    elif (choice==4):
        try:
            if (isEmpty() <= 0):
                print('no data yet')
            else:
                ans=input('enter 1 to print data in tabular form else just press enter')
                if(ans=="1"):
                    table()
                else:
                    run()
        except:
            print("none database created\nKindly create it !!!! ")




    elif (choice==5):
        delete()

    elif(choice==6):
        exit()

    elif(choice==7):
        table()

    else:
        print('Oops !!! Invalid choice \n')




