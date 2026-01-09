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
          <svg
            width="24"
            height="24"
            viewBox="0 0 24 24"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <circle cx="12" cy="12" r="10" fill="#8B5CF6"/>
            <text x="12" y="16" fontSize="12" fontWeight="bold" fill="white" textAnchor="middle">D</text>
          </svg>
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
          background: linear-gradient(135deg, #8B5CF6 0%, #7C3AED 100%);
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

        .logo svg {
          flex-shrink: 0;
        }

        .logo-text {
          font-size: 1.25rem;
          font-weight: 600;
          color: white;
          font-style: italic;
        }

        .login-button {
          background: transparent;
          border: none;
          color: white;
          font-size: 1rem;
          font-weight: 500;
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
        }
      `}</style>
    </header>
  );
}
