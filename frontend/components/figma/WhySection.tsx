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
    <div className="feature-item">
      <div className="feature-icon-box" style={{ backgroundColor: iconColor }}>
        <div className="icon-square"></div>
      </div>
      <div className="feature-content">
        <h3 className="feature-title">{title}</h3>
        <p className="feature-description">{description}</p>
      </div>
    </div>
  );
}

export default function WhySection() {
  const features = [
    {
      iconColor: '#8B5CF6',
      title: 'Personalização total',
      description: 'Matemática com assuntos do dia a dia, física com futebol, química com k-pop. Tu escolhe!'
    },
    {
      iconColor: '#FF7043',
      title: 'Tradução instantânea',
      description: 'Formula complexas viram exemplos simples. Conceitos abstratos viram simples mas...'
    },
    {
      iconColor: '#42A5F5',
      title: 'Vira um game',
      description: 'Ganhe XP, suba de nível, desbloqueie bônus, skins e conteúdo exclusivo.'
    },
    {
      iconColor: '#66BB6A',
      title: 'Feito pra todo mundo',
      description: 'Ensino inclusivo, para todas as deficiências, idades e neurodivergências.'
    }
  ];

  return (
    <section className="why-section">
      <div className="container">
        <h2 className="section-title">
          Por que você vai amar estudar aqui?
        </h2>
        <div className="features-list">
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
          padding: 5rem 2rem;
        }

        .container {
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

        .features-list {
          display: flex;
          flex-direction: column;
          gap: 2.5rem;
        }

        .feature-item {
          display: flex;
          align-items: flex-start;
          gap: 1.5rem;
        }

        .feature-icon-box {
          width: 48px;
          height: 48px;
          border-radius: 8px;
          display: flex;
          align-items: center;
          justify-content: center;
          flex-shrink: 0;
        }

        .icon-square {
          width: 24px;
          height: 24px;
          background: rgba(255, 255, 255, 0.9);
          border-radius: 4px;
        }

        .feature-content {
          flex: 1;
        }

        .feature-title {
          font-size: 1.5rem;
          font-weight: 700;
          color: #1a1a1a;
          margin: 0 0 0.5rem 0;
        }

        .feature-description {
          font-size: 1rem;
          color: #666;
          line-height: 1.6;
          margin: 0;
        }

        @media (max-width: 768px) {
          .why-section {
            padding: 3rem 1.5rem;
          }

          .section-title {
            font-size: 2rem;
            margin-bottom: 3rem;
          }

          .features-list {
            gap: 2rem;
          }

          .feature-item {
            flex-direction: column;
            gap: 1rem;
          }

          .feature-icon-box {
            width: 40px;
            height: 40px;
          }

          .feature-title {
            font-size: 1.25rem;
          }
        }
      `}</style>
    </section>
  );
}
