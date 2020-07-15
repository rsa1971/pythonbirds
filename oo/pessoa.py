class Pessoa:
    olhos = 3
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome=None
        self.filhos=list(filhos)
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')
    luciano = Pessoa(renzo, nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome='Ramalho'
    del luciano.filhos
    luciano.olhos=1
    del luciano.olhos
    print(luciano.__dict__)
    print(renzo.__dict__)
    print(Pessoa.olhos)
    print(renzo.olhos)
    print(luciano.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(renzo.olhos))


