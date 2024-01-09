class NovaConta:
    
    def __init__(self, parConta):
        self.__conta = parConta

    def depositar(self, parSalario):
        self.__conta += parSalario

    def verSaldo(self):
        return self.__conta

    def sacar(self, parSaque):
        self.__conta = self.__conta - parSaque
        return self.__conta

    


    

