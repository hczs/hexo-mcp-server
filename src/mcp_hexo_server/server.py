# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     server.py
   Description :
   Author :       powercheng
   date：          2025/6/7
-------------------------------------------------
   Change Activity:
                   2025/6/7:
-------------------------------------------------
"""

__author__ = "powercheng"

import os

from mcp.server.fastmcp import FastMCP

from . import utils

app = FastMCP("mcp-hexo-server")

BASE_DIR = os.getenv("HEXO_DIR")

if not BASE_DIR:
    raise ValueError("Error: HEXO_BASE_DIR environment variable is not set.")


@app.tool()
async def create_hexo_page(title: str) -> str:
    """
    Create a new Hexo page with the given title.
    You should tell user where is the page created, like "page created at {path}".

    :param title: The title of the Hexo page to create.
    :return: A message indicating the result of the operation.
    """
    command = f'hexo new "{title}"'
    output = await utils.run_command(command, BASE_DIR)
    return f"New post created: {output}"


def main():
    app.run(transport="stdio")
