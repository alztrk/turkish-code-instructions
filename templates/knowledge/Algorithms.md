# Algoritmalar Bilgi Referansi

## Genel Bakis

Algoritma, bir problemi cozmek icin tanimlanan adim adim, sonlu islem dizisidir. "Algoritma" kelimesi 9. yuzyilda yasamis Pers matematikci Harezmi'den (Al-Khwarizmi) gelir. Algoritmalar her programlama dilinden bagimsiz, verimli kod ve problem cozme becerisi icin temel bir kavramdir.

Dogru algoritma secimi: Time complexity (zaman karmasikligi), space complexity (bellek karmasikligi), girdi buyuklugu ve veri yapisina baglidir. Algoritma bilgisi yazilim mulakatlarinin (FAANG, FAANG benzeri) en onemli konusudur. LeetCode, HackerRank, Codeforces gibi platformlarda algoritma yetenekleri olculur. Big-O notasyonu ile analiz edilir.

## Temel Veri Yapilari

```python
# --- Dizi (Array / List) ---
# O(1) erisim, O(n) ekleme/silme
dizi = [3, 1, 4, 1, 5, 9, 2, 6]
dizi.append(7)           # O(1) amortized
dizi.insert(0, 0)        # O(n)
dizi.pop()               # O(1)
dizi.pop(0)              # O(n)
dizi.sort()              # O(n log n)

# --- Bagli Liste (Linked List) ---
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def listeyi_olustur(degerler):
    dummy = ListNode()
    current = dummy
    for v in degerler:
        current.next = ListNode(v)
        current = current.next
    return dummy.next

def listeyi_yazdir(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# --- Yigin (Stack - LIFO) ---
# Python'da list ile implemente edilir
yigin = []
yigin.append(1)           # push
yigin.append(2)
yigin.append(3)
print(yigin.pop())         # 3 (pop)
print(yigin[-1])           # 2 (peek)
print(len(yigin) == 0)     # isEmpty

# --- Kuyruk (Queue - FIFO) ---
from collections import deque
kuyruk = deque()
kuyruk.append(1)           # enqueue
kuyruk.append(2)
kuyruk.append(3)
print(kuyruk.popleft())    # 1 (dequeue)
print(kuyruk[0])           # 2 (peek)

# --- Hash Map (Sozluk) ---
# O(1) ortalama erisim/ekleme/silme
hash_map = {}
hash_map["anahtar"] = "deger"
hash_map.get("anahtar", "varsayilan")
hash_map.keys()
hash_map.values()
hash_map.items()
for k, v in hash_map.items():
    print(f"{k}: {v}")

# --- Hash Set (Kume) ---
kume = {1, 2, 3, 4, 5}
kume.add(6)
kume.remove(1)
print(3 in kume)           # True (O(1))
print(kume & {2, 3})       # intersection
print(kume | {7, 8})       # union
print(kume - {2, 3})       # difference

# --- Heap (Oncelik Kuyrugu) ---
import heapq
heap = []
heapq.heappush(heap, 3)    # en kucuk basta
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
print(heapq.heappop(heap))  # 1 (en kucuk)
print(heap[0])              # 2 (peek)

# Max heap icin negatif deger kullan
max_heap = []
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -2)
print(-heapq.heappop(max_heap))  # 3

# --- Graph (Komsuluk Listesi) ---
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}

# --- Trie (On Ek Agaci) ---
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
```

## Temel Algoritmalar

### Arama Algoritmalari

```python
def linear_search(arr, target):           # O(n)
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

def binary_search(arr, target):           # O(log n) - Sadece sirali dizilerde
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Binary search recursive
def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# Lower bound / Upper bound (C++ lower_bound/upper_bound)
import bisect
arr = [1, 2, 3, 3, 3, 4, 5]
print(bisect.bisect_left(arr, 3))   # 2 (ilk 3)
print(bisect.bisect_right(arr, 3))  # 5 (son 3 + 1)
```

### Siralama Algoritmalari

```python
# --- Bubble Sort (O(n^2)) ---
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# --- Selection Sort (O(n^2)) ---
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# --- Insertion Sort (O(n^2)) ---
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# --- Merge Sort (O(n log n)) ---
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# --- Quick Sort (ortalama O(n log n)) ---
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Quick Sort in-place (daha verimli)
def quick_sort_inplace(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_inplace(arr, low, pi - 1)
        quick_sort_inplace(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# --- Heap Sort (O(n log n)) ---
import heapq
def heap_sort(arr):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]
```

### Graf Algoritmalari

```python
from collections import deque

# --- Depth-First Search (DFS) - O(V+E) ---
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited

# DFS iterative
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node, end=" ")
            stack.extend(reversed(graph[node]))
    return visited

# --- Breadth-First Search (BFS) - O(V+E) ---
def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited

# --- Dijkstra (En Kisa Yol) - O(E log V) ---
import heapq
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_dist, current = heapq.heappop(pq)
        if current_dist > distances[current]:
            continue
        for neighbor, weight in graph[current].items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances

# Ornek graf (agirlikli)
weighted_graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8},
    'D': {'B': 5, 'C': 8},
}

# --- Union-Find (Disjoint Set Union) ---
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        return True

# --- Topological Sort ---
def topological_sort(graph):
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] = in_degree.get(neighbor, 0) + 1

    queue = deque([node for node in graph if in_degree[node] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return result if len(result) == len(graph) else []
```

### Dinamik Programlama

```python
# --- Fibonacci (DP ile) ---
def fibonacci(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# Fibonacci O(1) space
def fibonacci_optimized(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# --- 0/1 Knapsack (Sirt Cantasi) ---
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacity]

# 1D Knapsack (optimize)
def knapsack_1d(weights, values, capacity):
    dp = [0] * (capacity + 1)
    for i in range(len(weights)):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])
    return dp[capacity]

# --- Longest Common Subsequence (LCS) ---
def lcs(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]

# --- Longest Increasing Subsequence (LIS) ---
def lis(arr):
    import bisect
    tails = []
    for x in arr:
        i = bisect.bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)
```

## Karmasiklik Analizi (Big-O)

| Notasyon | Isim | Ornek |
|----------|------|-------|
| O(1) | Sabit | Dizi erisimi, hash lookup |
| O(log n) | Logaritmik | Binary search |
| O(n) | Dogrusal | Linear search, dizi traversal |
| O(n log n) | Linearithmic | Merge sort, Quick sort (ortalama) |
| O(n^2) | Karesel | Bubble sort, nested loop |
| O(2^n) | Ustel | Fibonacci recursive, subset problems |
| O(n!) | Faktoriyel | Permutation problems |

```python
import time

def olc(func, *args):
    start = time.time()
    result = func(*args)
    return result, time.time() - start
```

## Yaygin Algoritma Turleri

1. **Siralama Algoritmalari**: Merge Sort (O(n log n), stable), Quick Sort, Heap Sort, Counting Sort (O(n+k), integer)
2. **Arama Algoritmalari**: Binary Search, DFS, BFS, Ternary Search, Jump Search
3. **Dinamik Programlama**: Fibonacci, Knapsack, LCS, LIS, Edit Distance, Matrix Chain, Bellman-Ford
4. **Greedy Algoritmalar**: Dijkstra, Huffman Coding, Activity Selection, Kruskal/Prim (MST), Coin Change (bazi)
5. **Graf Algoritmalari**: Dijkstra, Bellman-Ford (negative edges), Floyd-Warshall (all pairs), Kruskal/Prim (MST), Union-Find
6. **String Algoritmalari**: KMP (string matching), Rabin-Karp (hashing based), Levenshtein Distance, Z-Algorithm, Manacher (palindrome)
7. **Divide and Conquer**: Merge Sort, Quick Sort, Binary Search, Strassen (matrix multiplication)
8. **Backtracking**: N-Queens, Sudoku Solver, Subset Sum, Permutations
9. **Two Pointers**: Rain Water Trapping, Container with Most Water, 3Sum
10. **Sliding Window**: Maximum subarray sum, Longest substring without repeating characters
11. **Bit Manipulation**: XOR tricks, `x & (x-1)` (clear lowest set bit), power of two check

```python
# Sliding Window ornegi
def max_subarray_sum(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum

# Two Pointers - 3Sum
def three_sum(nums):
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0: left += 1
            elif total > 0: right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]: left += 1
                while left < right and nums[right] == nums[right - 1]: right -= 1
                left += 1; right -= 1
    return result
```

## Yaygin Hatalar

1. **Time complexity hesaplamamak**: Buyuk girdilerde algoritmanin calisma suresini ongorememek
2. **Off-by-one (sinir kosullari)**: Dizi indeksleri, dongu sinirlarinda yanlis karsilastirma (`<=` vs `<`)
3. **Recursive base case unutmak**: Stack overflow (infinite recursion)
4. **Greedy her zaman optimal degildir**: Coin Change, Traveling Salesman gibi problemlerde greedy cozum bazen optimal degil
5. **Mutation problemleri**: Referans kopyalama vs deep copy karistirmak
6. **Integer overflow**: Buyuk sayilarda (ozellikle factorial/DP) overflow'a dikkat
7. **Input validation yapmamak**: Gecersiz girdilerde hata
8. **Cache kullanmamak (DP memoization)**: Ayni alt problemi tekrar tekrar cozmek
9. **Graph'te visited kontrolu yapmamak**: Sonsuz dongu (cycle)
10. **Edge case'leri unutmak**: Bos dizi, tek eleman, buyuk sayi, negatif deger
11. **Hash collision farkinda olmamak**: Worst case O(n) performans
12. **Stack vs heap memory**: Recursive cagrilarda stack overflow riski

## Performans Ipuclari

1. **Dogru veri yapisi secimi**: Hash set O(1) arama vs list O(n), heap O(log n) min/max
2. **Space-time tradeoff**: Daha fazla bellek kullanarak zamandan kazanma (DP tabulation)
3. **Erken cikis (early termination)**: Kosul saglaninca donguden cikma
4. **Memoization kullanmak**: Tekrarlanan hesaplamalari cacheleme
5. **Tail recursion optimization**: Recursive fonksiyonlarda tail call optimization
6. **Array yerine bitset kullanmak**: Boolean dizilerini bit olarak temsil
7. **Lazy evaluation**: Ihtiyac aninda hesaplama (generator)

```python
# Early termination
def has_pair_sum(arr, target):
    seen = set()
    for num in arr:
        if target - num in seen:
            return True  # erken cikis
        seen.add(num)
    return False

# Bitset ornegi (bool listesi yerine bit)
primes = 0b1010100  # 2, 3, 5, 7 prime
print(bin(primes))
```

## Kaynaklar

**Kitaplar**:
- Introduction to Algorithms (CLRS) - Algoritmalarin Incili
- Grokking Algorithms (Aditya Bhargava) - Gorsel anlatim
- Cracking the Coding Interview (Gayle Laakmann McDowell)
- Algorithm Design Manual (Steven Skiena)
- The Art of Computer Programming (Donald Knuth)

**Web Siteleri**:
- geeksforgeeks.org - Kapsamli algoritma aciklamalari
- visualgo.net - Gorsel algoritma animasyonlari
- algorithm-visualizer.org - Interaktif gorsellestirme
- bigocheatsheet.com - Complexity tablolari

**Problem Cozme Platformlari**:
- leetcode.com - En populer mulakat platformu
- hackerrank.com - Kategori bazli problemler
- codewars.com - Seviyeli challenge'lar
- codeforces.com - Online yarismalar
- atcoder.jp - Japon yarisma platformu
- projecteuler.net - Matematiksel problemler
- adventofcode.com - Yillik kod takvimi

**Interaktif Ogrenme**:
- exercism.org/tracks/python (algoritma kategorisi)
- algodaily.com
- interviewcake.com

**Topluluk**: reddit.com/r/algorithms, Stack Overflow, LeetCode Discord/Forum, Codeforces toplulugu
