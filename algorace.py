from funcforThird.boer import boyer_moore_search
from funcforThird.kmp import kmp_search
from funcforThird.jew import rabin_karp_search
import timeit
import requests

data1ID = "18_R5vEQ3eDuy2VdV3K5Lu-R-B-adxXZh"
data2ID = "18BfXyQcmuinEI_8KDSnQm4bLx6yIFS_w"

data1 = requests.get(
    f"https://drive.google.com/uc?export=download&id={data1ID}"
).content.decode("windows-1251")
data2 = requests.get(
    f"https://drive.google.com/uc?export=download&id={data2ID}"
).content.decode("UTF-8")

print(
    f"Перший текст з існуючим словом: \nРабіна-Карпа: {timeit.timeit(lambda: rabin_karp_search(data1, 'виключно'), number=100)}\n Кнута-Морріса-Пратта:{timeit.timeit(lambda: kmp_search(data1, 'виключно'), number=100)}  \nБоєра-Мура: {timeit.timeit(lambda: boyer_moore_search(data1, 'виключно'), number=100)}\n"
)
print(
    f"Перший текст з неіснуючим словом: \nРабіна-Карпа: {timeit.timeit(lambda: rabin_karp_search(data1, 'aboba'), number=100)}\n Кнута-Морріса-Пратта:{timeit.timeit(lambda: kmp_search(data1, 'aboba'), number=100)}  \nБоєра-Мура: {timeit.timeit(lambda: boyer_moore_search(data1, 'aboba'), number=100)}\n"
)
print(
    f"Другий текст з існуючим словом: \nРабіна-Карпа: {timeit.timeit(lambda: rabin_karp_search(data2, 'B+-дерево'), number=100)}\n Кнута-Морріса-Пратта:{timeit.timeit(lambda: kmp_search(data2, 'B+-дерево'), number=100)}  \nБоєра-Мура: {timeit.timeit(lambda: boyer_moore_search(data2, 'B+-дерево'), number=100)}\n"
)
print(
    f"Другий текст з неіснуючим словом: \nРабіна-Карпа: {timeit.timeit(lambda: rabin_karp_search(data2, 'aboba'), number=100)}\n Кнута-Морріса-Пратта:{timeit.timeit(lambda: kmp_search(data2, 'aboba'), number=100)}  \nБоєра-Мура: {timeit.timeit(lambda: boyer_moore_search(data2, 'aboba'), number=100)}\n"
)
