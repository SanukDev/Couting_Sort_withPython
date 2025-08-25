import random


arr = [random.randint(1, 50) for _ in range(100)]
# arr = [1,4,1,2,7,1,5,23,12,2,34,1,2,0,2]

print('ARRAY COM OS VALORES')
print(arr)
num_de_passos = 0
# checking the max
max_var = 0
num = 0
for i in arr:
    num_de_passos += 1
    if i > num:
        max_var = i
        num = i
print('Numero do range:')
print(max_var)
max_var +=1
# add 0 in the positions arr
arr_c = [0] * max_var
print('array c com as posicoes em 0')
print(arr_c)

# Add positions the num in arr
for i in arr:
    arr_c[i] += 1
    num_de_passos += 1
# for i in range(len(arr)):
#     for j in range(len(arr_c)):
#         num_de_passos += 1
#         if arr[i] == j:
#             arr_c[j] += 1

    print("Adicionando quantos valores exitesm de acordo com a posição do array C")
    print(arr_c)
print('array c com as posicoes em ja   populadas')
print(arr_c)

# Checking the positions
for i in range(len(arr_c)-1):
    num_de_passos += 1
    print("Adicionando a posição de cada dado em array C")
    print(arr_c)
    arr_c[i+1] = arr_c[i] + arr_c[1+i]



# Creating a arr with real positions
arr_b = [0] * len(arr)


for i in range(len(arr)-1, -1, -1):
    index_c = arr[i]
    index_b = arr_c[index_c]
    arr_b[index_b-1] = arr[i]
    arr_c[index_c] = arr_c[index_c] - 1
    num_de_passos += 1
    print('Colocando cada dado em sua devida posicao')
    print(arr_b)

print(f'\n\nESSE FOI O NÚMERO TOTAL DE PASSOS DADOS: {num_de_passos}')
