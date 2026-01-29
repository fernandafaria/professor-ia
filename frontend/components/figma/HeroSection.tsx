/**
 * Hero Section - Landing mano, traduz
 * Design: https://www.figma.com/design/ILmQnETiI8BLMHNat02e1W/Untitled?node-id=3-248
 */

'use client';

import { useRouter } from 'next/navigation';
import { useState } from 'react';

export default function HeroSection() {
  const router = useRouter();
  const [loading, setLoading] = useState(false);

  const handleStart = () => {
    setLoading(true);
    router.push('/onboarding');
  };

  const handleSeeHow = () => {
    const element = document.getElementById('como-funciona');
    if (element) element.scrollIntoView({ behavior: 'smooth' });
  };

  return (
    <section className="hero-section">
      <div className="hero-container">
        <div className="hero-content">
          <h1 className="hero-title">
            estudos do jeito que a sua cabeça aprende
          </h1>
          <p className="hero-description">
            A matéria não entra do jeito que a escola ensina? A gente traduz o conteúdo pro seu jeito com seus interesses. Sem estresse, com autonomia. Sem julgamento, no seu tempo.
          </p>
          <div className="hero-buttons">
            <button className="cta-primary" onClick={handleStart} disabled={loading}>
              {loading ? 'Carregando...' : 'começar grátis'}
            </button>
            <button className="cta-secondary" onClick={handleSeeHow}>
              ver como funciona
            </button>
          </div>
          <div className="feature-tags">
            <div className="tag">Ensino Fundamental e Médio</div>
            <div className="tag">TDAH · dislexia · TEA</div>
            <div className="tag">Sem desculpas</div>
            <div className="tag">No seu ritmo</div>
          </div>
        </div>
        <div className="hero-chat-mock">
          <div className="chat-bubble">
            <div className="chat-header">
              <span className="chat-logo">f</span>
              <span className="chat-name">Mano</span>
            </div>
            <p className="chat-label">Matemática + Motivador</p>
            <p className="chat-question">
              Mano, tipo assim: se você tem 1/4 de HP no LoL, você tá com quantos % de vida? Isso é fração?
            </p>
            <button type="button" className="chat-cta">Entendeu!</button>
          </div>
          <p className="streak-label">Streak ativo</p>
        </div>
      </div>

      <style jsx>{`
        .hero-section {
          background: linear-gradient(135deg, #7C3AED 0%, #5B21B6 100%);
          padding: 4rem 2rem 6rem;
          min-height: 600px;
          display: flex;
          align-items: center;
          position: relative;
          overflow: hidden;
        }

        .hero-container {
          max-width: 1200px;
          margin: 0 auto;
          width: 100%;
          display: grid;
          grid-template-columns: 1fr 1fr;
          gap: 3rem;
          align-items: center;
        }

        .hero-content {
          display: flex;
          flex-direction: column;
          gap: 1.5rem;
        }

        .hero-chat-mock {
          display: flex;
          flex-direction: column;
          align-items: flex-end;
          gap: 0.75rem;
        }

        .chat-bubble {
          background: white;
          border-radius: 16px;
          padding: 1.25rem 1.5rem;
          max-width: 320px;
          box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
        }

        .chat-header {
          display: flex;
          align-items: center;
          gap: 0.5rem;
          margin-bottom: 0.5rem;
        }

        .chat-logo {
          width: 28px;
          height: 28px;
          border-radius: 50%;
          background: #7C3AED;
          color: white;
          display: flex;
          align-items: center;
          justify-content: center;
          font-size: 0.875rem;
          font-weight: 700;
        }

        .chat-name {
          font-weight: 600;
          color: #1a1a1a;
          font-size: 0.9375rem;
        }

        .chat-label {
          font-size: 0.75rem;
          color: #7C3AED;
          margin: 0 0 0.5rem 0;
          font-weight: 600;
        }

        .chat-question {
          font-size: 0.875rem;
          color: #333;
          line-height: 1.5;
          margin: 0 0 1rem 0;
        }

        .chat-cta {
          background: #FF6B35;
          color: white;
          border: none;
          padding: 0.5rem 1rem;
          border-radius: 8px;
          font-size: 0.875rem;
          font-weight: 600;
          cursor: pointer;
          width: 100%;
        }

        .streak-label {
          font-size: 0.8125rem;
          color: rgba(255, 255, 255, 0.85);
          margin: 0;
        }

        .yellow-tag {
          display: inline-flex;
          align-items: center;
          background: #FFC107;
          color: #1a1a1a;
          padding: 0.5rem 1rem;
          border-radius: 24px;
          font-size: 0.875rem;
          font-weight: 600;
          width: fit-content;
          text-transform: lowercase;
        }

        .hero-title {
          font-size: 4rem;
          font-weight: 700;
          color: white;
          line-height: 1.1;
          margin: 0;
          text-transform: lowercase;
        }

        .hero-description {
          font-size: 1.125rem;
          color: rgba(255, 255, 255, 0.9);
          line-height: 1.6;
          margin: 0;
        }

        .hero-buttons {
          display: flex;
          gap: 1rem;
          flex-wrap: wrap;
          margin-top: 0.5rem;
        }

        .cta-primary {
          background: #FF6B35;
          color: white;
          border: none;
          padding: 1rem 2rem;
          border-radius: 12px;
          font-size: 1.125rem;
          font-weight: 600;
          cursor: pointer;
          transition: all 0.2s;
          text-transform: lowercase;
        }

        .cta-primary:hover:not(:disabled) {
          background: #FF5722;
          transform: translateY(-2px);
          box-shadow: 0 4px 12px rgba(255, 107, 53, 0.4);
        }

        .cta-primary:disabled {
          opacity: 0.7;
          cursor: not-allowed;
        }

        .cta-secondary {
          background: transparent;
          color: white;
          border: 2px solid white;
          padding: 1rem 2rem;
          border-radius: 12px;
          font-size: 1.125rem;
          font-weight: 600;
          cursor: pointer;
          transition: all 0.2s;
          text-transform: lowercase;
        }

        .cta-secondary:hover {
          background: rgba(255, 255, 255, 0.1);
        }

        .feature-tags {
          display: flex;
          gap: 0.75rem;
          flex-wrap: wrap;
          margin-top: 1rem;
        }

        .tag {
          display: inline-flex;
          align-items: center;
          gap: 0.5rem;
          padding: 0.5rem 1rem;
          border: 1px solid rgba(255, 255, 255, 0.3);
          border-radius: 24px;
          font-size: 0.875rem;
          font-weight: 500;
          color: white;
          background: rgba(255, 255, 255, 0.1);
          backdrop-filter: blur(10px);
        }

        @media (max-width: 968px) {
          .hero-container {
            grid-template-columns: 1fr;
          }

          .hero-chat-mock {
            display: none;
          }

          .hero-title {
            font-size: 3rem;
          }
        }

        @media (max-width: 768px) {
          .hero-section {
            padding: 2rem 1.5rem 4rem;
          }

          .hero-title {
            font-size: 2.5rem;
          }

          .hero-description {
            font-size: 1rem;
          }

          .hero-buttons {
            flex-direction: column;
          }

          .cta-primary,
          .cta-secondary {
            width: 100%;
          }
        }
      `}</style>
    </section>
  );
}
