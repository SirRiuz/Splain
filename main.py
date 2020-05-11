
from bin.splain import splain
from bin.fb_login import login_


print('''


   _____       _       _       
  /  ___|     | |     (_)      
  \ `--. _ __ | | __ _ _ _ __  
   `--. \ '_ \| |/ _` | | '_ \ 
  /\__/ / |_) | | (_| | | | | |
  \____/| .__/|_|\__,_|_|_| |_|
        | |                    
        |_|                    



        .::GitHub:https://github.com/SirRiuz::.
        .::Facebook:https://www.facebook.com/profile.php?id=100008598818256::.

''')

objeto = splain(email=str(input('Correo o Id : ')) , wordKeys=str(input('Numero de palabras claves : ')) , formatNameFile='txt')
login_(objeto.getEmail() , objeto.getKeysGenerator())

