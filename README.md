# 邮件格式转换工具

这个工具用于将邮件.txt文件转换为CSV格式，提供命令行版本和Web界面版本。

## 🌐 Web版本（推荐）

### 在线使用
访问我们的在线工具：[邮件格式转换工具](https://your-app-url.streamlit.app)

### 本地运行Web版本
```bash
# 安装依赖
pip install -r requirements.txt

# 运行Web应用
streamlit run app.py
```

### Web版本特点
- 🎯 **直观界面** - 拖拽上传，一键下载
- 📊 **实时预览** - 查看转换前后的数据
- 📈 **统计信息** - 显示转换成功率和错误详情
- 🛡️ **安全可靠** - 数据不会保存在服务器
- 📱 **响应式设计** - 支持手机和电脑访问

## 💻 命令行版本

## 文件格式说明

### 输入格式 (邮件.txt)
```
email----password----client_id----refresh_token
```

### 输出格式 (CSV)
```csv
email,client_id,refresh_token
```

## 使用方法

### 方法1：使用默认文件名
```bash
python convert_email_to_csv.py
```
- 输入文件：`邮件.txt`
- 输出文件：`converted_accounts.csv`

### 方法2：指定输入和输出文件
```bash
python convert_email_to_csv.py 输入文件.txt 输出文件.csv
```

### 方法3：只指定输入文件
```bash
python convert_email_to_csv.py 输入文件.txt
```
- 输出文件默认为：`converted_accounts.csv`

## 功能特点

1. **自动跳过空行**：忽略文件中的空行
2. **格式验证**：检查每行是否包含正确的4个字段
3. **错误处理**：对格式不正确的行给出警告并跳过
4. **UTF-8编码支持**：正确处理中文字符
5. **详细输出**：显示转换进度和结果统计

## 示例

### 输入文件 (邮件.txt)
```
xmuzyvos4506@outlook.com----lwzigtb696423----dbc8e03a-b00c-46bd-ae65-b683e7707cb0----M.C519_BAY.0.U.-Ci6kMqO!ZLPI8gdNqc41uknWXLOd7*PC*sXAfW02ioLtQ!nGAC*3MwndY8wwl!6mS2nOJg0gsgd5kVh3KHX1nWHXNepIEXCxdbh04sQILosGrmaMI8nKr3wDXlSHP5UiACTqCfoyosj5lVHBLmPZz8nZAVrGCsMhoIX0I8NXgZXD6Sm0erk5Oz2oG08XeyvjLz8WM*YUF93A!Dv7*!Y3MSExc04d1G52oTbjihW8WxDYY1d!22GNyO3JPk4hQnqp3DcfK9z6vmVr3Ro54UoWrWXfsSWbi3OOggjGoWjpoELZ0Fo3ob0fNJAI2PETzZHwaH7r7sktXXZ3wAmh3mFWl7z4OdvSWYFSuzmluLnP6dFYyZrSCku2Riz*d1ZliRHz0g$$
```

### 输出文件 (converted_accounts.csv)
```csv
xmuzyvos4506@outlook.com,dbc8e03a-b00c-46bd-ae65-b683e7707cb0,M.C519_BAY.0.U.-Ci6kMqO!ZLPI8gdNqc41uknWXLOd7*PC*sXAfW02ioLtQ!nGAC*3MwndY8wwl!6mS2nOJg0gsgd5kVh3KHX1nWHXNepIEXCxdbh04sQILosGrmaMI8nKr3wDXlSHP5UiACTqCfoyosj5lVHBLmPZz8nZAVrGCsMhoIX0I8NXgZXD6Sm0erk5Oz2oG08XeyvjLz8WM*YUF93A!Dv7*!Y3MSExc04d1G52oTbjihW8WxDYY1d!22GNyO3JPk4hQnqp3DcfK9z6vmVr3Ro54UoWrWXfsSWbi3OOggjGoWjpoELZ0Fo3ob0fNJAI2PETzZHwaH7r7sktXXZ3wAmh3mFWl7z4OdvSWYFSuzmluLnP6dFYyZrSCku2Riz*d1ZliRHz0g$$
```

## 注意事项

1. 确保输入文件使用UTF-8编码
2. 每行必须包含4个字段，用`----`分隔
3. 脚本会自动跳过格式不正确的行
4. 输出文件不包含CSV表头，直接输出数据

## 🚀 部署到Streamlit Cloud

### 步骤1：准备GitHub仓库
1. 将代码推送到GitHub仓库
2. 确保包含以下文件：
   - `app.py` - Streamlit应用主文件
   - `requirements.txt` - 依赖文件
   - `.streamlit/config.toml` - 配置文件

### 步骤2：部署到Streamlit Cloud
1. 访问 [share.streamlit.io](https://share.streamlit.io)
2. 使用GitHub账号登录
3. 点击"New app"
4. 选择您的仓库和分支
5. 主文件路径设置为 `app.py`
6. 点击"Deploy"

### 步骤3：获取应用链接
部署成功后，您将获得一个永久的应用链接，可以分享给任何人使用。

## 系统要求

### Web版本
- 现代浏览器（Chrome、Firefox、Safari、Edge）
- 稳定的网络连接

### 命令行版本
- Python 3.6+
- 依赖包：见 `requirements.txt`

## 错误处理

脚本会处理以下情况：
- 文件不存在
- 文件编码问题
- 行格式不正确
- 写入权限问题

如果遇到错误，脚本会显示详细的错误信息。 