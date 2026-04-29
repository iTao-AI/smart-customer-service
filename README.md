# Smart Customer Service System

A teaching-oriented LLM-driven dialogue system for e-commerce customer service, built on LangGraph + LangChain + 通义千问 (Qwen).

This project implements a complete intelligent customer service framework including order inquiry, logistics tracking, after-sales processing, and knowledge base Q&A — designed for learning dialogue system architecture.

## Features

- **LLM-Powered Dialogue Understanding**: Uses LLM (Qwen/DashScope) to understand user intent and generate structured commands
- **Flow-Based Dialogue Management**: YAML-defined conversation flows with conditional branching, slot filling, and action execution
- **Graph-Based Message Processing**: Built on LangGraph for orchestrating complex dialogue pipelines
- **E-Commerce Demo**: Complete customer service for an online store:
  - Order inquiry & detail display
  - Order cancellation
  - Shipping info modification
  - Logistics tracking
  - After-sales (refund / return / exchange)
- **Knowledge Base Retrieval**: GraphRAG + Neo4j for enterprise knowledge Q&A
- **Multi-Channel Support**: REST API, WebSocket (SocketIO), CLI shell, and web-based inspect UI
- **Custom Actions**: Python-based action classes that interact with MySQL database
- **Training Module**: Support for fine-tuning data generation and model export

## Architecture

```
smart-customer-service/
├── smart_ai/                 # Core dialogue framework
│   ├── agent/                  # Agent & LangGraph message processing
│   ├── dialogue_understanding/ # LLM command generator & flow executor
│   ├── policies/               # FlowPolicy & EnterpriseSearchPolicy
│   ├── core/                   # Tracker, Domain, Slot, Store
│   ├── nlg/                    # Natural language generation
│   ├── retrieval/              # Vector & graph retrieval
│   ├── api/                    # FastAPI web server
│   ├── channels/               # REST / SocketIO / Console channels
│   ├── training/               # Training & fine-tuning
│   ├── cli/                    # CLI commands (init/train/run/shell)
│   └── shared/                 # Config, LLM clients, utilities
└── ecs_demo/                   # E-commerce customer service demo
    ├── config.yml              # Pipeline & policy configuration
    ├── endpoints.yml           # LLM, vector store, database endpoints
    ├── domain/                 # Domain definitions (slots, responses, actions)
    │   ├── domain_order.yml
    │   ├── domain_logistics.yml
    │   ├── domain_postsale.yml
    │   └── domain_patterns.yml
    ├── data/flows/             # Conversation flow definitions
    │   ├── flow_order.yml
    │   ├── flow_logistics.yml
    │   └── flow_postsale.yml
    ├── actions/                # Custom action implementations
    │   ├── action_order.py
    │   ├── action_logistics.py
    │   ├── action_postsale.py
    │   └── db.py / db_table_class.py
    ├── addons/                 # Knowledge retrieval extensions
    │   ├── information_retrieval.py
    │   └── create_indexing.py
    ├── gen_data.py             # Fake data generator for MySQL
    └── models/                 # Embedding model (bge-base-zh-v1.5)
```

## Quick Start

### Prerequisites

- Python >= 3.10
- MySQL 5.7+ (for e-commerce demo database)
- Neo4j 5+ (optional, for GraphRAG knowledge base)
- [DashScope API Key](https://bailian.console.aliyun.com/) (for 通义千问 LLM)

### 1. Install Dependencies

```bash
# Create a virtual environment
python -m venv .venv
source .venv/bin/activate

# Install the smart_ai framework in development mode
pip install -e . -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 2. Configure Environment

```bash
# Copy and edit the environment file
cp .env.example ecs_demo/.env
vim ecs_demo/.env
```

Fill in your actual API keys and passwords:

```env
DASHSCOPE_API_KEY=your-actual-api-key
NEO4J_PASSWORD=your-neo4j-password
MYSQL_PASSWORD=your-mysql-password
EMBEDDING_MODEL=./models/bge-base-zh-v1.5
```

### 3. Setup Database (for ecs_demo)

```bash
# Create the MySQL database
mysql -u root -p -e "CREATE DATABASE ecommerce CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"

# Use sqlacodegen to generate ORM models from your existing database schema
# (or use the provided db_table_class.py if you already have the schema)
cd ecs_demo
python db.py
```

> **Note**: The demo assumes you have an e-commerce database with tables for users, orders, logistics, after-sales, etc. You'll need to create the database schema first or modify the `db_table_class.py` to match your own schema.

### 4. Run the Demo

```bash
cd ecs_demo

# Start the web server (REST API + WebSocket + Inspect UI)
smrt run

# Or start an interactive CLI shell
smrt shell
```

The web server provides:
- **API Docs**: http://localhost:5005/docs
- **Inspect UI** (debug console): http://localhost:5005/inspect

## CLI Commands

```bash
smrt init          # Initialize a new project
smrt train         # Train the dialogue model
smrt run           # Start the web service
smrt shell         # Interactive CLI dialogue
smrt inspect       # Launch the debug inspector
smrt -V            # Show version info
```

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

## Project Stats

- ~22,000 lines of Python code
- ~150+ source files
- 3 conversation flows (order, logistics, after-sales)
- 15+ custom actions
- Multi-turn dialogue with slot filling and conditional branching

## License

MIT
