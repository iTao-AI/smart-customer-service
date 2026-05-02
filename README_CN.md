[English](./README.md) | [中文](./README_CN.md)

# Smart Customer Service

一个基于 LangGraph + LangChain 的生产级电商客服对话系统框架。支持 YAML 定义的对话流程、GraphRAG 知识库检索和多渠道接入（REST API、WebSocket、CLI）。

## 架构

```
用户输入（REST / WebSocket / CLI）
    │
    ▼
┌──────────────────────────────────────┐
│         LangGraph 处理管道             │
│  ┌────────────┐  ┌─────────────────┐ │
│  │ 命令生成器  │→ │ 流程执行器       │ │
│  │            │  │ （YAML 流程）     │ │
│  └────────────┘  └────────┬────────┘ │
│                           │          │
│  ┌────────────┐  ┌────────▼────────┐ │
│  │ 自然语言    │← │ 动作执行器       │ │
│  │ 生成（响应） │  │ + 策略路由       │ │
│  └────────────┘  └─────────────────┘ │
└──────────────────────────────────────┘
                            │
              ┌─────────────┼─────────────┐
              ▼             ▼             ▼
         MySQL        Neo4j          自定义
         （订单）      （GraphRAG）    动作
```

**对话流程：**
1. 用户输入 → LLM 生成结构化命令（意图 + 槽位）
2. 流程执行器将命令匹配到 YAML 定义的对话流程
3. 策略路由决定下一步动作（查库、调 API、询问用户）
4. 自定义动作执行业务逻辑（订单查询、退款处理）
5. NLG 生成自然语言响应

## 技术栈

| 层级 | 技术 |
|------|------|
| 大模型 | 通义千问（DashScope / Qwen-Plus） |
| 对话引擎 | LangGraph + LangChain |
| Web 框架 | FastAPI + Uvicorn |
| 向量/图数据库 | Neo4j + sentence-transformers |
| 业务数据库 | MySQL + SQLAlchemy |
| 数据校验 | Pydantic + Pydantic Settings |
| 嵌入模型 | BGE-Base-ZH-v1.5 |

## 核心功能

- **LLM 驱动的对话理解**：通过 LLM 进行意图识别和槽位填充，替代基于规则的 NLU
- **YAML 定义对话流程**：声明式流程定义，支持条件分支和槽位校验
- **GraphRAG 知识库**：基于 Neo4j 的企业知识检索，用于复杂问答
- **多渠道接入**：REST API、WebSocket（SocketIO）、CLI 交互式 shell、Web Inspect 界面
- **自定义动作系统**：Python 动作类实现业务逻辑（订单查询、退款处理、物流跟踪）
- **策略路由**：FlowPolicy + EnterpriseSearchPolicy 管理对话状态
- **训练管道**：支持微调数据生成和模型导出

## 快速开始

### 前置要求

- Python >= 3.10
- MySQL 5.7+（电商演示数据库）
- Neo4j 5+（可选，GraphRAG 知识库）
- DashScope API 密钥

### 1. 安装

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e .
```

### 2. 配置

```bash
cp .env.example ecs_demo/.env
vim ecs_demo/.env
```

### 3. 设置数据库

```bash
mysql -u root -p -e "CREATE DATABASE ecommerce CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
cd ecs_demo && python db.py
```

### 4. 运行

```bash
cd ecs_demo
smrt run       # 启动 Web 服务（API + Inspect 界面）
smrt shell     # 交互式 CLI 对话
```

- **API 文档**: http://localhost:5005/docs
- **Inspect 界面**: http://localhost:5005/inspect

## CLI 命令

```bash
smrt init          # 初始化新项目
smrt train         # 训练对话模型
smrt run           # 启动 Web 服务
smrt shell         # 交互式 CLI 对话
smrt inspect       # 启动调试检查器
```

## 对话流程

演示包含三个电商流程：

| 流程 | 能力 |
|------|------|
| 订单管理 | 查询订单详情、取消订单 |
| 物流 | 跟踪物流状态、修改配送信息 |
| 售后 | 处理退款、退货、换货 |

每个流程使用 YAML 定义（`ecs_demo/data/flows/`），包含槽位、条件和动作映射。

## 项目结构

```
smart-customer-service/
├── smart_ai/                 # 核心对话框架
│   ├── agent/                # LangGraph 消息处理
│   ├── dialogue_understanding/  # LLM 命令生成器和流程执行器
│   ├── policies/             # FlowPolicy 和搜索策略
│   ├── core/                 # Tracker、Domain、Slot、Store
│   ├── nlg/                  # 自然语言生成
│   ├── retrieval/            # 向量和图检索
│   ├── api/                  # FastAPI Web 服务
│   ├── channels/             # REST / SocketIO / Console
│   ├── cli/                  # CLI 命令
│   └── shared/               # 配置、LLM 客户端、工具函数
└── ecs_demo/                 # 电商演示
    ├── config.yml            # 管道和策略配置
    ├── domain/               # 领域定义（槽位、响应）
    ├── data/flows/           # 对话流程定义
    └── actions/              # 自定义业务逻辑动作
```

## 项目统计

- 约 22,000 行 Python 代码
- 150+ 源文件
- 3 个多轮对话流程
- 15+ 自定义动作
- 支持条件分支和槽位填充

## License

MIT
