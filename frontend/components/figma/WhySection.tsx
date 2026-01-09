/**
 * Why Section - Por que você vai amar estudar aqui?
 * 4 features em grid 2x2
 */

'use client';

interface FeatureProps {
  icon: React.ReactNode;
  title: string;
  description: string;
  iconColor: string;
}

function Feature({ icon, title, description, iconColor }: FeatureProps) {
  return (
    <div className="feature-card">
      <div className="feature-icon" style={{ color: iconColor }}>
        {icon}
      </div>
      <h3 className="feature-title">{title}</h3>
      <p className="feature-description">{description}</p>
    </div>
  );
}

export default function WhySection() {
  const features = [
    {
      icon: (
        <svg width="32" height="32" viewBox="0 0 24 24" fill="none">
          <path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z" fill="currentColor"/>
        </svg>
      ),
      title: 'Seu Professor, Seu Estilo ✨',
      description: 'Crie um professor com a personalidade que combina com você: motivador, paciente, desafiador ou amigável',
      iconColor: '#ea580c',
    },
    {
      icon: (
        <svg width="32" height="32" viewBox="0 0 24 24" fill="none">
          <path d="M13 2L3 14H12L11 22L21 10H12L13 2Z" fill="currentColor"/>
        </svg>
      ),
      title: 'Aprende Rapidão ⚡',
      description: 'Sessões de 8-15 minutos. Perfeito pra encaixar entre uma aula e outra ou antes de dormir',
      iconColor: '#8B5CF6',
    },
    {
      icon: (
        <svg width="32" height="32" viewBox="0 0 24 24" fill="none">
          <circle cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="2" fill="none"/>
          <circle cx="12" cy="12" r="3" fill="currentColor"/>
        </svg>
      ),
      title: 'Vira um Game 🎮',
      description: 'Ganhe XP, suba de nível, desbloqueie badges épicos e monte suas streaks. Estudar nunca foi tão viciante!',
      iconColor: '#2563eb',
    },
    {
      icon: (
        <svg width="32" height="32" viewBox="0 0 24 24" fill="none">
          <path d="M12 2C6.48 2 2 6.48 2 12C2 17.52 6.48 22 12 22C17.52 22 22 17.52 22 12C22 6.48 17.52 2 12 2ZM12 20C7.59 20 4 16.41 4 12C4 7.59 7.59 4 12 4C16.41 4 20 7.59 20 12C20 16.41 16.41 20 12 20Z" fill="currentColor"/>
          <circle cx="8" cy="10" r="1.5" fill="currentColor"/>
          <circle cx="16" cy="10" r="1.5" fill="currentColor"/>
          <path d="M12 15C10.34 15 8.94 14.11 8 12.83L8.5 12.5C9.28 13.5 10.55 14.17 12 14.17C13.45 14.17 14.72 13.5 15.5 12.5L16 12.83C15.06 14.11 13.66 15 12 15Z" fill="currentColor"/>
        </svg>
      ),
      title: 'Ele Te Entende 🧠',
      description: 'A IA aprende com você! Fala de esportes, games, música... do que você curte de verdade',
      iconColor: '#16a34a',
    },
  ];

  return (
    <section className="why-section" id="como-funciona">
      <div className="why-container">
        <h2 className="section-title">
          Por que você vai amar estudar aqui? 💜
        </h2>
        <p className="section-subtitle">
          Seu professor, suas regras. Aprenda do jeito que funciona pra você!
        </p>
        <div className="features-grid">
          {features.map((feature, index) => (
            <Feature
              key={index}
              icon={feature.icon}
              title={feature.title}
              description={feature.description}
              iconColor={feature.iconColor}
            />
          ))}
        </div>
      </div>

      <style jsx>{`
        .why-section {
          background: #fafafa;
          padding: 5rem 2rem;
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
          margin: 0 0 3rem 0;
        }

        .features-grid {
          display: grid;
          grid-template-columns: repeat(2, 1fr);
          gap: 2rem;
        }

        .feature-card {
          background: white;
          padding: 2rem;
          border-radius: 16px;
          box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
          transition: transform 0.2s, box-shadow 0.2s;
        }

        .feature-card:hover {
          transform: translateY(-4px);
          box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
        }

        .feature-icon {
          margin-bottom: 1rem;
        }

        .feature-title {
          font-size: 1.25rem;
          font-weight: 600;
          color: #1a1a1a;
          margin: 0 0 0.75rem 0;
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
          }

          .features-grid {
            grid-template-columns: 1fr;
            gap: 1.5rem;
          }

          .feature-card {
            padding: 1.5rem;
          }
        }
      `}</style>
    </section>
  );
}
