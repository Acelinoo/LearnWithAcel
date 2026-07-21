import Image from "next/image";
import Link from "next/link";
import { ArrowRight, Github, Globe, Heart, Instagram, Mail, Twitter } from "lucide-react";
import Reveal from "@/components/ui/Reveal";
import SectionHeading from "@/components/ui/SectionHeading";

export const metadata = {
  title: "About — Cerita di balik LearnWithAcel",
  description:
    "Kenalan dengan Acel, alasan dibalik LearnWithAcel, dan visi platform ini untuk pemula di Indonesia.",
};

const journey = [
  {
    year: "2021",
    title: "Pertama kali berkenalan dengan kode",
    desc: "Belajar HTML di sekolah dan otodidak dari tutorial di YouTube. Bingung, gangerti, sempet nyerah karna gak tau harus mulai darimana, tapi itu titik menyenangkanya. Kenapa bisa? Coba dulu deh, nanti kamu bakal tau kenapa bisa seru.",
  },
  {
    year: "2022",
    title: "Masuk ke JavaScript & React",
    desc: "Mulai paham cara berpikir komponen. Project pertama: website portofolio pribadi.",
  },
  {
    year: "2023",
    title: "PKL pertama",
    desc: "Membuat beberapa project seperti Website Hotel, dll.",
  },
  {
    year: "2024",
    title: "Menjadi Mahasiswa UNIKOM",
    desc: "Di UNIKOM saya mengambil prodi Manajemen Informatika.",
  },
  {
    year: "2026",
    title: "Lahirnya LearnWithAcel",
    desc: "Platform ini dibuat untuk orang seperti aku dulu. Ingin memulai tapi bingung dari mana.",
  },
];

const faqs = [
  {
    q: "Beneran gratis?",
    a: "Iya. Semua materi di LearnWithAcel bisa diakses tanpa biaya. Donasi bersifat opsional dan sangat dihargai.",
  },
  {
    q: "Cocok untuk pemula?",
    a: "Sangat cocok. Semua materi ditulis dengan asumsi kamu baru pertama kali kenal web development.",
  },
  {
    q: "Kenapa fokusnya frontend dulu?",
    a: "Frontend memberi feedback visual cepat. Pemula lebih termotivasi karena hasilnya langsung terlihat.",
  },
];

export default function AboutPage() {
  return (
    <div>
      {/* Header */}
      <section className="container-page pt-16">
        <Reveal>
          <span className="section-eyebrow">About</span>
        </Reveal>
        <Reveal delay={0.05}>
          <h1 className="mt-5 max-w-3xl font-display text-4xl font-semibold tracking-tight text-balance sm:text-5xl">
            Alasanku membuat LearnWithAcel karna masalalu.
          </h1>
        </Reveal>
        <Reveal delay={0.1}>
          <p className="mt-5 max-w-2xl text-lg leading-relaxed text-muted">
            Aku pernah mengalami kebingungan karna gak tau harus mulai dari mana. Udah coba nonton tutorial berjam-jam
            tapi tetap aja gak tahu harus mulai dari mana. Dan Platform ini adalah
            jalan yang kuharap ada pada saat itu.
          </p>
        </Reveal>
      </section>

      {/* Creator card */}
      <section className="container-page mt-16">
        <Reveal>
          <div className="card-base overflow-hidden p-8 sm:p-10">
            <div className="grid gap-8 md:grid-cols-[auto_1fr] md:items-center">
              <div className="relative">
                <div className="relative h-36 w-36 overflow-hidden rounded-2xl border border-border">
                  <Image
                    src="/me.png"
                    alt="Foto Acel"
                    fill
                    className="object-cover"
                    sizes="144px"
                  />
                </div>
                <div className="absolute -right-2 -top-2 h-3 w-3 rounded-full bg-emerald-400 shadow-[0_0_12px_rgba(52,211,153,0.8)]" />
              </div>
              <div>
                <div className="font-mono text-xs uppercase tracking-[0.14em] text-accent-hover">
                  Creator
                </div>
                <h2 className="mt-2 font-display text-3xl font-semibold">
                  Acel
                </h2>
                <p className="mt-1 text-muted">
                  Frontend developer. Indonesia.
                </p>
                <p className="mt-5 max-w-2xl text-[15px] leading-relaxed text-foreground/85">
                  Aku membuat interface yang rapi, nyaman, dan memberikan materi dari hal dasar. Percayalah, setiap orang bisa menjadi developer asalkan mempunyai niat dan diberikan kemudahan untuk memahami porsi demi porsi materi.
                </p>
                <div className="mt-6 flex flex-wrap gap-2">
                  <a href="https://github.com" className="btn-secondary">
                    <Github size={16} />
                    GitHub
                  </a>
                  <a href="https://twitter.com" className="btn-secondary">
                    <Instagram size={16} />
                    Instagram
                  </a>
                  <a href="https://example.com" className="btn-secondary">
                    <Globe size={16} />
                    Portfolio
                  </a>
                  <a
                    href="mailto:halo@learnwithacel.dev"
                    className="btn-secondary"
                  >
                    <Mail size={16} />
                    Email
                  </a>
                </div>
              </div>
            </div>
          </div>
        </Reveal>
      </section>

      {/* Vision */}
      <section className="container-page py-24">
        <div className="grid gap-10 lg:grid-cols-2 lg:items-start">
          <div>
            <SectionHeading
              eyebrow="Visi"
              title="Belajar coding gak harus mahal, cukup siapkan niat."
              description="Aku percaya jalan paling pendek menuju developer dimulai dari satu langkah yang jelas, bukan seratus tutorial acak."
            />
          </div>
          <Reveal>
            <div className="grid gap-3 sm:grid-cols-2">
              {[
                {
                  t: "Akses terbuka",
                  d: "Semua materi dasar gratis dan selalu begitu.",
                },
                {
                  t: "Ramah pemula",
                  d: "Bahasa santai, tanpa istilah membingungkan di awal.",
                },
                {
                  t: "Progresif",
                  d: "Level demi level, satu langkah nyata setiap hari.",
                },
                {
                  t: "Nyata",
                  d: "Mini project di setiap level agar langsung terasa.",
                },
              ].map((x) => (
                <div key={x.t} className="card-base p-5">
                  <div className="font-display text-sm font-semibold">
                    {x.t}
                  </div>
                  <p className="mt-2 text-sm leading-relaxed text-muted">
                    {x.d}
                  </p>
                </div>
              ))}
            </div>
          </Reveal>
        </div>
      </section>

      {/* Journey */}
      <section className="container-page pb-24">
        <SectionHeading
          eyebrow="Perjalanan"
          title="Dari otodidak ke mengajar."
          description="Beberapa titik penting dalam perjalanan belajarku, yang akhirnya membawa ke platform ini."
        />
        <div className="relative space-y-4">
          <div className="absolute left-[18px] top-4 bottom-4 w-px bg-gradient-to-b from-accent/40 via-white/10 to-transparent" />
          {journey.map((j, i) => (
            <Reveal key={j.year} delay={i * 0.05}>
              <div className="relative pl-12">
                <div className="absolute left-0 top-4 flex h-9 w-9 items-center justify-center rounded-xl border border-border bg-card">
                  <Heart size={14} className="text-accent-hover" />
                </div>
                <div className="card-base p-5">
                  <div className="flex items-baseline gap-3">
                    <span className="font-mono text-xs text-accent-hover">
                      {j.year}
                    </span>
                    <h3 className="font-display text-lg font-semibold">
                      {j.title}
                    </h3>
                  </div>
                  <p className="mt-2 text-sm leading-relaxed text-muted">
                    {j.desc}
                  </p>
                </div>
              </div>
            </Reveal>
          ))}
        </div>
      </section>

      {/* FAQ */}
      <section id="faq" className="container-page pb-24">
        <SectionHeading
          eyebrow="FAQ"
          title="Pertanyaan yang sering muncul."
        />
        <div className="grid gap-3 md:grid-cols-3">
          {faqs.map((f, i) => (
            <Reveal key={f.q} delay={i * 0.05}>
              <div className="card-base h-full p-6">
                <h4 className="font-display text-base font-semibold">
                  {f.q}
                </h4>
                <p className="mt-2 text-sm leading-relaxed text-muted">
                  {f.a}
                </p>
              </div>
            </Reveal>
          ))}
        </div>
      </section>

      {/* Support CTA */}
      <section className="container-page pb-24">
        <Reveal>
          <div className="flex flex-wrap items-center justify-between gap-6 rounded-2xl border border-border bg-gradient-to-r from-card to-accent/10 p-8">
            <div>
              <div className="font-display text-lg font-semibold">
                Ingin mendukung platform ini?
              </div>
              <p className="mt-1 text-sm text-muted">
                Donasimu membantu materi baru terus hadir. Gratis tetap gratis.
              </p>
            </div>
            <Link href="/donate" className="btn-primary">
              Support LearnWithAcel
              <ArrowRight size={16} />
            </Link>
          </div>
        </Reveal>
      </section>
    </div>
  );
}
