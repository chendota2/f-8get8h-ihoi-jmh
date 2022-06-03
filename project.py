import json
import urllib.request
import webbrowser
import os
try:

#python IP-icker.py

# '\033[93m' - желтый
# 
#
#

    R='\033[91m'
    Y='\033[93m'
    G='\033[92m'
    CY='\033[96m'
    W='\033[97m'
     
    def start():
     
       
        try:
            print(R+"""\n
🙈 🙉 🙊"""+Y+""" Выберите вариант: """+Y+"""🙈 🙉 🙊

1)"""+G+""" Посмотреть информацию о вашем IP"""+Y+"""
2)"""+G+""" Посмотреть информацию о IP другого человека"""+Y+"""
3)"""+G+""" Выйти
""")
            ch=int(input(CY+"Введите цифру: "+W))
            if ch==1:
                main2()
                
            elif ch==2:
                main()
                
            elif ch==3:
                print(Y+"Выход................"+W)
            else:
                print(R+"\nНеизвестная команда\n")
               
        except ValueError:
            print(R+"\nНеизвестная команда\n")
        
        
    def finder(u):
        try:
            try:
                response = urllib.request.urlopen(u)
                data = json.load(response)
                ip=data['query']
                org=data['org']
                c=data['city']
                cont=data['country']
                reg=data['regionName']
                latt=data['lat']
                lonp=data['lon']

                print(R+"\n====================================================")
                print(G+"1) IP-адрес : "+Y,ip,'\n')
                print(G+"2) Провайдер : "+Y,org,'\n')
                print(G+"3) Город : "+Y,c,'\n')
                print(G+"4) Область : "+Y,reg,'\n')
                print(G+"5) Страна : "+Y,cont,'\n')
                print(G+"6) Координаты\n")
                print(G+"\tШирота : "+Y,latt,'\n')
                print(G+"\tДолгота : "+Y,lonp,'\n')
                l='https://www.google.com/maps/place/'+str(latt)+'+'+str(lonp)
                print(R+"\n⚡"+Y+" Ссылка Google-maps : "+CY,l)
                path=False
                if path:
                    link='am start -a android.intent.action.VIEW -d '+str(l)
                    pr=input(R+"\n⚡"+Y+" Открыть в браузере?"+G+" (да|нет): "+W)
                    if pr=="да":
                        lnk=str(link)+" > /dev/null"
                        os.system(str(lnk))
                        start()
                       
                    elif pr=="нет":
                        print("\nПродолжить работу или выйти Ctrl + C\n\n")
                        start()
                        
                    else:
                        print("\nХорошо\n")
                        
                else:
                    pr=input(R+"\n⚡"+Y+" Открыть в браузере?"+G+" (да|нет): "+W)
                    if pr=="да":
                        webbrowser.open(l,new=0)
                        start()
                      
                    elif pr=="n":
                        print(R+"\n==================================================")
                        print(Y+"\nПродолжить работу или выйти Ctrl + C "+R+"Ctrl + C\n\n")
                        start()
                       
                    else:
                        print(R+"\nХорошо\n")
                       
                return
            except KeyError:
                print(R+"\nНеверный IP-адрес\n"+W)
                
        except urllib.error.URLError:
            print(R+"\nError!"+Y+" проверьте подключение к интернету\n"+W)
            exit()

        
    def main():
        u=input(G+"\n>>> "+Y+"Введите IP-адрес:"+W+" ")
        if u=="":
            print(R+"\nВведите IP-адрес!")
            main()
        else:
            url ='http://ip-api.com/json/'+u
            finder(url)
    def main2():
        url ='http://ip-api.com/json/'
        finder(url)
        
    start()
   
except KeyboardInterrupt:
    print(Y+"\nХорошего дня"+W)


      