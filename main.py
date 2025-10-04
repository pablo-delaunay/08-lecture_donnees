#### Imports et définition des variables globales

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    l = []

    with open(filename, mode="r", encoding="utf8") as file:
        lines = file.readlines()
    for line in lines:
        line = line.strip() 
        str_values = line.split(';')  
        int_values = [int(x) for x in str_values] 
        l.append(int_values)

    return l

def get_list_k(l, k):
    return l[k]

def get_first(l):
    return l[0]

def get_last(l):
    return l[-1]

def get_max(l):
    return max(l)

def get_min(l):
    return min(l)

def get_sum(l):
    return sum(l)


#### Fonction principale


def main():
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    l_k = get_list_k(data, k)
    print(f"\nListe {k} :", l_k)
    print("Premier :", get_first(l_k))
    print("Dernier :", get_last(l_k))
    print("Max :", get_max(l_k))
    print("Min :", get_min(l_k))
    print("Somme :", get_sum(l_k))
    


if __name__ == "__main__":
    main()
