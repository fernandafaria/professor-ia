/**
 * Final CTA Section - CTA roxo final
 */

'use client';

import { useRouter } from 'next/navigation';
import { useState } from 'react';

export default function FinalCTA() {
  const router = useRouter();
  const [loading, setLoading] = useState(false);

  const handleCreate = () => {
    setLoading(true);
    router.push('/onboarding');
  };

  return (
    <section className="final-cta">
      <div className="final-cta-content">
        <h2 className="cta-title">
          Bora dominar os estudos? 🚀
        </h2>
        <p className="cta-description">
          Crie seu professor em 2 minutos e já começa a ganhar XP. É grátis e você não precisa de cartão de crédito!
        </p>
        <button
          className="cta-button"
          onClick={handleCreate}
          disabled={loading}
        >
          {loading ? 'Carregando...' : 'Criar Meu Professor Agora'}
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
            <path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z" fill="currentColor"/>
          </svg>
        </button>
        <p className="cta-subtext">
          Demora menos que escolher uma série pra assistir
        </p>
      </div>

      <style jsx>{`
        .final-cta {
          background: linear-gradient(135deg, #8B5CF6 0%, #7C3AED 100%);
          padding: 5rem 2rem;
          display: flex;
          justify-content: center;
          align-items: center;
        }

        .final-cta-content {
          max-width: 800px;
          text-align: center;
          color: white;
        }

        .cta-title {
          font-size: 3rem;
          font-weight: 700;
          margin: 0 0 1.5rem 0;
          line-height: 1.2;
        }

        .cta-description {
          font-size: 1.25rem;
          margin: 0 0 2.5rem 0;
          opacity: 0.95;
          line-height: 1.6;
        }

        .cta-button {
          background: white;
          color: #8B5CF6;
          border: none;
          padding: 1.25rem 3rem;
          border-radius: 12px;
          font-size: 1.25rem;
          font-weight: 600;
          cursor: pointer;
          display: inline-flex;
          align-items: center;
          gap: 0.75rem;
          transition: all 0.3s;
          box-shadow: 0 4px 14px rgba(0, 0, 0, 0.2);
          margin-bottom: 1rem;
        }

        .cta-button:hover:not(:disabled) {
          transform: translateY(-2px);
          box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
        }

        .cta-button:disabled {
          opacity: 0.7;
          cursor: not-allowed;
        }

        .cta-subtext {
          font-size: 0.875rem;
          opacity: 0.9;
          margin: 0;
        }

        @media (max-width: 768px) {
          .final-cta {
            padding: 3rem 1.5rem;
          }

          .cta-title {
            font-size: 2rem;
          }

          .cta-description {
            font-size: 1.125rem;
          }

          .cta-button {
            width: 100%;
            font-size: 1.125rem;
            padding: 1rem 2rem;
          }
        }
      `}</style>
    </section>
  );
}
