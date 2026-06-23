import json
entries = []

def T(code, test, lang):
    entries.append({"instruction": "Asagidaki fonksiyon icin unit test yaz:\n" + code, "response": test, "language": lang, "category": "test", "type": "manual", "format": "test"})

P="python";JS="javascript";JV="java";G="go"

def pyA(asserts):
    return "def test_():\n    " + "\n    ".join(asserts) + "\nimport pytest; pytest.main()"

def jsA(asserts):
    parts = ["console.assert(" + p + ")" for p in asserts]
    return "function test_(){\n  " + ";\n  ".join(parts) + ";\n}test_();"

def goA(name, asserts):
    return "package main\nimport \"testing\"\nfunc Test" + name + "(t *testing.T) {\n    " + "\n    ".join(asserts) + "\n}"

def javaA(name, asserts):
    lines = ["        " + p + ";" for p in asserts]
    return "import org.junit.*;\nimport static org.junit.Assert.*;\npublic class " + name + "Test {\n    @Test\n    public void test" + name + "() {\n" + "\n".join(lines) + "\n    }\n}"

def add(name, code, asserts, lang, make):
    test = make(asserts) if lang in (P, JS) else make(name, asserts)
    T(code, test, lang)

counts = {P:0, JS:0, JV:0, G:0}

# PYTHON (200)
py_funcs = [
    ("add", "add(a,b)", "return a+b", ["add(2,3)==5", "add(-1,1)==0", "add(0,0)==0"]),
]
for n, sig, body, asserts in py_funcs:
    code = "def " + sig + ": " + body
    test = "def test_" + n + "():\n    " + "\n    ".join(asserts) + "\nimport pytest; pytest.main()"
    T(code, test, P)
    counts[P] += 1

print("Total:", sum(counts.values()))
print("Counts:", counts)
