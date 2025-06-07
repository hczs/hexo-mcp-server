# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     mcp_dev.py
   Description :
   Author :       powercheng
   date：          2025/6/7
-------------------------------------------------
   Change Activity:
                   2025/6/7:
-------------------------------------------------
"""

__author__ = "powercheng"

from src.mcp_hexo_server.server import app
from loguru import logger

logger.info(f"Started MCP Hexo Server development mode: {app.name}")