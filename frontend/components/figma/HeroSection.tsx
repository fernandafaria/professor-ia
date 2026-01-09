/**
 * Hero Section - Seção principal da landing page
 * Design completo do Figma
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
    // Scroll para seção "Como Funciona" ou abrir modal
    const element = document.getElementById('como-funciona');
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <section className="hero-section">
      <div className="hero-container">
        <div className="hero-content">
          {/* Badge Novo */}
          <div className="new-badge">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none">
              <path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z" fill="currentColor"/>
            </svg>
            Novo: Ganhe XP, suba de nível e desbloqueie badges!
          </div>

          {/* Título Principal */}
          <h1 className="hero-title">
            Aprenda com um Professor de IA Feito pra Você 🚀
          </h1>

          {/* Descrição */}
          <p className="hero-description">
            Chega de aulas chatas! Crie seu professor virtual do jeito que você gosta. 
            Escolha a personalidade, a matéria e até o estilo de ensino. É tipo ter um 
            tutor particular que te entende de verdade.
          </p>

          {/* Botões CTA */}
          <div className="hero-buttons">
            <button
              className="cta-primary"
              onClick={handleStart}
              disabled={loading}
            >
              Bora Começar! É de Graça
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none">
                <path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z" fill="currentColor"/>
              </svg>
            </button>
            <button
              className="cta-secondary"
              onClick={handleSeeHow}
            >
              Ver Como Funciona
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none">
                <path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z" fill="currentColor"/>
              </svg>
            </button>
          </div>

          {/* Feature Tags */}
          <div className="feature-tags">
            <div className="tag tag-green">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none">
                <path d="M12 1L3 5V11C3 16.55 6.16 21.74 12 23C17.84 21.74 21 16.55 21 11V5L12 1Z" fill="currentColor"/>
              </svg>
              100% Grátis
            </div>
            <div className="tag tag-orange">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none">
                <path d="M13 2L3 14H12L11 22L21 10H12L13 2Z" fill="currentColor"/>
              </svg>
              Pronto em 2 min
            </div>
            <div className="tag tag-pink">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none">
                <path d="M12 2C6.48 2 2 6.48 2 12C2 17.52 6.48 22 12 22C17.52 22 22 17.52 22 12C22 6.48 17.52 2 12 2ZM13 17H11V15H13V17ZM13 13H11V7H13V13Z" fill="currentColor"/>
              </svg>
              Super Divertido
            </div>
          </div>
        </div>

        {/* Card do Professor */}
        <div className="professor-card">
          <div className="xp-badge">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none">
              <path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z" fill="currentColor"/>
            </svg>
            +50 XP
          </div>
          <div className="professor-header">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
              <path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z" fill="#8B5CF6"/>
            </svg>
            <span className="professor-name">Prof. Alex</span>
          </div>
          <div className="professor-subject">Matemática • Motivador</div>
          <div className="professor-message">
            "Vamos resolver esse problema juntos! Você está indo muito bem!" 💪
          </div>
          <div className="professor-duration">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none">
              <path d="M12 2C6.48 2 2 6.48 2 12C2 17.52 6.48 22 12 22C17.52 22 22 17.52 22 12C22 6.48 17.52 2 12 2ZM13 17H11V15H13V17ZM13 13H11V7H13V13Z" fill="#8B5CF6"/>
            </svg>
            7 dias
          </div>
        </div>
      </div>

      <style jsx>{`
        .hero-section {
          background: white;
          padding: 4rem 2rem;
          min-height: 600px;
          display: flex;
          align-items: center;
        }

        .hero-container {
          max-width: 1200px;
          margin: 0 auto;
          display: grid;
          grid-template-columns: 1fr 1fr;
          gap: 4rem;
          align-items: center;
        }

        .hero-content {
          display: flex;
          flex-direction: column;
          gap: 1.5rem;
        }

        .new-badge {
          display: inline-flex;
          align-items: center;
          gap: 0.5rem;
          background: #f5f0ff;
          color: #8B5CF6;
          padding: 0.5rem 1rem;
          border-radius: 20px;
          font-size: 0.875rem;
          font-weight: 500;
          width: fit-content;
        }

        .hero-title {
          font-size: 3.5rem;
          font-weight: 700;
          color: #1a1a1a;
          line-height: 1.1;
          margin: 0;
        }

        .hero-description {
          font-size: 1.125rem;
          color: #666;
          line-height: 1.6;
          margin: 0;
        }

        .hero-buttons {
          display: flex;
          gap: 1rem;
          flex-wrap: wrap;
        }

        .cta-primary {
          background: #8B5CF6;
          color: white;
          border: none;
          padding: 1rem 2rem;
          border-radius: 12px;
          font-size: 1.125rem;
          font-weight: 600;
          cursor: pointer;
          display: flex;
          align-items: center;
          gap: 0.5rem;
          transition: all 0.2s;
        }

        .cta-primary:hover:not(:disabled) {
          background: #7C3AED;
          transform: translateY(-2px);
          box-shadow: 0 4px 12px rgba(139, 92, 246, 0.4);
        }

        .cta-primary:disabled {
          opacity: 0.7;
          cursor: not-allowed;
        }

        .cta-secondary {
          background: white;
          color: #8B5CF6;
          border: 2px solid #8B5CF6;
          padding: 1rem 2rem;
          border-radius: 12px;
          font-size: 1.125rem;
          font-weight: 600;
          cursor: pointer;
          display: flex;
          align-items: center;
          gap: 0.5rem;
          transition: all 0.2s;
        }

        .cta-secondary:hover {
          background: #f5f0ff;
        }

        .feature-tags {
          display: flex;
          gap: 0.75rem;
          flex-wrap: wrap;
        }

        .tag {
          display: inline-flex;
          align-items: center;
          gap: 0.5rem;
          padding: 0.5rem 1rem;
          border-radius: 20px;
          font-size: 0.875rem;
          font-weight: 500;
        }

        .tag-green {
          background: #f0fdf4;
          color: #16a34a;
        }

        .tag-orange {
          background: #fff7ed;
          color: #ea580c;
        }

        .tag-pink {
          background: #fdf2f8;
          color: #db2777;
        }

        .professor-card {
          background: #f5f0ff;
          border-radius: 16px;
          padding: 1.5rem;
          position: relative;
          box-shadow: 0 4px 20px rgba(139, 92, 246, 0.15);
        }

        .xp-badge {
          position: absolute;
          top: -10px;
          right: 16px;
          background: white;
          color: #ea580c;
          padding: 0.5rem 0.75rem;
          border-radius: 20px;
          font-size: 0.875rem;
          font-weight: 600;
          display: flex;
          align-items: center;
          gap: 0.25rem;
          box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        }

        .professor-header {
          display: flex;
          align-items: center;
          gap: 0.5rem;
          margin-bottom: 0.5rem;
        }

        .professor-name {
          font-size: 1.125rem;
          font-weight: 600;
          color: #1a1a1a;
        }

        .professor-subject {
          font-size: 0.875rem;
          color: #666;
          margin-bottom: 1rem;
        }

        .professor-message {
          background: white;
          padding: 1rem;
          border-radius: 12px;
          font-size: 0.875rem;
          color: #333;
          margin-bottom: 1rem;
          line-height: 1.5;
        }

        .professor-duration {
          display: flex;
          align-items: center;
          gap: 0.5rem;
          font-size: 0.875rem;
          color: #8B5CF6;
          font-weight: 500;
        }

        @media (max-width: 968px) {
          .hero-container {
            grid-template-columns: 1fr;
            gap: 2rem;
          }

          .hero-title {
            font-size: 2.5rem;
          }
        }

        @media (max-width: 768px) {
          .hero-section {
            padding: 2rem 1.5rem;
          }

          .hero-title {
            font-size: 2rem;
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
