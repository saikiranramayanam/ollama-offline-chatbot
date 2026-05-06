# 🛍️ Offline Customer Support Chatbot (Llama 3 + Ollama)

##  Overview

This project is an **offline AI-powered customer support chatbot** built using **Llama 3** running locally via **Ollama**.  

The chatbot is designed to handle common e-commerce queries such as:
- Order tracking
- Returns and refunds
- Product inquiries
- Payment issues  

It ensures **complete data privacy** and **zero API cost** by running entirely on local hardware.

---

##  Features

- ✅ Runs completely offline (no internet required after setup)
- ✅ Uses Llama 3 via Ollama
- ✅ Handles real-world customer queries
- ✅ Implements prompt engineering (Zero-shot vs One-shot)
- ✅ Automated evaluation of responses
- ✅ Manual scoring for performance analysis

---

##  Key Concepts Used

- Large Language Models (LLMs)
- Prompt Engineering
  - Zero-shot prompting
  - One-shot prompting
- REST API integration
- Local AI deployment

---

##  Tech Stack

- Python  
- Ollama  
- Llama 3  
- Requests library  

---

##  Project Structure
project/
│
├── chatbot.py
├── README.md
├── setup.md
├── report.md
│
├── prompts/
│ ├── zero_shot_template.txt
│ └── one_shot_template.txt
│
└── eval/
└── results.md

---

## ▶️ How to Run the Project

Follow these steps to run the chatbot locally:

### 1. Install Ollama
Download from: https://ollama.com/download

---

### 2. Pull the Llama Model
```bash
ollama pull llama3
```

---

### 3. Start Ollama (if not running)
```bash
ollama run llama3
```

---

### 4. Set Up Python Environment
```bash
python -m venv venv
```

Activate environment:

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

---

### 5. Install Dependencies
```bash
pip install requests
```

---

### 6. Run the Chatbot
```bash
python chatbot.py
```

---

### 7. View Results
After execution, results will be saved in:

```
eval/results.md
```

## 🔄 How It Works

1. Customer queries are defined in `chatbot.py`
2. Prompts are generated using:
   - Zero-shot template
   - One-shot template
3. Requests are sent to Ollama API
4. Llama 3 generates responses
5. Results are stored in `eval/results.md`
6. Responses are manually evaluated

---

## 📊 Evaluation

Responses are evaluated using:

| Metric | Description |
|------|-------------|
| Relevance | Accuracy of response |
| Coherence | Clarity and readability |
| Helpfulness | Practical usefulness |

👉 One-shot prompting showed better performance than zero-shot.

---

##  Results Summary

- One-shot prompting produced more **structured and helpful responses**
- Zero-shot responses were more **generic**
- Local LLM performed well for basic support queries

---

##  Advantages

- No data leaves the system (privacy safe)
- No API cost
- Works without internet after setup

---

##  Limitations

- Slower response time on CPU
- No real-time data integration
- Possible incorrect responses (hallucination)

---

##  Future Improvements

- Add Streamlit UI
- Connect to real database
- Improve prompt engineering
- Multi-language support

---

##  Author

- Pavan Teja

---

## 📌 Conclusion

This project demonstrates how **LLMs can be deployed locally** to build privacy-focused AI applications while maintaining good performance using prompt engineering techniques.