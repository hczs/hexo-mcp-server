## Hexo MCP Server

[简体中文](README.md) | English

> An MCP server for automating and managing Hexo blogs.

### 📋 Project Introduction
Hexo MCP Server aims to help you automate and manage your Hexo blog via the MCP protocol.

### ✨ Features
- One-click creation of Hexo pages

🪧Effect

Usage effect in Trae:

![mcp demo](img/mcp.png)

### 🚀 Installation
Install via JSON configuration
```json
{
  "mcpServers": {
    "mcp-hexo-server": {
      "command": "uvx",
      "args": [
        "mcp-hexo-server"
      ],
      "env": {
        "HEXO_DIR": "<YOUR_HEXO_DIRECTORY>"
      }
    }
  }
}
```
Note: Be sure to configure the HEXO_DIR environment variable in the JSON to your Hexo blog directory. For example, if your blog directory is at: `D:\study\myblog`, you can configure the JSON as follows:

```json
{
  "mcpServers": {
    "mcp-hexo-server": {
      "command": "uvx",
      "args": [
        "mcp-hexo-server"
      ],
      "env": {
        "HEXO_DIR": "D:\\study\\myblog"
      }
    }
  }
}
```

### 🛠️ Available Tools
- create_hexo_page(title: str): Create a new Hexo page based on the title.

### 📓 Development Plan
- [ ] Start/Stop Hexo server tool
- [ ] Add page content when creating a Hexo page

### 🧪 Testing
Run tests:

```
pytest
```
### 📄 License
MIT License

### 📬 Contact
- Author: powercheng
- Email: hczshd@gmail.com