# Definir a estrutura das lacunas como um dicionário em Python
class BestChoice:
    def __init__(self, start=0, end=0, total=0):
        self.start = start
        self.end = end
        self.total = total

# Função Worst-Fit em Python
def worst_fit(memory, space, total_space):
    bc = []  # lista para armazenar as lacunas
    valid = False  # flag para indicar uma lacuna válida
    size_bc = 0  # tamanho do vetor que armazena as lacunas
    bigger = -1  # variável usada para armazenar o início da maior lacuna

    # Encontrar lacunas livres na memória
    for i in range(total_space):
        if memory[i] == 0:  # se a posição está livre
            if not valid:
                bc.append(BestChoice(start=i))  # início da lacuna
            valid = True
        else:  # se a posição está ocupada
            if valid:
                bc[size_bc].end = i  # fim da lacuna
                bc[size_bc].total = bc[size_bc].end - bc[size_bc].start
                size_bc += 1
            valid = False

    # Procurar pela maior lacuna
    valid = False
    for i in range(size_bc):
        if bc[i].total >= space:  # encontrar maior lacuna com espaço suficiente
            if bc[i].total > bigger:
                bigger = bc[i].start  # atualiza com o início da maior lacuna
                valid = True

    # Alocar memória se encontrou uma lacuna válida
    if valid:
        print(f"\nPosição: {bigger}")
        for i in range(bigger, bigger + space):
            memory[i] = 1  # marcar a lacuna como ocupada
        print("\n************ Espaço alocado com SUCESSO **************")
    else:
        # Se não encontrou espaço suficiente
        print("\n************ Espaço insuficiente **************")


# Função principal para testar a heurística
def main():
    # Definir a memória e seu tamanho
    total_space = 10  # tamanho total da memória
    memory = [0, 1, 0, 0, 1, 0, 0, 0, 1, 0]  # memória simulada (0 = livre, 1 = ocupada)

    # Mostrar estado inicial da memória
    print("Memória inicial:")
    print(memory)

    # Tamanho do bloco de memória que você quer alocar
    space_to_allocate = 3

    # Chamar a função Worst-Fit para alocar memória
    worst_fit(memory, space_to_allocate, total_space)

    # Mostrar estado final da memória após a alocação
    print("\nMemória após alocação:")
    print(memory)


if __name__ == "__main__":
    main()
