# Start Here

## 1. 下載

不熟悉 Git 時，在 GitHub 選擇 `Code → Download ZIP`，解壓縮後保留完整
資料夾。

## 2. 建立私人學習設定

複製：

```text
LOCAL_PROFILE.example.md
```

改名為：

```text
LOCAL_PROFILE.md
```

填入母語、目標語言、口音、證照與目前最想改善的能力。這個檔案已被
`.gitignore` 排除。

## 3. 開啟 Local Project

把 `2torGPT` 根目錄設為 Codex Local Project 的 primary folder，然後
建立一個全新的 Voice task。

Local Project 會讀取根目錄的 `AGENTS.md`，再依啟動指令載入對應 coach。

## 4. 選擇一個 coach

一般英文口說：

```text
Start practice. Scenario: explaining my project to a new friend.
```

TOEFL：

```text
Start TOEFL practice.
```

IELTS：

```text
Start IELTS practice.
```

JLPT：

```text
Start JLPT practice. Level: N3.
```

## 5. 結束並保存

一般口說結束時說：

```text
I'm finished. Give me my Practice Receipt.
```

考試 coach 會在該次練習完成後主動生成 Receipt。所有 Receipt 都寫入：

```text
sessions/
```

系統不得覆蓋既有檔案，也不得捏造時長、逐字內容或分數。

## 6. 閱讀紀錄

- Obsidian：把整個 `2torGPT` 資料夾開成 Vault。
- VS Code：直接開啟資料夾並使用 Markdown Preview。
- 其他工具：打開 `sessions/*.md`。

沒有任何筆記軟體時，也可以先在 Voice 對話中取得 Markdown Receipt。
