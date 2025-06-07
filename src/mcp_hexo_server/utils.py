# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     utils
   Description :
   Author :       powercheng
   date：          2025/6/7
-------------------------------------------------
   Change Activity:
                   2025/6/7:
-------------------------------------------------
"""
__author__ = 'powercheng'

import asyncio


async def run_command(command: str, base_dir: str) -> str:
    """
    Asynchronously run a shell command and return its output.

    :param command: The command string to execute.
    :param base_dir: The working directory for command execution.
    :return: The command output string (prefer stdout, fallback to stderr).
    """
    process = await asyncio.create_subprocess_shell(
        command,
        cwd=base_dir,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    output = stdout or stderr
    return output.decode(errors="ignore").strip()