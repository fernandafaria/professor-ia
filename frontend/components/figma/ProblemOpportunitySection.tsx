/**
 * Problema + Oportunidade - Landing mano, traduz
 * Comunica o problema e a oportunidade de forma objetiva.
 */

'use client';

export default function ProblemOpportunitySection() {
  return (
    <section className="problem-opportunity" aria-label="Problema e oportunidade">
      <div className="container">
        <div className="block problem">
          <h2 className="label">a dor que a gente resolve</h2>
          <p className="text">
            A escola ensina do mesmo jeito pra todo mundo. Quem aprende diferente trava: a matéria não entra, a lição vira pesadelo, os prazos disparam. Em casa, teus pais querem te ajudar e não sabem como — e a hora do estudo vira briga ou culpa. A gente sabe que não é falta de esforço. É falta de um jeito que funcione pra ti.
          </p>
        </div>
        <div className="block opportunity">
          <h2 className="label">o que a gente faz</h2>
          <p className="text">
            A gente traduz: do &quot;professorês&quot; pro teu jeito. Explicação que entra na cabeça, no teu ritmo. Menos sofrimento pra ti, mais clareza pros teus pais. O mano, traduz existe pra reconectar todo mundo — e fazer o estudo fazer sentido.
          </p>
        </div>
      </div>

      <style jsx>{`
        .problem-opportunity {
          background: #f8f6fc;
          padding: 4rem 2rem;
          border-top: 1px solid rgba(124, 58, 237, 0.1);
        }

        .container {
          max-width: 800px;
          margin: 0 auto;
          display: grid;
          grid-template-columns: 1fr 1fr;
          gap: 3rem;
          align-items: start;
        }

        .block {
          display: flex;
          flex-direction: column;
          gap: 0.75rem;
        }

        .label {
          font-size: 0.875rem;
          font-weight: 600;
          color: #7C3AED;
          text-transform: lowercase;
          margin: 0;
          letter-spacing: 0.02em;
        }

        .text {
          font-size: 1rem;
          color: #333;
          line-height: 1.6;
          margin: 0;
        }

        @media (max-width: 768px) {
          .problem-opportunity {
            padding: 3rem 1.5rem;
          }

          .container {
            grid-template-columns: 1fr;
            gap: 2.5rem;
          }

          .text {
            font-size: 0.9375rem;
          }
        }
      `}</style>
    </section>
  );
}
