cat > README.md << 'EOF'
# 🦎 SINT-O TOOL

**Advanced OSINT Aggregator** — Terminal Hunter

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-brightgreen?style=for-the-badge)](LICENSE)
[![Version](https://img.shields.io/badge/Version-0.2-success?style=for-the-badge)](https://github.com/stupidcollegegirl/sint-o-tool)

> Fast, beautiful and deadly accurate OSINT tool in your terminal.

---

### 🎥 Demo

![SINT-O TOOL Demo](https://github.com/stupidcollegegirl/sint-o-tool/blob/main/demo.gif)  

---

### ✨ Key Features

| Feature                    | Status     | Description |
|---------------------------|------------|-------------|
| **Multi-target Scan**     | ✅ Done    | Username, Email, Domain, Phone, IP |
| **Beautiful Rich UI**     | ✅ Done    | Lizard ASCII + modern panels |
| **Async & Parallel**      | ✅ Done    | Lightning fast checks |
| **Risk Score**            | ✅ Done    | Smart threat evaluation |
| **Phone Lookup (RU)**     | ✅ Done    | Operator + region |
| **IP Geo + Proxy detect** | ✅ Done    | Full geolocation |
| **Modular Providers**     | ✅ Done    | Easy to add new sources |

---

### 🚀 Quick Start

```
# 1. Clone
git clone https://github.com/stupidcollegegirl/sint-o-tool.git
cd sint-o-tool

# 2. Install
pip install -r requirements.txt

# 3. Run
python main.py
```

📁 Project Structure
textsint-o-tool/
├── main.py                 # Main CLI menu
├── core/
│   ├── orchestrator.py
│   └── scanner.py
├── providers/              # All data sources
├── utils/
│   └── formatter.py
├── requirements.txt
└── README.md
