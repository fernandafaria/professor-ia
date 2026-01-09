/**
 * Header Component - Landing Page Professor IA
 * Design completo do Figma: https://www.figma.com/design/masYeVMxkPMQ0zDMDrvZCx/Untitled
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
          <span className="logo-text">Professor IA</span>
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
          background-color: white;
          padding: 1.5rem 2rem;
          border-bottom: 1px solid #f0f0f0;
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
          gap: 0.5rem;
        }

        .logo svg {
          flex-shrink: 0;
        }

        .logo-text {
          font-size: 1.25rem;
          font-weight: 600;
          color: #333;
        }

        .login-button {
          background: transparent;
          border: none;
          color: #8B5CF6;
          font-size: 1rem;
          font-weight: 600;
          cursor: pointer;
          padding: 0.5rem 1rem;
          border-radius: 6px;
          transition: background-color 0.2s;
        }

        .login-button:hover {
          background-color: #f5f0ff;
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
