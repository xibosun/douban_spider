## Douban Movie Tags Spider

[![Build Status](docs/build_status.svg)](https://github.com/xibosun/spider)
[![issues](docs/issues.svg)](https://github.com/xibosun/spider/issues)
[![Stars](docs/stars.svg)](https://github.com/xibosun/spider/stargazers)
[![Dependencies](docs/dependencies.svg)](https://www.python.org/downloads/release/python-363/)
[![Release](docs/release.svg)](https://github.com/xibosun/spider)
[![License](docs/license.svg)](https://opensource.org/licenses/mit-license.php)
[![](docs/chinese.svg)](README-zh.md)

### Introduce

Douban Movie Tags Spider can help you find tags of the movie you are interested in.

### Dependencies

install `gzip`, `json`, `re`, `zlib` using `pip`.

### Usage

First, type the keyword of the movie to search. Take "Jurassic World" as an example.

```python
input the keyword: Jurassic World
```

Then it would show serval movies related to the keyword with its id, name and year.

```python
id: 26416062     name: 侏罗纪世界2 (2018)
id: 10440138     name: 侏罗纪世界 (2015)
id: 26423994     name: Jurassic World (2018)
id: 1293702      name: 侏罗纪公园2：失落的世界 (1997)
id: 26873582     name: 侏罗纪世界3 (2021)
id: 26883254     name: 乐高侏罗纪世界：I-Rex大逃脱 (2016)
```

Choose a movie and type the id from the above.

```python
Choose an id and type it: 26416062
```

### result

Then it would show the tags.

```python
恐龙
侏罗纪
科幻
美国
冒险
2018
惊悚
动作
```
