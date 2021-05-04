def query(s):
    while "()" in s or "{}" in s or '[]' in s:
        s = s.replace("()", "").replace('{}', "").replace('[]', "")
    return s == ''
    print(query(s)
query("([]{}{})")