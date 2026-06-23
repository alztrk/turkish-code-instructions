import json, textwrap

entries = []

def add(instruction, py=None, js=None, java=None, go=None):
    for lang, code in [("python", py), ("javascript", js), ("java", java), ("go", go)]:
        if code:
            entries.append({
                "instruction": instruction,
                "response": textwrap.dedent(code).strip(),
                "language": lang,
                "category": "cross_lang",
                "type": "manual",
                "format": "cross_lang"
            })

add("Ikili arama algoritmasini uygulayan fonksiyon yaz",
    py="def binary_search(arr, target):\n    left, right = 0, len(arr) - 1\n    while left <= right:\n        mid = (left + right) // 2\n        if arr[mid] == target: return mid\n        elif arr[mid] < target: left = mid + 1\n        else: right = mid - 1\n    return -1",
    js="function binarySearch(arr, target) {\n    let left = 0, right = arr.length - 1;\n    while (left <= right) {\n        const mid = Math.floor((left + right) / 2);\n        if (arr[mid] === target) return mid;\n        else if (arr[mid] < target) left = mid + 1;\n        else right = mid - 1;\n    }\n    return -1;\n}",
    java="public static int binarySearch(int[] arr, int target) {\n    int left = 0, right = arr.length - 1;\n    while (left <= right) {\n        int mid = left + (right - left) / 2;\n        if (arr[mid] == target) return mid;\n        else if (arr[mid] < target) left = mid + 1;\n        else right = mid - 1;\n    }\n    return -1;\n}",
    go="func BinarySearch(arr []int, target int) int {\n    left, right := 0, len(arr)-1\n    for left <= right {\n        mid := left + (right-left)/2\n        if arr[mid] == target { return mid }\n        if arr[mid] < target { left = mid + 1 } else { right = mid - 1 }\n    }\n    return -1\n}")

print(len(entries))
