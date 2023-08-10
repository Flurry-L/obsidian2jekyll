#!/bin/bash

while getopts "i:o:" opt; do
  case "$opt" in
    i) input_directory=$OPTARG ;;
    o) output_directory=$OPTARG ;;
    *) echo "Usage: $0 -i <input_directory> -o <output_directory>"; exit 1 ;;
  esac
done

if [[ -z $input_directory || -z $output_directory ]]; then
  echo "Usage: $0 -i <input_directory> -o <output_directory>"
  exit 1
fi

# 删除原有内容
rm -rf "$output_directory/_posts"
rm -rf "$output_directory/assets"

# 运行 Python 脚本
python script.py "$input_directory" "$output_directory"

echo "更新操作已完成"

cd "$output_directory"

echo "正在启动 Jekyll 服务器"

# 启动 Jekyll 服务器
bundle exec jekyll serve
