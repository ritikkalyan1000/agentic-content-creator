# agentic-content-creator
A Streamlit app powered by LangGraph agents that turns simple topics into fully researched, illustrated markdown blogs

# ✍️ Agentic Content Creator

An autonomous, multi-agent workflow built with **LangGraph** and **Streamlit** that takes a simple user prompt and orchestrates a team of AI agents to research, write, and illustrate a complete, publication-ready blog post in Markdown.

## 🚀 Overview

This project utilizes a graph-based state machine to manage complex LLM interactions. Instead of relying on a single prompt, the application routes tasks through specialized agents:
<img width="120" height="505" alt="image" src="https://github.com/user-attachments/assets/fae8427d-7f47-46de-91e2-080dc0f43989" />

- A **Router** determines if external internet research is required.
- A **Researcher** fetches real-time context using the Tavily Search API.
- An **Orchestrator** develops a comprehensive content plan and breaks it down into sub-tasks.
- **Worker Agents** generate targeted content for specific sections.
- A **Reducer** stitches the content together and intelligently places image placeholders.
- An **Image Generator** uses Google's Imagen 3 to create contextually relevant visuals.

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **Agent Orchestration:** LangGraph, LangChain
* **Language Models:** OpenAI (`gpt-4o` or similar via `ChatOpenAI`)
* **Image Generation:** Google GenAI (Imagen 3)
* **Search/Tools:** Tavily API

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/agentic-content-creator.git](https://github.com/YOUR_USERNAME/agentic-content-creator.git)
   cd agentic-content-creator
   ```
2. **Create a virtual environment:**
```
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. **Install dependencies:**
   ```pip install -r requirements.txt```
4.**Set up Environment Variables:**
  Create a .env file in the root directory and add your API keys:
```
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
GEMINI_API_KEY=your_gemini_api_key
```

5. **Usage**
   ```
   streamlit run app.py
   ```
   replace app with you frontend app like in my case it is frontend.py
   
