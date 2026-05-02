# -*- coding: utf-8 -*-
"""
对话理解模块 (Dialogue Understanding / DU)

本架构的核心模块，负责：
- 命令生成：使用LLM将用户输入转换为命令
- 命令处理：执行命令并更新对话状态
- Flow管理：管理对话流程的执行
- 对话栈：管理多轮对话的上下文
"""

from smart_ai.dialogue_understanding.commands import (
    Command,
    StartFlowCommand,
    SetSlotCommand,
    CancelFlowCommand,
    ChitChatAnswerCommand,
    CannotHandleCommand,
    ClarifyCommand,
    HumanHandoffCommand,
    ErrorCommand,
    SessionStartCommand,
)

__all__ = [
    # Commands
    "Command",
    "StartFlowCommand",
    "SetSlotCommand",
    "CancelFlowCommand",
    "ChitChatAnswerCommand",
    "CannotHandleCommand",
    "ClarifyCommand",
    "HumanHandoffCommand",
    "ErrorCommand",
    "SessionStartCommand",
]
