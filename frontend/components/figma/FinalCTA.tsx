/**
 * Final CTA Section - Pronto pra entender de verdade?
 * Design: https://www.figma.com/design/kYaKQo5HILal0lD7HEcGcN/Untitled
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
      <div className="final-cta-card">
        <h2 className="cta-title">
          Pronto pra entender de verdade?
        </h2>
        <p className="cta-description">
          Começa agora, sem custo, 100% de verdade. E vai ver o que é MENTORIA ILIMITADA. 
          E começa a mandar bem.
        </p>
        <button
          className="cta-button"
          onClick={handleCreate}
          disabled={loading}
        >
          {loading ? 'Carregando...' : 'começar agora e grátis'}
        </button>
      </div>

      <style jsx>{`
        .final-cta {
          background: white;
          padding: 5rem 2rem;
          display: flex;
          justify-content: center;
          align-items: center;
        }

        .final-cta-card {
          max-width: 900px;
          width: 100%;
          background: linear-gradient(135deg, #8B5CF6 0%, #7C3AED 100%);
          border-radius: 16px;
          padding: 4rem 3rem;
          text-align: center;
          color: white;
        }

        .cta-title {
          font-size: 2.5rem;
          font-weight: 700;
          margin: 0 0 1.5rem 0;
          line-height: 1.2;
        }

        .cta-description {
          font-size: 1.125rem;
          margin: 0 0 2.5rem 0;
          opacity: 0.95;
          line-height: 1.6;
        }

        .cta-button {
          background: #FF7043;
          color: white;
          border: none;
          padding: 1.25rem 3rem;
          border-radius: 12px;
          font-size: 1.25rem;
          font-weight: 600;
          cursor: pointer;
          transition: all 0.3s;
          box-shadow: 0 4px 14px rgba(0, 0, 0, 0.2);
        }

        .cta-button:hover:not(:disabled) {
          background: #FF5722;
          transform: translateY(-2px);
          box-shadow: 0 6px 20px rgba(255, 112, 67, 0.4);
        }

        .cta-button:disabled {
          opacity: 0.7;
          cursor: not-allowed;
        }

        @media (max-width: 768px) {
          .final-cta {
            padding: 3rem 1.5rem;
          }

          .final-cta-card {
            padding: 3rem 2rem;
          }

          .cta-title {
            font-size: 2rem;
          }

          .cta-description {
            font-size: 1rem;
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
