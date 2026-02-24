# Submission: Domain-Specific AI Assistant - VK64 (Software Engineering)

## 1. Project Overview

This project implements **VK64**, a Software Engineering Expert AI Assistant using **FastAPI** (MVC Pattern), **LangChain**, and **OpenRouter API**. The assistant is strictly bounded to the software engineering domain, providing technical analysis, architectural solutions, and code implementations.

## 2. Technical Stack

- **Backend**: FastAPI (Python)
- **LLM Orchestration**: LangChain
- **LLM Provider**: OpenRouter (`upstage/solar-pro-3:free`)
- **Frontend**: Vanilla HTML/CSS/JS with modern glassmorphism design.
- **Environment**: `.env` for secret management.

## 3. Prompt Design Strategy

The system prompt is engineered with:

- **Role Definition**: "Expert Software Engineer, Architect, Mathematician, and Problem Solver."
- **In-Domain Examples**: Explicitly listed (System Design, Algorithms, Mathematics).
- **Out-of-Domain Refusal**: A predefined friendly yet professional refusal message.
- **Output Constraints**: Mandatory sections (Analysis, Solution, Implementation, Closing, Disclaimer).
- **Tone Control**: Professional and technical.

## 4. Source Code Highlights

### System Prompt (LangChain)

```python
system_prompt = \"\"\"
You are an Expert Software Engineer...
### Rules:
1. If the user asks anything outside of Software Engineering... decline politely.
2. Use a professional but friendly tone.
4. Mandatory Disclaimer: Every response must end with \"--- Disclaimer: ...\"
\"\"\"
```

### FastAPI Chat Controller

```python
@router.post("/chat")
async def chat(request: ChatRequest):
    response_text = await llm_service.get_response(request.message)
    return ChatResponse(response=response_text)
```

## 5. Sample Outputs

### User: "Explain the Strategy Pattern."

**Assistant**:

> **Analysis**: The Strategy Pattern is a behavioral design pattern that turns a set of behaviors into objects...
> **Solution**: Use this when you have multiple algorithms for a specific task and want to switch them at runtime...
> **Implementation**: `class PaymentStrategy: ...`
> **Disclaimer**: This is technical advice based on standard software engineering practices...

### User: "Tell me a recipe for pizza."

**Assistant**:

> Hello! I am specialized in Software Engineering and related technical domains. I would be happy to help you with coding or architectural questions, but I cannot assist with recipes. How about we discuss some software patterns instead?

## 6. Limitations Observed

- **Knowledge Cutoff**: The model may not be aware of very recent library releases (post-2024).
- **Complex UI**: While the UI is responsive, deep complex mathematical renderings (like LaTeX) might require additional libraries like MathJax.
- **Single-Turn focus**: Although history is managed in the UI, the current backend implementation is optimized for single-turn per request (context is passed via UI).

---

_Created by KALEESWARAN V_
