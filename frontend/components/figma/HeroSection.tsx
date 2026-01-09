/**
 * Hero Section - Landing Page mano, traduz!
 * Design: https://www.figma.com/design/kYaKQo5HILal0lD7HEcGcN/Untitled
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

  const handleSeeOpportunities = () => {
    const element = document.getElementById('como-funciona');
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <section className="hero-section">
      <div className="hero-container">
        <div className="hero-content">
          {/* Tag Amarela */}
          <div className="yellow-tag">
            Traduzir o que você não entende de forma interativa
          </div>

          {/* Título Principal */}
          <h1 className="hero-title">
            Aprende do jeito que tu entende
          </h1>

          {/* Descrição */}
          <p className="hero-description">
            Aprenda do seu jeito! Explica aí com exemplos dos seus interesses, 
            da sua realidade e tudo mais que faz sentido pra você!
          </p>

          {/* Botões CTA */}
          <div className="hero-buttons">
            <button
              className="cta-primary"
              onClick={handleStart}
              disabled={loading}
            >
              {loading ? 'Carregando...' : 'começar grátis'}
            </button>
            <button
              className="cta-secondary"
              onClick={handleSeeOpportunities}
            >
              ver oportunidades
            </button>
          </div>

          {/* Feature Tags */}
          <div className="feature-tags">
            <div className="tag">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none">
                <path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z" fill="currentColor"/>
              </svg>
              XP na aula
            </div>
            <div className="tag">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none">
                <path d="M13 2L3 14H12L11 22L21 10H12L13 2Z" fill="currentColor"/>
              </svg>
              Pontos XP
            </div>
            <div className="tag">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none">
                <path d="M12 2C6.48 2 2 6.48 2 12C2 17.52 6.48 22 12 22C17.52 22 22 17.52 22 12C22 6.48 17.52 2 12 2ZM10 17L5 12L6.41 10.59L10 14.17L17.59 6.58L19 8L10 17Z" fill="currentColor"/>
              </svg>
              Resultados
            </div>
          </div>
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
        }

        .hero-content {
          display: flex;
          flex-direction: column;
          gap: 1.5rem;
          max-width: 700px;
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
