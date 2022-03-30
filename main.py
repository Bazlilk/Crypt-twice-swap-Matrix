import random
# Функция преобразования в матрицу длиной n x m

def tomatrx(list,n,m):
    out = []
    len_lst = len(list)
    while len_lst < n*m:
        list.append(" ")
        len_lst = len(list)
    n_0 = 0
    m_0 = n
    for i in range(m):
        out.append(list[n_0:m_0])
        n_0 += n
        m_0 += n
    return out
def crypt(text,key):
    # Текст в строку
    text = list(text)
    # Определяем высоту матрицы
    lenght_key = int(len(text) / len(list(str(key))))
    if len(text) % len(list(str(key))) != 0:
        lenght_key += 1
    key_2 = [i+1 for i in range(lenght_key)]
    random.shuffle(key_2)
    key_2_str = ''
    for i in key_2:
        key_2_str += str(i)
    print("Ваш второй ключ: ", key_2_str)
    # Превращаем строку из текста в матрицу длиной ключа 1 высотой ключа 2
    text = tomatrx(text,len(list(str(key))),lenght_key)
    # Переводим ключи в строки
    key_2 = [int(i) for i in list(key_2)]
    key = [int(i) for i in list(str(key))]
    # Вывод первой итерации
    print("Матрица до расшифровки: \n")
    for i in text:
        print(i)
    result = []
    print("\nИтерация 1: ")
    # меняем столбцы по ключу
    for i in range(len(key_2)):
        a = []
        for j in range(len(key)):
            a.append(text[i][key.index(j+1)])
        result.append(a)
        print(a)
    print("\nИтерация 2: ")
    output = []
    # меняем строки по ключу
    for i in range(len(key_2)):
        print(result[key_2.index(i+1)])
        output.append(result[key_2.index(i+1)])
    print("Зашифрованный текст: ")
    crypt_text = ''
    for i in output:
        for j in i:
            crypt_text += j
    print(crypt_text)
    decrypt(output,key,key_2)


def decrypt(list_crypt, key, key_2):
    print("Расшифровка: ")
    list_1 = []
    # Сначала переставляем строки в обратном порядке
    print("Итрация 1: \n")
    for i in range(len(key_2)):
        print(list_crypt[key_2[i] - 1])
        list_1.append(list_crypt[key_2[i]-1])
    result = []
    # Далее переставляем столбцы так же, в обратном порядке
    print("Итерация 2: \n")
    for i in range(len(key_2)):
        a = []
        # Меняем буквы в порядке ключа
        for j in range(len(key)):
            a.append(list_1[i][key[j]-1])
        result.append(a)
        print(a)
    print("Расшифрованный текст: ")
    decrypt_text = ''
    for i in result:
        for j in i:
            decrypt_text += j
    print(decrypt_text)
    return decrypt_text

