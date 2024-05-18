def encontrar_menor_numero(arr):

    menor_valor = arr[0]
    indice_do_menor_valor = 0

    for i in range(1, len(arr)):
        if arr[i] < menor_valor:
            menor_valor = arr[i]
            indice_do_menor_valor = i

    return indice_do_menor_valor


def ordenacao_por_selecao(arr):
    novoArr = []

    for i in range(len(arr)):
        menor = encontrar_menor_numero(arr)
        novoArr.append(arr.pop(menor))
    return(novoArr)

print(ordenacao_por_selecao([5,2,3,7,9]))
