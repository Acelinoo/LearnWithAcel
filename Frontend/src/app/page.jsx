import Hero from "@/components/home/Hero";
import RoadmapPreview from "@/components/home/RoadmapPreview";
import Features from "@/components/home/Features";
import MaterialPreview from "@/components/home/MaterialPreview";
import WhyLearnHere from "@/components/home/WhyLearnHere";
import AboutCreator from "@/components/home/AboutCreator";
import DonationCTA from "@/components/home/DonationCTA";
import ViewTracker from "@/components/ui/ViewTracker";

export default function HomePage() {
  return (
    <>
      <ViewTracker entityType="page" entityId="home" />
      <Hero />
      <RoadmapPreview />
      <Features />
      <MaterialPreview />
      <WhyLearnHere />
      <AboutCreator />
      <DonationCTA />
    </>
  );
}
