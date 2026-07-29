# 2torGPT

用 GPT Live 練習語言，並把每次練習留下成可追蹤的 Markdown Receipt。

2torGPT 是一個 local-first starter workspace，不是線上課程、官方考試評分
服務或雲端資料庫。Obsidian 是推薦的閱讀介面，但不是必要依賴。

## 它解決什麼

```text
選擇 coach
→ 用 Voice 做一次真實練習
→ 結束後只保留最重要的修正
→ 寫入 sessions/*.md
→ 下次從上一份 Receipt 繼續
```

所有個人練習紀錄預設只留在使用者自己的電腦，且被 `.gitignore` 排除。

## 目前的 coaches

| Coach | 狀態 | 啟動指令 |
|---|---|---|
| General English Speaking | active | `Start practice. Scenario: introducing my project.` |
| TOEFL iBT 2026 Speaking | active | `Start TOEFL practice.` |
| IELTS Speaking | reviewed / not session-tested | `Start IELTS practice.` |
| JLPT | reviewed / not session-tested | `Start JLPT practice. Level: N3.` |

`active` 代表 coach 已經有完整練習與 Receipt 規則；不代表它能提供官方
考試成績。其餘 coach 已依官方公開格式建立邊界，但仍需要真實語音或題型
練習後才能升級為 active。

## 三分鐘開始

1. 下載或 clone 這個 repo。
2. 複製 `LOCAL_PROFILE.example.md` 為 `LOCAL_PROFILE.md`，填入自己的
   目標；這個檔案不會進 Git。
3. 把 repo 根目錄設為支援本機檔案寫入的 Codex Local Project。
4. 開一個全新的 Voice task。
5. 說出上表其中一個啟動指令。
6. 一般對話結束時說：

   `I'm finished. Give me my Practice Receipt.`

完成後，Receipt 會寫入 `sessions/`。如果 Voice 對話所在的產品沒有本機
資料夾寫入權限，coach 仍可在對話中回傳 Markdown，但使用者需要自行保存。

詳細步驟見 [START_HERE.md](START_HERE.md)。

## Obsidian 是選配

用 Obsidian 直接開啟 repo 資料夾，就能閱讀、搜尋與連結 `sessions/`
裡的 Markdown。沒有 Obsidian 時，也可以使用 VS Code、Typora 或任何
Markdown 編輯器。

2torGPT 不需要 Obsidian API、外掛或雲端同步。

## Coach 架構

```text
coaches/
├── english/
│   ├── general-speaking/
│   ├── toefl-ibt-2026-speaking/
│   └── ielts-speaking/
└── japanese/
    └── jlpt/
```

每個 coach 都有自己的：

- `COACH.md`：對話、題型、糾錯與證據邊界；
- `RECEIPT.md`：練習完成後的固定輸出格式；
- 狀態與官方來源。

新增 coach 時遵守
[Coach Pack Contract](docs/COACH_PACK_CONTRACT.md)，不要只換語言名稱便
宣稱支援新的證照。

## 重要邊界

- AI 產生的等級或分數不是官方成績。
- 不虛構練習時長、使用者原話、音訊診斷或考試結果。
- JLPT 沒有口說科目；JLPT coach 只能練官方涵蓋的語言知識、閱讀與聽力。
- 題目必須自行生成或使用可公開的官方樣題，不收錄外洩或受限制題庫。
- `sessions/` 可能含有個人資訊，預設不得 commit 或 push。

## 來源與差異

這個 workflow 受到
[@changloria0816 的 GPT Live + Obsidian 練習方法](https://x.com/changloria0816/status/2080893224181547481)
啟發。原方法把 GPT 的固定格式輸出手動貼進 Obsidian；2torGPT 的
Local Project 模式則在練習後直接寫入本機 Markdown。

## License

[MIT](LICENSE)
