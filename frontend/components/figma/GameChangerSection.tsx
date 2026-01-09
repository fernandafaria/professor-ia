/**
 * Game Changer Section - Isso aqui vai mudar seu jogo
 * 3 features em linha
 */

'use client';

interface GameFeatureProps {
  icon: React.ReactNode;
  title: string;
  description: string;
  iconColor: string;
}

function GameFeature({ icon, title, description, iconColor }: GameFeatureProps) {
  return (
    <div className="game-feature">
      <div className="game-icon" style={{ color: iconColor }}>
        {icon}
      </div>
      <h3 className="game-title">{title}</h3>
      <p className="game-description">{description}</p>
    </div>
  );
}

export default function GameChangerSection() {
  const features = [
    {
      icon: (
        <svg width="40" height="40" viewBox="0 0 24 24" fill="none">
          <path d="M19 3H5C3.9 3 3 3.9 3 5V19C3 20.1 3.9 21 5 21H19C20.1 21 21 20.1 21 19V5C21 3.9 20.1 3 19 3ZM19 19H5V5H19V19ZM17 12H15V15H13V12H11V10H13V7H15V10H17V12Z" fill="currentColor"/>
        </svg>
      ),
      title: 'Todas as Matérias 📚',
      description: 'Matemática, Física, Química, Biologia, Português, História, Geografia... Tudo o que você precisa!',
      iconColor: '#8B5CF6',
    },
    {
      icon: (
        <svg width="40" height="40" viewBox="0 0 24 24" fill="none">
          <path d="M19 5H5V19H19V5ZM5 3C3.9 3 3 3.9 3 5V19C3 20.1 3.9 21 5 21H19C20.1 21 21 20.1 21 19V5C21 3.9 20.1 3 19 3H5ZM12 7L14 10L17 6L19 9L12 17L7 11L9 8L12 11Z" fill="currentColor"/>
        </svg>
      ),
      title: 'Level Up na Vida Real 🏆',
      description: 'Ganhe XP, suba de nível, conquiste badges épicos. É tipo RPG, mas você evolui de verdade!',
      iconColor: '#ea580c',
    },
    {
      icon: (
        <svg width="40" height="40" viewBox="0 0 24 24" fill="none">
          <path d="M12 2C6.48 2 2 6.48 2 12C2 17.52 6.48 22 12 22C17.52 22 22 17.52 22 12C22 6.48 17.52 2 12 2ZM13 17H11V15H13V17ZM13 13H11V7H13V13Z" fill="currentColor"/>
        </svg>
      ),
      title: 'Streak de Campeão 🔥',
      description: 'Estude todo dia, construa sua streak e vire um monstro nos estudos. Sem desculpas!',
      iconColor: '#dc2626',
    },
  ];

  return (
    <section className="game-changer-section">
      <div className="game-changer-container">
        <h2 className="section-title">
          Isso aqui vai mudar seu jogo 🔥
        </h2>
        <p className="section-subtitle">
          Aprenda de um jeito que realmente funciona pra você
        </p>
        <div className="game-features">
          {features.map((feature, index) => (
            <GameFeature
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
        .game-changer-section {
          background: white;
          padding: 5rem 2rem;
        }

        .game-changer-container {
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

        .game-features {
          display: grid;
          grid-template-columns: repeat(3, 1fr);
          gap: 2rem;
        }

        .game-feature {
          text-align: center;
          padding: 2rem;
        }

        .game-icon {
          margin-bottom: 1.5rem;
          display: flex;
          justify-content: center;
        }

        .game-title {
          font-size: 1.5rem;
          font-weight: 600;
          color: #1a1a1a;
          margin: 0 0 1rem 0;
        }

        .game-description {
          font-size: 1rem;
          color: #666;
          line-height: 1.6;
          margin: 0;
        }

        @media (max-width: 968px) {
          .game-features {
            grid-template-columns: 1fr;
            gap: 2rem;
          }
        }

        @media (max-width: 768px) {
          .game-changer-section {
            padding: 3rem 1.5rem;
          }

          .section-title {
            font-size: 2rem;
          }

          .game-feature {
            padding: 1.5rem;
          }
        }
      `}</style>
    </section>
  );
}
