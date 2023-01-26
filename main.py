import mysql.connector
mydb = mysql.connector.connect(host='localhost',user='root',password='rootpass',database ='BANK_MANAGEMENT')

def OpenAcc():
    n = input("Enter the Name :")
    ac= input("Enter the Account No :")
    db = input("Enter the Date of Birth :")
    add = input("Enter the Address :")
    cn = input("Enter the Contact Number :")
    ob= int(input("Enter the Opening Balance :"))
    data1 = (n,ac,db,add,cn,ob)
    data2= (n,ac,ob)
    sql1=('insert into account values (%s,%s,%s,%s,%s,%s)')
    sql2= ('insert into amount values (%s,%s,%s)')
    x=mydb.cursor()
    x.execute(sql1,data1)
    x.execute(sql2,data2)
    mydb.commit()
    print("Data entered Successfully..")
    main()

def DepoAmo():
    amount = input("Enter the amount you want to deposit:")
    ac= input("Enter the Account No :")
    a= 'select balance from amount where AccNo=%s'
    data =(ac,)
    x=mydb.cursor()
    x.execute(a,data)
    result = x.fetchone()
    t=result[0]+amount
    sql=('update amuont set balance where AccNo = %s')
    d=(t,ac)
    x.execute(sql,d)
    mydb.commit()
    main()

def WithdrawAmo():
    amount = input("Enter the amount you want to withdraw:")
    ac = input("Enter the Account No :")
    a = 'select balance from amount where AccNo=%s'
    data = (ac,)
    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    t = result[0] - amount
    sql = ('update amuont set balance where AccNo = %s')
    d = (t, ac)
    x.execute(sql, d)
    mydb.commit()
    main()


def BalEnq ():
    ac = input("Enter the Account No :")
    a = 'select * from amount where AccNo=%s'
    data = (ac,)
    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    print("Balance for account :",ac,"is",result[-1])
    main()

def DisDetails():
    ac = input("Enter the Account No :")
    a = 'select * from amount where AccNo=%s'
    data = (ac,)
    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    for i in result:
        print(i)
    main()


def closeAcc() :
    ac = input("Enter the Account No :")
    sql1= 'delete from account where AccNo=%s'
    sql2 = 'delete from account where AccNo=%s'
    data = (ac,)
    x = mydb.cursor()
    x.execute(sql1, data)
    x.execute(sql2, data)
    mydb.commit()
    main()


def main():
    print('''
            1.OPERN ACCOUNT
            2. DEPOSITE AMOUNT
            3.WITHDRAW AMOUNT
            4.BALANCE ENQUIRY
            5.DISPLAY CUSTOMER DETAILS
            6.CLOSE AN ACCOUNT
            ''');

    choice = input("Enter the task you want to perform :")
    if(choice =='1'):
        OpenAcc();
    elif(choice =='2'):
        DepoAmo();
    elif (choice == '3'):
        WithdrawAmo();
    elif(choice =='4'):
        BalEnq();
    elif(choice =='5'):
        DisDetails();
    elif (choice == '6'):
        closeAcc();
    else :
        print("Invalid Choice")
        main()
main()
