import { EarlyAccess } from "@/components/EarlyAccess";
import { Footer } from "@/components/Footer";
import { Hero } from "@/components/Hero";
import { HowItWorks } from "@/components/HowItWorks";
import { Navbar } from "@/components/Navbar";
import { RevealObserver } from "@/components/Reveal";
import { SecurityPrivacy } from "@/components/SecurityPrivacy";
import { UsefulForFamilies } from "@/components/UsefulForFamilies";
import { WhyFamilyKit } from "@/components/WhyFamilyKit";

export default function Home() {
  return (
    <>
      <a className="skip-link" href="#main">
        Skip to content
      </a>
      <Navbar />
      <main id="main">
        <Hero />
        <WhyFamilyKit />
        <HowItWorks />
        <UsefulForFamilies />
        <SecurityPrivacy />
        <EarlyAccess />
      </main>
      <Footer />
      <RevealObserver />
    </>
  );
}
