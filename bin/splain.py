
#Escritp por SrRiuz :)

class splain (object):

    WordKeysList = []
    ListKeysGenerate = []

    def __init__ (self , wordKeys , fileName='none' , formatNameFile='txt' , email='undefine'):
        self.fileName = fileName
        self.Email = email
        self.fileFormat = formatNameFile
        self.AddWordKeys(wordKeys)
        self.GenerateKeys()
        print('\n')
        #self.CreateFileKeys(splain.ListKeysGenerate)

    def AddWordKeys (self , wordNumber):
        try:
            if int(wordNumber) > 0:
                for number in range(0 , int(wordNumber)):
                    splain.WordKeysList.append(str(input('Palabra clave : ')))
                print(splain.WordKeysList)
            else:
                print('[ERROR] >> El numero tiene que ser mayor que 0')
        except ValueError:
            print("[ERROR] >> El valor '{}' no es un numero valido...".format(wordNumber))

    def getWordKeysList (self):
        return splain().WordKeysList

    def GenerateKeys (self):
        counter = 0
        for item in range(0 , len(splain.WordKeysList)):
            for item_y in range(0 , len(splain.WordKeysList)):
                counter = counter + 1
                keyGenerate = '{}{}'.format(splain.WordKeysList[item] , splain.WordKeysList[item_y])
                splain.ListKeysGenerate.append(keyGenerate)
                print("[{}] >> Se ha generado : '{}'".format(counter , keyGenerate))

    def CreateFileKeys (self , listKeys):
        try:
            file = open('{}.{}'.format(self.fileName , self.fileFormat) , 'w')
            for keyPosition in range(0 , len(listKeys)):
                file.write('{}\n'.format(listKeys[keyPosition]))
            file.close()
            print('Se a creado un nuevo diccionario {}.{}'.format(self.fileName , self.fileFormat))
        except OSError:
            print('[ERROR] >> No se a podido crear el archivo porque el nombre no es valido ...')

        except Exception:
            print('[ERROR] >> No se a podido crear ...')

    def getKeysGenerator (self):
        return self.ListKeysGenerate


    def getEmail (self):
        return self.Email


