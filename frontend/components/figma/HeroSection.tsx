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
          {/* Tagline */}
          <div className="tagline-badge">
            Traduzir o que ninguem te da para aprender.
          </div>

          {/* Título Principal */}
          <h1 className="hero-title">
            Aprende do jeito que tu entende
          </h1>

          {/* Descrição */}
          <p className="hero-description">
            compara textos gigantes, dúvidas complexas, moderniza a linguagem, 
            simplifica o que parecia complicado
          </p>

          {/* Botões CTA */}
          <div className="hero-buttons">
            <button
              className="cta-primary"
              onClick={handleStart}
              disabled={loading}
            >
              começar gratis
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
              100% gratuito
            </div>
            <div className="tag">
              Foco no Código
            </div>
            <div className="tag">
              Receba certificado
            </div>
          </div>
        </div>
      </div>

      <style jsx>{`
        .hero-section {
          background: linear-gradient(135deg, #8B5CF6 0%, #7C3AED 100%);
          padding: 4rem 2rem;
          min-height: 70vh;
          display: flex;
          align-items: center;
        }

        .hero-container {
          max-width: 1200px;
          margin: 0 auto;
          width: 100%;
        }

        .hero-content {
          max-width: 800px;
          display: flex;
          flex-direction: column;
          gap: 2rem;
        }

        .tagline-badge {
          display: inline-flex;
          align-items: center;
          background: #FFA726;
          color: #1a1a1a;
          padding: 0.625rem 1.25rem;
          border-radius: 30px;
          font-size: 0.875rem;
          font-weight: 500;
          width: fit-content;
        }

        .hero-title {
          font-size: 4rem;
          font-weight: 700;
          color: white;
          line-height: 1.1;
          margin: 0;
        }

        .hero-description {
          font-size: 1.25rem;
          color: rgba(255, 255, 255, 0.9);
          line-height: 1.6;
          margin: 0;
        }

        .hero-buttons {
          display: flex;
          gap: 1rem;
          flex-wrap: wrap;
        }

        .cta-primary {
          background: #FF7043;
          color: white;
          border: none;
          padding: 1rem 2rem;
          border-radius: 12px;
          font-size: 1.125rem;
          font-weight: 600;
          cursor: pointer;
          transition: all 0.2s;
        }

        .cta-primary:hover:not(:disabled) {
          background: #FF5722;
          transform: translateY(-2px);
          box-shadow: 0 4px 12px rgba(255, 112, 67, 0.4);
        }

        .cta-primary:disabled {
          opacity: 0.7;
          cursor: not-allowed;
        }

        .cta-secondary {
          background: white;
          color: #8B5CF6;
          border: 2px solid white;
          padding: 1rem 2rem;
          border-radius: 12px;
          font-size: 1.125rem;
          font-weight: 600;
          cursor: pointer;
          transition: all 0.2s;
        }

        .cta-secondary:hover {
          background: rgba(255, 255, 255, 0.9);
        }

        .feature-tags {
          display: flex;
          gap: 1rem;
          flex-wrap: wrap;
          margin-top: 1rem;
        }

        .tag {
          display: inline-flex;
          align-items: center;
          background: white;
          color: #8B5CF6;
          border: 1px solid #8B5CF6;
          padding: 0.625rem 1.25rem;
          border-radius: 30px;
          font-size: 0.875rem;
          font-weight: 500;
        }

        @media (max-width: 968px) {
          .hero-title {
            font-size: 3rem;
          }

          .hero-description {
            font-size: 1.125rem;
          }
        }

        @media (max-width: 768px) {
          .hero-section {
            padding: 3rem 1.5rem;
            min-height: 60vh;
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

          .feature-tags {
            flex-direction: column;
            gap: 0.75rem;
          }
        }
      `}</style>
    </section>
  );
}
