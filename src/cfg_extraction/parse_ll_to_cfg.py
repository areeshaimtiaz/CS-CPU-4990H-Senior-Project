
import sys, re, pathlib
import networkx as nx

def parse_ir_to_edges(ir_text: str):
    # Extremely simple placeholder: detect 'br' instructions and labels
    # This should be replaced with proper IR parsing.
    labels = re.findall(r'([a-zA-Z0-9_]+):', ir_text)
    edges = []
    for m in re.finditer(r'br .* label %([a-zA-Z0-9_]+), label %([a-zA-Z0-9_]+)', ir_text):
        edges.append((m.group(1), m.group(2)))
    return labels, edges

def main(path):
    text = pathlib.Path(path).read_text(encoding="utf-8", errors="ignore")
    labels, edges = parse_ir_to_edges(text)
    print("Labels:", labels[:10], "...")
    print("Edges :", edges[:10], "...")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python parse_ll_to_cfg.py path/to/file.ll")
        sys.exit(1)
    main(sys.argv[1])
