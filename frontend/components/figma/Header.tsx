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
        <button 
          className="login-button"
          onClick={() => router.push('/login')}
        >
          Entrar
        </button>
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
        }

        .login-button:hover {
          background-color: rgba(255, 255, 255, 0.1);
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
        }
      `}</style>
    </header>
  );
}
