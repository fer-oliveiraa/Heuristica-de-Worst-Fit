# Decorator de cálculo de tempo gasto
gasto = {}

def tempo_gastado(func):
    import time
    
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()  # Começa a contagem do tempo
        result = func(*args, **kwargs)  # Chama a função decorada
        fim = time.perf_counter()  # Para a contagem do tempo

        if func.__name__ not in gasto:
            gasto[func.__name__] = {'tempo': []} 

        gasto[func.__name__]['tempo'].append(fim - inicio)
        return result 
    return wrapper

# Função para gerar a memória simulada
def gerar_memoria(tamanho):
    import random
    return [random.choice([0, 1]) for _ in range(tamanho)]

# Definir a estrutura das lacunas como um dicionário em Python
class BestChoice:
    def __init__(self, start=0, end=0, total=0):
        self.start = start
        self.end = end
        self.total = total

# Função Worst-Fit em Python
@tempo_gastado
def worst_fit(memory, space, total_space):
    #print("\n--- Método Worst Fit ---")
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
        #print(f"\nPosição: {bigger}")
        for i in range(bigger, bigger + space):
            memory[i] = 1  # marcar a lacuna como ocupada
        #print("\n************ Espaço alocado com SUCESSO **************")
    #else:
        # Se não encontrou espaço suficiente
        #print("\n************ Espaço insuficiente **************")


# Função que implementa o método por força bruta
@tempo_gastado
def brute_force_fit(memory, space, total_space):
    #print("\n--- Método por Força Bruta ---")
    for i in range(total_space - space + 1):  # Itera sobre todas as posições possíveis
        if all(memory[j] == 0 for j in range(i, i + space)):  # Verifica se o bloco é contínuo e livre
            #print(f"\nPosição: {i}")
            for j in range(i, i + space):
                memory[j] = 1  # Marca o bloco como ocupado
            #print("\n************ Espaço alocado com SUCESSO **************")
            return

    # Se não encontrou espaço suficiente
    #print("\n************ Espaço insuficiente **************")

def gerarGrafico(total_space, gasto):
    import os
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()

    if 'worst_fit' in gasto:
        ax.plot(range(1, total_space + 1), gasto['worst_fit']['tempo'], marker='o', label='Worst Fit', color='blue')

    if 'brute_force_fit' in gasto:
        ax.plot(range(1, total_space + 1), gasto['brute_force_fit']['tempo'], marker='o', label='Brute Force Fit', color='orange')

    ax.set_title('Comparação de Eficiência entre Algoritmos')
    ax.set_xlabel('Iterações')
    ax.set_ylabel('Tempo Gasto (segundos)')

    ax.legend()
    ax.grid(True)

    output_path = os.path.join(os.path.dirname(__file__), 'grafico_custo_algoritmos2.png')
    fig.savefig(output_path)
    print(f"Gráfico salvo em: {output_path}")

if __name__ == "__main__":
    import tqdm
    import random
    # Definir a memória e seu tamanho
    total_space = 100  # tamanho total da memória

    for space in tqdm.tqdm(range(1, total_space + 1)):
        memory = gerar_memoria(total_space)  # Gerar memória simulada

        #print("Memória inicial:")
        #print(memory)

        space_to_allocate = random.randint(1, total_space // 2)

        worst_fit(memory, space_to_allocate, total_space)
        #print("\nMemória após alocação:")
        #print(memory)

        memory = gerar_memoria(total_space)  # Gerar nova memória simulada
        brute_force_fit(memory, space_to_allocate, total_space)

        #print("\nMemória após alocação:")
        #print(memory)

    gerarGrafico(total_space, gasto)
