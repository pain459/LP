import os
directory = "."
lines = ["# Project Scripts\n", "\n## Index\n"]

entries = []
for filename in os.listdir(directory):
    if filename.endswith(".sh") or filename.endswith(".py"):
        filepath = os.path.join(directory, filename)
        # Extract metadata from script (e.g., first comment lines)
        with open(filepath, 'r') as f:
            doc_lines = []
            for line in f:
                if line.strip().startswith("#"):
                    doc_lines.append(line.strip("# ").strip())
                else:
                    # Stop reading after initial comment block
                    break
        description = " ".join(doc_lines) if doc_lines else "No description available."
        entries.append((filename, description))

# Create a table of contents or listing
for fname, desc in entries:
    lines.append(f"- [{fname}](#{fname.replace('.', '-')}) - {desc}\n")

lines.append("\n## Details\n")
for fname, desc in entries:
    lines.append(f"### {fname}\n")
    lines.append(f"{desc}\n\n")

with open("README.md", "w") as readme:
    readme.writelines(lines)
