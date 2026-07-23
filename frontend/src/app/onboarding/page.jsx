"use client";

import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import { motion, AnimatePresence } from "framer-motion";
import {
  ArrowRight,
  ArrowLeft,
  CheckCircle2,
  Sparkles,
} from "lucide-react";
import { updateRole, getMe } from "@/lib/api/auth";
import { getClientToken } from "@/lib/auth/token";
import { getRoadmap } from "@/lib/api/content";
import { ROLE_CATEGORIES as CATEGORIES } from "@/lib/constants";

export default function OnboardingPage() {
  const router = useRouter();
  const [step, setStep] = useState(1);
  const [selectedCat, setSelectedCat] = useState(null);
  const [selectedRole, setSelectedRole] = useState(null);
  const [isSubmitting, setIsSubmitting] = useState(false);

  useEffect(() => {
    const checkUser = async () => {
      const token = getClientToken();
      if (!token) {
        router.push("/login?redirectTo=/onboarding");
        return;
      }
      try {
        const user = await getMe(token);
        if (user.has_completed_onboarding) {
          router.push("/roadmap");
        }
      } catch (err) {
        console.error("Gagal mendapatkan data user", err);
      }
    };
    checkUser();
  }, [router]);

  const activeCategory = CATEGORIES.find((c) => c.id === selectedCat);

  const handleNext = () => {
    if (step === 1 && selectedCat) {
      setStep(2);
    }
  };

  const handleBack = () => {
    if (step === 2) {
      setStep(1);
      setSelectedRole(null);
    }
  };

  const handleSubmit = async () => {
    if (!selectedCat || !selectedRole) return;
    setIsSubmitting(true);
    try {
      const token = getClientToken();
      if (!token) {
        router.push("/login?redirectTo=/onboarding");
        return;
      }
      
      // Update selected category and role in backend
      await updateRole(token, {
        selected_category: selectedCat,
        selected_role: selectedRole,
      });

      window.location.href = "/roadmap";
    } catch (err) {
      console.error(err);
      alert("Terjadi kesalahan saat menyimpan pilihan role. Silakan coba lagi.");
      setIsSubmitting(false);
    }
  };

  return (
    <div className="container-page py-16">
      <div className="mx-auto max-w-3xl">
        {/* Header */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="text-center"
        >
          <span className="section-eyebrow">
            <Sparkles size={12} />
            Langkah {step} dari 2
          </span>
          <h1 className="mt-4 font-display text-4xl font-semibold tracking-tight text-balance sm:text-5xl">
            {step === 1 ? "Pilih Bidang Keahlian" : "Pilih Spesialisasi Kamu"}
          </h1>
          <p className="mt-4 text-[15px] leading-relaxed text-muted">
            {step === 1
              ? "Pilih kategori besar yang paling sesuai dengan minat kamu."
              : `Kamu memilih ${activeCategory?.title}. Sekarang, pilih peran yang ingin kamu kuasai.`}
          </p>
        </motion.div>

        {/* Content */}
        <div className="mt-12">
          <AnimatePresence mode="wait">
            {step === 1 && (
              <motion.div
                key="step1"
                initial={{ opacity: 0, x: -20 }}
                animate={{ opacity: 1, x: 0 }}
                exit={{ opacity: 0, x: 20 }}
                className="grid gap-4 sm:grid-cols-3"
              >
                {CATEGORIES.map((cat) => (
                  <button
                    key={cat.id}
                    onClick={() => setSelectedCat(cat.id)}
                    className={`group relative flex flex-col items-start rounded-2xl border p-6 text-left transition-all ${
                      selectedCat === cat.id
                        ? "border-accent bg-accent/10 shadow-[0_0_30px_-5px_rgba(139,92,246,0.3)]"
                        : "border-border bg-card hover:border-accent/40 hover:bg-accent/5"
                    }`}
                  >
                    <div className={`flex h-12 w-12 items-center justify-center rounded-xl border ${selectedCat === cat.id ? "border-accent/50 bg-accent/20" : "border-border bg-black/30"} text-accent-hover transition-colors`}>
                      <cat.icon size={20} />
                    </div>
                    <h3 className="mt-4 font-display text-xl font-semibold">{cat.title}</h3>
                    <p className="mt-2 text-sm text-muted">{cat.description}</p>
                  </button>
                ))}
              </motion.div>
            )}

            {step === 2 && activeCategory && (
              <motion.div
                key="step2"
                initial={{ opacity: 0, x: -20 }}
                animate={{ opacity: 1, x: 0 }}
                exit={{ opacity: 0, x: 20 }}
                className="grid gap-4"
              >
                {activeCategory.roles.map((role) => (
                  <button
                    key={role.slug}
                    onClick={() => setSelectedRole(role.slug)}
                    className={`group relative flex flex-col items-start gap-4 rounded-2xl border p-6 text-left transition-all sm:flex-row sm:items-center ${
                      selectedRole === role.slug
                        ? "border-accent bg-accent/10 shadow-[0_0_30px_-5px_rgba(139,92,246,0.3)]"
                        : "border-border bg-card hover:border-accent/40 hover:bg-accent/5"
                    }`}
                  >
                    <div className="flex-1">
                      <h3 className="font-display text-xl font-semibold">{role.name}</h3>
                      <p className="mt-1 text-sm text-muted">{role.description}</p>
                      <div className="mt-3 flex flex-wrap gap-2">
                        {role.tasks.map((task) => (
                          <span key={task} className="rounded-md border border-border bg-black/30 px-2 py-1 text-[11px] font-medium text-muted">
                            {task}
                          </span>
                        ))}
                      </div>
                    </div>
                    {selectedRole === role.slug && (
                      <div className="shrink-0 text-accent-hover">
                        <CheckCircle2 size={24} />
                      </div>
                    )}
                  </button>
                ))}
              </motion.div>
            )}
          </AnimatePresence>
        </div>

        {/* Footer Actions */}
        <div className="mt-12 flex items-center justify-between border-t border-border pt-6">
          {step === 1 ? (
            <div />
          ) : (
            <button
              onClick={handleBack}
              className="flex items-center gap-2 rounded-xl px-4 py-2 text-sm font-medium text-muted transition-colors hover:text-foreground"
            >
              <ArrowLeft size={16} />
              Kembali
            </button>
          )}

          {step === 1 ? (
            <button
              onClick={handleNext}
              disabled={!selectedCat}
              className={`btn-primary ${!selectedCat ? "opacity-50 cursor-not-allowed" : ""}`}
            >
              Lanjutkan
              <ArrowRight size={16} />
            </button>
          ) : (
            <button
              onClick={handleSubmit}
              disabled={!selectedRole || isSubmitting}
              className={`btn-primary ${(!selectedRole || isSubmitting) ? "opacity-50 cursor-not-allowed" : ""}`}
            >
              {isSubmitting ? "Menyimpan..." : "Mulai Belajar"}
              {!isSubmitting && <ArrowRight size={16} />}
            </button>
          )}
        </div>
      </div>
    </div>
  );
}
