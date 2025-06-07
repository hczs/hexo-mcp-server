# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_server
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
from src.mcp_hexo_server.server import create_hexo_page


@pytest.mark.asyncio
async def test_create_new_hexo_page():
    """
    test create_hexo_page tool function.
    """
    title = "Test Page"
    output = await create_hexo_page(title)
    assert output is not None
