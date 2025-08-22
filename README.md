# 🚀 NERPOS Workshop: From Prototype to Production

Welcome to **NLPOps with Python: From Prototype to Production**! 🎉  

In this 120-minute hands-on workshop, we’ll build and deploy a simple **NER (Named Entity Recognition)** and **POS (Part-of-Speech Tagger)** system using **spaCy + FastAPI**, and then take it all the way to **deployment in the cloud**.

---

## 📋 Prerequisites

Before starting, make sure you have:

- **Python 3.9+** 👉 [Download here](https://www.python.org/downloads/)
- **Git** 👉 [Download here](https://git-scm.com/downloads)
- **Docker Desktop** 👉 [Download here](https://www.docker.com/products/docker-desktop)
- A code editor (recommended: [VS Code](https://code.visualstudio.com/))
- A stable internet connection  

---
📂 Project Structure
```
nerpos/
│── app.py              # FastAPI application
│── requirements.txt    # Python dependencies
│── Dockerfile          # Containerization setup
│── static/
│    └── index.html     # Simple frontend interface
```
---
## ⚡ Step 1: Clone the Repository

Open your terminal (PowerShell on Windows, Terminal on macOS/Linux) and run:

```
git clone https://github.com/minna-lproc/nerpos/
cd nerpos
```

## ⚡ Step 2: Create a Virtual Environment
Windows (PowerShell)
```
python -m venv .nerpos
.nerpos\Scripts\activate
```
macOS/Linux
```
python3 -m venv .nerpos
source .nerpos/bin/activate
```
## ⚡ Step 3: Install Dependencies

Once the environment is activated, install everything from requirements.txt:
```
pip install --upgrade pip
pip install -r requirements.txt
```
## ⚡ Step 4: Download spaCy Model
We’ll use the English small model for NER and POS tagging:
```
python -m spacy download en_core_web_sm
```
## ⚡ Step 5: Run the Application
Start the FastAPI server with:
```
uvicorn app:app --reload --port 8000
```
If successful, you’ll see logs similar to:
```
Uvicorn running on http://127.0.0.1:8000
```
## ⚡ Step 6: Test the API

## ⚡ Step 7: Containerize with Docker
Create a Dockerfile in your project folder:
```
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py ./ 

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```
Build the image
```
docker build -t nerpos:latest .
```
Run the container
```
docker run -d -p 8000:8000 nerpos:latest
```
## ⚡ Step 8: Deploy to the Cloud (Render Example)
1. Push your project to GitHub.
   ```
   git init
   git remote add origin https://github.com/<your-username>/nerpos.git
   git add .
   git commit -m "Initial commit"
   git push -u origin main
   ```
2. Go to [Render](https://render.com/) and create a free account.
3. Create a New Web Service → Connect your GitHub repo.
4. Configure:
   - Environment: Docker
   - Build Command: leave blank (Docker handles it)
   - Start Command:
     ```
     uvicorn app:app --host 0.0.0.0 --port 8000
     ```
5. Deploy
   Your app will be live at:
   ```
   https://<your-service-name>.onrender.com/static/index.html
   ```
