# 🔓 Vulnerable API - AppSec Lab

## 🧾 Descrição
API propositalmente vulnerável desenvolvida para estudo de **Application Security (AppSec)**.  
Este projeto simula falhas reais encontradas em aplicações web modernas.

---

## 🎯 Objetivo
Permitir que desenvolvedores e estudantes pratiquem:

- Exploração de vulnerabilidades
- Entendimento de falhas de segurança
- Mentalidade ofensiva (hacker mindset)

---

## 💥 Vulnerabilidades Implementadas

- **SQL Injection** → Bypass de autenticação
- **IDOR (Insecure Direct Object Reference)** → Acesso a dados de outros usuários
- **Stored XSS** → Execução de scripts maliciosos
- **JWT Inseguro** → Token manipulável
- **Upload Inseguro** → Upload sem validação
- **Admin sem autenticação** → Acesso indevido

---

## ⚙️ Tecnologias

- Python
- FastAPI
- SQLite
- JWT

---

## 🚀 Como rodar

```bash
pip install -r requirements.txt
python init_db.py
uvicorn app:app --reload
