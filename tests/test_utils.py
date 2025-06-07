# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_utils
   Description :
   Author :       powercheng
   date：          2025/6/7
-------------------------------------------------
   Change Activity:
                   2025/6/7:
-------------------------------------------------
"""
__author__ = 'powercheng'

import pytest

from src.mcp_hexo_server.utils import run_command


@pytest.mark.asyncio
async def test_run_command():
    """
    测试 run_command 函数。
    """
    command = 'echo Hello'
    base_dir = '.'
    output = await run_command(command, base_dir)
    assert output == "Hello"
