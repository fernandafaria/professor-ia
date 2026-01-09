/**
 * Dashboard - Página principal após criar o professor
 * TODO: Implementar dashboard completo com conversas, perfil, etc.
 */

'use client';

import { useEffect, useState } from 'react';
import { useRouter } from 'next/navigation';
import { api } from '@/lib/api';

export default function DashboardPage() {
  const router = useRouter();
  const [loading, setLoading] = useState(true);
  const [user, setUser] = useState<any>(null);
  const [conversations, setConversations] = useState<any[]>([]);

  useEffect(() => {
    loadDashboard();
  }, []);

  const loadDashboard = async () => {
    try {
      // Verificar se está autenticado
      const token = localStorage.getItem('token');
      if (!token) {
        router.push('/');
        return;
      }

      // Carregar dados do usuário
      try {
        const userData = await api.getCurrentUser();
        setUser(userData);
      } catch (err) {
        console.error('Erro ao carregar usuário:', err);
      }

      // Carregar conversas
      try {
        const convs = await api.getConversations();
        setConversations(Array.isArray(convs) ? convs : []);
      } catch (err) {
        console.error('Erro ao carregar conversas:', err);
        setConversations([]);
      }
    } catch (err) {
      console.error('Erro ao carregar dashboard:', err);
      router.push('/');
    } finally {
      setLoading(false);
    }
  };

  const handleLogout = () => {
    localStorage.removeItem('token');
    router.push('/');
  };

  if (loading) {
    return (
      <div className="dashboard-loading">
        <p>Carregando...</p>
      </div>
    );
  }

  return (
    <div className="dashboard-container">
      <header className="dashboard-header">
        <h1>Dashboard - Professor IA</h1>
        <button onClick={handleLogout} className="logout-button">
          Sair
        </button>
      </header>

      <main className="dashboard-main">
        <section className="welcome-section">
          <h2>
            Bem-vindo, {user?.name || 'Usuário'}! 👋
          </h2>
          <p>Seu professor IA está pronto para ajudá-lo a aprender.</p>
        </section>

        <section className="conversations-section">
          <h3>Suas Conversas</h3>
          {conversations.length === 0 ? (
            <div className="empty-state">
              <p>Você ainda não tem conversas.</p>
              <button
                onClick={async () => {
                  try {
                    const newConv = await api.createConversation({
                      title: 'Nova Conversa',
                    });
                    router.push(`/conversations/${newConv.id}`);
                  } catch (err) {
                    console.error('Erro ao criar conversa:', err);
                  }
                }}
                className="btn-primary"
              >
                Iniciar Nova Conversa
              </button>
            </div>
          ) : (
            <div className="conversations-list">
              {conversations.map((conv) => (
                <div
                  key={conv.id}
                  className="conversation-card"
                  onClick={() => router.push(`/conversations/${conv.id}`)}
                >
                  <h4>{conv.title || 'Conversa sem título'}</h4>
                  <p className="conversation-date">
                    {new Date(conv.created_at).toLocaleDateString('pt-BR')}
                  </p>
                </div>
              ))}
            </div>
          )}
        </section>
      </main>

      <style jsx>{`
        .dashboard-loading {
          min-height: 100vh;
          display: flex;
          align-items: center;
          justify-content: center;
        }

        .dashboard-container {
          min-height: 100vh;
          background: #f5f5f5;
        }

        .dashboard-header {
          background: white;
          padding: 1.5rem 2rem;
          border-bottom: 1px solid #e0e0e0;
          display: flex;
          justify-content: space-between;
          align-items: center;
        }

        .dashboard-header h1 {
          margin: 0;
          font-size: 1.5rem;
          color: #333;
        }

        .logout-button {
          padding: 0.5rem 1rem;
          background: #f5f5f5;
          border: 1px solid #ddd;
          border-radius: 6px;
          cursor: pointer;
          color: #666;
        }

        .logout-button:hover {
          background: #e0e0e0;
        }

        .dashboard-main {
          max-width: 1200px;
          margin: 0 auto;
          padding: 2rem;
        }

        .welcome-section {
          background: white;
          padding: 2rem;
          border-radius: 12px;
          margin-bottom: 2rem;
          box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
        }

        .welcome-section h2 {
          margin: 0 0 0.5rem 0;
          color: #333;
        }

        .welcome-section p {
          color: #666;
          margin: 0;
        }

        .conversations-section h3 {
          margin: 0 0 1rem 0;
          color: #333;
        }

        .empty-state {
          background: white;
          padding: 3rem;
          border-radius: 12px;
          text-align: center;
          box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
        }

        .empty-state p {
          color: #666;
          margin-bottom: 1.5rem;
        }

        .conversations-list {
          display: grid;
          gap: 1rem;
        }

        .conversation-card {
          background: white;
          padding: 1.5rem;
          border-radius: 8px;
          cursor: pointer;
          transition: all 0.2s;
          box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
        }

        .conversation-card:hover {
          transform: translateY(-2px);
          box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }

        .conversation-card h4 {
          margin: 0 0 0.5rem 0;
          color: #333;
        }

        .conversation-date {
          margin: 0;
          color: #999;
          font-size: 0.875rem;
        }

        .btn-primary {
          background: linear-gradient(135deg, #8B5CF6 0%, #7C3AED 100%);
          color: white;
          border: none;
          padding: 0.875rem 1.5rem;
          border-radius: 8px;
          font-weight: 600;
          cursor: pointer;
          transition: all 0.2s;
        }

        .btn-primary:hover {
          transform: translateY(-2px);
          box-shadow: 0 4px 12px rgba(139, 92, 246, 0.4);
        }
      `}</style>
    </div>
  );
}
