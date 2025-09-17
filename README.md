
# AI-CFG-Optimizer

AI-assisted code optimization for C++ using **Control Flow Graphs (CFGs)** and machine learning.

## ✨ What it does
- Parses C++ → LLVM IR → CFG
- Extracts graph features
- Predicts suggested optimizations (baseline ML → optional GNN in future)
- Applies/compares optimizations and reports speedups
- (Optional) Flask UI for uploading `.cpp` files and viewing results

## 🗂 Repo Structure
```
AI-CFG-Optimizer/
├─ src/
│  ├─ cfg_extraction/       # C++ → LLVM IR (.ll) → CFG edges
│  ├─ cfg_visualization/    # Graphviz/NetworkX visualization
│  ├─ ml_model/             # Baseline model + notebooks
│  └─ ui/                   # Flask app
├─ experiments/             # Benchmarks & logs
└─ docs/
   ├─ paper/                # Research paper draft & figures
   ├─ honors/               # Honors proposal & artifacts
   └─ rsrc/figures/         # Images
```

## 🔧 Quickstart (dev)
1. Install LLVM (clang/opt). On Ubuntu:
   ```bash
   sudo apt-get update && sudo apt-get install -y clang llvm
   ```
2. Create a virtual env & install deps:
   ```bash
   python3 -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. Try sample pipeline:
   ```bash
   # 1) compile to IR
   clang -emit-llvm -S -o ./experiments/sample.ll ./src/cfg_extraction/samples/sample.cpp
   # 2) parse and visualize
   python ./src/cfg_visualization/visualize_cfg.py ./experiments/sample.ll
   # 3) train baseline model (toy data)
   python ./src/ml_model/train_baseline.py
   # 4) run Flask UI
   python ./src/ui/app.py
   ```

## 📄 Honors Deliverables
- Proposal form (see `docs/honors/`)
- Research paper draft + figures (`docs/paper/`)
- Presentation assets

## 📚 References
- Dragon Book, Ch. 9
- LLVM LangRef + Passes docs
- CFG tutorials (CMU)
