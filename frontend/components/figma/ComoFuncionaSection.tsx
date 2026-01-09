/**
 * Como Funciona Section - Tradução em 3 passos
 * Design: https://www.figma.com/design/kYaKQo5HILal0lD7HEcGcN/Untitled
 */

'use client';

export default function ComoFuncionaSection() {
  const steps = [
    {
      number: 1,
      icon: '💬',
      title: 'Conta tua dúvida',
      description: 'Manda a pergunta ou o problema que tu não sabe. Pode ser foto, audio, texto... como quiser!'
    },
    {
      number: 2,
      icon: '⚡',
      title: 'mano traduz',
      description: 'A IA gera exato a explicação clara e bondosa em algo que tu entende de verdade.'
    },
    {
      number: 3,
      icon: '🏆',
      title: 'Tu entende',
      description: 'Pronto! Agora faz sentido e tu ainda ganha XP e sobe de nível!'
    }
  ];

  return (
    <section id="como-funciona" className="como-funciona-section">
      <div className="container">
        <div className="section-header">
          <p className="section-label">COMO FUNCIONA</p>
          <h2 className="section-title">Tradução em 3 passos</h2>
        </div>

        <div className="steps-grid">
          {steps.map((step) => (
            <div key={step.number} className="step-card">
              <div className="step-number">{step.number}</div>
              <div className="step-content">
                <div className="step-icon">{step.icon}</div>
                <h3 className="step-title">{step.title}</h3>
                <p className="step-description">{step.description}</p>
              </div>
            </div>
          ))}
        </div>
      </div>

      <style jsx>{`
        .como-funciona-section {
          background: white;
          padding: 5rem 2rem;
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
          font-weight: 600;
          color: #666;
          text-transform: uppercase;
          letter-spacing: 0.05em;
          margin: 0 0 0.5rem 0;
        }

        .section-title {
          font-size: 2.5rem;
          font-weight: 700;
          color: #1a1a1a;
          margin: 0;
        }

        .steps-grid {
          display: grid;
          grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
          gap: 2rem;
        }

        .step-card {
          position: relative;
          background: white;
          border-radius: 16px;
          padding: 2rem;
          box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
          display: flex;
          gap: 1.5rem;
        }

        .step-number {
          position: absolute;
          left: -20px;
          top: 2rem;
          width: 40px;
          height: 40px;
          background: #FF7043;
          color: white;
          border-radius: 50%;
          display: flex;
          align-items: center;
          justify-content: center;
          font-size: 1.25rem;
          font-weight: 700;
          flex-shrink: 0;
        }

        .step-content {
          flex: 1;
          margin-left: 1rem;
        }

        .step-icon {
          font-size: 2rem;
          margin-bottom: 1rem;
        }

        .step-title {
          font-size: 1.5rem;
          font-weight: 700;
          color: #1a1a1a;
          margin: 0 0 0.75rem 0;
        }

        .step-description {
          font-size: 1rem;
          color: #666;
          line-height: 1.6;
          margin: 0;
        }

        @media (max-width: 768px) {
          .como-funciona-section {
            padding: 3rem 1.5rem;
          }

          .section-title {
            font-size: 2rem;
          }

          .steps-grid {
            grid-template-columns: 1fr;
            gap: 2.5rem;
          }

          .step-number {
            left: -15px;
            width: 35px;
            height: 35px;
            font-size: 1.125rem;
          }
        }
      `}</style>
    </section>
  );
}
