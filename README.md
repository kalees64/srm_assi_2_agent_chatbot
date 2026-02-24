# VK64 - Expert Software Engineering AI Assistant

Welcome to **VK64**, a specialized AI platform designed for Software Engineers, Architects, and technical problem solvers. This application uses FastAPI, LangChain, and OpenRouter to provide deep technical insights while maintaining strict domain boundaries.

---

## 🚀 Getting Started

### 1. Prerequisites

- Python 3.10 or higher
- An OpenRouter API Key ([Get one here](https://openrouter.ai/settings/keys))

### 2. Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/kalees64/srm_assi_2_agent_chatbot.git
cd srm_assi_2_agent_chatbot
pip install -r requirements.txt
```

### 3. Configuration

Create a `.env` file in the root directory (or modify the existing one) with the following content:

```env
OPENROUTER_API_KEY=your_api_key_here
OPENROUTER_MODEL=arcee-ai/trinity-large-preview:free
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
```

### 4. Running the Application

Start the development server:

```bash
python main.py
```

Visit `http://127.0.0.1:8000` in your web browser.

---

## 🛠 User Guide: How to Prompt VK64

VK64 is an **Expert Software Engineering** agent. To get the best results, follow these guidelines:

### ✅ What to Ask (In-Domain)

VK64 excels at:

- **Architecture & System Design**: "How should I design a scalable notification system?"
- **Algorithm Optimization**: "What is the Big O complexity of this Python function and how can I improve it?"
- **Design Patterns**: "Show me an example of the Observer pattern in TypeScript."
- **Mathematics for CS**: "Explain how the Diffie-Hellman key exchange works with a practical example."
- **Debugging & Refactoring**: "My React component is re-rendering too often. How can I use memoization?"

### ❌ What NOT to Ask (Out-of-Domain)

VK64 will politely decline queries unrelated to software engineering, such as:

- Cooking recipes
- Sports scores or updates
- General medical or legal advice
- Arts or lifestyle topics

### 💡 Pro-Tips for Better Responses

1. **Be Specific**: Instead of "How do I fix my code?", try "Why am I getting a `MemoryError` when processing a 2GB CSV file in Python?"
2. **Context Matters**: Mention your tech stack (e.g., "In a FastAPI and Docker environment...") for more relevant architectural advice.
3. **Request Structure**: You can ask for specific formats, like "Explain this using a sequence diagram description" or "Provide a step-by-step migration guide."

---

## 📂 Project Architecture (MVC)

- **app/core**: Configuration and settings management.
- **app/models**: Data structures and Pydantic validation schemas.
- **app/services**: Core logic, LangChain orchestration, and Prompt Engineering.
- **app/controllers**: FastAPI endpoints and routing.
- **app/static & templates**: Modern, responsive UI with chat history.

---

## 📝 License

Created by **KALEESWARAN V** as part of the M.Tech Assignment.
[GitHub Repository](https://github.com/kalees64/srm_assi_2_agent_chatbot)
