# 🔐 Basic SIEM Tool

A lightweight Security Information and Event Management (SIEM) tool that includes a Flask UI, log collection, rule-based detection, and full ELK Stack integration using Docker.

> **Developed by:** Pavan Teja  
> **GitHub:** [@Pavansoc](https://github.com/Pavansoc)

---

## 📦 Features

- 🧪 Simulated log collection with CLI menu (Metasploit-style)
- 📜 Rule engine to detect suspicious activity
- 🌐 Flask dashboard to display alerts
- 📊 ELK Stack integration (Elasticsearch, Logstash, Kibana)
- 🐳 Docker support for quick deployment
- ✅ Works on Linux (test-ready in VMs)

---

## 🚀 Usage

### 🖥️ 1. Run Locally (Manual)

```bash
git clone https://github.com/Pavansoc/basic-siem.git
cd basic-siem

pip install flask

cd log_collector
python3 collect_logs.py

cd ../flask_ui
python3 app.py

 2. Run with Docker (Recommended)

# From root of project
docker-compose up --build

Access the apps:

    Flask UI: http://localhost:5000

    Kibana: http://localhost:5601

    Elasticsearch: http://localhost:9200

🧪 3. Setup on Virtual Linux OS

    💡 Use the included script: setup_siem_linux.sh

chmod +x setup_siem_linux.sh
./setup_siem_linux.sh

This script will:

    Update your system

    Install Python, Docker, Git

    Clone this repo

    Run the Docker environment
    