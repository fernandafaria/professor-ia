/**
 * Landing Page Principal - mano, traduz
 * Design: https://www.figma.com/design/ILmQnETiI8BLMHNat02e1W/Untitled?node-id=3-248
 * Estrutura: Hero → Como funciona → Por que → Em breve → CTA → Footer
 */

import Header from '@/components/figma/Header';
import HeroSection from '@/components/figma/HeroSection';
import ComoFuncionaSection from '@/components/figma/ComoFuncionaSection';
import WhySection from '@/components/figma/WhySection';
import EmBreveSection from '@/components/figma/EmBreveSection';
import FinalCTA from '@/components/figma/FinalCTA';
import Footer from '@/components/figma/Footer';

export default function Home() {
  return (
    <main className="landing-page">
      <Header />
      <HeroSection />
      <ComoFuncionaSection />
      <WhySection />
      <EmBreveSection />
      <FinalCTA />
      <Footer />
    </main>
  );
}
