# mcp-mysql
Building a MySQL MCP Server from the DBA perspective. This project is a MySQL MCP Server implementation based on the MCP protocol.

## 项目结构

```
mcp-mysql/
├── src/
│   └── mcp_mysql/         # 主要源代码目录
│       ├── core/          # 核心功能模块
│       ├── tools/         # MCP工具实现
│       ├── resources/     # MCP资源实现
│       └── utils/         # 通用工具函数
├── tests/                 # 测试代码目录
│   ├── unit/             # 单元测试
│   └── integration/      # 集成测试
├── docs/                 # 项目文档
│   ├── api/             # API文档
│   └── guides/          # 使用指南
├── config/              # 配置文件目录
├── examples/            # 示例代码和使用案例
├── scripts/             # 工具脚本
└── README.md           # 项目说明文档
```

## 目录结构设计逻辑$$

### src/mcp_mysql
- core/: 包含服务器核心功能实现，如服务器启动、连接管理等
- tools/: 实现各种MySQL相关的MCP工具，如查询执行、表管理等
- resources/: 实现MySQL相关的MCP资源，如数据库信息、表结构等
- utils/: 存放通用工具函数和辅助类

### tests
- unit/: 单元测试，确保各个组件的独立功能正确性
- integration/: 集成测试，验证各组件之间的交互和整体功能

### docs
- api/: API文档，详细说明每个工具和资源的使用方法
- guides/: 使用指南，包含安装、配置和最佳实践

### config
存放配置文件，包括服务器配置、数据库连接配置等

### examples
提供示例代码和使用案例，帮助用户快速理解和使用MCP服务器

### scripts
存放各种工具脚本，如安装脚本、部署脚本等

## 设计原则
1. 模块化：清晰的目录结构使得代码组织更加模块化，便于维护和扩展
2. 关注点分离：核心功能、工具、资源分别在不同目录中实现
3. 可测试性：独立的测试目录，支持不同级别的测试
4. 文档完备：专门的文档目录，确保使用者可以方便地查找信息
5. 示例驱动：通过examples目录提供实际使用案例
