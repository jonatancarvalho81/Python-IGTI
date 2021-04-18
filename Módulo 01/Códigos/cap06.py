# Classes em Python:
# Construtores:
# São métodos (funções) de uma classe que começam com '__init__()';
# São chamadas sempre que os objetos são instanciados;
# Normalmente, utilizamos os construtores oara iniciar as variáveis de uma
# classe.

# Construtor de uma classe:
class Carro:
    def __init__(self, cor='vermelho', n_portas=3):
        self.cor_carro = cor
        self.n_portas_carro = n_portas

    def get_cor_carro(self):
        return self.cor_carro

    def get_numero_portas(self):
        return self.n_portas_carro


carro_1 = Carro(cor='azul')
carro_2 = Carro()
carro_3 = Carro(cor='prata')
print(carro_1.get_cor_carro())
print(carro_2.get_cor_carro())
print(carro_3.get_cor_carro())

# O parâmetro 'self':
# Referencia a instâcia corrente do objeto;
# Utilizada para acessar os elementos que pertence a mesma classe;
# A palavra 'self' é uma convenção, não uma palavra-chave em python.

# Modificando valores de atributos das classes:
carro_1 = Carro('preto', 5)
print(f'A cor do carro é {carro_1.get_cor_carro()}.')
print(f'O carro possui {carro_1.get_numero_portas()} portas.')

# Acessando diretamente os atributos:
print(carro_1.cor_carro)

# Modificando atributos:
carro_1.cor_carro = 'verde'
print(carro_1.cor_carro)

# Deletando atributos de um objeto:
carro_1 = Carro('azul', 4)
del carro_1.cor_carro
#print(carro_1.get_cor_carro())

# Deletando o objeto:
del carro_1
#print(carro_1.get_cor_carro())

# Herança:
# Permite reutilizar o código;
# A subclasse ou classe filha, obtém os atríbutos da classe pai;
# A classe filha pode adicionar novos atributos ou funções;
# Para a classe filha não é necessário escrever todo o código da classe pai.

class Formas:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    descricao = 'A forma ainda não foi definida'
    autor = 'Ainda não foi definido um autor para ela.'

    def area(self):
        return self.x * self.y

    def get_perimetro(self):
        return 2 * self.x + 2 * self.y

    def set_descricao(self, texto):
        self.descricao = texto

    def set_nome_autor(self, texto):
        self.autor = texto

    def set_escala(self, escala):
        self.x = self.x * escala
        self.y = self.y * escala


retangulo = Formas(5, 8)
print(retangulo.area())

# Criando uma classe filha ou subclasse:
class Quadrado(Formas):
    def __init__(self, x):
        self.x = x
        self.y = x

    # Definindo novo método:
    def perimetro_quadrado(self):
        return (self.x) * 4


quadrado = Quadrado(3)
print(quadrado.area())

quadrado.set_nome_autor('Jonatan Carvalho')
print(quadrado.autor)

print(quadrado.perimetro_quadrado())

# Outra forma:
class Retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def area(self):
        return self.comprimento * self.largura

    def perimetro(self):
        return 2 * self.comprimento + 2 * self.largura


class Quadrado(Retangulo):
    def __init__(self, comprimento):
        super().__init__(comprimento, comprimento)


quadrado = Quadrado(6)
print(quadrado.area())
print(quadrado.perimetro())

# Criando uma subclasse de uma subclasse:
class Cubo(Quadrado):
    def area_superficie(self):
        area_face = super().area()
        return area_face * 6

    def volume(self):
        area_face = super().area()
        return area_face * self.comprimento


cubo = Cubo(4)
print(cubo.area_superficie())
print(cubo.volume())

# Verificando as heranças:
print(issubclass(Cubo, Retangulo))
print(issubclass(Cubo, Quadrado))
print(issubclass(Cubo, Formas))

# Verificando instâncias:
print(isinstance(cubo, Cubo))
print(isinstance(cubo, Quadrado))
print(isinstance(cubo, Retangulo))
print(isinstance(cubo, Formas))

# Polimorfismo:
# Um método possui várias versões sobre ele;
class Retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def area(self):
        return self.comprimento * self.largura

    def perimetro(self):
        return 2 * self.comprimento + 2 * self.largura


class Quadrado(Retangulo):
    def __init__(self, comprimento):
        super().__init__(comprimento, comprimento)

    # Polimorfismo:
    def area(self):
        return self.comprimento * self.comprimento

    def perimetro(self):
        return self.comprimento * 4


retangulo = Retangulo(4, 5)
quadrado = Quadrado(5)
print(retangulo.area())
print(retangulo.perimetro())
print(quadrado.area())
print(quadrado.perimetro())
