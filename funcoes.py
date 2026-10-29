grid = [
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
  ]

def define_posicoes(linha, coluna, orientacao, tam):
    final = []
    i = 0
    while i < tam:
        grupo = [0] * 2
        if orientacao == 'vertical':
            grupo[0] = linha + i
            grupo[1] = coluna
            i += 1
        elif orientacao == 'horizontal':
            grupo[0] = linha
            grupo[1] = coluna + i
            i += 1
        final.append(grupo)
    
    return final

# linha = int(input("qual a linha? "))
# coluna = int(input("qual a coluna? "))
# orientacao = input("qual a orientação? (horizontal ou vertical)\n ").lower().strip()
# tamanho = int(input("qual o tamanho? "))

# print(define_posicoes(linha, coluna, orientacao, tamanho))
# # deve sair [[2, 4], [3, 4], [4, 4]]

