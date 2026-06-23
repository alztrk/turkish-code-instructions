import json, random
random.seed(42)

entries = []
def T(code, test, lang):
    entries.append({"instruction": "Asagidaki fonksiyon icin unit test yaz:\n" + code, "response": test, "language": lang, "category": "test", "type": "manual", "format": "test"})

P="python";J="javascript";JV="java";G="go"

def E(data, lang, make_fn):
    for name, code, asserts in data:
        test = make_fn(name, asserts)
        T(code, test, lang)

def py_asserts(name, a):
    return f"def test_{name}():\n    " + "\n    ".join(a.split("\n")) + "\nimport pytest; pytest.main()"

def js_asserts(name, a):
    parts = [f"console.assert({p})" for p in a.split("\n")]
    return f"function test_{name}(){{\n  " + ";\n  ".join(parts) + ";\n}}test_{name}();"

def go_asserts(name, a):
    return f"package main\nimport \"testing\"\nfunc Test{name}(t *testing.T) {{\n    " + "\n    ".join(a.split("\n")) + "\n}}"

def java_asserts(name, a):
    lines = [f"        {p};" for p in a.split("\n")]
    return f"import org.junit.*;\nimport static org.junit.Assert.*;\npublic class {name}Test {{\n    @Test\n    public void test{name}() {{\n" + "\n".join(lines) + "\n    }\n}}"

py_data = [
("add","def add(a,b): return a+b","assert add(2,3)==5\nassert add(-1,1)==0\nassert add(0,0)==0"),
("sub","def sub(a,b): return a-b","assert sub(10,3)==7\nassert sub(0,5)==-5"),
("mul","def mul(a,b): return a*b","assert mul(3,4)==12\nassert mul(-2,5)==-10\nassert mul(0,100)==0"),
("div","def div(a,b):\n    if b==0: raise ValueError(\"Hata\")\n    return a/b","assert div(10,2)==5.0\nassert div(7,2)==3.5\nimport pytest\nwith pytest.raises(ValueError): div(5,0)"),
("power","def power(b,e): return b**e","assert power(2,3)==8\nassert power(5,0)==1\nassert power(10,2)==100"),
("sqrt","import math\ndef sqrt(x):\n    if x<0: raise ValueError(\"Neg\")\n    return math.sqrt(x)","assert sqrt(9)==3.0\nassert sqrt(0)==0.0\nimport pytest\nwith pytest.raises(ValueError): sqrt(-1)"),
("factorial","def fact(n):\n    if n<0: raise ValueError(\"Neg\")\n    return 1 if n<=1 else n*fact(n-1)","assert fact(0)==1\nassert fact(5)==120\nassert fact(10)==3628800\nimport pytest\nwith pytest.raises(ValueError): fact(-1)"),
("fib","def fib(n):\n    if n<0: raise ValueError(\"Neg\")\n    return n if n<=1 else fib(n-1)+fib(n-2)","assert fib(0)==0\nassert fib(1)==1\nassert fib(10)==55"),
("prime","def is_prime(n):\n    if n<2: return False\n    for i in range(2,int(n**0.5)+1):\n        if n%i==0: return False\n    return True","assert is_prime(2)==True\nassert is_prime(17)==True\nassert is_prime(1)==False\nassert is_prime(4)==False"),
("gcd","def gcd(a,b):\n    while b: a,b=b,a%b\n    return a","assert gcd(12,8)==4\nassert gcd(17,5)==1\nassert gcd(0,5)==5"),
("lcm","def lcm(a,b): return a*b//gcd(a,b)\ndef gcd(a,b):\n    while b: a,b=b,a%b\n    return a","assert lcm(4,6)==12\nassert lcm(3,5)==15"),
("c2f","def c2f(c): return (c*9/5)+32","assert c2f(0)==32\nassert c2f(100)==212\nassert c2f(-40)==-40"),
("f2c","def f2c(f): return (f-32)*5/9","assert f2c(32)==0\nassert f2c(212)==100\nassert f2c(-40)==-40"),
("mean","def mean(nums): return sum(nums)/len(nums)","assert mean([1,2,3,4,5])==3.0\nassert mean([10,20,30])==20.0\nassert mean([5])==5.0"),
("median","def median(nums):\n    s=sorted(nums); n=len(s); mid=n//2\n    if n%2==0: return (s[mid-1]+s[mid])/2\n    return s[mid]","assert median([1,3,3,6,7,8,9])==6\nassert median([1,2,3,4])==2.5"),
("mode","from collections import Counter\ndef mode(nums):\n    c=Counter(nums); mx=max(c.values())\n    return [k for k,v in c.items() if v==mx]","assert mode([1,2,2,3])==[2]\nassert set(mode([1,1,2,2]))=={1,2}"),
("pal","def is_pal(s):\n    s=s.lower().replace(\" \",\"\"); return s==s[::-1]","assert is_pal(\"kek\")==True\nassert is_pal(\"A man a plan a canal Panama\")==True\nassert is_pal(\"merhaba\")==False"),
("rev_str","def rev_str(s): return s[::-1]","assert rev_str(\"abc\")==\"cba\"\nassert rev_str(\"\")==\"\"\nassert rev_str(\"merhaba\")==\"abahrem\""),
("count_v","def count_v(s): return sum(1 for c in s if c in \"aeiouAEIOU\")","assert count_v(\"merhaba\")==3\nassert count_v(\"xyz\")==0"),
("count_w","def count_w(s): return len(s.split())","assert count_w(\"merhaba dunya\")==2\nassert count_w(\"\")==0"),
("anagram","def is_anagram(s1,s2): return sorted(s1.lower())==sorted(s2.lower())","assert is_anagram(\"listen\",\"silent\")==True\nassert is_anagram(\"hello\",\"world\")==False"),
("cap_w","def cap_w(s): return \" \".join(w.capitalize() for w in s.split())","assert cap_w(\"merhaba dunya\")==\"Merhaba Dunya\""),
("trunc","def trunc(s,m): return s if len(s)<=m else s[:m-3]+\"...\"","assert trunc(\"merhaba\",6)==\"mer...\"\nassert trunc(\"test\",10)==\"test\""),
("mask","def mask(s): return s if len(s)<=4 else s[:2]+\"*\"*(len(s)-4)+s[-2:]","assert mask(\"1234567890\")==\"12******90\"\nassert mask(\"test\")==\"test\""),
("slug","import re\ndef slug(s):\n    s=re.sub(r\"[^a-z0-9\\s-]\",\"\",s.lower().strip())\n    return re.sub(r\"[\\s-]+\",\"-\",s)","assert slug(\"Merhaba Dunya\")==\"merhaba-dunya\""),
("email_v","import re\ndef email_v(e): return bool(re.match(r\"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$\",e))","assert email_v(\"test@x.com\")==True\nassert email_v(\"bad\")==False"),
("pw_strong","import re\ndef pw_s(p): return len(p)>=8 and bool(re.search(r\"[A-Z]\",p)) and bool(re.search(r\"[a-z]\",p)) and bool(re.search(r\"[0-9]\",p))","assert pw_s(\"Test1234\")==True\nassert pw_s(\"weak\")==False"),
("phone","def fmt_phone(p):\n    d=\"\".join(filter(str.isdigit,p))\n    return f\"({d[:3]}) {d[3:6]}-{d[6:]}\" if len(d)==10 else p","assert fmt_phone(\"5551234567\")==\"(555) 123-4567\""),
("url_v","import re\ndef url_v(u): return bool(re.match(r\"^https?://[\\w.-]+(:\\d+)?(/[\\w./%-]*)?$\",u))","assert url_v(\"https://x.com\")==True\nassert url_v(\"bad\")==False"),
("ip_v","import re\ndef ip_v(ip):\n    m=re.match(r\"^(\\d{1,3}\\.){3}\\d{1,3}$\",ip)\n    if not m: return False\n    return all(0<=int(p)<=255 for p in ip.split(\".\"))","assert ip_v(\"192.168.1.1\")==True\nassert ip_v(\"256.1.2.3\")==False"),
("chunk","def chunk(l,s): return [l[i:i+s] for i in range(0,len(l),s)]","assert chunk([1,2,3,4,5],2)==[[1,2],[3,4],[5]]"),
("flatten","def flatten(l):\n    r=[]\n    for i in l:\n        if isinstance(i,list): r.extend(flatten(i))\n        else: r.append(i)\n    return r","assert flatten([1,[2,[3,4]],5])==[1,2,3,4,5]"),
("unique","def unique(l): return list(dict.fromkeys(l))","assert unique([1,2,2,3,1])==[1,2,3]"),
("inter","def inter(a,b): return list(set(a)&set(b))","assert sorted(inter([1,2,3],[2,3,4]))==[2,3]"),
("union_f","def union_f(a,b): return list(set(a)|set(b))","assert sorted(union_f([1,2],[2,3]))==[1,2,3]"),
("rotate","def rotate(l,k):\n    if not l: return l\n    k%=len(l); return l[-k:]+l[:-k]","assert rotate([1,2,3,4,5],2)==[4,5,1,2,3]"),
("bubble","def bubble(arr):\n    n=len(arr)\n    for i in range(n):\n        for j in range(0,n-i-1):\n            if arr[j]>arr[j+1]: arr[j],arr[j+1]=arr[j+1],arr[j]\n    return arr","assert bubble([3,1,4,1,5])==[1,1,3,4,5]"),
("quick","def quick(arr):\n    if len(arr)<=1: return arr\n    p=arr[0]; l=[x for x in arr[1:] if x<=p]; r=[x for x in arr[1:] if x>p]\n    return quick(l)+[p]+quick(r)","assert quick([3,6,8,10,1,2,1])==[1,1,2,3,6,8,10]"),
("merge_s","def merge_s(arr):\n    if len(arr)<=1: return arr\n    m=len(arr)//2; return merge(merge_s(arr[:m]),merge_s(arr[m:]))\ndef merge(l,r):\n    res=[]; i=j=0\n    while i<len(l) and j<len(r):\n        if l[i]<=r[j]: res.append(l[i]); i+=1\n        else: res.append(r[j]); j+=1\n    return res+l[i:]+r[j:]","assert merge_s([38,27,43,3,9,82,10])==[3,9,10,27,38,43,82]"),
("bin_s","def bin_s(arr,t):\n    l,r=0,len(arr)-1\n    while l<=r:\n        m=(l+r)//2\n        if arr[m]==t: return m\n        if arr[m]<t: l=m+1\n        else: r=m-1\n    return -1","assert bin_s([1,3,5,7,9],5)==2\nassert bin_s([],1)==-1"),
("linear","def lin_s(arr,t):\n    for i,v in enumerate(arr):\n        if v==t: return i\n    return -1","assert lin_s([4,2,7,1],7)==2\nassert lin_s([],1)==-1"),
("sel_s","def sel_s(arr):\n    n=len(arr)\n    for i in range(n):\n        mi=i\n        for j in range(i+1,n):\n            if arr[j]<arr[mi]: mi=j\n        arr[i],arr[mi]=arr[mi],arr[i]\n    return arr","assert sel_s([64,25,12,22,11])==[11,12,22,25,64]"),
("ins_s","def ins_s(arr):\n    for i in range(1,len(arr)):\n        key=arr[i]; j=i-1\n        while j>=0 and arr[j]>key:\n            arr[j+1]=arr[j]; j-=1\n        arr[j+1]=key\n    return arr","assert ins_s([12,11,13,5,6])==[5,6,11,12,13]"),
("heap_s","def heapify(arr,n,i):\n    l=i*2+1; r=i*2+2; lg=i\n    if l<n and arr[l]>arr[lg]: lg=l\n    if r<n and arr[r]>arr[lg]: lg=r\n    if lg!=i: arr[i],arr[lg]=arr[lg],arr[i]; heapify(arr,n,lg)\ndef heap_s(arr):\n    n=len(arr)\n    for i in range(n//2-1,-1,-1): heapify(arr,n,i)\n    for i in range(n-1,0,-1): arr[i],arr[0]=arr[0],arr[i]; heapify(arr,i,0)\n    return arr","assert heap_s([4,10,3,5,1])==[1,3,4,5,10]"),
("cnt_s","def cnt_s(arr):\n    if not arr: return arr\n    mx=max(arr); c=[0]*(mx+1)\n    for x in arr: c[x]+=1\n    r=[]\n    for i,n in enumerate(c): r.extend([i]*n)\n    return r","assert cnt_s([4,2,2,8,3,3,1])==[1,2,2,3,3,4,8]"),
]
E(py_data, P, py_asserts)
