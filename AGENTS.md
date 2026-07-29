# 2torGPT workspace

This repository is a local-first language-practice workspace.

## Before a session

1. Read `LOCAL_PROFILE.md` when it exists. Never require the user to commit it.
2. Route the start command to exactly one coach:
   - `Start practice...` → `coaches/english/general-speaking/COACH.md`
   - `Start TOEFL practice...` →
     `coaches/english/toefl-ibt-2026-speaking/COACH.md`
   - `Start IELTS practice...` →
     `coaches/english/ielts-speaking/COACH.md`
   - `Start JLPT practice...` → `coaches/japanese/jlpt/COACH.md`
3. Read that coach's `COACH.md` and `RECEIPT.md` completely before responding.
4. If the requested language or exam has no coach, say that it is unsupported;
   do not silently reuse another exam rubric.

## During a Voice session

- Begin the selected exercise immediately.
- Keep instructions short and voice-friendly.
- Ask or play one item at a time.
- Let the learner do most of the speaking.
- Do not interrupt pauses, hesitation, or small self-corrections.
- Do not correct between scored exam items.
- Use only evidence from the current session and available audio.
- Never invent exact timing, quotes, pronunciation diagnoses, or scores.

## Session output

When the learner uses the coach's finish command:

1. End the exercise.
2. Fill the selected coach's `RECEIPT.md` structure.
3. Write a new file to:

   `sessions/YYYY-MM-DD-HHMM-<coach-slug>.md`

4. Never overwrite or append to an existing Receipt.
5. Keep user records local. Do not stage, commit, push, publish, or transmit
   `sessions/*.md`.
6. If the current product cannot write local files, return the Markdown in the
   conversation and state that local saving was not performed.

## Exam boundaries

- Practice estimates are not official exam scores.
- Read the coach's current official sources and version date before changing
  exam structure.
- Do not use leaked, confidential, or memorized live-test questions.
- JLPT has no speaking section. Do not describe conversation practice as an
  official JLPT speaking simulation.
