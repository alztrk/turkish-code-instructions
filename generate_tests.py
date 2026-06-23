import json, random, textwrap
random.seed(42)

entries = []

def T(code, test, lang):
    entries.append({
        "instruction": f"Asagidaki fonksiyon icin unit test yaz:\n{code}",
        "response": test,
        "language": lang,
        "category": "test",
        "type": "manual",
        "format": "test"
    })

P="python";J="javascript";JV="java";G="go"

def py(code, test):
    T(code, test + "\nimport pytest; pytest.main()", P)
def js(code, test):
    T(code, test, J)
def java(code, test):
    T(code, test, JV)
def go(code, test):
    T(code, test, G)

# Generate Python (200)
topics = [
    ("add", "def add(a,b): return a+b", "assert add(2,3)==5\nassert add(-1,1)==0\nassert add(0,0)==0"),
    ("sub", "def sub(a,b): return a-b", "assert sub(10,3)==7\nassert sub(0,5)==-5\nassert sub(100,100)==0"),
    ("mul", "def mul(a,b): return a*b", "assert mul(3,4)==12\nassert mul(-2,5)==-10\nassert mul(0,100)==0"),
    ("div", "def div(a,b):\n    if b==0: raise ValueError('Hata')\n    return a/b", "assert div(10,2)==5.0\nassert div(7,2)==3.5\nimport pytest\nwith pytest.raises(ValueError): div(5,0)"),
]# Data-driven generator
def make_py(name, code, assertions):
    test = f"def test_{name}():\n    " + "\n    ".join(assertions.split("\n"))
    T(code, test + "\nimport pytest; pytest.main()", P)

def make_js(name, code, assertions):
    parts = [f"console.assert({a})" for a in assertions.split("\n")]
    test = f"function test{name}(){{\n  " + ";\n  ".join(parts) + ";\n}}test" + name + "();"
    T(code, test, J)

def make_java(name, code, assertions, imports="import org.junit.*;\nimport static org.junit.Assert.*;"):
    test = f"{imports}\npublic class {name}Test {{\n    @Test\n    public void test{name}() {{\n"
    for a in assertions.split("\n"):
        test += f"        {a};\n"
    test += "    }\n}"
    T(code, test, JV)

def make_go(name, code, assertions):
    test = f"package main\n\nimport \"testing\"\n\nfunc Test{name}(t *testing.T) {{\n"
    for a in assertions.split("\n"):
        test += f"    {a}\n"
    test += "}"
    T(code, test, G)

# ========= PYTHON 200 =========
py_data = [
    ("add","def add(a,b): return a+b","assert add(2,3)==5\nassert add(-1,1)==0\nassert add(0,0)==0"),
    ("sub","def sub(a,b): return a-b","assert sub(10,3)==7\nassert sub(0,5)==-5\nassert sub(-5,-5)==0"),
    ("mul","def mul(a,b): return a*b","assert mul(3,4)==12\nassert mul(-2,5)==-10\nassert mul(0,100)==0"),
    ("div","def div(a,b):\n    if b==0: raise ValueError('Hata')\n    return a/b","assert div(10,2)==5.0\nassert div(7,2)==3.5\nimport pytest\nwith pytest.raises(ValueError): div(5,0)"),
    ("power","def power(b,e): return b**e","assert power(2,3)==8\nassert power(5,0)==1\nassert power(10,2)==100"),
    ("sqrt","import math\ndef sqrt(x):\n    if x<0: raise ValueError('Neg')\n    return math.sqrt(x)","assert sqrt(9)==3.0\nassert sqrt(0)==0.0\nimport pytest\nwith pytest.raises(ValueError): sqrt(-1)"),
    ("factorial","def fact(n):\n    if n<0: raise ValueError('Neg')\n    return 1 if n<=1 else n*fact(n-1)","assert fact(0)==1\nassert fact(5)==120\nassert fact(10)==3628800\nimport pytest\nwith pytest.raises(ValueError): fact(-1)"),
    ("fib","def fib(n):\n    if n<0: raise ValueError('Neg')\n    return n if n<=1 else fib(n-1)+fib(n-2)","assert fib(0)==0\nassert fib(1)==1\nassert fib(10)==55"),
    ("prime","def is_prime(n):\n    if n<2: return False\n    for i in range(2,int(n**0.5)+1):\n        if n%i==0: return False\n    return True","assert is_prime(2)==True\nassert is_prime(17)==True\nassert is_prime(1)==False\nassert is_prime(4)==False"),
    ("gcd","def gcd(a,b):\n    while b: a,b=b,a%b\n    return a","assert gcd(12,8)==4\nassert gcd(17,5)==1\nassert gcd(0,5)==5"),
    ("lcm","def lcm(a,b): return a*b//gcd(a,b)\ndef gcd(a,b):\n    while b: a,b=b,a%b\n    return a","assert lcm(4,6)==12\nassert lcm(3,5)==15\nassert lcm(12,18)==36"),
    ("c_to_f","def c_to_f(c): return (c*9/5)+32","assert c_to_f(0)==32\nassert c_to_f(100)==212\nassert c_to_f(-40)==-40"),
    ("f_to_c","def f_to_c(f): return (f-32)*5/9","assert f_to_c(32)==0\nassert f_to_c(212)==100\nassert f_to_c(-40)==-40"),
    ("mean","def mean(nums): return sum(nums)/len(nums)","assert mean([1,2,3,4,5])==3.0\nassert mean([10,20,30])==20.0\nassert mean([5])==5.0"),
    ("median","def median(nums):\n    s=sorted(nums); n=len(s); mid=n//2\n    if n%2==0: return (s[mid-1]+s[mid])/2\n    return s[mid]","assert median([1,3,3,6,7,8,9])==6\nassert median([1,2,3,4])==2.5"),
    ("mode","from collections import Counter\ndef mode(nums):\n    c=Counter(nums); mx=max(c.values())\n    return [k for k,v in c.items() if v==mx]","assert mode([1,2,2,3])==[2]\nassert set(mode([1,1,2,2]))=={1,2}"),
    ("pal","def is_pal(s):\n    s=s.lower().replace(' ',''); return s==s[::-1]","assert is_pal('kek')==True\nassert is_pal('A man a plan a canal Panama')==True\nassert is_pal('merhaba')==False"),
    ("rev_str","def rev_str(s): return s[::-1]","assert rev_str('abc')=='cba'\nassert rev_str('')==''\nassert rev_str('merhaba')=='abahrem'"),
    ("count_vowels","def count_v(s): return sum(1 for c in s if c in 'aeiouAEIOU')","assert count_v('merhaba')==3\nassert count_v('AEIOU')==5\nassert count_v('xyz')==0"),
    ("count_words","def count_w(s): return len(s.split())","assert count_w('merhaba dunya')==2\nassert count_w('')==0"),
]
py_data2 = [
    ("anagram","def is_anagram(s1,s2): return sorted(s1.lower())==sorted(s2.lower())","assert is_anagram('listen','silent')==True\nassert is_anagram('hello','world')==False"),
    ("cap_words","def cap_words(s): return ' '.join(w.capitalize() for w in s.split())","assert cap_words('merhaba dunya')=='Merhaba Dunya'"),
    ("truncate","def trunc(s,m): return s if len(s)<=m else s[:m-3]+'...'","assert trunc('merhaba dunya',10)=='merhaba...'\nassert trunc('test',10)=='test'"),
    ("mask_str","def mask_str(s): return s if len(s)<=4 else s[:2]+'*'*(len(s)-4)+s[-2:]","assert mask_str('1234567890')=='12******90'\nassert mask_str('test')=='test'"),
    ("slugify","import re\ndef slugify(s):\n    s=re.sub(r'[^a-z0-9\\s-]','',s.lower().strip())\n    return re.sub(r'[\\s-]+','-',s)","assert slugify('Merhaba Dunya')=='merhaba-dunya'\nassert slugify('Test! @Yazi')=='test-yazi'"),
    ("email_valid","import re\ndef is_email(e): return bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$',e))","assert is_email('test@example.com')==True\nassert is_email('invalid')==False"),
    ("password","import re\ndef is_pw(p): return len(p)>=8 and bool(re.search(r'[A-Z]',p)) and bool(re.search(r'[a-z]',p)) and bool(re.search(r'[0-9]',p))","assert is_pw('Test1234')==True\nassert is_pw('weak')==False"),
    ("phone","def fmt_phone(p):\n    d=''.join(filter(str.isdigit,p))\n    return f'({d[:3]}) {d[3:6]}-{d[6:]}' if len(d)==10 else p","assert fmt_phone('5551234567')=='(555) 123-4567'\nassert fmt_phone('123')=='123'"),
    ("url_valid","import re\ndef valid_url(u): return bool(re.match(r'^https?://[\\w.-]+(:\\d+)?(/[\\w./%-]*)?$',u))","assert valid_url('https://x.com')==True\nassert valid_url('invalid')==False"),
    ("ip_valid","import re\ndef valid_ip(ip):\n    m=re.match(r'^(\\d{1,3}\\.){3}\\d{1,3}$',ip)\n    if not m: return False\n    return all(0<=int(p)<=255 for p in ip.split('.'))","assert valid_ip('192.168.1.1')==True\nassert valid_ip('256.1.2.3')==False"),
    ("chunk","def chunk(l,s): return [l[i:i+s] for i in range(0,len(l),s)]","assert chunk([1,2,3,4,5],2)==[[1,2],[3,4],[5]]"),
    ("flatten","def flatten(l):\n    r=[]\n    for i in l:\n        if isinstance(i,list): r.extend(flatten(i))\n        else: r.append(i)\n    return r","assert flatten([1,[2,[3,4]],5])==[1,2,3,4,5]"),
    ("unique","def unique(l): return list(dict.fromkeys(l))","assert unique([1,2,2,3,1])==[1,2,3]"),
    ("intersection","def intersect(a,b): return list(set(a)&set(b))","assert sorted(intersect([1,2,3],[2,3,4]))==[2,3]"),
    ("union","def union(a,b): return list(set(a)|set(b))","assert sorted(union([1,2],[2,3]))==[1,2,3]"),
    ("rotate","def rotate(l,k):\n    if not l: return l\n    k%=len(l); return l[-k:]+l[:-k]","assert rotate([1,2,3,4,5],2)==[4,5,1,2,3]"),
    ("bubble","def bubble(arr):\n    n=len(arr)\n    for i in range(n):\n        for j in range(0,n-i-1):\n            if arr[j]>arr[j+1]: arr[j],arr[j+1]=arr[j+1],arr[j]\n    return arr","assert bubble([3,1,4,1,5])==[1,1,3,4,5]"),
    ("quick","def quick(arr):\n    if len(arr)<=1: return arr\n    p=arr[0]; l=[x for x in arr[1:] if x<=p]; r=[x for x in arr[1:] if x>p]\n    return quick(l)+[p]+quick(r)","assert quick([3,6,8,10,1,2,1])==[1,1,2,3,6,8,10]"),
    ("merge","def merge_sort(arr):\n    if len(arr)<=1: return arr\n    m=len(arr)//2; return merge(merge_sort(arr[:m]),merge_sort(arr[m:]))\ndef merge(l,r):\n    res=[]; i=j=0\n    while i<len(l) and j<len(r):\n        if l[i]<=r[j]: res.append(l[i]); i+=1\n        else: res.append(r[j]); j+=1\n    return res+l[i:]+r[j:]","assert merge_sort([38,27,43,3,9,82,10])==[3,9,10,27,38,43,82]"),
    ("binary_s","def bin_search(arr,t):\n    l,r=0,len(arr)-1\n    while l<=r:\n        m=(l+r)//2\n        if arr[m]==t: return m\n        if arr[m]<t: l=m+1\n        else: r=m-1\n    return -1","assert bin_search([1,3,5,7,9],5)==2\nassert bin_search([1,3,5,7,9],2)==-1"),
]
py_data3 = [
    ("linear","def lin_search(arr,t):\n    for i,v in enumerate(arr):\n        if v==t: return i\n    return -1","assert lin_search([4,2,7,1],7)==2\nassert lin_search([],1)==-1"),
    ("selection","def sel_sort(arr):\n    n=len(arr)\n    for i in range(n):\n        mi=i\n        for j in range(i+1,n):\n            if arr[j]<arr[mi]: mi=j\n        arr[i],arr[mi]=arr[mi],arr[i]\n    return arr","assert sel_sort([64,25,12,22,11])==[11,12,22,25,64]"),
    ("insertion","def ins_sort(arr):\n    for i in range(1,len(arr)):\n        key=arr[i]; j=i-1\n        while j>=0 and arr[j]>key:\n            arr[j+1]=arr[j]; j-=1\n        arr[j+1]=key\n    return arr","assert ins_sort([12,11,13,5,6])==[5,6,11,12,13]"),
    ("heap","def heapify(arr,n,i):\n    l=i*2+1; r=i*2+2; lg=i\n    if l<n and arr[l]>arr[lg]: lg=l\n    if r<n and arr[r]>arr[lg]: lg=r\n    if lg!=i: arr[i],arr[lg]=arr[lg],arr[i]; heapify(arr,n,lg)\ndef heap_sort(arr):\n    n=len(arr)\n    for i in range(n//2-1,-1,-1): heapify(arr,n,i)\n    for i in range(n-1,0,-1): arr[i],arr[0]=arr[0],arr[i]; heapify(arr,i,0)\n    return arr","assert heap_sort([4,10,3,5,1])==[1,3,4,5,10]"),
    ("counting","def cnt_sort(arr):\n    if not arr: return arr\n    mx=max(arr); c=[0]*(mx+1)\n    for x in arr: c[x]+=1\n    r=[]\n    for i,n in enumerate(c): r.extend([i]*n)\n    return r","assert cnt_sort([4,2,2,8,3,3,1])==[1,2,2,3,3,4,8]"),
    ("stack","class Stack:\n    def __init__(s): s.items=[]\n    def push(s,i): s.items.append(i)\n    def pop(s):\n        if s.is_empty(): raise IndexError('Bos')\n        return s.items.pop()\n    def peek(s): return s.items[-1]\n    def is_empty(s): return len(s.items)==0\n    def size(s): return len(s.items)","s=Stack()\nassert s.is_empty()==True\ns.push(1);s.push(2);s.push(3)\nassert s.pop()==3\nassert s.peek()==2\nassert s.size()==2\nimport pytest\nwith pytest.raises(IndexError): Stack().pop()"),
    ("queue","class Queue:\n    def __init__(s): s.items=[]\n    def enq(s,i): s.items.append(i)\n    def deq(s):\n        if s.is_empty(): raise IndexError('Bos')\n        return s.items.pop(0)\n    def front(s): return s.items[0]\n    def is_empty(s): return len(s.items)==0\n    def size(s): return len(s.items)","q=Queue()\nq.enq(1);q.enq(2);q.enq(3)\nassert q.deq()==1\nassert q.front()==2\nassert q.size()==2\nimport pytest\nwith pytest.raises(IndexError): Queue().deq()"),
    ("linked","class Node:\n    def __init__(s,d): s.data=d; s.next=None\nclass LinkedList:\n    def __init__(s): s.head=None\n    def append(s,d):\n        if not s.head: s.head=Node(d); return\n        c=s.head\n        while c.next: c=c.next\n        c.next=Node(d)\n    def to_list(s):\n        r=[]; c=s.head\n        while c: r.append(c.data); c=c.next\n        return r","ll=LinkedList()\nassert ll.to_list()==[]\nll.append(1);ll.append(2);ll.append(3)\nassert ll.to_list()==[1,2,3]"),
    ("bst","class TreeNode:\n    def __init__(s,v): s.val=v; s.left=s.right=None\nclass BST:\n    def __init__(s): s.root=None\n    def insert(s,v):\n        if not s.root: s.root=TreeNode(v); return\n        s._insert(s.root,v)\n    def _insert(s,n,v):\n        if v<n.val:\n            if n.left: s._insert(n.left,v)\n            else: n.left=TreeNode(v)\n        else:\n            if n.right: s._insert(n.right,v)\n            else: n.right=TreeNode(v)\n    def search(s,v): return s._search(s.root,v)\n    def _search(s,n,v):\n        if not n: return False\n        if n.val==v: return True\n        return s._search(n.left,v) if v<n.val else s._search(n.right,v)","bst=BST()\nbst.insert(5);bst.insert(3);bst.insert(7)\nassert bst.search(5)==True\nassert bst.search(9)==False"),
    ("bfs","def bfs(graph,start):\n    v=set(); q=[start]; r=[]\n    while q:\n        n=q.pop(0)\n        if n not in v: v.add(n); r.append(n); q.extend(graph[n])\n    return r","g={'A':['B','C'],'B':['D'],'C':['E'],'D':[],'E':[]}\nassert bfs(g,'A')==['A','B','C','D','E']"),
    ("dfs","def dfs(graph,start):\n    v=set(); r=[]\n    def _dfs(n):\n        v.add(n); r.append(n)\n        for nb in graph[n]:\n            if nb not in v: _dfs(nb)\n    _dfs(start)\n    return r","g={'A':['B','C'],'B':['D'],'C':['E'],'D':[],'E':[]}\nassert dfs(g,'A')==['A','B','D','C','E']"),
    ("dijkstra","import heapq\ndef dijkstra(graph,start):\n    d={n:float('inf') for n in graph}\n    d[start]=0; pq=[(0,start)]\n    while pq:\n        cd,c=heapq.heappop(pq)\n        if cd>d[c]: continue\n        for nb,w in graph[c].items():\n            nd=cd+w\n            if nd<d[nb]: d[nb]=nd; heapq.heappush(pq,(nd,nb))\n    return d","g={'A':{'B':1,'C':4},'B':{'C':2,'D':5},'C':{'D':1},'D':{}}\n    d=dijkstra(g,'A')\n    assert d['A']==0 and d['B']==1 and d['C']==3 and d['D']==4"),
    ("knapsack","def knap(W,wt,val,n):\n    dp=[[0]*(W+1) for _ in range(n+1)]\n    for i in range(1,n+1):\n        for w in range(1,W+1):\n            if wt[i-1]<=w: dp[i][w]=max(val[i-1]+dp[i-1][w-wt[i-1]],dp[i-1][w])\n            else: dp[i][w]=dp[i-1][w]\n    return dp[n][W]","val=[60,100,120]; wt=[10,20,30]\nassert knap(50,wt,val,3)==220"),
    ("edit_dist","def edit_dist(s1,s2):\n    m,n=len(s1),len(s2); dp=[[0]*(n+1) for _ in range(m+1)]\n    for i in range(m+1): dp[i][0]=i\n    for j in range(n+1): dp[0][j]=j\n    for i in range(1,m+1):\n        for j in range(1,n+1):\n            if s1[i-1]==s2[j-1]: dp[i][j]=dp[i-1][j-1]\n            else: dp[i][j]=1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])\n    return dp[m][n]","assert edit_dist('kitten','sitting')==3\nassert edit_dist('same','same')==0"),
    ("lcs","def lcs(X,Y):\n    m,n=len(X),len(Y); dp=[[0]*(n+1) for _ in range(m+1)]\n    for i in range(1,m+1):\n        for j in range(1,n+1):\n            if X[i-1]==Y[j-1]: dp[i][j]=dp[i-1][j-1]+1\n            else: dp[i][j]=max(dp[i-1][j],dp[i][j-1])\n    return dp[m][n]","assert lcs('AGGTAB','GXTXAYB')==4\nassert lcs('ABC','DEF')==0"),
    ("csv","import csv,io\ndef parse_csv(text):\n    return [row for row in csv.reader(io.StringIO(text))]","r=parse_csv('a,b,c\\n1,2,3\\n4,5,6')\nassert r==[['a','b','c'],['1','2','3'],['4','5','6']]"),
    ("json_fmt","import json\ndef fmt_json(obj): return json.dumps(obj,indent=2,ensure_ascii=False)","r=fmt_json({'name':'Ali','age':30})\nassert '\"name\": \"Ali\"' in r"),
    ("query","from urllib.parse import parse_qs\ndef parse_qs_f(qs):\n    return {k:v[0] if len(v)==1 else v for k,v in parse_qs(qs).items()}","assert parse_qs_f('a=1&b=2')=={'a':'1','b':'2'}"),
    ("cookies","def parse_cookies(c):\n    r={}\n    for i in c.split(';'):\n        i=i.strip()\n        if '=' in i: k,v=i.split('=',1); r[k.strip()]=v.strip()\n    return r","assert parse_cookies('a=1; b=2')=={'a':'1','b':'2'}"),
    ("url_parse","from urllib.parse import urlparse\ndef parse_url(url):\n    p=urlparse(url)\n    return {'scheme':p.scheme,'host':p.hostname,'port':p.port,'path':p.path}","r=parse_url('https://example.com:8080/path?q=1')\nassert r['scheme']=='https'\nassert r['host']=='example.com'"),
]
