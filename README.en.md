# 2torGPT

[繁體中文](README.md) | [简体中文](README.zh-CN.md) |
[English](README.en.md)

Practice languages with GPT Live and turn every session into a trackable
Markdown Receipt.

2torGPT is a local-first starter workspace. It is not an online course, an
official exam-scoring service, or a cloud database. Obsidian is a recommended
reading interface, but it is not required.

## What it solves

```text
Choose a coach
→ Complete a real Voice practice session
→ Keep only the most useful corrections
→ Write a Receipt to sessions/*.md
→ Continue from that evidence next time
```

Personal practice records stay on the learner's computer by default and are
excluded by `.gitignore`.

## Available coaches

| Coach | Status | Start command |
|---|---|---|
| General English Speaking | active | `Start practice.` |
| TOEFL iBT 2026 Speaking | active | `Start TOEFL practice.` |
| IELTS Speaking | reviewed / not session-tested | `Start IELTS practice.` |
| JLPT | reviewed / not session-tested | `Start JLPT practice. Level: N3.` |

`active` means the coach has a complete practice and Receipt contract. It does
not mean that the coach can issue an official exam result. The other coaches
have been checked against their public exam formats but still need real
end-to-end session testing before becoming active.

## Start in three minutes

1. Download or clone this repository.
2. Copy `LOCAL_PROFILE.example.md` to `LOCAL_PROFILE.md` and enter your own
   goals. The private profile is excluded from Git.
3. Add the repository root as a Codex Local Project with local-file write
   access.
4. Open a new Voice task.
5. Say one of the start commands in the table above.
6. The coach briefly confirms today's goal. If that coach has a prior Receipt,
   it offers one continuation focus from the newest record before practice.
7. To finish a general conversation, say:

   `I'm finished. Give me my Practice Receipt.`

The completed Receipt is written to `sessions/`. If the Voice product does not
have permission to write to the local project, the coach can still return the
Markdown in the conversation, but the learner must save it manually.

For a detailed Traditional Chinese guide, see
[START_HERE.md](START_HERE.md).

## Obsidian is optional

Open the repository folder as an Obsidian Vault to read, search, and link the
Markdown files in `sessions/`. Without Obsidian, use VS Code, Typora, or any
other Markdown editor.

2torGPT does not require the Obsidian API, a plugin, or cloud sync.

## Coach structure

```text
coaches/
├── english/
│   ├── general-speaking/
│   ├── toefl-ibt-2026-speaking/
│   └── ielts-speaking/
└── japanese/
    └── jlpt/
```

Each coach owns:

- `COACH.md`: conversation, task, correction, and evidence boundaries;
- `RECEIPT.md`: the stable session-output format;
- status and official sources.

Follow the
[Coach Pack Contract](docs/COACH_PACK_CONTRACT.md)
when adding a coach. Do not claim support for a new language or certificate by
only renaming an existing coach.

## Important boundaries

- AI-generated levels and scores are not official results.
- Never invent practice time, learner quotes, audio diagnoses, or exam
  results.
- JLPT has no speaking section. The JLPT coach covers only language knowledge,
  reading, and listening.
- Generate original practice items or use public official samples. Do not
  include leaked or restricted test banks.
- `sessions/` may contain personal information and must not be committed or
  pushed by default.

## Origin and difference

This workflow was inspired by
[@changloria0816's GPT Live + Obsidian practice method](https://x.com/changloria0816/status/2080893224181547481).
The original workflow manually pastes GPT's structured output into Obsidian.
In 2torGPT's Local Project mode, the coach writes the structured Markdown
directly to the local workspace after practice.

## License

[MIT](LICENSE)
