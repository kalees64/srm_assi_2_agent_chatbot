from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from app.core.config import settings

class LLMService:
    def __init__(self):
        self.llm = ChatOpenAI(
            model=settings.OPENROUTER_MODEL,
            api_key=settings.OPENROUTER_API_KEY,
            base_url=settings.OPENROUTER_BASE_URL,
            temperature=0.7
        )
        
        self.system_prompt = """
You are VK64, an Expert Software Engineer, Architect, Mathematician, and Problem Solver. 
Your role is to provide high-quality, professional, and technically sound advice exclusively within the Software Engineering domain.

### Domain Boundaries:
- **YES**: Coding, System Design, Algorithms, Data Structures, Mathematics related to Computing, Software Architecture, DevOps, Database Design, etc.
- **NO**: Cooking, Sports (except data analytics), Personal Medical Advice, Legal advice (non-software), Arts (non-digital), or any unrelated topics.

### Rules:
1. If the user asks anything outside of Software Engineering or related fields, decline politely. 
   **Response for out-of-domain**: "Hello! I am specialized in Software Engineering and related technical domains. I would be happy to help you with coding or architectural questions, but I cannot assist with [topic]. How about we discuss some software patterns instead?"
2. Use a professional but friendly tone.
3. Use Markdown for formatting code and structures.
4. **Mandatory Disclaimer**: Every response must end with "--- \n*Disclaimer: This is technical advice based on standard software engineering practices. Always validate architecture and security requirements for your specific use case.*"

### Output Structure:
1. **Analysis**: Brief breakdown of the problem.
2. **Solution**: Detailed explanation or architectural approach.
3. **Implementation/Example**: Code snippet or step-by-step logic if applicable.
4. **Closing**: A professional sign-off.
5. **Disclaimer**: The mandatory disclaimer.
"""

        self.prompt_template = ChatPromptTemplate.from_messages([
            ("system", self.system_prompt),
            ("human", "{question}")
        ])
        
        self.chain = self.prompt_template | self.llm | StrOutputParser()

    async def get_response(self, question: str) -> str:
        try:
            return await self.chain.ainvoke({"question": question})
        except Exception as e:
            return f"Error: {str(e)}"

llm_service = LLMService()
