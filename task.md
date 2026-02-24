# Assignment Title

## Domain-Specific LLM Assistant using OpenRouter and LangChain

---

## Objective

Build a **domain-focused AI assistant** using the **OpenRouter API** integrated through **LangChain**.  
The assistant must **strictly control responses** using prompt engineering techniques.

Students may choose any domain of interest (e.g., healthcare, finance, law, education, sports analytics, software engineering, marketing, environmental science, travel advisory, etc.).

---

## Domain Selection

- Choose **one specific domain**.
- Clearly define the **scope** of the assistant.
- Clearly define **what the assistant will NOT answer**.

---

## Basic Requirements

### 1. Technical Stack

- Use **OpenRouter API** for LLM access.
- Use **LangChain** for prompt templates and model orchestration.
- Implement a **basic LLM chain** (agent optional).
- Single-turn interaction is sufficient (multi-turn optional).

---

### 2. Prompt Engineering (Mandatory)

The solution must include:

- Explicit **role definition**
- Clear **domain boundaries**
- Structured output format (fixed sections)
- Tone control
- Mandatory disclaimer
- Refusal behavior for out-of-domain queries

---

### 3. Domain Control

- The assistant must reject or safely redirect unrelated questions.
- The assistant must avoid unsafe or unauthorized advice.
- All responses must follow the predefined output structure.

---

### 4. Testing

- Provide at least **10 test queries**.
- Include at least **2 out-of-domain queries** to demonstrate refusal behavior.

---

## Output Criteria

Each response must:

- Follow a consistent structured format.
- Stay strictly within the chosen domain.
- Maintain a consistent professional tone.
- Avoid unsupported or fabricated claims.

---

## Optional UI Elements (Not Mandatory)

If implementing a UI, you may include:

- Chat-style interface
- Domain selection input
- Temperature control slider
- Conversation history display
- Reset conversation option

---

## Evaluation Criteria

- Quality of prompt engineering
- Strict domain adherence
- Output structure consistency
- Safety and refusal handling
- Proper integration of OpenRouter and LangChain

---

## Submission Requirements

Submit the following:

- Source code
- Prompt template(s)
- Sample outputs
- Short explanation (1–2 pages) describing:
  - Domain scope
  - Prompt design strategy
  - Limitations observed

---
