# obsidian2jekyll

> [!WARNING]  
> 随便写的自用脚本，使用前注意替换对应目录。

```
.
├── assets
│   └── pictures-change-everytime.png
├── _config.yml
├── imgs
│   └── pictures-not-change.jpg
└── _posts
    ├── 2023-08-07-xxx.md
    └── 2023-08-08-yyy.md
```

主要只修改了 `assets` 和 `_posts` 目录下内容，把 obsidian 中的 markdown 文件里引用的图片复制过来、把 markdown 文件重命名为 jekyll 需要的有日期前缀的格式。

为了方便转换，在 obsidian 里写好的文章中插入 template，脚本中只是把 `date` 段加入了文件名中，其他部分按需修改。

```
---
layout: single
toc: true
show_date: true
title: <% tp.file.title %>
date: <% tp.file.creation_date("YYYY-MM-DD") %>
categories: <% tp.file.folder(relative = false) %>
tags: 
published: false
---
```
