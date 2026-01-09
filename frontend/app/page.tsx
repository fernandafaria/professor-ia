/**
 * Landing Page Principal - mano, traduz!
 * Design: https://www.figma.com/design/kYaKQo5HILal0lD7HEcGcN/Untitled
 */

import Header from '@/components/figma/Header';
import HeroSection from '@/components/figma/HeroSection';
import ComoFuncionaSection from '@/components/figma/ComoFuncionaSection';
import WhySection from '@/components/figma/WhySection';
import FinalCTA from '@/components/figma/FinalCTA';
import Footer from '@/components/figma/Footer';

export default function Home() {
  return (
    <main className="landing-page">
      <Header />
      <HeroSection />
      <ComoFuncionaSection />
      <WhySection />
      <FinalCTA />
      <Footer />
    </main>
  );
}
