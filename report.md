# 📊 Report: Offline Customer Support Chatbot using Llama 3

## 1. Introduction

The goal of this project is to build an offline customer support chatbot using a locally deployed Large Language Model (LLM) through Ollama. The chatbot is designed to handle common e-commerce queries such as order tracking, returns, refunds, and product inquiries.

This project focuses on ensuring **data privacy**, **zero API cost**, and **local inference**, which are critical requirements in modern applications handling sensitive user data.

Additionally, this project compares two prompt engineering techniques:
- Zero-shot prompting
- One-shot prompting

---

## 2. Methodology

### 2.1 Data Preparation

A total of 20 customer queries were created based on real-world e-commerce scenarios. These queries simulate common user interactions such as:
- Order tracking
- Returns and refunds
- Payment issues
- Product inquiries

---

### 2.2 Prompt Design

Two prompt templates were created:

#### 🔹 Zero-Shot Prompt
- Contains only instructions
- No example provided

#### 🔹 One-Shot Prompt
- Includes one example query-response pair
- Helps guide model output style

---

### 2.3 Evaluation Metrics

Each response was evaluated manually using the following criteria:

| Metric | Description |
|------|-------------|
| Relevance | How well the response answers the query |
| Coherence | Clarity and readability of response |
| Helpfulness | Usefulness and actionability |

Scores were given on a scale of **1 to 5**.

---

## 3. Results & Analysis

### 📊 Observations

- Both prompting techniques produced grammatically correct responses.
- One-shot prompting generated more structured and direct answers.
- Zero-shot responses sometimes asked follow-up questions instead of giving solutions.

---

### 📈 Performance Comparison

| Metric | Zero-Shot (Avg) | One-Shot (Avg) |
|-------|----------------|----------------|
| Relevance | 4.6 | 4.9 |
| Coherence | 5.0 | 5.0 |
| Helpfulness | 4.0 | 4.5 |

---

### 🔍 Key Findings

- One-shot prompting improves **helpfulness and clarity**
- Zero-shot is more **generic and less direct**
- Providing examples helps guide model behavior effectively

---

## 4. Conclusion

This project demonstrates that a locally deployed LLM can effectively handle customer support queries while ensuring complete data privacy.

The results show that:
- One-shot prompting significantly improves response quality
- Llama 3 is capable of handling basic customer support tasks

---

## 5. Limitations

- Responses may not always be accurate (hallucination risk)
- No real-time data (order tracking is simulated)
- Slower performance due to CPU-based inference

---

## 6. Future Improvements

- Add a user interface (Streamlit or web app)
- Integrate with real databases (orders, users)
- Improve prompt engineering with few-shot learning
- Add multi-language support

---

## 7. Final Summary

This project successfully demonstrates:
- Offline LLM deployment using Ollama
- Prompt engineering techniques
- Real-world chatbot application

It provides a strong foundation for building privacy-focused AI systems in production environments.