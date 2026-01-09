/**
 * Login Page - Página de Login
 * Design do Figma será extraído e aplicado aqui
 */

'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';
import { api } from '@/lib/api';

export default function LoginPage() {
  const router = useRouter();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    try {
      const response = await api.login(email, password);
      localStorage.setItem('token', response.access_token);
      router.push('/dashboard');
    } catch (err: any) {
      setError(err.message || 'Erro ao fazer login. Verifique suas credenciais.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="login-container">
      <div className="login-card">
        <div className="logo-section">
          <div className="logo-icon">
            <span>D</span>
          </div>
          <h1 className="logo-text">mano, traduz!</h1>
        </div>

        <h2 className="login-title">Entrar</h2>
        <p className="login-subtitle">Bem-vindo de volta!</p>

        {error && <div className="error-message">{error}</div>}

        <form onSubmit={handleSubmit} className="login-form">
          <div className="form-group">
            <label htmlFor="email">Email</label>
            <input
              id="email"
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder="seu@email.com"
              required
            />
          </div>

          <div className="form-group">
            <label htmlFor="password">Senha</label>
            <input
              id="password"
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="Sua senha"
              required
            />
          </div>

          <button type="submit" className="btn-primary" disabled={loading}>
            {loading ? 'Entrando...' : 'Entrar'}
          </button>
        </form>

        <div className="login-footer">
          <p>
            Não tem conta?{' '}
            <a href="/onboarding" className="link">
              Criar conta grátis
            </a>
          </p>
        </div>
      </div>

      <style jsx>{`
        .login-container {
          min-height: 100vh;
          display: flex;
          align-items: center;
          justify-content: center;
          padding: 2rem;
          background: linear-gradient(135deg, #7C3AED 0%, #5B21B6 100%);
        }

        .login-card {
          background: white;
          border-radius: 16px;
          padding: 3rem;
          max-width: 450px;
          width: 100%;
          box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
        }

        .logo-section {
          text-align: center;
          margin-bottom: 2rem;
        }

        .logo-icon {
          width: 60px;
          height: 60px;
          border-radius: 50%;
          background: linear-gradient(135deg, #7C3AED 0%, #5B21B6 100%);
          display: inline-flex;
          align-items: center;
          justify-content: center;
          font-size: 2rem;
          font-weight: 700;
          color: white;
          margin-bottom: 1rem;
        }

        .logo-text {
          font-size: 1.5rem;
          font-weight: 600;
          color: #7C3AED;
          margin: 0;
          text-transform: lowercase;
        }

        .login-title {
          font-size: 2rem;
          font-weight: 700;
          color: #1a1a1a;
          margin: 0 0 0.5rem 0;
          text-align: center;
        }

        .login-subtitle {
          font-size: 1rem;
          color: #666;
          margin: 0 0 2rem 0;
          text-align: center;
        }

        .login-form {
          display: flex;
          flex-direction: column;
          gap: 1.5rem;
        }

        .form-group {
          display: flex;
          flex-direction: column;
          gap: 0.5rem;
        }

        .form-group label {
          font-weight: 500;
          color: #555;
          font-size: 0.875rem;
        }

        .form-group input {
          padding: 0.875rem;
          border: 1px solid #ddd;
          border-radius: 8px;
          font-size: 1rem;
          transition: border-color 0.2s;
        }

        .form-group input:focus {
          outline: none;
          border-color: #7C3AED;
        }

        .btn-primary {
          background: linear-gradient(135deg, #FF6B35 0%, #FF5722 100%);
          color: white;
          border: none;
          padding: 1rem;
          border-radius: 8px;
          font-size: 1.125rem;
          font-weight: 600;
          cursor: pointer;
          transition: all 0.2s;
          margin-top: 0.5rem;
        }

        .btn-primary:hover:not(:disabled) {
          transform: translateY(-2px);
          box-shadow: 0 4px 12px rgba(255, 107, 53, 0.4);
        }

        .btn-primary:disabled {
          opacity: 0.7;
          cursor: not-allowed;
        }

        .error-message {
          padding: 0.875rem;
          background-color: #fee;
          color: #c33;
          border-radius: 8px;
          border: 1px solid #fcc;
          margin-bottom: 1rem;
          text-align: center;
          font-size: 0.875rem;
        }

        .login-footer {
          text-align: center;
          margin-top: 2rem;
          padding-top: 2rem;
          border-top: 1px solid #e5e5e5;
        }

        .login-footer p {
          margin: 0;
          color: #666;
          font-size: 0.875rem;
        }

        .link {
          color: #7C3AED;
          font-weight: 600;
          text-decoration: none;
        }

        .link:hover {
          text-decoration: underline;
        }

        @media (max-width: 768px) {
          .login-container {
            padding: 1rem;
          }

          .login-card {
            padding: 2rem 1.5rem;
          }

          .login-title {
            font-size: 1.75rem;
          }
        }
      `}</style>
    </div>
  );
}
