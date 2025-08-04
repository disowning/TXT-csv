# 部署指南

## 🚀 部署到Streamlit Cloud（推荐）

### 前提条件
- GitHub账号
- 代码已推送到GitHub仓库

### 部署步骤

#### 1. 准备GitHub仓库
确保您的仓库包含以下文件：
```
├── app.py                    # Streamlit应用主文件
├── requirements.txt          # Python依赖
├── .streamlit/
│   └── config.toml          # Streamlit配置
├── README.md                # 项目说明
└── DEPLOYMENT.md            # 部署指南（本文件）
```

#### 2. 访问Streamlit Cloud
1. 打开 [share.streamlit.io](https://share.streamlit.io)
2. 使用GitHub账号登录

#### 3. 创建新应用
1. 点击 "New app" 按钮
2. 选择 "From existing repo"
3. 填写以下信息：
   - **Repository**: 选择您的GitHub仓库
   - **Branch**: 选择 `main` 或 `master`
   - **Main file path**: 输入 `app.py`
   - **App URL**: 自定义应用URL（可选）

#### 4. 部署应用
1. 点击 "Deploy!" 按钮
2. 等待部署完成（通常需要2-5分钟）
3. 部署成功后会自动打开应用

#### 5. 获取应用链接
部署成功后，您将获得一个永久链接，格式如下：
```
https://your-app-name.streamlit.app
```

### 部署后管理

#### 自动更新
- 每次推送到GitHub仓库时，应用会自动重新部署
- 无需手动操作

#### 查看日志
- 在Streamlit Cloud控制台可以查看应用日志
- 用于调试和监控

#### 应用设置
- 可以修改应用名称和URL
- 可以设置环境变量（如果需要）

## 🔧 本地开发

### 安装依赖
```bash
pip install -r requirements.txt
```

### 运行应用
```bash
streamlit run app.py
```

### 访问应用
打开浏览器访问：http://localhost:8501

## 📊 使用统计

### 免费额度
Streamlit Cloud提供慷慨的免费额度：
- ✅ 无限制的公开应用
- ✅ 每月1GB带宽
- ✅ 1GB存储空间
- ✅ 社区支持

### 适用场景
- ✅ 个人项目和工具
- ✅ 原型和演示
- ✅ 小型团队使用
- ✅ 偶尔使用的工具（完美匹配您的需求）

## 🛠️ 故障排除

### 常见问题

#### 1. 部署失败
- 检查 `requirements.txt` 文件格式
- 确保 `app.py` 文件存在且无语法错误
- 查看部署日志获取详细错误信息

#### 2. 应用无法访问
- 检查GitHub仓库是否为公开状态
- 确认文件路径设置正确

#### 3. 功能异常
- 检查Python版本兼容性
- 验证依赖包版本

### 获取帮助
- [Streamlit文档](https://docs.streamlit.io)
- [Streamlit社区论坛](https://discuss.streamlit.io)
- [GitHub Issues](https://github.com/streamlit/streamlit/issues)

## 🎯 优化建议

### 性能优化
- 使用 `@st.cache_data` 缓存数据处理函数
- 避免在每次重新运行时重复计算

### 用户体验
- 添加加载指示器
- 提供清晰的错误消息
- 优化移动端显示

### 安全考虑
- 不要在代码中硬编码敏感信息
- 使用环境变量存储配置
- 验证用户输入

---

**恭喜！** 您现在拥有一个专业的、免费的、随时可用的Web应用，完美适合偶尔使用的需求。
