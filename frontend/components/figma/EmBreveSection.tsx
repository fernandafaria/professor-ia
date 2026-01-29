/**
 * Em breve - Kit e Planejador
 * Comunica que Kit de Ferramentas e Planejador estão vindo e permite captar interesse.
 */

'use client';

function scrollToNewsletter() {
  const el = document.getElementById('newsletter');
  if (el) el.scrollIntoView({ behavior: 'smooth' });
}

export default function EmBreveSection() {
  return (
    <section className="em-breve" id="em-breve" aria-label="Em breve">
      <div className="container">
        <h2 className="section-title">em breve na tua mão</h2>
        <p className="section-subtitle">
          A gente tá preparando mais coisa pra te ajudar. Quer que a gente te avise quando sair?
        </p>
        <div className="cards">
          <div className="card">
            <span className="card-badge">em breve</span>
            <h3 className="card-title">kit de ferramentas</h3>
            <p className="card-desc">
              Leitura em voz alta, ditado, máscara pra focar, bloco de notas pra matemática. Tudo num lugar.
            </p>
          </div>
          <div className="card">
            <span className="card-badge">em breve</span>
            <h3 className="card-title">planejador visual</h3>
            <p className="card-desc">
              Tarefas, calendário e rotina. O que tu for estudar vira tarefa sozinho — e tu ganha hábito no jogo.
            </p>
          </div>
        </div>
        <button type="button" className="cta-avise" onClick={scrollToNewsletter}>
          me avisa quando tiver
        </button>
      </div>

      <style jsx>{`
        .em-breve {
          background: white;
          padding: 5rem 2rem;
          border-top: 1px solid #eee;
        }

        .container {
          max-width: 900px;
          margin: 0 auto;
          text-align: center;
        }

        .section-title {
          font-size: 2rem;
          font-weight: 700;
          color: #1a1a1a;
          margin: 0 0 0.5rem 0;
          text-transform: lowercase;
        }

        .section-subtitle {
          font-size: 1.125rem;
          color: #666;
          margin: 0 0 2.5rem 0;
          line-height: 1.5;
        }

        .cards {
          display: grid;
          grid-template-columns: 1fr 1fr;
          gap: 1.5rem;
          margin-bottom: 2.5rem;
          text-align: left;
        }

        .card {
          background: #f8f6fc;
          border: 1px solid rgba(124, 58, 237, 0.15);
          border-radius: 16px;
          padding: 1.5rem;
          position: relative;
        }

        .card-badge {
          position: absolute;
          top: 1rem;
          right: 1rem;
          font-size: 0.75rem;
          font-weight: 600;
          color: #7C3AED;
          text-transform: lowercase;
        }

        .card-title {
          font-size: 1.125rem;
          font-weight: 700;
          color: #1a1a1a;
          margin: 0 0 0.5rem 0;
          padding-right: 4rem;
          text-transform: lowercase;
        }

        .card-desc {
          font-size: 0.9375rem;
          color: #666;
          line-height: 1.5;
          margin: 0;
        }

        .cta-avise {
          background: transparent;
          color: #7C3AED;
          border: 2px solid #7C3AED;
          padding: 0.75rem 1.5rem;
          border-radius: 12px;
          font-size: 1rem;
          font-weight: 600;
          cursor: pointer;
          transition: all 0.2s;
          text-transform: lowercase;
        }

        .cta-avise:hover {
          background: #7C3AED;
          color: white;
        }

        @media (max-width: 768px) {
          .em-breve {
            padding: 4rem 1.5rem;
          }

          .section-title {
            font-size: 1.75rem;
          }

          .cards {
            grid-template-columns: 1fr;
            gap: 1rem;
            margin-bottom: 2rem;
          }

          .card-title {
            padding-right: 0;
          }
        }
      `}</style>
    </section>
  );
}
