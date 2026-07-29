# 2torGPT

[繁體中文](README.md) | [简体中文](README.zh-CN.md) |
[English](README.en.md)

用 GPT Live 练习语言，并把每次练习保存成可追踪的 Markdown Receipt。

2torGPT 是一个 local-first starter workspace，不是在线课程、官方考试评分
服务或云端数据库。Obsidian 是推荐的阅读界面，但不是必要依赖。

## 它解决什么

```text
选择 coach
→ 用 Voice 完成一次真实练习
→ 结束后只保留最重要的修改建议
→ 写入 sessions/*.md
→ 下次从上一份 Receipt 继续
```

所有个人练习记录默认只保留在用户自己的电脑中，并被 `.gitignore` 排除。

## 当前 coaches

| Coach | 状态 | 启动指令 |
|---|---|---|
| General English Speaking | active | `Start practice. Scenario: introducing my project.` |
| TOEFL iBT 2026 Speaking | active | `Start TOEFL practice.` |
| IELTS Speaking | reviewed / not session-tested | `Start IELTS practice.` |
| JLPT | reviewed / not session-tested | `Start JLPT practice. Level: N3.` |

`active` 表示 coach 已有完整的练习与 Receipt 规则；不表示它能够提供官方
考试成绩。其余 coach 已根据官方公开格式建立边界，但仍需完成真实的端到端
session 测试，才能升级为 active。

## 三分钟开始

1. 下载或 clone 这个 repo。
2. 将 `LOCAL_PROFILE.example.md` 复制为 `LOCAL_PROFILE.md`，填写自己的
   目标；这个私人文件不会进入 Git。
3. 将 repo 根目录设为具有本地文件写入权限的 Codex Local Project。
4. 打开一个全新的 Voice task。
5. 说出上表中的任意一条启动指令。
6. 一般对话结束时说：

   `I'm finished. Give me my Practice Receipt.`

完成后，Receipt 会写入 `sessions/`。如果 Voice 所在的产品没有本地
文件夹写入权限，coach 仍可在对话中返回 Markdown，但用户需要自行保存。

繁体中文详细步骤见 [START_HERE.md](START_HERE.md)。

## Obsidian 是可选项

用 Obsidian 直接打开 repo 文件夹，就能阅读、搜索和链接 `sessions/`
里的 Markdown。没有 Obsidian 时，也可以使用 VS Code、Typora 或任何
Markdown 编辑器。

2torGPT 不需要 Obsidian API、插件或云端同步。

## Coach 架构

```text
coaches/
├── english/
│   ├── general-speaking/
│   ├── toefl-ibt-2026-speaking/
│   └── ielts-speaking/
└── japanese/
    └── jlpt/
```

每个 coach 都有自己的：

- `COACH.md`：对话、题型、纠错与证据边界；
- `RECEIPT.md`：练习完成后的固定输出格式；
- 状态与官方来源。

新增 coach 时应遵守
[Coach Pack Contract](docs/COACH_PACK_CONTRACT.md)，不要只替换语言名称就
声称支持新的语言或证书。

## 重要边界

- AI 生成的等级或分数不是官方成绩。
- 不虚构练习时长、用户原话、音频诊断或考试结果。
- JLPT 没有口语科目；JLPT coach 只能练习官方涵盖的语言知识、阅读和听力。
- 题目必须自行生成或使用公开的官方样题，不收录泄露或受限制的题库。
- `sessions/` 可能包含个人信息，默认不得 commit 或 push。

## 来源与差异

这个 workflow 受到
[@changloria0816 的 GPT Live + Obsidian 练习方法](https://x.com/changloria0816/status/2080893224181547481)
启发。原方法把 GPT 的固定格式输出手动粘贴到 Obsidian；2torGPT 的
Local Project 模式则在练习后直接写入本地 Markdown。

## License

[MIT](LICENSE)
