/**
 * Landing Page Principal - Professor IA
 * Design completo do Figma: https://www.figma.com/design/masYeVMxkPMQ0zDMDrvZCx/Untitled
 */

import Header from '@/components/figma/Header';
import HeroSection from '@/components/figma/HeroSection';
import WhySection from '@/components/figma/WhySection';
import GameChangerSection from '@/components/figma/GameChangerSection';
import FinalCTA from '@/components/figma/FinalCTA';
import Footer from '@/components/figma/Footer';

export default function Home() {
  return (
    <main className="landing-page">
      <Header />
      <HeroSection />
      <WhySection />
      <GameChangerSection />
      <FinalCTA />
      <Footer />
    </main>
  );
}
