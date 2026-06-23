# Algoritmalar Bilgi Referansi

## Genel Bakis
Algoritma, problemi cozmek icin adim adim tanimlanan islem dizisidir. Her programlama dilinden bagimsiz, verimli kod ve problem cozme icin temeldir.

## Temel Veri Yapilari

```python
dizi = [3, 1, 4, 1, 5]; dizi.sort()
yigin = []; yigin.append(1); yigin.pop()        # LIFO
from collections import deque
kuyruk = deque(); kuyruk.append(1); kuyruk.popleft()  # FIFO
map = {"anahtar": "deger"}
kume = {1, 2, 3}
```

## Temel Algoritmalar

```python
def binary_search(arr, hedef):           # O(log n)
    sol, sag = 0, len(arr)-1
    while sol <= sag:
        orta = (sol + sag) // 2
        if arr[orta] == hedef: return orta
        elif arr[orta] < hedef: sol = orta + 1
        else: sag = orta - 1
    return -1

def dfs(graph, node, visited=set()):     # O(V+E)
    if node in visited: return
    visited.add(node)
    for komsu in graph[node]: dfs(graph, komsu, visited)

def bfs(graph, baslangic):                # O(V+E)
    visited, queue = {baslangic}, deque([baslangic])
    while queue:
        node = queue.popleft()
        for komsu in graph[node]:
            if komsu not in visited:
                visited.add(komsu); queue.append(komsu)
```

## Karmasiklik Analizi

- **O(1)**: Sabit -- **O(log n)**: Logaritmik -- **O(n)**: Dogrusal
- **O(n log n)**: Merge/Quick sort -- **O(n^2)**: Ic ice dongu
- **O(2^n)**: Ustel (kacin)

## Yaygin Algoritma Turleri

- **Siralama**: Merge Sort, Quick Sort, Insertion Sort
- **Arama**: Binary Search, DFS, BFS
- **Dinamik Programlama**: Fibonacci, Knapsack, LCS
- **Greedy**: Dijkstra, Huffman Coding
- **Graf**: Dijkstra, Union-Find, Topological Sort
- **String**: KMP, Levenshtein Distance

## Yaygin Hatalar

- Time complexity hesaplamamak
- Off-by-one (sinir kosullari)
- Recursive'de base case unutmak (stack overflow)
- Greedy algoritmanin her zaman optimal olmadigini unutmak
- Mutation problemleri (referans kopyalama)
