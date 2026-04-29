# -*- coding: utf-8 -*-
"""
smart_ai API模块

提供基于FastAPI的Web服务接口。
"""

from smart_ai.api.server import SmartAIServer, create_app

__all__ = [
    "SmartAIServer",
    "create_app",
]
