# Coach Pack Contract

A coach is publishable only when it contains:

1. `COACH.md` with language, goal, status, task boundary, session flow,
   correction policy, evidence boundary, finish behavior, and sources.
2. `RECEIPT.md` with a stable Markdown output structure.
3. A start command that does not conflict with another coach.
4. An explicit distinction between practice feedback and official results.
5. A real session test before the status becomes `active`.

## Status values

- `active`: the full start → practice → Receipt flow was session-tested.
- `reviewed-not-session-tested`: checked against public sources but still needs
  a real end-to-end session.
- `planned`: only a product direction; do not route users to it.

## Exam coach requirements

An exam coach must additionally record:

- official exam and section name;
- format effective date or last verified date;
- tested modalities;
- task types and timing boundaries;
- scoring or evaluation criteria;
- official source links;
- what the coach cannot validly estimate.

One exam pack cannot be cloned into another by renaming headings. If the exam
does not test speaking, a Voice session may support listening or recall drills,
but it must not be presented as a speaking simulation.

## Regrade rule

Recheck a coach when:

- the exam owner changes its public format or scoring scale;
- a real session exposes an unusable prompt, timing, or Receipt field;
- the coach repeatedly invents unavailable audio, timing, quotes, or scores.

Update the coach only after the source or failure is documented.
