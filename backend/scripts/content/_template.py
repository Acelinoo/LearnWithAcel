"""
Lesson template, builder, and reusable Markdown render helpers.

Every lesson follows the same canonical structure so the reading
experience stays predictable on any device:

  1. Tools yang dipakai (metadata)
  2. Yang akan kamu bisa setelah ini (outcomes)
  3. TL;DR
  4. Pembuka
  5. Penjelasan inti
  6. Contoh code
  7. Mini Practice
  8. Fix Error Challenge (Hint + Jawaban)
  9. Quiz (5 soal, format konsisten)
  10. Kesalahan umum
  11. Checkpoint

Reminders:
- The frontend Markdown renderer (Frontend/src/lib/markdown.tsx)
  supports headings, paragraphs, lists, fenced code blocks,
  blockquotes, hr, and inline bold/italic/code/links.
- Raw HTML is escaped — never inject `<details>` etc.
- Indented lines become preformatted blocks. Helpers here output
  flush-left Markdown to avoid that.
- Paragraphs should be 3-4 sentences max for mobile readability.
- No hardcoded viewer numbers or random stats inside content.

Each render helper returns a Markdown fragment with a single trailing
newline so `"\n\n".join(...)` keeps a blank line between sections.
"""

from __future__ import annotations

from textwrap import dedent
from typing import Iterable, List, Sequence, TypedDict


# ─────────────────────────────────────────────────────────────────────────────
# Typed structures
# ─────────────────────────────────────────────────────────────────────────────


class FixError(TypedDict):
    language: str
    broken_code: str
    hint: str
    answer_explanation: str
    fixed_code: str


class QuizItem(TypedDict):
    question: str
    options: Sequence[str]
    correct_letter: str
    explanation: str


# ─────────────────────────────────────────────────────────────────────────────
# Internal: scrub indentation from arbitrary user-provided strings before
# they get embedded into a flush-left Markdown context.
# ─────────────────────────────────────────────────────────────────────────────


def _flush(text: str) -> str:
    """Strip common leading whitespace and surrounding blank lines."""
    return dedent(text).strip("\n")


# ─────────────────────────────────────────────────────────────────────────────
# Reusable Markdown helpers
# ─────────────────────────────────────────────────────────────────────────────


def render_metadata(tools: Sequence[str], outcomes: Sequence[str]) -> str:
    tools_md = "\n".join(f"- {t}" for t in tools)
    outcomes_md = "\n".join(f"- {o}" for o in outcomes)
    return (
        "## Tools yang dipakai\n\n"
        f"{tools_md}\n\n"
        "## Yang akan kamu bisa setelah ini\n\n"
        f"{outcomes_md}\n"
    )


def render_tldr(text: str) -> str:
    return f"## Ringkasan Kilat\n\n{_flush(text)}\n"


def render_section(heading: str, body_md: str) -> str:
    return f"## {heading}\n\n{_flush(body_md)}\n"


def render_practice(text: str) -> str:
    body = _flush(text)
    quoted = "\n".join(f"> {line}" if line else ">" for line in body.split("\n"))
    return f"## Mini Practice\n\n{quoted}\n"


def render_fix_error(fix: FixError) -> str:
    lang = fix["language"]
    broken = _flush(fix["broken_code"])
    fixed = _flush(fix["fixed_code"])
    hint = _flush(fix["hint"])
    explanation = _flush(fix["answer_explanation"])

    return (
        "## Fix Error Challenge\n\n"
        "Coba perbaiki dulu sebelum scroll ke hint.\n\n"
        f"```{lang}\n{broken}\n```\n\n"
        "### Hint\n\n"
        f"{hint}\n\n"
        "### Jawaban\n\n"
        f"{explanation}\n\n"
        f"```{lang}\n{fixed}\n```\n"
    )


def render_quiz_question(index: int, item: QuizItem) -> str:
    options = list(item["options"])
    if len(options) != 4:
        raise ValueError("Each quiz question must have exactly 4 options")
    a, b, c, d = options
    return (
        f"### Soal {index}\n\n"
        f"{_flush(item['question'])}\n\n"
        f"- A. {a}\n"
        f"- B. {b}\n"
        f"- C. {c}\n"
        f"- D. {d}\n\n"
        f"Jawaban benar: {item['correct_letter']}\n\n"
        f"Penjelasan: {_flush(item['explanation'])}\n"
    )


def render_quiz(items: Sequence[QuizItem]) -> str:
    body = "\n\n".join(
        render_quiz_question(i + 1, item).rstrip()
        for i, item in enumerate(items)
    )
    return (
        "## Quiz\n\n"
        "Jawab semua soal di bawah. Tujuannya bukan asal benar — tapi paham kenapa pilihanmu benar.\n\n"
        f"{body}\n"
    )


def render_common_mistakes(items: Sequence[str]) -> str:
    body = "\n".join(f"- {m}" for m in items)
    return f"## Kesalahan umum\n\n{body}\n"


def render_checkpoint(items: Sequence[str]) -> str:
    body = "\n".join(f"- [ ] {c}" for c in items)
    return (
        "## Checkpoint\n\n"
        "Sebelum lanjut ke materi berikutnya, pastikan kamu sudah:\n\n"
        f"{body}\n"
    )


# ─────────────────────────────────────────────────────────────────────────────
# Quiz convenience constructor
# ─────────────────────────────────────────────────────────────────────────────


def q(
    question: str,
    options: Sequence[str],
    correct: str,
    explanation: str,
) -> QuizItem:
    """Shorthand to define a quiz item inline."""
    return {
        "question": question,
        "options": options,
        "correct_letter": correct,
        "explanation": explanation,
    }


# ─────────────────────────────────────────────────────────────────────────────
# Lesson builder
# ─────────────────────────────────────────────────────────────────────────────


def _word_count(*sources: str) -> int:
    return sum(len(s.split()) for s in sources)


def make_lesson(
    *,
    title: str,
    slug: str,
    order_index: int,
    read_time: str,
    summary: str,
    tools: Sequence[str],
    outcomes: Sequence[str],
    tldr: str,
    pembuka: str,
    penjelasan: str,
    contoh_code_md: str,
    practice: str,
    fix_error: FixError,
    quiz: Sequence[QuizItem],
    common_mistakes: Sequence[str],
    checkpoint: Sequence[str] = (),
    quiz_count: int | None = None,
    xp_reward: int = 0,
    is_project: bool = False,
) -> dict:
    """Assemble a lesson dict with content Markdown + forward-compat metadata.

    Returned dict carries DB-ready fields (title, slug, summary, content,
    duration, order_index) plus extras (read_time, word_count, quiz_count,
    xp_reward, is_project) that the seed loader silently strips before
    talking to Prisma — but downstream tools can still read them.
    """
    # Note: `checkpoint` is still accepted as a parameter (so existing
    # lesson modules don't need to change) but it no longer renders into
    # the Markdown body. The "Sebelum lanjut / Checkpoint" section was
    # removed because it felt template-y and added length without value.
    sections: List[str] = [
        f"# {title}",
        render_metadata(tools, outcomes),
        render_tldr(tldr),
        render_section("Pembuka", pembuka),
        render_section("Penjelasan inti", penjelasan),
        render_section("Contoh code", contoh_code_md),
        render_practice(practice),
        render_fix_error(fix_error),
        render_quiz(quiz),
        render_common_mistakes(common_mistakes),
    ]
    content = "\n\n".join(s.strip("\n") for s in sections) + "\n"

    return {
        # DB-ready (matches Lesson model in schema.prisma)
        "title": title,
        "slug": slug,
        "summary": summary,
        "content": content,
        "duration": read_time,
        "order_index": order_index,
        # Forward-compatible metadata
        "read_time": read_time,
        "word_count": _word_count(tldr, pembuka, penjelasan),
        "quiz_count": quiz_count if quiz_count is not None else len(quiz),
        "xp_reward": xp_reward,
        "is_project": is_project,
    }


def make_placeholder_lesson(
    *,
    title: str,
    slug: str,
    summary: str,
    teaser: str,
    coming_outcomes: Sequence[str],
    order_index: int = 1,
) -> dict:
    """Friendly placeholder lesson while a level is being written."""
    outcomes_md = "\n".join(f"- {o}" for o in coming_outcomes)
    body = (
        f"# {title}\n\n"
        "## Status materi\n\n"
        "Level ini sedang disiapkan. Setelah kamu menyelesaikan level sebelumnya, materi baru akan segera hadir di sini.\n\n"
        "## Sekilas yang akan dibahas\n\n"
        f"{_flush(teaser)}\n\n"
        "## Yang akan kamu bisa setelah ini\n\n"
        f"{outcomes_md}\n\n"
        "## Sambil menunggu\n\n"
        "Selesaikan dulu mini project di level sebelumnya. Itu akan jadi pondasi yang kuat saat materi level ini rilis.\n"
    )
    return {
        "title": title,
        "slug": slug,
        "summary": summary,
        "content": body,
        "duration": "Coming soon",
        "order_index": order_index,
        "read_time": "Coming soon",
        "word_count": 0,
        "quiz_count": 0,
        "xp_reward": 0,
        "is_project": False,
    }


# ─────────────────────────────────────────────────────────────────────────────
# Level helper
# ─────────────────────────────────────────────────────────────────────────────


def make_level(
    *,
    number: int,
    slug: str,
    title: str,
    subtitle: str,
    description: str,
    duration: str,
    difficulty: str,
    accent_color: str,
    mini_project: str,
    tags: Sequence[str],
    lessons: Iterable[dict],
    coming_soon: bool = False,
) -> dict:
    lessons_list = list(lessons)
    quiz_total = sum(int(l.get("quiz_count") or 0) for l in lessons_list)
    return {
        "number": number,
        "slug": slug,
        "title": title,
        "subtitle": subtitle,
        "description": description,
        "duration": duration,
        "difficulty": difficulty,
        "accent_color": accent_color,
        "mini_project": mini_project,
        "tags": list(tags),
        "coming_soon": coming_soon,
        "quiz_count": quiz_total,
        "lessons": lessons_list,
    }
