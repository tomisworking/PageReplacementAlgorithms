import matplotlib.pyplot as plt

def draw_mem(data: list, name: str):
    fig, ax1 = plt.subplots()
    ax1.set_title(name)
    ax1.set_ylabel('Błędy stron')
    ax1.violinplot(data)
    plt.show()
