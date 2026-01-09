/**
 * Why Section - Por que você vai amar estudar aqui?
 * Design: https://www.figma.com/design/kYaKQo5HILal0lD7HEcGcN/Untitled
 */

'use client';

interface FeatureProps {
  iconColor: string;
  title: string;
  description: string;
}

function Feature({ iconColor, title, description }: FeatureProps) {
  return (
    <div className="feature-card">
      <div className="feature-icon" style={{ backgroundColor: iconColor }}>
        <div className="icon-square"></div>
      </div>
      <h3 className="feature-title">{title}</h3>
      <p className="feature-description">{description}</p>
    </div>
  );
}

export default function WhySection() {
  const features = [
    {
      iconColor: '#7C3AED',
      title: 'Personalização total',
      description: 'Matemática com assuntos do dia a dia, física com futebol, química com K-pop. Tu escolhe!',
    },
    {
      iconColor: '#FF6B35',
      title: 'Tradução instantânea',
      description: 'Fórmulas complexas viram exemplos simples. Conceitos abstratos viram exemplos reais.',
    },
    {
      iconColor: '#2563EB',
      title: 'Vira um game',
      description: 'Ganhe XP, suba de nível, desbloqueie bônus diários e crie seu mundo virtual.',
    },
    {
      iconColor: '#16A34A',
      title: 'Feito pra todo mundo',
      description: 'Inclusivo: acessível, disponível em desktop/mobile, rápido, fácil, intuitivo.',
    },
  ];

  return (
    <section className="why-section">
      <div className="why-container">
        <h2 className="section-title">
          Por que você vai amar estudar aqui?
        </h2>
        <div className="features-grid">
          {features.map((feature, index) => (
            <Feature
              key={index}
              iconColor={feature.iconColor}
              title={feature.title}
              description={feature.description}
            />
          ))}
        </div>
      </div>

      <style jsx>{`
        .why-section {
          background: white;
          padding: 6rem 2rem;
        }

        .why-container {
          max-width: 1200px;
          margin: 0 auto;
        }

        .section-title {
          font-size: 2.5rem;
          font-weight: 700;
          color: #1a1a1a;
          text-align: center;
          margin: 0 0 4rem 0;
        }

        .features-grid {
          display: grid;
          grid-template-columns: repeat(2, 1fr);
          gap: 2rem;
        }

        .feature-card {
          display: flex;
          flex-direction: column;
          gap: 1rem;
        }

        .feature-icon {
          width: 48px;
          height: 48px;
          border-radius: 8px;
          display: flex;
          align-items: center;
          justify-content: center;
        }

        .icon-square {
          width: 24px;
          height: 24px;
          background: white;
          border-radius: 4px;
        }

        .feature-title {
          font-size: 1.5rem;
          font-weight: 700;
          color: #1a1a1a;
          margin: 0;
          text-transform: lowercase;
        }

        .feature-description {
          font-size: 1rem;
          color: #666;
          line-height: 1.6;
          margin: 0;
        }

        @media (max-width: 768px) {
          .why-section {
            padding: 4rem 1.5rem;
          }

          .section-title {
            font-size: 2rem;
          }

          .features-grid {
            grid-template-columns: 1fr;
            gap: 2rem;
          }
        }
      `}</style>
    </section>
  );
}
