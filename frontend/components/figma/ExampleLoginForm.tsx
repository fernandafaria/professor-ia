/**
 * Exemplo de Componente do Figma Integrado com Backend
 * 
 * Este é um exemplo que você pode usar como referência ao criar seus próprios
 * componentes a partir do Figma.
 * 
 * Para usar:
 * 1. Substitua o HTML/CSS pelo código gerado do Figma
 * 2. Mantenha a lógica de integração com o backend
 * 3. Ajuste conforme suas necessidades
 */

'use client';

import { useState } from 'react';
import { api } from '@/lib/api';

export default function ExampleLoginForm() {
  // Estados do formulário
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  
  // Estados de UI
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState(false);

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setError('');
    setSuccess(false);
    setLoading(true);

    try {
      // 🔗 Conectar com o backend
      const response = await api.login(email, password);
      
      // Salvar token de autenticação
      if (response.access_token) {
        localStorage.setItem('token', response.access_token);
        setSuccess(true);
        
        // Redirecionar após 1 segundo
        setTimeout(() => {
          window.location.href = '/dashboard';
        }, 1000);
      }
    } catch (err: any) {
      // Tratamento de erro
      setError(
        err.message || 
        'Erro ao fazer login. Verifique suas credenciais.'
      );
      console.error('Login error:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="login-form-container">
      <form onSubmit={handleSubmit} className="login-form">
        <h2>Login</h2>
        
        {/* Campo Email */}
        <div className="form-group">
          <label htmlFor="email">Email</label>
          <input
            id="email"
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="seu@email.com"
            required
            disabled={loading}
          />
        </div>

        {/* Campo Senha */}
        <div className="form-group">
          <label htmlFor="password">Senha</label>
          <input
            id="password"
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="••••••••"
            required
            disabled={loading}
          />
        </div>

        {/* Mensagem de Erro */}
        {error && (
          <div className="error-message" role="alert">
            {error}
          </div>
        )}

        {/* Mensagem de Sucesso */}
        {success && (
          <div className="success-message">
            Login realizado com sucesso! Redirecionando...
          </div>
        )}

        {/* Botão de Submit */}
        <button 
          type="submit" 
          className="submit-button"
          disabled={loading || !email || !password}
        >
          {loading ? 'Entrando...' : 'Entrar'}
        </button>
      </form>

      <style jsx>{`
        .login-form-container {
          max-width: 400px;
          margin: 0 auto;
          padding: 2rem;
        }

        .login-form {
          background: white;
          padding: 2rem;
          border-radius: 8px;
          box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        }

        .login-form h2 {
          margin-top: 0;
          margin-bottom: 1.5rem;
          color: #333;
        }

        .form-group {
          margin-bottom: 1.5rem;
        }

        .form-group label {
          display: block;
          margin-bottom: 0.5rem;
          font-weight: 500;
          color: #555;
        }

        .form-group input {
          width: 100%;
          padding: 0.75rem;
          border: 1px solid #ddd;
          border-radius: 4px;
          font-size: 1rem;
          transition: border-color 0.2s;
        }

        .form-group input:focus {
          outline: none;
          border-color: #0070f3;
        }

        .form-group input:disabled {
          background-color: #f5f5f5;
          cursor: not-allowed;
        }

        .error-message {
          padding: 0.75rem;
          background-color: #fee;
          color: #c33;
          border-radius: 4px;
          margin-bottom: 1rem;
          border: 1px solid #fcc;
        }

        .success-message {
          padding: 0.75rem;
          background-color: #efe;
          color: #3c3;
          border-radius: 4px;
          margin-bottom: 1rem;
          border: 1px solid #cfc;
        }

        .submit-button {
          width: 100%;
          padding: 0.75rem;
          background-color: #0070f3;
          color: white;
          border: none;
          border-radius: 4px;
          font-size: 1rem;
          font-weight: 500;
          cursor: pointer;
          transition: background-color 0.2s;
        }

        .submit-button:hover:not(:disabled) {
          background-color: #0051cc;
        }

        .submit-button:disabled {
          background-color: #ccc;
          cursor: not-allowed;
        }
      `}</style>
    </div>
  );
}
