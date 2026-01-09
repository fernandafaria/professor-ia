/**
 * Footer Component - Rodapé mano, traduz!
 * Design: https://www.figma.com/design/kYaKQo5HILal0lD7HEcGcN/Untitled
 */

'use client';

export default function Footer() {
  return (
    <footer className="footer">
      <div className="footer-content">
        <div className="footer-main">
          <div className="footer-brand">
            <div className="logo">
              <svg
                width="24"
                height="24"
                viewBox="0 0 24 24"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <circle cx="12" cy="12" r="10" fill="white"/>
                <text x="12" y="16" fontSize="12" fontWeight="bold" fill="#8B5CF6" textAnchor="middle">D</text>
              </svg>
              <span className="brand-name">mano, traduz!</span>
            </div>
            <p className="brand-description">
              PROJETO QUE ACREDITA em um jeito diferente para mudar o estudo do mundo.
            </p>
          </div>

          <div className="footer-links">
            <div className="links-column">
              <h4 className="links-title">produto</h4>
              <ul className="links-list">
                <li><a href="#recursos">Recursos</a></li>
                <li><a href="#faq">FAQ</a></li>
                <li><a href="#comunidade">Comunidade</a></li>
              </ul>
            </div>

            <div className="links-column">
              <h4 className="suporte">suporte</h4>
              <ul className="links-list">
                <li><a href="#duvidas">Dúvidas frequentes</a></li>
                <li><a href="#contato">Contato</a></li>
                <li><a href="#status">Status</a></li>
              </ul>
            </div>
          </div>

          <div className="newsletter">
            <h4 className="newsletter-title">Newsletter</h4>
            <div className="newsletter-input">
              <input 
                type="email" 
                placeholder="receba dicas de estudo"
                className="newsletter-field"
              />
              <button className="newsletter-button">→</button>
            </div>
          </div>
        </div>

        <div className="footer-bottom">
          <p className="copyright">
            © 2024 mano traduz! Todos os direitos reservados.
          </p>
        </div>
      </div>

      <style jsx>{`
        .footer {
          background: linear-gradient(135deg, #8B5CF6 0%, #7C3AED 100%);
          color: white;
          padding: 4rem 2rem 2rem;
        }

        .footer-content {
          max-width: 1200px;
          margin: 0 auto;
        }

        .footer-main {
          display: grid;
          grid-template-columns: 2fr 1fr 1fr;
          gap: 3rem;
          margin-bottom: 3rem;
        }

        .footer-brand {
          display: flex;
          flex-direction: column;
          gap: 1rem;
        }

        .logo {
          display: flex;
          align-items: center;
          gap: 0.75rem;
          margin-bottom: 0.5rem;
        }

        .brand-name {
          font-size: 1.25rem;
          font-weight: 600;
          color: white;
          font-style: italic;
        }

        .brand-description {
          font-size: 0.875rem;
          color: rgba(255, 255, 255, 0.9);
          line-height: 1.5;
          margin: 0;
        }

        .footer-links {
          display: flex;
          gap: 3rem;
        }

        .links-column {
          display: flex;
          flex-direction: column;
          gap: 1rem;
        }

        .links-title {
          font-size: 0.875rem;
          font-weight: 600;
          text-transform: uppercase;
          margin: 0 0 0.5rem 0;
          color: white;
        }

        .links-list {
          list-style: none;
          padding: 0;
          margin: 0;
          display: flex;
          flex-direction: column;
          gap: 0.5rem;
        }

        .links-list li a {
          color: rgba(255, 255, 255, 0.8);
          text-decoration: none;
          font-size: 0.875rem;
          transition: color 0.2s;
        }

        .links-list li a:hover {
          color: white;
        }

        .newsletter {
          display: flex;
          flex-direction: column;
          gap: 1rem;
        }

        .newsletter-title {
          font-size: 0.875rem;
          font-weight: 600;
          text-transform: uppercase;
          margin: 0;
          color: white;
        }

        .newsletter-input {
          display: flex;
          gap: 0.5rem;
        }

        .newsletter-field {
          flex: 1;
          padding: 0.75rem 1rem;
          border: 1px solid rgba(255, 255, 255, 0.3);
          border-radius: 8px;
          background: rgba(255, 255, 255, 0.1);
          color: white;
          font-size: 0.875rem;
        }

        .newsletter-field::placeholder {
          color: rgba(255, 255, 255, 0.6);
        }

        .newsletter-field:focus {
          outline: none;
          border-color: rgba(255, 255, 255, 0.5);
          background: rgba(255, 255, 255, 0.15);
        }

        .newsletter-button {
          background: white;
          color: #8B5CF6;
          border: none;
          padding: 0.75rem 1.25rem;
          border-radius: 8px;
          font-size: 1.25rem;
          font-weight: 600;
          cursor: pointer;
          transition: all 0.2s;
        }

        .newsletter-button:hover {
          background: rgba(255, 255, 255, 0.9);
          transform: translateX(2px);
        }

        .footer-bottom {
          border-top: 1px solid rgba(255, 255, 255, 0.2);
          padding-top: 2rem;
        }

        .copyright {
          font-size: 0.75rem;
          color: rgba(255, 255, 255, 0.7);
          text-align: center;
          margin: 0;
        }

        @media (max-width: 968px) {
          .footer-main {
            grid-template-columns: 1fr;
            gap: 2.5rem;
          }

          .footer-links {
            gap: 2rem;
          }
        }

        @media (max-width: 768px) {
          .footer {
            padding: 3rem 1.5rem 1.5rem;
          }

          .newsletter-input {
            flex-direction: column;
          }

          .newsletter-button {
            width: 100%;
          }
        }
      `}</style>
    </footer>
  );
}
