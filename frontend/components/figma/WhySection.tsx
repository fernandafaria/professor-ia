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
      title: 'feito pra neurodivergentes',
      description: 'Interface e explicações pensadas para TDAH, dislexia, TEA. Sessões curtas, sem sobrecarga, no seu ritmo.',
    },
    {
      iconColor: '#FF6B35',
      title: 'do professorês pro seu jeito',
      description: 'Matemática com Fortnite, química com K-pop. A IA adapta o conteúdo aos seus interesses.',
    },
    {
      iconColor: '#2563EB',
      title: 'do difícil pro simples',
      description: 'Conceitos da aula viram explicações e exemplos que você entende de verdade.',
    },
    {
      iconColor: '#16A34A',
      title: 'vira um game',
      description: 'XP, níveis, badges e streaks. Progresso visível, sem cobrança de tempo ou formato único.',
    },
  ];

  return (
    <section id="por-que" className="why-section">
      <div className="why-container">
        <h2 className="section-title">
          Por que o mano, traduz?
        </h2>
        <p className="section-subtitle">
          Feito pra quem aprende diferente. Seu ritmo, seu jeito.
        </p>
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
          margin: 0 0 1rem 0;
        }

        .section-subtitle {
          font-size: 1.125rem;
          color: #666;
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
