/**
 * Footer Component - Rodapé da landing page
 * Design completo do Figma
 */

'use client';

export default function Footer() {
  return (
    <footer className="footer">
      <div className="footer-content">
        <div className="footer-brand">
          <svg
            width="20"
            height="20"
            viewBox="0 0 24 24"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z"
              fill="#8B5CF6"
            />
          </svg>
          <span className="brand-name">Professor IA</span>
        </div>
        <div className="footer-copyright">
          © 2026 Professor Particular IA. Todos os direitos reservados.
        </div>
      </div>

      <style jsx>{`
        .footer {
          background-color: #1a1a1a;
          color: white;
          padding: 2.5rem 2rem;
        }

        .footer-content {
          max-width: 1200px;
          margin: 0 auto;
          display: flex;
          justify-content: space-between;
          align-items: center;
        }

        .footer-brand {
          display: flex;
          align-items: center;
          gap: 0.5rem;
        }

        .brand-name {
          font-size: 1.25rem;
          font-weight: 600;
          color: white;
        }

        .footer-copyright {
          font-size: 0.875rem;
          color: #999;
        }

        @media (max-width: 768px) {
          .footer {
            padding: 2rem 1.5rem;
          }

          .footer-content {
            flex-direction: column;
            gap: 1rem;
            text-align: center;
          }

          .brand-name {
            font-size: 1.125rem;
          }

          .footer-copyright {
            font-size: 0.75rem;
          }
        }
      `}</style>
    </footer>
  );
}
