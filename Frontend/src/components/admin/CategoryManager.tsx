"use client";

import { useState, type FormEvent } from "react";
import { Plus, Save, Trash2, Pencil, X, Loader2 } from "lucide-react";
import {
  createCategory,
  deleteCategory,
  updateCategory,
  type CategoryCreate,
} from "@/lib/api/admin";
import {
  normalizeTechs,
  type ApiRoadmap,
  type TechGroup,
} from "@/lib/api/content";
import { ApiError } from "@/lib/api/client";
import { CheckBox, TextArea, TextField } from "./AdminField";

type Props = {
  roadmaps: ApiRoadmap[];
  token: string;
  onChange: () => void;
};

const EMPTY: CategoryCreate = {
  name: "",
  slug: "",
  available: false,
  role: "",
  side: "",
  description: "",
  tasks: "",
  techs: [],
};

function techsToText(techs: TechGroup[]): string {
  return techs
    .map((g) => `${g.label}: ${g.items.join(", ")}`)
    .join("\n");
}

function textToTechs(text: string): TechGroup[] {
  return text
    .split("\n")
    .map((line) => line.trim())
    .filter(Boolean)
    .map((line) => {
      const [label, items = ""] = line.split(":");
      return {
        label: label.trim(),
        items: items
          .split(",")
          .map((s) => s.trim())
          .filter(Boolean),
      };
    });
}

export default function CategoryManager({
  roadmaps,
  token,
  onChange,
}: Props) {
  const [editingId, setEditingId] = useState<string | null>(null);
  const [draft, setDraft] = useState<CategoryCreate>(EMPTY);
  const [techsText, setTechsText] = useState("");
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);

  function startCreate() {
    setEditingId(null);
    setDraft(EMPTY);
    setTechsText("");
    setError(null);
  }

  function startEdit(roadmap: ApiRoadmap) {
    const c = roadmap.category;
    const techs = normalizeTechs(c.techs);
    setEditingId(c.id);
    setDraft({
      name: c.name,
      slug: c.slug,
      available: c.available,
      role: c.role,
      side: c.side,
      description: c.description,
      tasks: c.tasks,
      techs,
    });
    setTechsText(techsToText(techs));
    setError(null);
  }

  async function onSubmit(e: FormEvent) {
    e.preventDefault();
    if (busy) return;
    setBusy(true);
    setError(null);

    const payload: CategoryCreate = {
      ...draft,
      techs: textToTechs(techsText),
    };

    try {
      if (editingId) {
        await updateCategory(editingId, payload, token);
      } else {
        await createCategory(payload, token);
      }
      onChange();
      startCreate();
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

  async function onDelete(id: string, name: string) {
    if (
      !confirm(
        `Hapus kategori "${name}"? Semua level dan lesson di dalamnya juga akan terhapus.`
      )
    )
      return;
    setBusy(true);
    setError(null);
    try {
      await deleteCategory(id, token);
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
    <div className="grid gap-6 lg:grid-cols-[1fr_1.1fr]">
      {/* List */}
      <div>
        <div className="flex items-center justify-between">
          <h2 className="font-display text-lg font-semibold">Categories</h2>
          <button onClick={startCreate} className="btn-secondary">
            <Plus size={14} />
            Baru
          </button>
        </div>

        <ul className="mt-4 space-y-2">
          {roadmaps.map(({ category, levels }) => (
            <li
              key={category.id}
              className={
                "flex items-center gap-3 rounded-xl border bg-white/[0.02] p-3 transition-colors " +
                (editingId === category.id
                  ? "border-accent/40"
                  : "border-white/5")
              }
            >
              <div className="min-w-0 flex-1">
                <div className="flex items-center gap-2 text-[11px] uppercase tracking-wider text-muted">
                  {category.available ? (
                    <span className="rounded-full border border-emerald-400/30 bg-emerald-400/10 px-1.5 py-0.5 text-[10px] text-emerald-300">
                      Available
                    </span>
                  ) : (
                    <span className="rounded-full border border-white/10 bg-white/[0.04] px-1.5 py-0.5 text-[10px] text-muted">
                      Hidden
                    </span>
                  )}
                  <span>/{category.slug}</span>
                  <span>· {levels.length} levels</span>
                </div>
                <div className="mt-0.5 truncate text-sm font-medium text-foreground">
                  {category.name}
                </div>
              </div>
              <button
                onClick={() => startEdit({ category, levels })}
                className="btn-ghost text-xs"
                title="Edit"
              >
                <Pencil size={13} />
              </button>
              <button
                onClick={() => onDelete(category.id, category.name)}
                className="btn-ghost text-xs text-rose-300 hover:text-rose-200"
                title="Hapus"
              >
                <Trash2 size={13} />
              </button>
            </li>
          ))}
          {roadmaps.length === 0 && (
            <li className="text-sm text-muted">Belum ada category.</li>
          )}
        </ul>
      </div>

      {/* Form */}
      <form onSubmit={onSubmit} className="space-y-3">
        <div className="flex items-center justify-between">
          <h2 className="font-display text-lg font-semibold">
            {editingId ? "Edit category" : "Buat category baru"}
          </h2>
          {editingId && (
            <button
              type="button"
              onClick={startCreate}
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
          <TextField
            label="Nama"
            value={draft.name}
            onChange={(e) => setDraft({ ...draft, name: e.target.value })}
            placeholder="Frontend"
            required
          />
          <TextField
            label="Slug"
            value={draft.slug}
            onChange={(e) => setDraft({ ...draft, slug: e.target.value })}
            placeholder="frontend"
            pattern="[a-z0-9\-]+"
            hint="lowercase, angka, dan tanda hubung"
            required
          />
        </div>

        <div className="grid gap-3 sm:grid-cols-2">
          <TextField
            label="Role"
            value={draft.role}
            onChange={(e) => setDraft({ ...draft, role: e.target.value })}
            placeholder="Front-End Developer"
            required
          />
          <TextField
            label="Side"
            value={draft.side}
            onChange={(e) => setDraft({ ...draft, side: e.target.value })}
            placeholder="Sisi Klien / Client-Side"
            required
          />
        </div>

        <TextArea
          label="Description"
          value={draft.description}
          onChange={(e) =>
            setDraft({ ...draft, description: e.target.value })
          }
          rows={3}
          required
        />

        <TextArea
          label="Tasks"
          value={draft.tasks}
          onChange={(e) => setDraft({ ...draft, tasks: e.target.value })}
          rows={2}
          required
        />

        <TextArea
          label="Techs"
          value={techsText}
          onChange={(e) => setTechsText(e.target.value)}
          rows={3}
          placeholder={"Dasar: HTML, CSS, JavaScript\nFramework: React.js, Next.js"}
          hint="Satu grup per baris. Format: Label: item1, item2, item3"
        />

        <CheckBox
          label="Available (terlihat di pilih-jalur)"
          checked={draft.available}
          onChange={(e) => setDraft({ ...draft, available: e.target.checked })}
        />

        <button
          type="submit"
          disabled={busy}
          className="btn-primary disabled:cursor-not-allowed disabled:opacity-60"
        >
          {busy ? <Loader2 size={14} className="animate-spin" /> : <Save size={14} />}
          {editingId ? "Simpan perubahan" : "Buat category"}
        </button>
      </form>
    </div>
  );
}
