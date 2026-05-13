import { CheckCircle2 } from "lucide-react";
import SectionHeading from "@/components/ui/SectionHeading";
import Reveal from "@/components/ui/Reveal";

const reasons = [
  "Materi fokus pada pemula, bukan ditulis untuk orang yang sudah paham.",
  "Jalur belajar jelas, tidak melompat-lompat antar topik.",
  "Fokus pada frontend dulu agar kamu cepat bisa membuat sesuatu yang terlihat.",
  "Setiap materi diakhiri dengan latihan dan refleksi.",
  "Dark mode nyaman di mata untuk sesi belajar panjang.",
  "Gratis, tanpa paywall tersembunyi.",
];

export default function WhyLearnHere() {
  return (
    <section className="container-page py-24">
      <div className="grid gap-10 lg:grid-cols-2 lg:items-center">
        <div>
          <SectionHeading
            eyebrow="Kenapa LearnWithAcel"
            title="Bukan kursus mahal, bukan tumpukan tutorial acak."
            description="Kami menyusun ulang cara belajar web dev supaya kamu tidak tersesat di tengah jalan."
          />
        </div>
        <Reveal>
          <div className="card-base p-2">
            <ul className="divide-y divide-white/5">
              {reasons.map((r) => (
                <li
                  key={r}
                  className="flex items-start gap-3 px-4 py-4 text-[15px] leading-relaxed text-foreground/90"
                >
                  <CheckCircle2
                    size={18}
                    className="mt-0.5 shrink-0 text-accent-hover"
                  />
                  {r}
                </li>
              ))}
            </ul>
          </div>
        </Reveal>
      </div>
    </section>
  );
}
