# Construtores:
# Criando uma classe:
class Carro:
    # Método construtor, tudo que em comum entre os objetos
    def __init__(self, numero_portas, preco):
        self.numero_portas = numero_portas
        self.preco = preco
        print('Objeto carro instanciado com sucesso!')

    def get_numero_portas(self):
        return self.numero_portas


# Instanciando objeto:
carro_1 = Carro(4, 50000)
print(f'Meu carro possui {carro_1.get_numero_portas()} porta(s).')

carro_2 = Carro(2, 80000)
print(f'Meu carro possui {carro_2.get_numero_portas()} porta(s).')

# Métodos acessores e modificadores:
# Getters (Métodos Acessores)
# Setters (Métodos Modificadores)
class Carro:
    # Método construtor, tudo que em comum entre os objetos
    def __init__(self, numero_portas, preco):
        self.numero_portas = numero_portas
        self.preco = preco
        print('Objeto carro instanciado com sucesso!')

    def get_numero_portas(self):
        return self.numero_portas

    def set_numero_portas(self, novo_numero_portas):
        self.numero_portas = novo_numero_portas


carro_3 = Carro(4, 50000)
print(f'Número de portas antes: {carro_3.get_numero_portas()}')
carro_3.set_numero_portas(2)
print(f'Novo número de portas: {carro_3.get_numero_portas()}')

carro_4 = carro_3
print(f'Número de portas: {carro_4.get_numero_portas()}')
carro_4.set_numero_portas(3)
print(f'Novo número de portas: {carro_4.get_numero_portas()}')
print(f'Número de porttas: {carro_3.get_numero_portas()}')
# Os dois objetos apontam para o mesmo local na mémoria, mudando um o outro
# também muda.
