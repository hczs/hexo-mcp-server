## Hexo MCP Server

简体中文 | [English](README_en.md)

> 一个用于 Hexo 博客自动化和管理的 MCP 服务器。

### 📋 项目简介
Hexo MCP Server 旨在通过 MCP 协议帮助你自动化和管理 Hexo 博客。

### ✨ 功能特性
- 一键新建 Hexo 页面

🪧效果

在 Trae 中使用效果如下：

![mcp demo](img/mcp.png)

### 🚀 安装
通过 JSON 配置安装
```json
{
  "mcpServers": {
    "hexo-mcp-server": {
      "command": "uvx",
      "args": [
        "hexo-mcp-server"
      ],
      "env": {
        "HEXO_DIR": "<YOUR_HEXO_DIRECTORY>"
      }
    }
  }
}
```
注意：一定要配置 JSON 中的 HEXO_DIR 环境变量，配置为你的 hexo 博客目录，例如你的博客目录在：`D:\study\myblog`，可以配置为如下JSON内容：

```json
{
  "mcpServers": {
    "hexo-mcp-server": {
      "command": "uvx",
      "args": [
        "hexo-mcp-server"
      ],
      "env": {
        "HEXO_DIR": "D:\\study\\myblog"
      }
    }
  }
}
```



### 🛠️ 可用工具
- create_hexo_page(title: str) ：根据标题新建 Hexo 页面。

### 📓开发计划

- [ ] 启动 / 停止 hexo 服务工具
- [ ] 创建 hexo 页面的时候同时可以添加页面内容

### 🧪 测试
运行测试：

```
pytest
```
### 📄 许可证
MIT License

### 📬 联系方式
- 作者: powercheng
- 邮箱: hczshd@gmail.com