
import sys, pathlib
import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path

from ..cfg_extraction.parse_ll_to_cfg import parse_ir_to_edges  # type: ignore

def main(path):
    text = Path(path).read_text(encoding="utf-8", errors="ignore")
    _, edges = parse_ir_to_edges(text)
    G = nx.DiGraph()
    G.add_edges_from(edges or [("entry","exit")])
    nx.draw(G, with_labels=True)
    plt.title("CFG (placeholder)")
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python visualize_cfg.py path/to/file.ll")
        sys.exit(1)
    main(sys.argv[1])
