#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
邮件格式转换 Streamlit Web应用
将邮件.txt文件转换为CSV格式的Web界面版本
"""

import streamlit as st
import pandas as pd
import io
import csv
from typing import List, Dict, Tuple

def convert_email_data(file_content: str) -> Tuple[List[Dict], List[str]]:
    """
    转换邮件数据格式
    
    Args:
        file_content (str): 上传文件的内容
        
    Returns:
        Tuple[List[Dict], List[str]]: (转换后的数据, 错误信息列表)
    """
    converted_data = []
    errors = []
    
    lines = file_content.strip().split('\n')
    
    for line_num, line in enumerate(lines, 1):
        line = line.strip()
        if not line:  # 跳过空行
            continue
        
        # 按----分割行
        parts = line.split('----')
        if len(parts) != 4:
            error_msg = f"第{line_num}行格式不正确，跳过：{line[:50]}..."
            errors.append(error_msg)
            continue
        
        email, password, client_id, refresh_token = parts
        
        # 添加到转换数据中（不包含密码）
        converted_data.append({
            'email_address': email.strip(),
            'client_id': client_id.strip(),
            'refresh_token': refresh_token.strip()
        })
    
    return converted_data, errors

def create_csv_download(data: List[Dict]) -> str:
    """
    创建CSV格式的字符串用于下载
    
    Args:
        data (List[Dict]): 转换后的数据
        
    Returns:
        str: CSV格式的字符串
    """
    if not data:
        return ""
    
    output = io.StringIO()
    fieldnames = ['email_address', 'client_id', 'refresh_token']
    writer = csv.DictWriter(output, fieldnames=fieldnames)
    
    # 不写入表头，直接写入数据
    writer.writerows(data)
    
    return output.getvalue()

def main():
    """主应用函数"""
    
    # 页面配置
    st.set_page_config(
        page_title="邮件格式转换工具",
        page_icon="📧",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # 主标题
    st.title("📧 邮件格式转换工具")
    st.markdown("---")
    
    # 侧边栏说明
    with st.sidebar:
        st.header("📋 使用说明")
        st.markdown("""
        ### 输入格式
        每行包含4个字段，用 `----` 分隔：
        ```
        email----password----client_id----refresh_token
        ```
        
        ### 输出格式
        CSV文件包含3个字段：
        - email_address
        - client_id  
        - refresh_token
        
        ### 注意事项
        - 支持UTF-8编码的.txt文件
        - 自动跳过空行和格式错误的行
        - 密码字段不会包含在输出中
        """)
        
        st.markdown("---")
        st.markdown("### 📝 示例")
        st.code("""
输入示例：
user@example.com----pass123----abc-123----token-xyz

输出CSV：
user@example.com,abc-123,token-xyz
        """)
    
    # 主内容区域
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("📁 文件上传")
        
        # 文件上传组件
        uploaded_file = st.file_uploader(
            "选择要转换的.txt文件",
            type=['txt'],
            help="请上传包含邮件信息的.txt文件"
        )
        
        if uploaded_file is not None:
            try:
                # 读取文件内容
                file_content = uploaded_file.read().decode('utf-8')
                
                st.success(f"✅ 文件上传成功：{uploaded_file.name}")
                
                # 显示文件预览
                with st.expander("📄 文件内容预览（前10行）"):
                    preview_lines = file_content.split('\n')[:10]
                    for i, line in enumerate(preview_lines, 1):
                        if line.strip():
                            st.text(f"{i:2d}: {line[:100]}{'...' if len(line) > 100 else ''}")
                
                # 转换数据
                with st.spinner("🔄 正在转换数据..."):
                    converted_data, errors = convert_email_data(file_content)
                
                # 显示转换结果
                st.header("📊 转换结果")
                
                if converted_data:
                    st.success(f"✅ 成功转换 {len(converted_data)} 条记录")
                    
                    # 显示错误信息（如果有）
                    if errors:
                        st.warning(f"⚠️ 跳过了 {len(errors)} 行格式错误的数据")
                        with st.expander("查看错误详情"):
                            for error in errors:
                                st.text(f"• {error}")
                    
                    # 数据预览
                    st.subheader("📋 转换后数据预览")
                    df = pd.DataFrame(converted_data)
                    st.dataframe(df, use_container_width=True)
                    
                    # 下载按钮
                    csv_data = create_csv_download(converted_data)
                    if csv_data:
                        st.download_button(
                            label="📥 下载CSV文件",
                            data=csv_data,
                            file_name="converted_accounts.csv",
                            mime="text/csv",
                            help="点击下载转换后的CSV文件"
                        )
                else:
                    st.error("❌ 没有找到有效的数据行，请检查文件格式")
                    if errors:
                        st.warning("发现的问题：")
                        for error in errors:
                            st.text(f"• {error}")
                            
            except UnicodeDecodeError:
                st.error("❌ 文件编码错误，请确保文件使用UTF-8编码")
            except Exception as e:
                st.error(f"❌ 处理文件时发生错误：{str(e)}")
    
    with col2:
        st.header("📈 统计信息")
        
        if uploaded_file is not None and 'converted_data' in locals():
            # 显示统计卡片
            st.metric("总处理行数", len(file_content.split('\n')))
            st.metric("成功转换", len(converted_data))
            st.metric("跳过行数", len(errors))
            
            if converted_data:
                # 成功率
                total_lines = len([line for line in file_content.split('\n') if line.strip()])
                success_rate = (len(converted_data) / total_lines * 100) if total_lines > 0 else 0
                st.metric("转换成功率", f"{success_rate:.1f}%")
        else:
            st.info("📤 请上传文件开始转换")
    
    # 页脚
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center; color: #666;'>
            <p>邮件格式转换工具 | 支持批量处理 | 安全可靠</p>
        </div>
        """, 
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
