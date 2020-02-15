import os
os.system ('cls' or 'clear')



class color :
    GREEN = '\33[92m'
    RED = '\033[91m'
    V = '\033[94m'
    S = '\033[90m'

print (color.GREEN + "__________________________________________________________________");
print ("");
print (color.GREEN + "           answer = yes or no  |    Machine Learning Group      ");
print (color.GREEN + "__________________________________________________________________");
print ("");
print ("");
print (color.GREEN + '| A.H.BAHRAMI'); print ("-------------"); 
print (color.RED + "| M.ZAFARI"); print ("------------");
print (color.RED + "| M.Z.RAFIEE"); print ("------------"); 
print (color.RED + "| M.NEZAKATI"); print ("-------------"); 
print (color.S + "| M.ABADI");print ("-------------");  


s1 = (color.V + "Aya Az Zendegi Khod Razi Hastid : ");
ss = input(str(s1));

if (ss == "no" or ss == "yes"):
    s2 = (color.V + "Aya Tabehal Dast Be Khodkoshi Zadid : ");
    ss2 = input(str(s2));


if (ss == "no" or ss2 == "no"):
    s3 = (color.V + "Ziad Asabani Mishavid : ");
    ss3 = input(str(s3));


if(ss == "no" and ss2 == "yes"):
        print (color.RED + "Shoma Afsordeh Hastid");


if(ss == "yes" and ss2 == "no"):
        print (color.GREEN + "Shoma Afsordeh Nistid");
if(ss == "no" and ss2 == "no" and ss3 == "yes"):
        print (color.RED + "Shoma Afsordeh Hastid");
if(ss == "no" and ss2 == "no" and ss3 == "no"):
        print (color.V + "   :| Shoma Afsordeh Nistid   ");

else:
    print ('...');



print (color.V + "ML PYTHON 3");
quit = input();