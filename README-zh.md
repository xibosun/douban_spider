## 豆瓣电影标签爬虫

[![Build Status](docs/build_status.svg)](https://github.com/xibosun/douban_spider)
[![issues](docs/issues.svg)](https://github.com/xibosun/douban_spider/issues)
[![Stars](docs/stars.svg)](https://github.com/xibosun/douban_spider/stargazers)
[![Dependencies](docs/dependencies.svg)](https://www.python.org/downloads/release/python-363/)
[![Release](docs/release.svg)](https://github.com/xibosun/douban_spider)
[![License](docs/license.svg)](https://opensource.org/licenses/mit-license.php)
[![](docs/english.svg)](README.md)

### 介绍

豆瓣电影标签爬虫可以帮助你寻找你感兴趣电影的标签

### 依赖库

通过 `pip` 安装 `gzip`, `json`, `re`, `zlib` 等库

### 使用方法

首先输入电影关键词，以“侏罗纪世界”为例。

```
input the keyword: 侏罗纪世界
```

之后程序会返回若干电影的id，名称及年份

```
id: 26416062     name: 侏罗纪世界2 (2018)
id: 10440138     name: 侏罗纪世界 (2015)
id: 1293702      name: 侏罗纪公园2：失落的世界 (1997)
id: 26873582     name: 侏罗纪世界3 (2021)
id: 26883254     name: 乐高侏罗纪世界：I-Rex大逃脱 (2016)
```

从以上id中选择一个输入

```
Choose an id and type it: 26416062
```

### 结果

接下来，会返回电影标签

```
恐龙
侏罗纪
科幻
美国
冒险
2018
惊悚
动作
```
