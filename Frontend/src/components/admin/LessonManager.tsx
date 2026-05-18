"use client";

import { useEffect, useMemo, useState, type FormEvent } from "react";
import { Plus, Save, Trash2, Pencil, X, Loader2, Eye } from "lucide-react";
import {
  createLesson,
  deleteLesson,
  updateLesson,
  type LessonCreate,
} from "@/lib/api/admin";
import {
  getLesson,
  type ApiLessonSummary,
  type ApiRoadmap,
} from "@/lib/api/content";
import { ApiError } from "@/lib/api/client";
import { Markdown } from "@/lib/markdown";
import { TextArea, TextField } from "./AdminField";

type Props = {
  roadmaps: ApiRoadmap[];
  token: string;
  onChange: () => void;
};

function emptyDraft(levelId: string): LessonCreate {
  return {
    level_id: levelId,
    title: "",
    slug: "",
    summary: "",
    content: "# Heading\n\nTulis konten lesson di sini dalam format Markdown.",
    duration: "",
    order_index: 1,
  };
}

export default function LessonManager({ roadmaps, token, onChange }: Props) {
  const firstCategory = roadmaps[0]?.category.id ?? "";
  const firstLevel = roadmaps[0]?.levels[0]?.id ?? "";

  const [activeCategory, setActiveCategory] = useState(firstCategory);
  const [activeLevel, setActiveLevel] = useState(firstLevel);
  const [editingId, setEditingId] = useState<string | null>(null);
  const [draft, setDraft] = useState<LessonCreate>(emptyDraft(firstLevel));
  const [busy, setBusy] = useState(false);
  const [loadingContent, setLoadingContent] = useState(false);
  const [showPreview, setShowPreview] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const activeRoadmap = useMemo(
    () => roadmaps.find((r) => r.category.id === activeCategory),
    [roadmaps, activeCategory]
  );

  const activeLevelObj = useMemo(
    () => activeRoadmap?.levels.find((l) => l.id === activeLevel),
    [activeRoadmap, activeLevel]
  );

  // Auto-pick first level when switching category.
  useEffect(() => {
    if (!activeRoadmap) return;
    const first = activeRoadmap.levels[0]?.id ?? "";
    if (first && !activeRoadmap.levels.some((l) => l.id === activeLevel)) {
      setActiveLevel(first);
      if (!editingId) {
        setDraft(emptyDraft(first));
      }
    }
  }, [activeRoadmap, activeLevel, editingId]);

  function startCreate(levelId: string = activeLevel) {
    setEditingId(null);
    setDraft(emptyDraft(levelId));
    setError(null);
    setShowPreview(false);
  }

  async function startEdit(lesson: ApiLessonSummary) {
    if (!activeLevel) return;
    setEditingId(lesson.id);
    setError(null);
    setShowPreview(false);
    setLoadingContent(true);

    // The summary listing doesn't include the full content; fetch detail.
    try {
      const levelSlug = activeLevelObj?.slug;
      if (!levelSlug) return;
      const detail = await getLesson(levelSlug, lesson.slug);
      setDraft({
        level_id: detail.level_id,
        title: detail.title,
        slug: detail.slug,
        summary: detail.summary,
        content: detail.content,
        duration: detail.duration,
        order_index: detail.order_index,
      });
    } catch (e) {
      setError(
        e instanceof ApiError
          ? e.message
          : e instanceof Error
            ? e.message
            : "Gagal memuat lesson."
      );
    } finally {
      setLoadingContent(false);
    }
  }

  async function onSubmit(e: FormEvent) {
    e.preventDefault();
    if (busy) return;
    setBusy(true);
    setError(null);

    try {
      if (editingId) {
        await updateLesson(editingId, draft, token);
      } else {
        await createLesson(draft, token);
      }
      onChange();
      startCreate(draft.level_id);
    } catch (e) {
      setError(
        e instanceof ApiError
          ? e.message
          : e instanceof Error
            ? e.message
            : "Gagal menyimpan."
      );
    } finally {
      setBusy(false);
    }
  }

  async function onDelete(id: string, title: string) {
    if (!confirm(`Hapus lesson "${title}"?`)) return;
    setBusy(true);
    setError(null);
    try {
      await deleteLesson(id, token);
      onChange();
      if (editingId === id) startCreate();
    } catch (e) {
      setError(
        e instanceof ApiError
          ? e.message
          : e instanceof Error
            ? e.message
            : "Gagal menghapus."
      );
    } finally {
      setBusy(false);
    }
  }

  return (
    <div className="space-y-5">
      {/* Category + level switcher */}
      <div className="space-y-3">
        <div className="flex flex-wrap gap-2">
          {roadmaps.map(({ category }) => (
            <button
              key={category.id}
              onClick={() => setActiveCategory(category.id)}
              className={
                "rounded-full border px-3 py-1.5 text-xs font-medium transition-colors " +
                (activeCategory === category.id
                  ? "border-accent/40 bg-accent/15 text-accent-hover"
                  : "border-border bg-black/30 text-muted hover:border-border hover:text-foreground")
              }
            >
              {category.name}
            </button>
          ))}
        </div>

        <div className="flex flex-wrap gap-2">
          {(activeRoadmap?.levels ?? []).map((level) => (
            <button
              key={level.id}
              onClick={() => {
                setActiveLevel(level.id);
                if (!editingId) startCreate(level.id);
              }}
              className={
                "rounded-lg border px-3 py-1.5 text-xs transition-colors " +
                (activeLevel === level.id
                  ? "border-accent/40 bg-accent/10 text-accent-hover"
                  : "border-border bg-black/30 text-muted hover:border-border hover:text-foreground")
              }
            >
              0{level.number} · {level.title}
            </button>
          ))}
          {(activeRoadmap?.levels.length ?? 0) === 0 && (
            <span className="text-xs text-muted">
              Buat level dulu sebelum menambah lesson.
            </span>
          )}
        </div>
      </div>

      <div className="grid gap-6 lg:grid-cols-[1fr_1.4fr]">
        {/* List */}
        <div>
          <div className="flex items-center justify-between">
            <h2 className="font-display text-lg font-semibold">
              Lessons{" "}
              {activeLevelObj ? `· ${activeLevelObj.title}` : ""}
            </h2>
            <button
              onClick={() => startCreate(activeLevel)}
              className="btn-secondary"
              disabled={!activeLevel}
            >
              <Plus size={14} />
              Baru
            </button>
          </div>

          <ul className="mt-4 space-y-2">
            {(activeLevelObj?.lessons ?? []).map((lesson) => (
              <li
                key={lesson.id}
                className={
                  "flex items-center gap-3 rounded-xl border bg-black/30 p-3 transition-colors " +
                  (editingId === lesson.id
                    ? "border-accent/40"
                    : "border-border")
                }
              >
                <span className="flex h-9 w-9 shrink-0 items-center justify-center rounded-lg border border-border bg-black/30 font-mono text-xs text-accent-hover">
                  {String(lesson.order_index).padStart(2, "0")}
                </span>
                <div className="min-w-0 flex-1">
                  <div className="text-[11px] uppercase tracking-wider text-muted">
                    /{lesson.slug} · {lesson.duration}
                  </div>
                  <div className="mt-0.5 truncate text-sm font-medium text-foreground">
                    {lesson.title}
                  </div>
                </div>
                <button
                  onClick={() => startEdit(lesson)}
                  className="btn-ghost text-xs"
                  title="Edit"
                >
                  <Pencil size={13} />
                </button>
                <button
                  onClick={() => onDelete(lesson.id, lesson.title)}
                  className="btn-ghost text-xs text-rose-300 hover:text-rose-200"
                  title="Hapus"
                >
                  <Trash2 size={13} />
                </button>
              </li>
            ))}
            {(activeLevelObj?.lessons.length ?? 0) === 0 && (
              <li className="text-sm text-muted">
                Belum ada lesson di level ini.
              </li>
            )}
          </ul>
        </div>

        {/* Form */}
        <form onSubmit={onSubmit} className="space-y-3">
          <div className="flex items-center justify-between">
            <h2 className="font-display text-lg font-semibold">
              {editingId ? "Edit lesson" : "Buat lesson baru"}
            </h2>
            <div className="flex items-center gap-2">
              {draft.content && (
                <button
                  type="button"
                  onClick={() => setShowPreview((v) => !v)}
                  className="btn-ghost text-xs"
                >
                  <Eye size={13} />
                  {showPreview ? "Tutup preview" : "Preview"}
                </button>
              )}
              {editingId && (
                <button
                  type="button"
                  onClick={() => startCreate(activeLevel)}
                  className="btn-ghost text-xs"
                >
                  <X size={13} />
                  Batal
                </button>
              )}
            </div>
          </div>

          {error && (
            <p className="rounded-lg border border-rose-400/40 bg-rose-400/10 px-3 py-2 text-xs text-rose-200">
              {error}
            </p>
          )}

          {loadingContent && (
            <p className="flex items-center gap-2 text-xs text-muted">
              <Loader2 size={12} className="animate-spin" />
              Memuat lesson...
            </p>
          )}

          <div>
            <label className="block text-[12px] font-medium text-foreground/80">
              Level
            </label>
            <select
              value={draft.level_id}
              onChange={(e) =>
                setDraft({ ...draft, level_id: e.target.value })
              }
              className="mt-1.5 w-full rounded-xl border border-border bg-black/30 px-3 py-2.5 text-sm outline-none focus:border-accent/60 focus:bg-black/30"
              required
            >
              {roadmaps.flatMap((r) =>
                r.levels.map((l) => (
                  <option
                    key={l.id}
                    value={l.id}
                    className="bg-[#1c1c1c]"
                  >
                    {r.category.name} · 0{l.number} {l.title}
                  </option>
                ))
              )}
            </select>
          </div>

          <div className="grid gap-3 sm:grid-cols-2">
            <TextField
              label="Title"
              value={draft.title}
              onChange={(e) => setDraft({ ...draft, title: e.target.value })}
              required
            />
            <TextField
              label="Slug"
              value={draft.slug}
              onChange={(e) => setDraft({ ...draft, slug: e.target.value })}
              pattern="[a-z0-9\-]+"
              required
            />
          </div>

          <TextArea
            label="Summary"
            value={draft.summary}
            onChange={(e) => setDraft({ ...draft, summary: e.target.value })}
            rows={2}
            required
          />

          <TextArea
            label="Content (Markdown)"
            value={draft.content}
            onChange={(e) => setDraft({ ...draft, content: e.target.value })}
            rows={14}
            hint="Mendukung heading, paragraf, list, code block, blockquote, bold, italic, dan link."
            required
          />

          {showPreview && (
            <div className="rounded-xl border border-border bg-[#0a0a0a] p-5">
              <div className="mb-3 font-mono text-[10px] uppercase tracking-wider text-accent-hover">
                Preview
              </div>
              <Markdown source={draft.content} />
            </div>
          )}

          <div className="grid gap-3 sm:grid-cols-2">
            <TextField
              label="Duration"
              value={draft.duration}
              onChange={(e) =>
                setDraft({ ...draft, duration: e.target.value })
              }
              placeholder="8 menit"
              required
            />
            <TextField
              label="Order index"
              type="number"
              min={1}
              value={String(draft.order_index)}
              onChange={(e) =>
                setDraft({ ...draft, order_index: Number(e.target.value) })
              }
              required
            />
          </div>

          <button
            type="submit"
            disabled={busy || loadingContent}
            className="btn-primary disabled:cursor-not-allowed disabled:opacity-60"
          >
            {busy ? <Loader2 size={14} className="animate-spin" /> : <Save size={14} />}
            {editingId ? "Simpan perubahan" : "Buat lesson"}
          </button>
        </form>
      </div>
    </div>
  );
}
