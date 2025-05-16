# AI Agents Platform 🚀

A modular, extensible CLI-based AI agent framework in Python—wired to an LLM for perception, planning, action, and (optional) memory. This project demonstrates how to architect and implement a production-grade AI agent from scratch, starting with a simple To-Do List Assistant.

---

## 📺 Video Demonstration

Watch the hands‑on tutorial on YouTube: **[Building Your First AI Agent CLI](https://youtu.be/HwHTPtBdBLY)**

---

## 🔍 Overview

This repo implements a foundational AI agent with:

* **Perception**: Normalizes and parses user inputs into structured commands.
* **Planning**: Uses OpenAI’s GPT model to decide which tool to call and with what arguments.
* **Action**: Executes tools (add/list/remove tasks) against a simple persistence layer (`tasks.txt`).
* **Memory (Future)**: Placeholder module for adding conversational context and history.

By following best practices in software engineering—modularity, testing, secrets management—you’ll learn how to build robust, maintainable agents.

---

## ⚙️ Features

* **CLI Orchestrator** (`agent.py`): Interactive loop accepting natural language commands.
* **LLM Integration**: Deterministic prompts (temperature=0) returning JSON for reliable parsing.
* **Task Management**: Flat‑file persistence with `add_task`, `list_tasks`, and `remove_task` functions.
* **Extensible Architecture**: Separate modules for perception, reasoning, and action—ready for future memory, plugins, and HTTP APIs.

---

## 🏗 Architecture

```text
Input Adapter  →  Perception  →  Planning (LLM)  →  Action  →  Output Adapter
                         ↕
                    Memory (Context)
```

See the [architecture diagram](docs/architecture.png) for a visual overview.

---

## 📋 Prerequisites

* Python 3.10+
* An OpenAI API key
* Git (for version control)

---

## 🛠 Installation

1. **Clone the repo**:

   ```bash
   git clone https://github.com/<your‑org>/ai‑agents‑platform.git
   cd ai‑agents‑platform
   ```
2. **Create & activate a virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate    # macOS/Linux
   # venv\Scripts\activate    # Windows
   ```
3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```
4. **Configure your OpenAI key**:

   ```bash
   echo "OPENAI_API_KEY=sk-<your_key>" > .env
   ```

---

## 🚀 Usage

1. **Activate your environment**:

   ```bash
   source venv/bin/activate
   ```
2. **Run the agent**:

   ```bash
   python agent.py
   ```
3. **Try natural language commands**:

   ```text
   > add buy groceries
   ✅ Added task: buy groceries

   > show my tasks
   📝 Your tasks:
     1. buy groceries

   > remove task 1
   🗑️ Removed task: buy groceries
   ```

---

## 🔧 Configuration

* **`.env`**: Set `OPENAI_API_KEY`.
* **`requirements.txt`**: Pin dependencies.
* **`tasks.txt`**: Automatically created in the project root when adding tasks.

---

## 📦 Project Structure

```
ai-agents-platform/
├── .env                # API key (gitignored)
├── requirements.txt    # Locked Python packages
├── agent.py            # Main CLI orchestrator
└── modules/
    ├── perception.py   # Input parsing
    ├── brain.py        # LLM-based planning
    └── action.py       # Task management tools
```

---

## 📈 Roadmap

* **Lesson 2**: Modularize code into packages, add unit tests, and implement dependency injection.
* **Lesson 3**: Introduce a Memory layer (Redis or in-memory cache).
* **Lesson 4**: Develop a plugin system and dynamic tool registry.
* **Lesson 5+**: Build an HTTP API, SDK/CLI, Dashboard, and security hardening.

---

## 🤝 Contributing

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/your-feature`.
3. Commit your changes: `git commit -m "Add some feature"`.
4. Push to the branch: `git push origin feature/your-feature`.
5. Open a Pull Request describing your changes.

Please ensure tests pass and follow existing code style.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙏 Acknowledgments

* Inspired by LangChain, CrewAI, and core agent design patterns.
* Thanks to the OpenAI team for the GPT API.

---

Happy coding, and let’s build powerful agents together! 🚀
