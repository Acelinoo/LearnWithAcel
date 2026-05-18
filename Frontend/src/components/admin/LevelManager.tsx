"use client";

import { useMemo, useState, type FormEvent } from "react";
import { Plus, Save, Trash2, Pencil, X, Loader2 } from "lucide-react";
import {
  createLevel,
  deleteLevel,
  updateLevel,
  type LevelCreate,
} from "@/lib/api/admin";
import {
  normalizeTags,
  type ApiLevelSummary,
  type ApiRoadmap,
} from "@/lib/api/content";
import { ApiError } from "@/lib/api/client";
import { CheckBox, TextArea, TextField } from "./AdminField";

type Props = {
  roadmaps: ApiRoadmap[];
  token: string;
  onChange: () => void;
};

function emptyDraft(categoryId: string): LevelCreate {
  return {
    category_id: categoryId,
    number: 1,
    title: "",
    slug: "",
    subtitle: "",
    description: "",
    duration: "",
    difficulty: "",
    accent_color: "from-accent/30 to-accent-hover/10",
    mini_project: "",
    quiz_count: 3,
    tags: [],
    coming_soon: false,
  };
}

export default function LevelManager({ roadmaps, token, onChange }: Props) {
  const firstCategory = roadmaps[0]?.category.id ?? "";

  const [activeCategory, setActiveCategory] = useState<string>(firstCategory);
  const [editingId, setEditingId] = useState<string | null>(null);
  const [draft, setDraft] = useState<LevelCreate>(emptyDraft(firstCategory));
  const [tagsText, setTagsText] = useState("");
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const activeRoadmap = useMemo(
    () => roadmaps.find((r) => r.category.id === activeCategory),
    [roadmaps, activeCategory]
  );

  function startCreate(categoryId: string = activeCategory) {
    setEditingId(null);
    setDraft(emptyDraft(categoryId));
    setTagsText("");
    setError(null);
  }

  function startEdit(level: ApiLevelSummary, categoryId: string) {
    const tags = normalizeTags(level.tags);
    setEditingId(level.id);
    setActiveCategory(categoryId);
    setDraft({
      category_id: categoryId,
      number: level.number,
      title: level.title,
      slug: level.slug,
      subtitle: level.subtitle,
      description: level.description,
      duration: level.duration,
      difficulty: level.difficulty,
      accent_color: level.accent_color,
      mini_project: level.mini_project,
      quiz_count: level.quiz_count,
      tags,
      coming_soon: level.coming_soon,
    });
    setTagsText(tags.join(", "));
    setError(null);
  }

  async function onSubmit(e: FormEvent) {
    e.preventDefault();
    if (busy) return;
    setBusy(true);
    setError(null);

    const payload: LevelCreate = {
      ...draft,
      tags: tagsText
        .split(",")
        .map((s) => s.trim())
        .filter(Boolean),
    };

    try {
      if (editingId) {
        await updateLevel(editingId, payload, token);
      } else {
        await createLevel(payload, token);
      }
      onChange();
      startCreate(payload.category_id);
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
    if (
      !confirm(`Hapus level "${title}"? Semua lesson di dalamnya akan terhapus.`)
    )
      return;
    setBusy(true);
    setError(null);
    try {
      await deleteLevel(id, token);
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
      {/* Category switcher */}
      <div>
        <div className="flex flex-wrap gap-2">
          {roadmaps.map(({ category }) => (
            <button
              key={category.id}
              onClick={() => {
                setActiveCategory(category.id);
                if (!editingId) startCreate(category.id);
              }}
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
      </div>

      <div className="grid gap-6 lg:grid-cols-[1fr_1.2fr]">
        {/* List */}
        <div>
          <div className="flex items-center justify-between">
            <h2 className="font-display text-lg font-semibold">
              Levels {activeRoadmap ? `· ${activeRoadmap.category.name}` : ""}
            </h2>
            <button
              onClick={() => startCreate(activeCategory)}
              className="btn-secondary"
            >
              <Plus size={14} />
              Baru
            </button>
          </div>

          <ul className="mt-4 space-y-2">
            {(activeRoadmap?.levels ?? []).map((level) => (
              <li
                key={level.id}
                className={
                  "flex items-center gap-3 rounded-xl border bg-black/30 p-3 transition-colors " +
                  (editingId === level.id
                    ? "border-accent/40"
                    : "border-border")
                }
              >
                <span className="flex h-9 w-9 shrink-0 items-center justify-center rounded-lg border border-border bg-black/30 font-mono text-xs text-accent-hover">
                  0{level.number}
                </span>
                <div className="min-w-0 flex-1">
                  <div className="text-[11px] uppercase tracking-wider text-muted">
                    /{level.slug} · {level.lessons.length} lessons
                  </div>
                  <div className="mt-0.5 truncate text-sm font-medium text-foreground">
                    {level.title}
                  </div>
                </div>
                <button
                  onClick={() => startEdit(level, activeCategory)}
                  className="btn-ghost text-xs"
                  title="Edit"
                >
                  <Pencil size={13} />
                </button>
                <button
                  onClick={() => onDelete(level.id, level.title)}
                  className="btn-ghost text-xs text-rose-300 hover:text-rose-200"
                  title="Hapus"
                >
                  <Trash2 size={13} />
                </button>
              </li>
            ))}
            {(activeRoadmap?.levels.length ?? 0) === 0 && (
              <li className="text-sm text-muted">Belum ada level di kategori ini.</li>
            )}
          </ul>
        </div>

        {/* Form */}
        <form onSubmit={onSubmit} className="space-y-3">
          <div className="flex items-center justify-between">
            <h2 className="font-display text-lg font-semibold">
              {editingId ? "Edit level" : "Buat level baru"}
            </h2>
            {editingId && (
              <button
                type="button"
                onClick={() => startCreate(activeCategory)}
                className="btn-ghost text-xs"
              >
                <X size={13} />
                Batal
              </button>
            )}
          </div>

          {error && (
            <p className="rounded-lg border border-rose-400/40 bg-rose-400/10 px-3 py-2 text-xs text-rose-200">
              {error}
            </p>
          )}

          <div className="grid gap-3 sm:grid-cols-2">
            <div>
              <label className="block text-[12px] font-medium text-foreground/80">
                Category
              </label>
              <select
                value={draft.category_id}
                onChange={(e) =>
                  setDraft({ ...draft, category_id: e.target.value })
                }
                className="mt-1.5 w-full rounded-xl border border-border bg-black/30 px-3 py-2.5 text-sm outline-none focus:border-accent/60 focus:bg-black/30"
                required
              >
                {roadmaps.map(({ category }) => (
                  <option
                    key={category.id}
                    value={category.id}
                    className="bg-[#1c1c1c]"
                  >
                    {category.name}
                  </option>
                ))}
              </select>
            </div>
            <TextField
              label="Number"
              type="number"
              min={0}
              value={String(draft.number)}
              onChange={(e) =>
                setDraft({ ...draft, number: Number(e.target.value) })
              }
              required
            />
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

          <TextField
            label="Subtitle"
            value={draft.subtitle}
            onChange={(e) =>
              setDraft({ ...draft, subtitle: e.target.value })
            }
            required
          />

          <TextArea
            label="Description"
            value={draft.description}
            onChange={(e) =>
              setDraft({ ...draft, description: e.target.value })
            }
            rows={3}
            required
          />

          <div className="grid gap-3 sm:grid-cols-2">
            <TextField
              label="Duration"
              value={draft.duration}
              onChange={(e) =>
                setDraft({ ...draft, duration: e.target.value })
              }
              placeholder="2 minggu"
              required
            />
            <TextField
              label="Difficulty"
              value={draft.difficulty}
              onChange={(e) =>
                setDraft({ ...draft, difficulty: e.target.value })
              }
              placeholder="Pemula"
              required
            />
          </div>

          <TextField
            label="Accent color"
            value={draft.accent_color}
            onChange={(e) =>
              setDraft({ ...draft, accent_color: e.target.value })
            }
            placeholder="from-violet-500/30 to-fuchsia-500/10"
            hint="Class Tailwind gradient"
            required
          />

          <TextField
            label="Mini project"
            value={draft.mini_project}
            onChange={(e) =>
              setDraft({ ...draft, mini_project: e.target.value })
            }
            placeholder="Landing page pribadi"
            required
          />

          <div className="grid gap-3 sm:grid-cols-2">
            <TextField
              label="Quiz count"
              type="number"
              min={0}
              value={String(draft.quiz_count ?? 0)}
              onChange={(e) =>
                setDraft({ ...draft, quiz_count: Number(e.target.value) })
              }
            />
            <TextField
              label="Tags"
              value={tagsText}
              onChange={(e) => setTagsText(e.target.value)}
              placeholder="HTML5, CSS3, Flexbox"
              hint="Pisahkan dengan koma"
            />
          </div>

          <CheckBox
            label="Coming soon"
            checked={!!draft.coming_soon}
            onChange={(e) =>
              setDraft({ ...draft, coming_soon: e.target.checked })
            }
          />

          <button
            type="submit"
            disabled={busy}
            className="btn-primary disabled:cursor-not-allowed disabled:opacity-60"
          >
            {busy ? <Loader2 size={14} className="animate-spin" /> : <Save size={14} />}
            {editingId ? "Simpan perubahan" : "Buat level"}
          </button>
        </form>
      </div>
    </div>
  );
}
