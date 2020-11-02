from database import *
Dataholder=DataBase("Information.txt")
name1="Andrew"
name2="Andrew2"
password1="123123"
password2="visualstudioisbetter"
email1="arfaulkner@gmail.com"
email2="myTAiscool@mcmaster.ca"
Dataholder.add_user(email1,password1,name1)
Dataholder.add_user(email2,password2,name2)
print(Dataholder.get_user(email1))
print("correct validation info",Dataholder.validate(email1,password1))
print(Dataholder.num_users())
Dataholder.delete_user(email1)
print(Dataholder.get_user(email1))
print("incorrect validation info",Dataholder.validate(email1,password1))
print(Dataholder.num_users())
