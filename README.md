# Agent Resume Builder

🚀 An agent-based tool built with **MCP** and **FastAPI** that generates automated CVs tailored to a given job profile by adapting an existing CV.  

---

## Features
- Uses **FastAPI** for API endpoints.  
- Integrates with **MCP** for agent orchestration.  
- Parses existing CVs (PDF/Word).  
- Aligns CVs with job descriptions using LLMs.  
- Generates new CVs in structured format.  

---

## Project Structure

```
cv-agent-tool/
│── app/
│   ├── agents/           # MCP agent logic
│   ├── api/              # FastAPI routes
│   ├── core/             # Config & utilities
│   ├── services/         # CV parsing & LLM services
│   └── main.py           # FastAPI entry point
│
├── data/                 # Sample CVs & job profiles
├── pyproject.toml        # Project dependencies
├── README.md             # Project documentation
└── .env                  # Environment variables (ignored in git)
```

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/cv-agent-tool.git
cd cv-agent-tool
```

### 2. Install Dependencies
This project uses **Poetry**. If you don’t have it:  
```bash
pip install poetry
```

Then install project dependencies:
```bash
poetry install
```

👉 [optional] If you want dev tools (testing, linting):  
```bash
poetry install --with dev
```

### 3. Set Environment Variables
Create a `.env` file in the project root:
```
OPENAI_API_KEY=your_api_key_here
```
(Add any other keys/configs your MCP agent or services need.)

### 4. Run the Application
```bash
poetry run uvicorn app.main:app --reload
```

Now visit **http://127.0.0.1:8000/docs** for interactive API docs (Swagger UI).

---

## Example Endpoints

- `GET /health` → Check if server is running.  
- `POST /generate-cv` → Submit existing CV + job profile → Get a tailored CV back.  

---

## Running Tests
```bash
poetry run pytest
```

---

## Contributing
1. Fork the repository.  
2. Create a new branch (`git checkout -b feature-name`).  
3. Commit your changes (`git commit -m "Added feature"`).  
4. Push to your fork (`git push origin feature-name`).  
5. Open a Pull Request 🚀.  

---

## License
MIT License © 2025  
