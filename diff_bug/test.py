from difflib import Differ
import json

def load_file(file_path):
    with open(file_path, "r", encoding="utf-8-sig") as f:
        content = json.loads(f.read())
        return json.dumps(content, indent=2, ensure_ascii=False).splitlines()

# Load files
base_path = "figuremap/avatar.figuremap.old"
temp_name = "figuremap/avatar.figuremap.new"

base_comp = load_file(base_path)
new_comp = load_file(temp_name)

# Compare files
d = Differ()
result = d.compare(base_comp, new_comp)

# Only keep diff lines
filtered_result = [line for line in result if line.startswith("- ") or line.startswith("+ ")]
formatted_result = "\n".join(filtered_result)

# Save output
with open("result.txt", "w", encoding="utf-8") as f:
    f.write(formatted_result)
