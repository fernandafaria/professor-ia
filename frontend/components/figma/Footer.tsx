/**
 * Footer Component - Rodapé mano, traduz!
 * Design: https://www.figma.com/design/kYaKQo5HILal0lD7HEcGcN/Untitled
 */

'use client';

import { useState } from 'react';

export default function Footer() {
  const [email, setEmail] = useState('');

  const handleNewsletterSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    // TODO: Implementar newsletter
    console.log('Newsletter:', email);
    setEmail('');
  };

  return (
    <footer className="footer">
      <div className="footer-content">
        {/* Brand */}
        <div className="footer-brand">
          <div className="logo-icon">
            <span>D</span>
          </div>
          <div className="brand-info">
            <span className="brand-name">mano, traduz!</span>
            <p className="brand-tagline">
              PROJETO QUE ACOMPANHA EM UM JEITO DIFERENTE PARA AJUDAR VOCÊ A APRENDER!
            </p>
          </div>
        </div>

        {/* Links */}
        <div className="footer-links">
          <div className="links-column">
            <h3 className="links-title">produto</h3>
            <ul className="links-list">
              <li><a href="#features">features</a></li>
              <li><a href="#faq">FAQ</a></li>
              <li><a href="#comunidade">comunidade</a></li>
            </ul>
          </div>
          <div className="links-column">
            <h3 className="links-title">suporte</h3>
            <ul className="links-list">
              <li><a href="#faq">perguntas frequentes</a></li>
              <li><a href="#contato">contato</a></li>
              <li><a href="#ajuda">ajuda</a></li>
            </ul>
          </div>
        </div>

        {/* Newsletter */}
        <div className="footer-newsletter">
          <h3 className="newsletter-title">newsletter</h3>
          <p className="newsletter-subtitle">receba dicas de estudo</p>
          <form onSubmit={handleNewsletterSubmit} className="newsletter-form">
            <input
              type="email"
              placeholder="Seu e-mail"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="newsletter-input"
              required
            />
            <button type="submit" className="newsletter-button">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
                <path d="M2.01 21L23 12L2.01 3L2 10L17 12L2 14L2.01 21Z" fill="white"/>
              </svg>
            </button>
          </form>
        </div>
      </div>

      {/* Copyright */}
      <div className="footer-copyright">
        <p>© 2024 mano traduz! Todos os direitos reservados.</p>
      </div>

      <style jsx>{`
        .footer {
          background: linear-gradient(135deg, #5B21B6 0%, #4C1D95 100%);
          color: white;
          padding: 4rem 2rem 2rem;
        }

        .footer-content {
          max-width: 1200px;
          margin: 0 auto;
          display: grid;
          grid-template-columns: 1.5fr 1fr 1fr;
          gap: 4rem;
          margin-bottom: 3rem;
        }

        .footer-brand {
          display: flex;
          flex-direction: column;
          gap: 1rem;
        }

        .logo-icon {
          width: 48px;
          height: 48px;
          border-radius: 50%;
          background: white;
          display: flex;
          align-items: center;
          justify-content: center;
          font-size: 1.5rem;
          font-weight: 700;
          color: #7C3AED;
          margin-bottom: 0.5rem;
        }

        .brand-name {
          font-size: 1.5rem;
          font-weight: 600;
          display: block;
          margin-bottom: 0.5rem;
          text-transform: lowercase;
        }

        .brand-tagline {
          font-size: 0.875rem;
          color: rgba(255, 255, 255, 0.9);
          line-height: 1.5;
          margin: 0;
        }

        .footer-links {
          display: grid;
          grid-template-columns: 1fr 1fr;
          gap: 2rem;
        }

        .links-column {
          display: flex;
          flex-direction: column;
          gap: 1rem;
        }

        .links-title {
          font-size: 1rem;
          font-weight: 600;
          margin: 0;
          text-transform: lowercase;
        }

        .links-list {
          list-style: none;
          padding: 0;
          margin: 0;
          display: flex;
          flex-direction: column;
          gap: 0.75rem;
        }

        .links-list a {
          color: rgba(255, 255, 255, 0.8);
          text-decoration: none;
          font-size: 0.875rem;
          transition: color 0.2s;
          text-transform: lowercase;
        }

        .links-list a:hover {
          color: white;
        }

        .footer-newsletter {
          display: flex;
          flex-direction: column;
          gap: 0.75rem;
        }

        .newsletter-title {
          font-size: 1rem;
          font-weight: 600;
          margin: 0;
          text-transform: lowercase;
        }

        .newsletter-subtitle {
          font-size: 0.875rem;
          color: rgba(255, 255, 255, 0.8);
          margin: 0;
          text-transform: lowercase;
        }

        .newsletter-form {
          display: flex;
          gap: 0.5rem;
          margin-top: 0.5rem;
        }

        .newsletter-input {
          flex: 1;
          padding: 0.75rem 1rem;
          border: 1px solid rgba(255, 255, 255, 0.3);
          border-radius: 8px;
          background: rgba(255, 255, 255, 0.1);
          color: white;
          font-size: 0.875rem;
        }

        .newsletter-input::placeholder {
          color: rgba(255, 255, 255, 0.6);
        }

        .newsletter-input:focus {
          outline: none;
          border-color: white;
          background: rgba(255, 255, 255, 0.15);
        }

        .newsletter-button {
          background: #7C3AED;
          border: none;
          padding: 0.75rem 1rem;
          border-radius: 8px;
          cursor: pointer;
          display: flex;
          align-items: center;
          justify-content: center;
          transition: background 0.2s;
        }

        .newsletter-button:hover {
          background: #8B5CF6;
        }

        .footer-copyright {
          max-width: 1200px;
          margin: 0 auto;
          padding-top: 2rem;
          border-top: 1px solid rgba(255, 255, 255, 0.2);
          text-align: center;
        }

        .footer-copyright p {
          font-size: 0.875rem;
          color: rgba(255, 255, 255, 0.7);
          margin: 0;
        }

        @media (max-width: 968px) {
          .footer-content {
            grid-template-columns: 1fr;
            gap: 3rem;
          }

          .footer-links {
            grid-template-columns: 1fr 1fr;
          }
        }

        @media (max-width: 768px) {
          .footer {
            padding: 3rem 1.5rem 2rem;
          }

          .footer-links {
            grid-template-columns: 1fr;
            gap: 2rem;
          }

          .newsletter-form {
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
