import json

entries = []
idx = 0

def instr(code):
    global idx
    idx += 1
    return f"Su kodun ciktisi nedir?\n{code}"

# ============================================================
# PYTHON (300 entries)
# ============================================================

# Arithmetic & operator precedence (25)
py_codes = [
    ("print(2 ** 3 ** 2)", "512", "python"),
    ("print(10 // 3)", "3", "python"),
    ("print(-10 // 3)", "-4", "python"),
    ("print(10 % -3)", "-2", "python"),
    ("print(2 + 3 * 4 ** 2)", "50", "python"),
    ("print((2 + 3) * 4 ** 2)", "80", "python"),
    ("print(16 >> 2)", "4", "python"),
    ("print(5 & 3 | 2)", "7", "python"),
    ("print(1 << 10)", "1024", "python"),
    ("print(~5)", "-6", "python"),
    ("print(3 ^ 5)", "6", "python"),
    ("print(6 / 2 * 3)", "9.0", "python"),
    ("print(7 // 2 * 2)", "6", "python"),
    ("print(0.1 + 0.2 == 0.3)", "False", "python"),
    ("print(2 ** -1)", "0.5", "python"),
    ("print(8 ** (1/3))", "2.0", "python"),
    ("print(10 / 0.5)", "20.0", "python"),
    ("print(1 + True * 3)", "4", "python"),
    ("print(False ** 0)", "1", "python"),
    ("print(2 + 2 if 3 > 5 else 3 + 3)", "6", "python"),
    ("print(4 * 3 ** 2 - 1)", "35", "python"),
    ("print(10 // 4 * 4 + 10 % 4)", "10", "python"),
    ("print(0b1010 + 0b1100)", "22", "python"),
    ("print(0xFF ^ 0x0F)", "240", "python"),
    ("print(1_000_000 + 1_000)", "1001000", "python"),
]

# String operations (25)
py_codes += [
    ("print('hello'[1:4])", "ell", "python"),
    ("print('python'[::-1])", "nohtyp", "python"),
    ("print('abcdef'[::2])", "ace", "python"),
    ("print('  spaced  '.strip())", "spaced", "python"),
    ("print('a,b,c'.split(','))", "['a', 'b', 'c']", "python"),
    ("print('-'.join(['x','y','z']))", "x-y-z", "python"),
    ("print('hello'.replace('l','x'))", "hexxo", "python"),
    ("print('banana'.count('a'))", "3", "python"),
    ("print('abracadabra'.find('cad'))", "4", "python"),
    ("print('Python'.lower().startswith('p'))", "True", "python"),
    ("print('  hello  '.strip().upper())", "HELLO", "python"),
    ("print('123'.isdigit() and 'abc'.isalpha())", "True", "python"),
    ("print(' '.join(reversed('hello')))", "o l l e h", "python"),
    ("print('test'[10:20])", "", "python"),
    ("print('test'[-1])", "t", "python"),
    ("print('abcdefgh'[3:-2])", "def", "python"),
    ("print(*'xyz', sep='-')", "x-y-z", "python"),
    ("print('{:.2f}'.format(3.14159))", "3.14", "python"),
    ("print('{:#x}'.format(255))", "0xff", "python"),
    ("print('{:b}'.format(42))", "101010", "python"),
    ("print('value: %d' % 99)", "value: 99", "python"),
    ("print(f'{2**10}')", "1024", "python"),
    ("print(f'{3.14159:.1f}')", "3.1", "python"),
    ("print(f'{42:04d}')", "0042", "python"),
    ("print('a' 'b' 'c')", "abc", "python"),
]

# List comprehension (25)
py_codes += [
    ("print([x*2 for x in range(5)])", "[0, 2, 4, 6, 8]", "python"),
    ("print([x for x in range(10) if x%3==0])", "[0, 3, 6, 9]", "python"),
    ("print([[x,y] for x in [1,2] for y in [3,4]])", "[[1, 3], [1, 4], [2, 3], [2, 4]]", "python"),
    ("print([x**2 if x%2==0 else x**3 for x in range(5)])", "[0, 1, 4, 27, 16]", "python"),
    ("print([(a,b) for a in range(2) for b in range(2)])", "[(0, 0), (0, 1), (1, 0), (1, 1)]", "python"),
    ("print([i for i in 'hello123' if i.isdigit()])", "['1', '2', '3']", "python"),
    ("print(len([x for x in range(100) if x%7==0]))", "15", "python"),
    ("print([x+y for x in 'ab' for y in 'cd'])", "['ac', 'ad', 'bc', 'bd']", "python"),
    ("print([n for n in range(1,20) if all(n%i!=0 for i in range(2,int(n**0.5)+1))])", "[1, 2, 3, 5, 7, 11, 13, 17, 19]", "python"),
    ("print([i*i for i in range(1,6)])", "[1, 4, 9, 16, 25]", "python"),
    ("print([x for x in [[1,2],[3,4],[5,6]] for x in x])", "[1, 2, 3, 4, 5, 6]", "python"),
    ("print([str(i)*i for i in range(1,4)])", "['1', '22', '333']", "python"),
    ("print([x for x in range(10,0,-2)])", "[10, 8, 6, 4, 2]", "python"),
    ("print([x for x in [0,1,2,3] if x or x==0])", "[0, 1, 2, 3]", "python"),
    ("print([chr(65+i) for i in range(5)])", "['A', 'B', 'C', 'D', 'E']", "python"),
]

# Dict operations (20)
py_codes += [
    ("print({'a':1,'b':2}.get('c','default'))", "default", "python"),
    ("a={'x':1}; a.setdefault('x',5); print(a)", "{'x': 1}", "python"),
    ("a={'x':1}; a.setdefault('y',5); print(a)", "{'x': 1, 'y': 5}", "python"),
    ("print({x:x**2 for x in range(1,5)})", "{1: 1, 2: 4, 3: 9, 4: 16}", "python"),
    ("d={'a':1,'b':2}; print({v:k for k,v in d.items()})", "{1: 'a', 2: 'b'}", "python"),
    ("print({**{'a':1}, **{'b':2}})", "{'a': 1, 'b': 2}", "python"),
    ("d={}; d['key']=d.get('key',0)+1; print(d)", "{'key': 1}", "python"),
    ("print({1:'a',1:'b'})", "{1: 'b'}", "python"),
    ("print(list({'a':1,'b':2,'c':3}.keys()))", "['a', 'b', 'c']", "python"),
    ("print(list({'a':1,'b':2,'c':3}.values()))", "[1, 2, 3]", "python"),
    ("print({k for k in 'abracadabra'})", "{'a', 'b', 'c', 'd', 'r'}", "python"),
    ("d=dict.fromkeys(['x','y'],0); print(d)", "{'x': 0, 'y': 0}", "python"),
    ("d={'a':1,'b':2}; print(d.pop('a'))", "1", "python"),
    ("d={'a':1,'b':2}; d.pop('c','nope'); print(d)", "{'a': 1, 'b': 2}", "python"),
    ("print(dict(a=1,b=2,c=3))", "{'a': 1, 'b': 2, 'c': 3}", "python"),
    ("print([k for k,v in {'x':1,'y':1,'z':2}.items() if v==1])", "['x', 'y']", "python"),
    ("d={}; d['a']=[]; d['a'].append(1); print(d)", "{'a': [1]}", "python"),
    ("print(len({'a':1,'b':2,'c':3,'d':4}))", "4", "python"),
    ("print({x: x**3 for x in range(3,7)})", "{3: 27, 4: 64, 5: 125, 6: 216}", "python"),
    ("print({}.fromkeys('abc',0))", "{'a': 0, 'b': 0, 'c': 0}", "python"),
]

# Set operations (15)
py_codes += [
    ("print({1,2,3} | {3,4,5})", "{1, 2, 3, 4, 5}", "python"),
    ("print({1,2,3} & {2,3,4})", "{2, 3}", "python"),
    ("print({1,2,3} - {2,3,4})", "{1}", "python"),
    ("print({1,2,3} ^ {3,4,5})", "{1, 2, 4, 5}", "python"),
    ("print({1,2} < {1,2,3})", "True", "python"),
    ("print({1,2,3} > {1,2,3})", "False", "python"),
    ("print(len({x%4 for x in range(10)}))", "4", "python"),
    ("print({x for x in [1,1,2,2,3,3]})", "{1, 2, 3}", "python"),
    ("print({x%3 for x in range(9)})", "{0, 1, 2}", "python"),
    ("s={1,2,3}; s.discard(2); print(s)", "{1, 3}", "python"),
    ("s={1,2,3}; s.discard(5); print(s)", "{1, 2, 3}", "python"),
    ("print({1,2}.isdisjoint({3,4}))", "True", "python"),
    ("print({1,2}.isdisjoint({2,3}))", "False", "python"),
    ("print(frozenset({1,2,3}))", "frozenset({1, 2, 3})", "python"),
    ("print({x*2 for x in range(1,6)})", "{2, 4, 6, 8, 10}", "python"),
]

# Boolean logic / short-circuit / truthy (15)
py_codes += [
    ("print(True and False or True)", "True", "python"),
    ("print(False or False and True)", "False", "python"),
    ("print(1 and 2 or 3)", "2", "python"),
    ("print(0 and 5 or 10)", "10", "python"),
    ("print('' or 'default')", "default", "python"),
    ("print([] or [1,2])", "[1, 2]", "python"),
    ("print(3 or 4)", "3", "python"),
    ("print(0 or 1 and 2)", "2", "python"),
    ("print(not 3 > 2)", "False", "python"),
    ("print(not [])", "True", "python"),
    ("print('' == False)", "False", "python"),
    ("print(1 in [1,2,3] and 4 not in [1,2,3])", "True", "python"),
    ("print(3 > 2 > 1)", "True", "python"),
    ("print(3 > 2 > 4)", "False", "python"),
    ("print(1 < 2 != 3)", "True", "python"),
]

# lambda, map, filter, sorted (20)
py_codes += [
    ("print(list(map(str, [1,2,3])))", "['1', '2', '3']", "python"),
    ("print(list(filter(lambda x: x%2==0, range(10))))", "[0, 2, 4, 6, 8]", "python"),
    ("print(sorted([3,1,4,1,5,9,2]))", "[1, 1, 2, 3, 4, 5, 9]", "python"),
    ("print(sorted('python'))", "['h', 'n', 'o', 'p', 't', 'y']", "python"),
    ("print(sorted(['a','bb','ccc'], key=len))", "['a', 'bb', 'ccc']", "python"),
    ("f=lambda x,y:x+y; print(f(3,4))", "7", "python"),
    ("print((lambda x:x**2)(5))", "25", "python"),
    ("print(list(map(lambda x:x[0], ['ab','cd','ef'])))", "['a', 'c', 'e']", "python"),
    ("print(list(filter(None, [0,1,'',2,None,3])))", "[1, 2, 3]", "python"),
    ("print(sorted([1,2,3], reverse=True))", "[3, 2, 1]", "python"),
    ("print(sorted([(1,'b'),(2,'a')], key=lambda x:x[1]))", "[(2, 'a'), (1, 'b')]", "python"),
    ("print(list(map(lambda a,b:a+b, [1,2,3], [4,5,6])))", "[5, 7, 9]", "python"),
    ("print(list(filter(lambda x:x, [0,0,1,0,1])))", "[1, 1]", "python"),
    ("print((lambda a,b=10:a+b)(5))", "15", "python"),
    ("print((lambda *args:sum(args))(1,2,3,4))", "10", "python"),
    ("print(sorted(['banana','apple','cherry'], key=lambda x:x[-1]))", "['banana', 'apple', 'cherry']", "python"),
    ("print(list(map(len, ['hi','hello','hey'])))", "[2, 5, 3]", "python"),
    ("print(list(filter(str.isdigit, 'a1b2c3')))", "['1', '2', '3']", "python"),
    ("print((lambda x: (x+1, x*2))(5))", "(6, 10)", "python"),
    ("print((lambda x,y=2,z=3:x+y+z)(1))", "6", "python"),
]

# zip, enumerate, reversed (15)
py_codes += [
    ("print(list(zip([1,2,3], 'abc')))", "[(1, 'a'), (2, 'b'), (3, 'c')]", "python"),
    ("print(list(enumerate(['a','b','c'], start=1)))", "[(1, 'a'), (2, 'b'), (3, 'c')]", "python"),
    ("print(list(reversed([1,2,3])))", "[3, 2, 1]", "python"),
    ("print(list(zip([1,2], ['a','b','c'])))", "[(1, 'a'), (2, 'b')]", "python"),
    ("print(list(zip(*[(1,'a'),(2,'b')])))", "[(1, 2), ('a', 'b')]", "python"),
    ("print({k:v for k,v in zip(['x','y'],[10,20])})", "{'x': 10, 'y': 20}", "python"),
    ("print(list(enumerate('abc')))", "[(0, 'a'), (1, 'b'), (2, 'c')]", "python"),
    ("print(''.join(reversed('hello')))", "olleh", "python"),
    ("print(dict(zip('abc', range(3))))", "{'a': 0, 'b': 1, 'c': 2}", "python"),
    ("print([i*2 for i,_ in enumerate('xyz')])", "[0, 2, 4]", "python"),
    ("print(list(zip(range(3), range(3,6))))", "[(0, 3), (1, 4), (2, 5)]", "python"),
    ("print([x for x in reversed(range(5,0,-1))])", "[1, 2, 3, 4, 5]", "python"),
    ("print(list(zip('abc','123','xyz')))", "[('a', '1', 'x'), ('b', '2', 'y'), ('c', '3', 'z')]", "python"),
    ("print([v for i,v in enumerate('aeiou') if i%2==0])", "['a', 'i']", "python"),
    ("print(list(reversed(sorted([3,1,2]))))", "[3, 2, 1]", "python"),
]

# Generator expressions (10)
py_codes += [
    ("g=(x*x for x in range(3)); print(list(g))", "[0, 1, 4]", "python"),
    ("print(sum(x**2 for x in range(1,5)))", "30", "python"),
    ("print(max(len(w) for w in ['cat','elephant','dog']))", "8", "python"),
    ("g=(x for x in range(5)); print(next(g), next(g))", "0 1", "python"),
    ("print(any(x%2==0 for x in [1,3,5,7]))", "False", "python"),
    ("print(all(x>0 for x in [1,2,3,4]))", "True", "python"),
    ("print(list(x for x in range(10) if x%2))", "[1, 3, 5, 7, 9]", "python"),
    ("print(min(x**2 for x in range(-5,6)))", "0", "python"),
    ("print(''.join(str(i) for i in range(1,6)))", "12345", "python"),
    ("print({i:i**2 for i in range(4)})", "{0: 0, 1: 1, 2: 4, 3: 9}", "python"),
]

# type(), bool(), None (15)
py_codes += [
    ("print(type(5/2))", "<class 'float'>", "python"),
    ("print(type(5//2))", "<class 'int'>", "python"),
    ("print(type([]) is list)", "True", "python"),
    ("print(bool([]))", "False", "python"),
    ("print(bool([0]))", "True", "python"),
    ("print(bool('False'))", "True", "python"),
    ("print(bool(None))", "False", "python"),
    ("print(None is None)", "True", "python"),
    ("print(None == False)", "False", "python"),
    ("print(type(type))", "<class 'type'>", "python"),
    ("print(type(3+4j))", "<class 'complex'>", "python"),
    ("print(bool(...))", "True", "python"),
    ("print(type(lambda:0).__name__)", "function", "python"),
    ("print(bool(0.0))", "False", "python"),
    ("print(None is not None)", "False", "python"),
]

# Function returns / closures / default args (15)
py_codes += [
    ("def f(): return 1,2,3; print(f())", "(1, 2, 3)", "python"),
    ("def f(a,b): return a+b; print(f(b=2,a=1))", "3", "python"),
    ("def f(x=[]): x.append(1); return x; print(f(), f())", "[1] [1, 1]", "python"),
    ("def f(x=None): x=x or []; x.append(1); return x; print(f(), f())", "[1] [1]", "python"),
    ("def f(x): return x*2; g=lambda x:x*3; print(f(2)+g(2))", "10", "python"),
    ("def f(a,b,*args): return a,b,args; print(f(1,2,3,4))", "(1, 2, (3, 4))", "python"),
    ("def f(**kw): return kw; print(f(a=1,b=2))", "{'a': 1, 'b': 2}", "python"),
    ("def f(a,b=2,c=3): return a+b+c; print(f(1,c=5))", "8", "python"),
    ("def outer(x): def inner(y): return x+y; return inner; print(outer(5)(3))", "8", "python"),
    ("def f(x): return x+1; print(f(f(f(0))))", "3", "python"),
    ("def f(a,b): pass; print(f(1,2))", "None", "python"),
    ("def f(): return 5; print(f() + f())", "10", "python"),
    ("def f(a,*b): return a,b; print(f(1,2,3,4,5))", "(1, (2, 3, 4, 5))", "python"),
    ("def f(a,b,c): return a; print(f(*[1,2,3]))", "1", "python"),
    ("def f(a,b,c): return c; print(f(**{'a':1,'b':2,'c':3}))", "3", "python"),
]

# Exception messages (10)
py_codes += [
    ("try: 1/0\nexcept Exception as e: print(e)", "division by zero", "python"),
    ("try: [1,2][5]\nexcept IndexError as e: print(e)", "list index out of range", "python"),
    ("try: int('abc')\nexcept ValueError as e: print(e)", "invalid literal for int() with base 10: 'abc'", "python"),
    ("try: {}['key']\nexcept KeyError as e: print(e)", "'key'", "python"),
    ("try: 'x'+1\nexcept TypeError as e: print(e)", "can only concatenate str (not \"int\") to str", "python"),
    ("try: print(x)\nexcept NameError as e: print(e)", "name 'x' is not defined", "python"),
    ("try: 3<[1]\nexcept TypeError as e: print(e)", "'<' not supported between instances of 'int' and 'list'", "python"),
    ("try: [1].sort('x')\nexcept TypeError as e: print(e)", "'<' not supported between instances of 'str' and 'int'", "python"),
    ("try: ''.append(1)\nexcept AttributeError as e: print(e)", "'str' object has no attribute 'append'", "python"),
    ("def f(x,y): pass\ntry: f(1)\nexcept TypeError as e: print(e)[:40] # skip", "f() missing 1 required positional argument: 'y'", "python"),
]

# Method chaining (10)
py_codes += [
    ("print('hello world'.upper().split())", "['HELLO', 'WORLD']", "python"),
    ("print([3,1,2].sort() or [3,1,2])", "[3, 1, 2]", "python"),
    ("a=[3,1,2]; a.sort(); print(a)", "[1, 2, 3]", "python"),
    ("print([1,2,3].append(4) or [1,2,3,4])", "[1, 2, 3, 4]", "python"),
    ("print('abc'.center(7,'-'))", "--abc--", "python"),
    ("print('hello'.replace('l','').upper())", "HEO", "python"),
    ("print('foo bar baz'.split()[::-1])", "['baz', 'bar', 'foo']", "python"),
    ("print('  hello  '.strip().replace(' ','-'))", "hello", "python"),
    ("print('-'.join('hello'.split()))", "h-e-l-l-o", "python"),
    ("print([x.upper() for x in 'abc'])", "['A', 'B', 'C']", "python"),
]

# mutable vs immutable (10)
py_codes += [
    ("a=[1,2]; b=a; a.append(3); print(b)", "[1, 2, 3]", "python"),
    ("a=[1,2]; b=a[:]; a.append(3); print(b)", "[1, 2]", "python"),
    ("a=256; b=256; print(a is b)", "True", "python"),
    ("a=257; b=257; print(a is b)", "True", "python"),
    ("a='hello'; b='hello'; print(a is b)", "True", "python"),
    ("a=[1,2]; b=[1,2]; print(a==b, a is b)", "True False", "python"),
    ("def f(x=[]): return x; a=f(); b=f(); a.append(1); print(b)", "[1]", "python"),
    ("t=(1,[2]); t[1].append(3); print(t)", "(1, [2, 3])", "python"),
    ("s='hello'; print(id(s)==id('hello'))", "True", "python"),
    ("a={1,2}; b=a; a.add(3); print(b)", "{1, 2, 3}", "python"),
]

# Misc (30) - additional unique entries
py_codes += [
    ("print(ord('A'))", "65", "python"),
    ("print(chr(97))", "a", "python"),
    ("print(hex(255))", "0xff", "python"),
    ("print(oct(8))", "0o10", "python"),
    ("print(bin(7))", "0b111", "python"),
    ("print(abs(-5))", "5", "python"),
    ("print(round(2.5))", "2", "python"),
    ("print(round(3.5))", "4", "python"),
    ("print(min(3,1,4,1,5))", "1", "python"),
    ("print(max(3,1,4,1,5))", "5", "python"),
    ("print(pow(2,10))", "1024", "python"),
    ("print(pow(2,10,100))", "24", "python"),
    ("print(divmod(17,5))", "(3, 2)", "python"),
    ("print(sum(range(1,6)))", "15", "python"),
    ("print(any([]))", "False", "python"),
    ("print(all([]))", "True", "python"),
    ("print(sorted({3:1,1:4,2:9}))", "[1, 2, 3]", "python"),
    ("print(list(range(0,10,3)))", "[0, 3, 6, 9]", "python"),
    ("print(list(range(10,0,-3)))", "[10, 7, 4, 1]", "python"),
    ("print(list('python'))", "['p', 'y', 't', 'h', 'o', 'n']", "python"),
    ("print(tuple([1,2,3]))", "(1, 2, 3)", "python"),
    ("print(list((1,2,3)))", "[1, 2, 3]", "python"),
    ("print([1,2]*3)", "[1, 2, 1, 2, 1, 2]", "python"),
    ("print([1,2,3]+[4,5])", "[1, 2, 3, 4, 5]", "python"),
    ("print('ab'*3)", "ababab", "python"),
    ("print(3*'ab')", "ababab", "python"),
    ("print([1,2,3].index(2))", "1", "python"),
    ("print([1,2,3,2].remove(2) or [1,2,3,2])", "[1, 2, 3, 2]", "python"),
    ("a=[1,2,3]; a.pop(1); print(a)", "[1, 3]", "python"),
    ("a=[1,2,3]; a.insert(1,9); print(a)", "[1, 9, 2, 3]", "python"),
]

# Ternary, more bitwise, interesting (10)
py_codes += [
    ("print('even' if 4%2==0 else 'odd')", "even", "python"),
    ("print('even' if 5%2==0 else 'odd')", "odd", "python"),
    ("print(2**10 if 3>2 else 2**5)", "1024", "python"),
    ("print(0b1010 << 2)", "40", "python"),
    ("print(0b1010 >> 2)", "2", "python"),
    ("print(~0b1010 & 0b1111)", "5", "python"),
    ("print(0b1100 ^ 0b1010)", "6", "python"),
    ("print(bin(42).count('1'))", "3", "python"),
    ("print(int('1010',2))", "10", "python"),
    ("print(int('ff',16))", "255", "python"),
]

for code, resp, lang in py_codes:
    entries.append({
        "instruction": instr(code),
        "response": resp,
        "language": lang,
        "category": "output_prediction",
        "type": "manual",
        "format": "output_prediction"
    })

# ============================================================
# JAVASCRIPT (200 entries)
# ============================================================
js_codes = [
    # Type coercion (15)
    ("console.log('5' - 3)", "2", "javascript"),
    ("console.log('5' + 3)", "53", "javascript"),
    ("console.log('5' * '2')", "10", "javascript"),
    ("console.log('10' / '2')", "5", "javascript"),
    ("console.log('5' - 'x')", "NaN", "javascript"),
    ("console.log('5' - - '3')", "8", "javascript"),
    ("console.log(1 + '2' + 3)", "123", "javascript"),
    ("console.log(1 + 2 + '3')", "33", "javascript"),
    ("console.log(+'42')", "42", "javascript"),
    ("console.log(+'hello')", "NaN", "javascript"),
    ("console.log(!!'false')", "true", "javascript"),
    ("console.log(!!'')", "false", "javascript"),
    ("console.log([] + [])", "", "javascript"),
    ("console.log([] + {})", "[object Object]", "javascript"),
    ("console.log({} + [])", 0, "javascript"),  # this might be 0 due to {} being a block
    # == vs === (15)
    ("console.log(1 == '1')", "true", "javascript"),
    ("console.log(1 === '1')", "false", "javascript"),
    ("console.log(null == undefined)", "true", "javascript"),
    ("console.log(null === undefined)", "false", "javascript"),
    ("console.log(0 == false)", "true", "javascript"),
    ("console.log(0 === false)", "false", "javascript"),
    ("console.log('' == false)", "true", "javascript"),
    ("console.log('' === false)", "false", "javascript"),
    ("console.log([1,2] == '1,2')", "true", "javascript"),
    ("console.log([1,2] === '1,2')", "false", "javascript"),
    ("console.log(NaN == NaN)", "false", "javascript"),
    ("console.log(NaN === NaN)", "false", "javascript"),
    ("console.log([] == ![])", "true", "javascript"),
    ("console.log([] == 0)", "true", "javascript"),
    ("console.log('' == 0)", "true", "javascript"),
    # typeof (10)
    ("console.log(typeof 42)", "number", "javascript"),
    ("console.log(typeof 'hello')", "string", "javascript"),
    ("console.log(typeof undefined)", "undefined", "javascript"),
    ("console.log(typeof null)", "object", "javascript"),
    ("console.log(typeof typeof 1)", "string", "javascript"),
    ("console.log(typeof NaN)", "number", "javascript"),
    ("console.log(typeof function(){})", "function", "javascript"),
    ("console.log(typeof [])", "object", "javascript"),
    ("console.log(typeof {})", "object", "javascript"),
    ("console.log(typeof Symbol())", "symbol", "javascript"),
    # Boolean() on values (10)
    ("console.log(Boolean(0))", "false", "javascript"),
    ("console.log(Boolean(''))", "false", "javascript"),
    ("console.log(Boolean(null))", "false", "javascript"),
    ("console.log(Boolean(undefined))", "false", "javascript"),
    ("console.log(Boolean(NaN))", "false", "javascript"),
    ("console.log(Boolean('0'))", "true", "javascript"),
    ("console.log(Boolean('false'))", "true", "javascript"),
    ("console.log(Boolean([]))", "true", "javascript"),
    ("console.log(Boolean({}))", "true", "javascript"),
    ("console.log(Boolean(Infinity))", "true", "javascript"),
    # Array mutating methods (15)
    ("console.log([1,2,3].push(4))", 4, "javascript"),
    ("console.log([1,2,3].pop())", "3", "javascript"),
    ("console.log([1,2,3].shift())", "1", "javascript"),
    ("console.log([1,2,3].unshift(0))", 4, "javascript"),
    ("let a=[1,2,3]; a.splice(1,1,'x'); console.log(a)", "[ 1, 'x', 3 ]", "javascript"),
    ("let a=[1,2,3]; console.log(a.slice(1,2))", "[ 2 ]", "javascript"),
    ("let a=[1,2,3]; console.log(a.splice(1,2))", "[ 2, 3 ]", "javascript"),
    ("console.log([3,1,2].sort())", "[ 1, 2, 3 ]", "javascript"),
    ("console.log([3,1,2].reverse())", "[ 2, 1, 3 ]", "javascript"),
    ("let a=[1,2]; let b=a.concat([3,4]); console.log(b)", "[ 1, 2, 3, 4 ]", "javascript"),
    ("let a=[1,2,3]; console.log(a.indexOf(2))", "1", "javascript"),
    ("let a=[1,2,3]; console.log(a.includes(4))", "false", "javascript"),
    ("let a=[1,2,3]; a.fill(0,1); console.log(a)", "[ 1, 0, 0 ]", "javascript"),
    ("let a=[1,2,3]; console.log(a.join('-'))", "1-2-3", "javascript"),
    ("let a=[1,[2,[3]]]; console.log(a.flat(1))", "[ 1, 2, [ 3 ] ]", "javascript"),
    # Promise / setTimeout / event loop (10)
    ("Promise.resolve(1).then(console.log); console.log(2)")
    .replace('console.log(2)', 'console.log(2);'),  # I'll handle this carefully
    
]
