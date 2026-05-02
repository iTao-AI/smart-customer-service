[English](./README.md) | [中文](./README_CN.md)

# Smart Customer Service

A production-grade dialogue system framework for e-commerce customer service, built on LangGraph + LangChain. Supports YAML-defined conversation flows, GraphRAG knowledge base retrieval, and multi-channel access (REST API, WebSocket, CLI).

## Architecture

```
User Input (REST / WebSocket / CLI)
    │
    ▼
┌──────────────────────────────────────┐
│         LangGraph Pipeline            │
│  ┌────────────┐  ┌─────────────────┐ │
│  │ Command    │→ │ Flow Executor   │ │
│  │ Generator  │  │ (YAML flows)    │ │
│  └────────────┘  └────────┬────────┘ │
│                           │          │
│  ┌────────────┐  ┌────────▼────────┐ │
│  │ NLG        │← │ Action Executor │ │
│  │ (Response) │  │ + Policy Router │ │
│  └────────────┘  └────────┬────────┘ │
└───────────────────────────┼──────────┘
                            │
              ┌─────────────┼─────────────┐
              ▼             ▼             ▼
         MySQL        Neo4j          Custom
         (Orders)     (GraphRAG)     Actions
```

**Dialogue flow:**
1. User input → LLM generates structured commands (intent + slots)
2. Flow executor matches commands to YAML-defined conversation flows
3. Policy router decides next action (query DB, call API, ask user)
4. Custom actions execute business logic (order lookup, refund processing)
5. NLG generates natural language response

## Tech Stack

| Layer | Technology |
|-------|-----------|
| LLM | 通义千问 (DashScope / Qwen-Plus) |
| Dialogue Engine | LangGraph + LangChain |
| Web Framework | FastAPI + Uvicorn |
| Vector/Graph DB | Neo4j + sentence-transformers |
| Business DB | MySQL + SQLAlchemy |
| Data Validation | Pydantic + Pydantic Settings |
| Embedding Model | BGE-Base-ZH-v1.5 |

## Features

- **LLM-Powered Dialogue Understanding**: Intent recognition and slot filling via LLM, replacing rule-based NLU
- **YAML-Defined Conversation Flows**: Declarative flow definitions with conditional branching and slot validation
- **GraphRAG Knowledge Base**: Neo4j-based enterprise knowledge retrieval for complex Q&A
- **Multi-Channel Access**: REST API, WebSocket (SocketIO), CLI shell, and web-based Inspect UI
- **Custom Action System**: Python action classes for business logic (order query, refund processing, logistics tracking)
- **Policy-Based Routing**: FlowPolicy + EnterpriseSearchPolicy for dialogue state management
- **Training Pipeline**: Support for fine-tuning data generation and model export

## Quick Start

### Prerequisites

- Python >= 3.10
- MySQL 5.7+ (for e-commerce demo database)
- Neo4j 5+ (optional, for GraphRAG knowledge base)
- DashScope API Key

### 1. Install

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e .
```

### 2. Configure

```bash
cp .env.example ecs_demo/.env
vim ecs_demo/.env
```

```env
DASHSCOPE_API_KEY=your-api-key
NEO4J_PASSWORD=your-neo4j-password
MYSQL_PASSWORD=your-mysql-password
EMBEDDING_MODEL=./models/bge-base-zh-v1.5
```

### 3. Setup Database

```bash
mysql -u root -p -e "CREATE DATABASE ecommerce CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
cd ecs_demo && python db.py
```

### 4. Run

```bash
cd ecs_demo
smrt run       # Start web server (API + Inspect UI)
smrt shell     # Interactive CLI dialogue
```

- **API Docs**: http://localhost:5005/docs
- **Inspect UI**: http://localhost:5005/inspect

## CLI Commands

```bash
smrt init          # Initialize a new project
smrt train         # Train the dialogue model
smrt run           # Start the web service
smrt shell         # Interactive CLI dialogue
smrt inspect       # Launch the debug inspector
```

## Conversation Flows

The demo includes three e-commerce flows:

| Flow | Capabilities |
|------|-------------|
| Order Management | Query order details, cancel orders |
| Logistics | Track shipping status, modify delivery info |
| After-Sales | Process refunds, returns, exchanges |

Each flow is defined in YAML (`ecs_demo/data/flows/`) with slots, conditions, and action mappings.

## Project Structure

```
smart-customer-service/
├── smart_ai/                 # Core dialogue framework
│   ├── agent/                # LangGraph message processing
│   ├── dialogue_understanding/  # LLM command generator & flow executor
│   ├── policies/             # FlowPolicy & search policies
│   ├── core/                 # Tracker, Domain, Slot, Store
│   ├── nlg/                  # Natural language generation
│   ├── retrieval/            # Vector & graph retrieval
│   ├── api/                  # FastAPI web server
│   ├── channels/             # REST / SocketIO / Console
│   ├── cli/                  # CLI commands
│   └── shared/               # Config, LLM clients, utilities
└── ecs_demo/                 # E-commerce demo
    ├── config.yml            # Pipeline & policy configuration
    ├── domain/               # Domain definitions (slots, responses)
    ├── data/flows/           # Conversation flow definitions
    └── actions/              # Custom business logic actions
```

## Project Stats

- ~22,000 lines of Python code
- ~150+ source files
- 3 conversation flows with multi-turn dialogue
- 15+ custom actions
- Slot filling with conditional branching

## License

MIT
