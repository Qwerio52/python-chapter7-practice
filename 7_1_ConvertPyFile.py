import keyword
import re

def process_py_file(src_path, dst_path):
    kw_set = set(keyword.kwlist)
    with open(src_path, "r", encoding="utf-8") as f:
        content = f.read()

    def replace_func(match):
        word = match.group(0)
        if word in kw_set:
            return word
        return word.upper()

    new_content = re.sub(r"[a-zA-Z_][a-zA-Z0-9_]*", replace_func, content)
    with open(dst_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Process finished, output file: {dst_path}")

if __name__ == "__main__":
    process_py_file("test.py", "test_upper.py")