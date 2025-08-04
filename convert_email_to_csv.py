#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
邮件格式转换脚本
将邮件.txt文件转换为CSV格式
"""

import csv
import sys
import os

def convert_email_to_csv(input_file, output_file):
    """
    将邮件.txt文件转换为CSV格式
    
    Args:
        input_file (str): 输入的邮件.txt文件路径
        output_file (str): 输出的CSV文件路径
    """
    try:
        # 检查输入文件是否存在
        if not os.path.exists(input_file):
            print(f"错误：输入文件 '{input_file}' 不存在")
            return False
        
        # 读取输入文件并转换
        converted_data = []
        
        with open(input_file, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line:  # 跳过空行
                    continue
                
                # 按----分割行
                parts = line.split('----')
                if len(parts) != 4:
                    print(f"警告：第{line_num}行格式不正确，跳过：{line[:50]}...")
                    continue
                
                email, password, client_id, refresh_token = parts
                
                # 添加到转换数据中
                converted_data.append({
                    'email_address': email,
                    'client_id': client_id,
                    'refresh_token': refresh_token
                })
        
        # 写入CSV文件
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['email_address', 'client_id', 'refresh_token']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # 不写入表头，直接写入数据
            writer.writerows(converted_data)
        
        print(f"转换完成！")
        print(f"输入文件：{input_file}")
        print(f"输出文件：{output_file}")
        print(f"转换了 {len(converted_data)} 条记录")
        
        return True
        
    except Exception as e:
        print(f"转换过程中发生错误：{str(e)}")
        return False

def main():
    """主函数"""
    # 默认文件路径
    input_file = "邮件.txt"
    output_file = "converted_accounts.csv"
    
    # 如果提供了命令行参数，使用指定的文件路径
    if len(sys.argv) >= 2:
        input_file = sys.argv[1]
    if len(sys.argv) >= 3:
        output_file = sys.argv[2]
    
    print("邮件格式转换脚本")
    print("=" * 50)
    print(f"输入文件：{input_file}")
    print(f"输出文件：{output_file}")
    print("=" * 50)
    
    # 执行转换
    success = convert_email_to_csv(input_file, output_file)
    
    if success:
        print("\n转换成功！")
    else:
        print("\n转换失败！")
        sys.exit(1)

if __name__ == "__main__":
    main() 