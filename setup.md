# ⚙️ Setup Guide: Offline Customer Support Chatbot

## 🧩 1. Install Ollama

Download and install Ollama from:

👉 https://ollama.com/download

---

## ✅ 2. Verify Installation

Open terminal / command prompt and run:

```bash
ollama --version
```

If installed correctly, it will display the version.

---

## 📦 3. Pull the Llama Model

Run the following command to download the model:

```bash
ollama pull llama3
```

> Note: This is a one-time download (~2GB)

---

## ▶️ 4. Run the Model (Optional Check)

```bash
ollama run llama3
```

Type any query to test and type `/bye` to exit.

---

## 🐍 5. Set Up Python Environment

Navigate to your project folder:

```bash
python -m venv venv
```

### Activate Environment

#### Windows:
```bash
venv\Scripts\activate
```

#### Mac/Linux:
```bash
source venv/bin/activate
```

---

## 📚 6. Install Required Libraries

```bash
pip install requests
```

---

## ▶️ 7. Run the Project

Make sure Ollama is running in the background.

Then run:

```bash
python chatbot.py
```

---

## 📂 8. View Results

After execution completes, results will be saved in:

```
eval/results.md
```

---

## ⚠️ Troubleshooting

### ❌ Connection refused
👉 Make sure Ollama is running

---

### ❌ Model not found
```bash
ollama pull llama3
```

---

### ❌ Slow responses
👉 This is normal for CPU-based systems

---

## ✅ Done!

Your offline chatbot is now ready 🎉