/**
 * Como Funciona Section - Tradução em 3 passos
 * Design: https://www.figma.com/design/kYaKQo5HILal0lD7HEcGcN/Untitled
 */

'use client';

export default function ComoFuncionaSection() {
  return (
    <section id="como-funciona" className="como-funciona-section">
      <div className="container">
        {/* Header */}
        <div className="section-header">
          <div className="section-label">COMO FUNCIONA</div>
          <h2 className="section-title">Do &quot;não entendi&quot; pro &quot;agora sim&quot; em 3 passos</h2>
          <p className="section-description">
            Manda a pergunta do jeito que você sabe. O mano traduz pra você.
          </p>
        </div>

        {/* Steps */}
        <div className="steps-grid">
          {/* Step 1 */}
          <div className="step-item">
            <div className="step-number">1</div>
            <div className="step-card">
              <div className="step-icon">
                <svg width="32" height="32" viewBox="0 0 24 24" fill="none">
                  <path d="M20 2H4C2.9 2 2 2.9 2 4V22L6 18H20C21.1 18 22 17.1 22 16V4C22 2.9 21.1 2 20 2ZM20 16H6L4 18V4H20V16Z" fill="#7C3AED"/>
                  <path d="M7 9H17V11H7V9ZM7 12H15V14H7V12ZM7 6H17V8H7V6Z" fill="#7C3AED"/>
                </svg>
              </div>
              <h3 className="step-title">Conta sua dúvida</h3>
              <p className="step-description">
                Manda a pergunta do jeito que você sabe: texto, foto ou áudio. Sem formalidade.
              </p>
            </div>
          </div>

          {/* Step 2 */}
          <div className="step-item">
            <div className="step-number">2</div>
            <div className="step-card">
              <div className="step-icon">
                <svg width="32" height="32" viewBox="0 0 24 24" fill="none">
                  <path d="M13 2L3 14H12L11 22L21 10H12L13 2Z" fill="#7C3AED"/>
                </svg>
              </div>
              <h3 className="step-title">mano traduz</h3>
              <p className="step-description">
                A IA pega aquela explicação difícil e transforma em algo que você entende, com exemplos dos seus interesses.
              </p>
            </div>
          </div>

          {/* Step 3 */}
          <div className="step-item">
            <div className="step-number">3</div>
            <div className="step-card">
              <div className="step-icon">
                <svg width="32" height="32" viewBox="0 0 24 24" fill="none">
                  <path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z" fill="#7C3AED"/>
                </svg>
              </div>
              <h3 className="step-title">Você entende e avança</h3>
              <p className="step-description">
                Explicação clara na hora. E você ainda ganha XP pra subir de nível.
              </p>
            </div>
          </div>
        </div>
      </div>

      <style jsx>{`
        .como-funciona-section {
          background: white;
          padding: 6rem 2rem;
        }

        .container {
          max-width: 1200px;
          margin: 0 auto;
        }

        .section-header {
          text-align: center;
          margin-bottom: 4rem;
        }

        .section-label {
          font-size: 0.875rem;
          color: #999;
          text-transform: uppercase;
          letter-spacing: 1px;
          margin-bottom: 0.5rem;
        }

        .section-title {
          font-size: 3rem;
          font-weight: 700;
          color: #1a1a1a;
          margin: 0 0 1rem 0;
          text-transform: lowercase;
        }

        .section-description {
          font-size: 1.125rem;
          color: #666;
          margin: 0;
          max-width: 600px;
          margin: 0 auto;
        }

        .steps-grid {
          display: grid;
          grid-template-columns: repeat(3, 1fr);
          gap: 3rem;
        }

        .step-item {
          display: flex;
          flex-direction: column;
          align-items: flex-start;
          position: relative;
        }

        .step-number {
          width: 48px;
          height: 48px;
          border-radius: 50%;
          background: #FF6B35;
          color: white;
          display: flex;
          align-items: center;
          justify-content: center;
          font-size: 1.5rem;
          font-weight: 700;
          margin-bottom: 1rem;
        }

        .step-card {
          background: white;
          border: 1px solid #e5e5e5;
          border-radius: 16px;
          padding: 2rem;
          flex: 1;
          width: 100%;
          transition: all 0.3s;
        }

        .step-card:hover {
          transform: translateY(-4px);
          box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
        }

        .step-icon {
          margin-bottom: 1rem;
        }

        .step-title {
          font-size: 1.5rem;
          font-weight: 700;
          color: #1a1a1a;
          margin: 0 0 0.75rem 0;
          text-transform: lowercase;
        }

        .step-description {
          font-size: 1rem;
          color: #666;
          line-height: 1.6;
          margin: 0;
        }

        @media (max-width: 968px) {
          .steps-grid {
            grid-template-columns: 1fr;
            gap: 2rem;
          }

          .step-item {
            flex-direction: row;
            gap: 1.5rem;
          }

          .step-number {
            flex-shrink: 0;
          }

          .section-title {
            font-size: 2.5rem;
          }
        }

        @media (max-width: 768px) {
          .como-funciona-section {
            padding: 4rem 1.5rem;
          }

          .section-title {
            font-size: 2rem;
          }

          .step-item {
            flex-direction: column;
          }
        }
      `}</style>
    </section>
  );
}
