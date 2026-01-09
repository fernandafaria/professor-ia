/**
 * Página de Onboarding - Criar Professor IA
 * Página para onde o usuário é redirecionado ao clicar em "Criar Meu Professor Agora"
 */

'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';
import { api } from '@/lib/api';

export default function OnboardingPage() {
  const router = useRouter();
  const [step, setStep] = useState(1);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  // Dados do formulário
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    password: '',
    subject: '',
    grade: '',
  });

  const handleInputChange = (field: string, value: string) => {
    setFormData((prev) => ({ ...prev, [field]: value }));
    setError('');
  };

  const handleNext = () => {
    if (step === 1) {
      if (!formData.name || !formData.email || !formData.password) {
        setError('Por favor, preencha todos os campos');
        return;
      }
      setStep(2);
    }
  };

  const handleBack = () => {
    if (step > 1) {
      setStep(step - 1);
    } else {
      router.push('/');
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    try {
      // 1. Criar conta
      await api.register(formData.email, formData.password, formData.name);

      // 2. Login automático
      const loginResponse = await api.login(formData.email, formData.password);
      localStorage.setItem('token', loginResponse.access_token);

      // 3. Criar perfil do professor
      await api.createProfile({
        name: formData.name,
        subject: formData.subject,
        grade: formData.grade,
      });

      // 4. Redirecionar para dashboard
      router.push('/dashboard');
    } catch (err: any) {
      setError(err.message || 'Erro ao criar professor. Tente novamente.');
      console.error('Onboarding error:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="onboarding-container">
      <div className="onboarding-card">
        <div className="progress-bar">
          <div
            className="progress-fill"
            style={{ width: `${(step / 2) * 100}%` }}
          />
        </div>

        <h1 className="onboarding-title">
          {step === 1 ? 'Crie sua conta' : 'Configure seu professor'}
        </h1>

        {error && <div className="error-message">{error}</div>}

        {step === 1 ? (
          <div className="step-content">
            <div className="form-group">
              <label htmlFor="name">Nome Completo</label>
              <input
                id="name"
                type="text"
                value={formData.name}
                onChange={(e) => handleInputChange('name', e.target.value)}
                placeholder="Seu nome"
                required
              />
            </div>

            <div className="form-group">
              <label htmlFor="email">Email</label>
              <input
                id="email"
                type="email"
                value={formData.email}
                onChange={(e) => handleInputChange('email', e.target.value)}
                placeholder="seu@email.com"
                required
              />
            </div>

            <div className="form-group">
              <label htmlFor="password">Senha</label>
              <input
                id="password"
                type="password"
                value={formData.password}
                onChange={(e) => handleInputChange('password', e.target.value)}
                placeholder="Mínimo 6 caracteres"
                required
                minLength={6}
              />
            </div>

            <div className="button-group">
              <button type="button" onClick={handleBack} className="btn-secondary">
                Voltar
              </button>
              <button type="button" onClick={handleNext} className="btn-primary">
                Continuar
              </button>
            </div>
          </div>
        ) : (
          <form onSubmit={handleSubmit} className="step-content">
            <div className="form-group">
              <label htmlFor="subject">Matéria que deseja aprender</label>
              <select
                id="subject"
                value={formData.subject}
                onChange={(e) => handleInputChange('subject', e.target.value)}
                required
              >
                <option value="">Selecione uma matéria</option>
                <option value="matematica">Matemática</option>
                <option value="portugues">Português</option>
                <option value="ciencias">Ciências</option>
                <option value="historia">História</option>
                <option value="geografia">Geografia</option>
                <option value="ingles">Inglês</option>
                <option value="fisica">Física</option>
                <option value="quimica">Química</option>
                <option value="biologia">Biologia</option>
              </select>
            </div>

            <div className="form-group">
              <label htmlFor="grade">Série/Ano</label>
              <select
                id="grade"
                value={formData.grade}
                onChange={(e) => handleInputChange('grade', e.target.value)}
                required
              >
                <option value="">Selecione sua série</option>
                <option value="6ano">6º Ano</option>
                <option value="7ano">7º Ano</option>
                <option value="8ano">8º Ano</option>
                <option value="9ano">9º Ano</option>
                <option value="1ano">1º Ano EM</option>
                <option value="2ano">2º Ano EM</option>
                <option value="3ano">3º Ano EM</option>
              </select>
            </div>

            <div className="button-group">
              <button
                type="button"
                onClick={handleBack}
                className="btn-secondary"
                disabled={loading}
              >
                Voltar
              </button>
              <button type="submit" className="btn-primary" disabled={loading}>
                {loading ? 'Criando...' : 'Criar Professor'}
              </button>
            </div>
          </form>
        )}
      </div>

      <style jsx>{`
        .onboarding-container {
          min-height: 100vh;
          display: flex;
          align-items: center;
          justify-content: center;
          padding: 2rem;
          background: linear-gradient(135deg, #f5f5f5 0%, #e0e0e0 100%);
        }

        .onboarding-card {
          background: white;
          border-radius: 16px;
          padding: 2.5rem;
          max-width: 500px;
          width: 100%;
          box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
        }

        .progress-bar {
          width: 100%;
          height: 4px;
          background-color: #e0e0e0;
          border-radius: 2px;
          margin-bottom: 2rem;
          overflow: hidden;
        }

        .progress-fill {
          height: 100%;
          background: linear-gradient(90deg, #8B5CF6 0%, #7C3AED 100%);
          transition: width 0.3s ease;
        }

        .onboarding-title {
          font-size: 1.75rem;
          font-weight: 700;
          color: #333;
          margin: 0 0 1.5rem 0;
          text-align: center;
        }

        .step-content {
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

        .form-group input,
        .form-group select {
          padding: 0.75rem;
          border: 1px solid #ddd;
          border-radius: 8px;
          font-size: 1rem;
          transition: border-color 0.2s;
        }

        .form-group input:focus,
        .form-group select:focus {
          outline: none;
          border-color: #8B5CF6;
        }

        .button-group {
          display: flex;
          gap: 1rem;
          margin-top: 1rem;
        }

        .btn-primary,
        .btn-secondary {
          flex: 1;
          padding: 0.875rem;
          border-radius: 8px;
          font-size: 1rem;
          font-weight: 600;
          cursor: pointer;
          transition: all 0.2s;
        }

        .btn-primary {
          background: linear-gradient(135deg, #8B5CF6 0%, #7C3AED 100%);
          color: white;
          border: none;
        }

        .btn-primary:hover:not(:disabled) {
          transform: translateY(-2px);
          box-shadow: 0 4px 12px rgba(139, 92, 246, 0.4);
        }

        .btn-primary:disabled {
          opacity: 0.7;
          cursor: not-allowed;
        }

        .btn-secondary {
          background: white;
          color: #666;
          border: 1px solid #ddd;
        }

        .btn-secondary:hover:not(:disabled) {
          background: #f5f5f5;
        }

        .error-message {
          padding: 0.875rem;
          background-color: #fee;
          color: #c33;
          border-radius: 8px;
          border: 1px solid #fcc;
          margin-bottom: 1rem;
          text-align: center;
        }

        @media (max-width: 768px) {
          .onboarding-container {
            padding: 1rem;
          }

          .onboarding-card {
            padding: 1.5rem;
          }
        }
      `}</style>
    </div>
  );
}
