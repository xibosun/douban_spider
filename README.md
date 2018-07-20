## Douban Movie Tags Spider

[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen.svg)](https://img.shields.io/badge/Build-Passing-Green.svg)
[![issue](https://img.shields.io/badge/Issue-0-red.svg)](https://img.shields.io/badge/Build-Passing-Green.svg)
[![Stars](https://img.shields.io/badge/Stars-0-blue.svg)](https://img.shields.io/badge/Build-Passing-Green.svg)
[![Dependencies](https://img.shields.io/badge/No-Dependencies-brightgreen.svg)](https://img.shields.io/badge/Build-Passing-Green.svg)
[![Release](https://img.shields.io/badge/Release-v1.0-blue.svg)](https://img.shields.io/badge/Build-Passing-Green.svg)
[![](https://jaywcjlove.github.io/sb/lang/chinese.svg)](README-zh.md)

### Introduce

Douban Movie Tags Spider can help you find tags of the movie you are interested in.

First, type the keyword of the movie to search. Take "Jurassic World" as an example.

```python
请输入电影名:
```

Then it would show serval movies related to the keyword with its id, name and year.

```python
id: 26416062     名称: 侏罗纪世界2 (2018)
id: 10440138     名称: 侏罗纪世界 (2015)
id: 26423994     名称: Jurassic World (2018)
id: 1293702      名称: 侏罗纪公园2：失落的世界 (1997)
id: 26873582     名称: 侏罗纪世界3 (2021)
id: 26883254     名称: 乐高侏罗纪世界：I-Rex大逃脱 (2016)
```

Choose a movie and type the id from the above.

```python
请在以上id中选择一个并输入: 26416062
```

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
