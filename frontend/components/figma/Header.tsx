/**
 * Header Component - Landing Page mano, traduz!
 * Design: https://www.figma.com/design/kYaKQo5HILal0lD7HEcGcN/Untitled
 */

'use client';

import { useRouter } from 'next/navigation';

export default function Header() {
  const router = useRouter();

  return (
    <header className="header">
      <div className="header-content">
        <div className="logo">
          <div className="logo-icon">
            <span>D</span>
          </div>
          <span className="logo-text">mano, traduz!</span>
        </div>
        
        <nav className="header-nav">
          <a href="#inicio" className="nav-link">início</a>
          <a href="#features" className="nav-link">feature</a>
          <a href="#precos" className="nav-link">preço</a>
          <a href="#como-funciona" className="nav-link">como funciona</a>
          <a href="#faq" className="nav-link">FAQ</a>
          <a href="#contato" className="nav-link">contato</a>
        </nav>

        <div className="header-actions">
          <button 
            className="login-button"
            onClick={() => router.push('/login')}
          >
            entrar
          </button>
          <button 
            className="cta-button"
            onClick={() => router.push('/onboarding')}
          >
            começar grátis
          </button>
        </div>
      </div>

      <style jsx>{`
        .header {
          background: linear-gradient(135deg, #7C3AED 0%, #5B21B6 100%);
          padding: 1.5rem 2rem;
          position: sticky;
          top: 0;
          z-index: 100;
        }

        .header-content {
          max-width: 1200px;
          margin: 0 auto;
          display: flex;
          justify-content: space-between;
          align-items: center;
          gap: 2rem;
        }

        .logo {
          display: flex;
          align-items: center;
          gap: 0.75rem;
        }

        .logo-icon {
          width: 40px;
          height: 40px;
          border-radius: 50%;
          background: white;
          display: flex;
          align-items: center;
          justify-content: center;
          font-size: 1.5rem;
          font-weight: 700;
          color: #7C3AED;
        }

        .logo-text {
          font-size: 1.25rem;
          font-weight: 600;
          color: white;
          text-transform: lowercase;
        }

        .header-nav {
          display: flex;
          gap: 1.5rem;
          align-items: center;
        }

        .nav-link {
          color: white;
          text-decoration: none;
          font-size: 0.875rem;
          font-weight: 500;
          transition: opacity 0.2s;
          text-transform: lowercase;
        }

        .nav-link:hover {
          opacity: 0.8;
        }

        .header-actions {
          display: flex;
          gap: 1rem;
          align-items: center;
        }

        .login-button {
          background: transparent;
          border: none;
          color: white;
          font-size: 1rem;
          font-weight: 600;
          cursor: pointer;
          padding: 0.5rem 1rem;
          border-radius: 6px;
          transition: background-color 0.2s;
          text-transform: lowercase;
        }

        .login-button:hover {
          background-color: rgba(255, 255, 255, 0.1);
        }

        .cta-button {
          background: #FF6B35;
          border: none;
          color: white;
          font-size: 1rem;
          font-weight: 600;
          cursor: pointer;
          padding: 0.5rem 1.5rem;
          border-radius: 6px;
          transition: all 0.2s;
          text-transform: lowercase;
        }

        .cta-button:hover {
          background: #FF5722;
          transform: translateY(-1px);
        }

        @media (max-width: 968px) {
          .header-nav {
            display: none;
          }
        }

        @media (max-width: 768px) {
          .header {
            padding: 1rem 1.5rem;
          }

          .logo-text {
            font-size: 1.125rem;
          }

          .logo-icon {
            width: 32px;
            height: 32px;
            font-size: 1.25rem;
          }

          .header-actions {
            gap: 0.5rem;
          }

          .cta-button {
            padding: 0.5rem 1rem;
            font-size: 0.875rem;
          }
        }
      `}</style>
    </header>
  );
}
