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

  const handleStart = () => {
    setLoading(true);
    router.push('/onboarding');
  };

  return (
    <section className="final-cta">
      <div className="final-cta-container">
        <h2 className="cta-title">
          Pronto pra estudar do seu jeito?
        </h2>
        <p className="cta-description">
          Começa grátis, sem cartão. Crie seu perfil e já começa a mandar bem no seu ritmo.
        </p>
        <button
          className="cta-button"
          onClick={handleStart}
          disabled={loading}
        >
          {loading ? 'Carregando...' : 'começar grátis'}
        </button>
      </div>

      <style jsx>{`
        .final-cta {
          background: white;
          padding: 6rem 2rem;
          display: flex;
          justify-content: center;
          align-items: center;
        }

        .final-cta-container {
          max-width: 900px;
          background: linear-gradient(135deg, #7C3AED 0%, #5B21B6 100%);
          border-radius: 24px;
          padding: 4rem 3rem;
          text-align: center;
          color: white;
          position: relative;
          overflow: hidden;
        }

        .final-cta-container::before {
          content: '';
          position: absolute;
          top: -50%;
          right: -50%;
          width: 300px;
          height: 300px;
          background: rgba(255, 255, 255, 0.1);
          border-radius: 50%;
        }

        .final-cta-container::after {
          content: '';
          position: absolute;
          bottom: -30%;
          left: -30%;
          width: 200px;
          height: 200px;
          background: rgba(255, 255, 255, 0.05);
          border-radius: 50%;
        }

        .cta-title {
          font-size: 3rem;
          font-weight: 700;
          margin: 0 0 1rem 0;
          line-height: 1.2;
          position: relative;
          z-index: 1;
          text-transform: lowercase;
        }

        .cta-description {
          font-size: 1.125rem;
          margin: 0 0 2.5rem 0;
          opacity: 0.95;
          line-height: 1.6;
          position: relative;
          z-index: 1;
        }

        .cta-button {
          background: #FF6B35;
          color: white;
          border: none;
          padding: 1.25rem 3rem;
          border-radius: 12px;
          font-size: 1.25rem;
          font-weight: 600;
          cursor: pointer;
          transition: all 0.3s;
          box-shadow: 0 4px 14px rgba(0, 0, 0, 0.2);
          position: relative;
          z-index: 1;
          text-transform: lowercase;
        }

        .cta-button:hover:not(:disabled) {
          background: #FF5722;
          transform: translateY(-2px);
          box-shadow: 0 6px 20px rgba(255, 107, 53, 0.4);
        }

        .cta-button:disabled {
          opacity: 0.7;
          cursor: not-allowed;
        }

        @media (max-width: 768px) {
          .final-cta {
            padding: 4rem 1.5rem;
          }

          .final-cta-container {
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
