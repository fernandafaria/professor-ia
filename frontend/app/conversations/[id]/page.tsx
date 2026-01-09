/**
 * Chat/Conversa Page - Interface de chat com professor IA
 * Design do Figma será extraído e aplicado aqui
 */

'use client';

import { useEffect, useState, useRef } from 'react';
import { useRouter, useParams } from 'next/navigation';
import { api } from '@/lib/api';

export default function ConversationPage() {
  const router = useRouter();
  const params = useParams();
  const conversationId = params.id as string;
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const [loading, setLoading] = useState(true);
  const [sending, setSending] = useState(false);
  const [conversation, setConversation] = useState<any>(null);
  const [messages, setMessages] = useState<any[]>([]);
  const [messageContent, setMessageContent] = useState('');

  useEffect(() => {
    loadConversation();
  }, [conversationId]);

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const loadConversation = async () => {
    try {
      const token = localStorage.getItem('token');
      if (!token) {
        router.push('/login');
        return;
      }

      // Carregar conversa e mensagens
      const [conv, msgs] = await Promise.all([
        api.getConversation(conversationId),
        api.getMessages(conversationId),
      ]);

      setConversation(conv);
      setMessages(msgs);
    } catch (err) {
      console.error('Erro ao carregar conversa:', err);
      router.push('/dashboard');
    } finally {
      setLoading(false);
    }
  };

  const handleSendMessage = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!messageContent.trim() || sending) return;

    setSending(true);
    try {
      const newMessage = await api.sendMessage(conversationId, messageContent);
      setMessages([...messages, newMessage]);
      setMessageContent('');
    } catch (err) {
      console.error('Erro ao enviar mensagem:', err);
    } finally {
      setSending(false);
    }
  };

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  if (loading) {
    return (
      <div className="conversation-loading">
        <p>Carregando conversa...</p>
      </div>
    );
  }

  return (
    <div className="conversation-container">
      {/* Header */}
      <header className="conversation-header">
        <button onClick={() => router.push('/dashboard')} className="back-button">
          ← Voltar
        </button>
        <h1 className="conversation-title">
          {conversation?.title || 'Conversa'}
        </h1>
        <div className="header-spacer"></div>
      </header>

      {/* Messages Area */}
      <main className="messages-area">
        {messages.length === 0 ? (
          <div className="empty-conversation">
            <p>Nenhuma mensagem ainda. Comece a conversar!</p>
          </div>
        ) : (
          <div className="messages-list">
            {messages.map((message) => (
              <div
                key={message.id}
                className={`message ${message.role === 'user' ? 'message-user' : 'message-assistant'}`}
              >
                <div className="message-content">
                  {message.content}
                </div>
                <div className="message-time">
                  {new Date(message.created_at).toLocaleTimeString('pt-BR', {
                    hour: '2-digit',
                    minute: '2-digit',
                  })}
                </div>
              </div>
            ))}
            <div ref={messagesEndRef} />
          </div>
        )}
      </main>

      {/* Input Area */}
      <footer className="input-area">
        <form onSubmit={handleSendMessage} className="message-form">
          <div className="input-wrapper">
            <input
              type="text"
              value={messageContent}
              onChange={(e) => setMessageContent(e.target.value)}
              placeholder="Manda tua dúvida aqui... pode ser texto, foto, áudio..."
              className="message-input"
              disabled={sending}
            />
            <button
              type="submit"
              className="send-button"
              disabled={!messageContent.trim() || sending}
            >
              {sending ? 'Enviando...' : 'Enviar'}
            </button>
          </div>
        </form>
      </footer>

      <style jsx>{`
        .conversation-loading {
          min-height: 100vh;
          display: flex;
          align-items: center;
          justify-content: center;
          background: #f5f5f5;
        }

        .conversation-container {
          display: flex;
          flex-direction: column;
          height: 100vh;
          background: #f5f5f5;
        }

        .conversation-header {
          background: white;
          padding: 1rem 1.5rem;
          border-bottom: 1px solid #e0e0e0;
          display: flex;
          align-items: center;
          gap: 1rem;
        }

        .back-button {
          background: transparent;
          border: none;
          color: #7C3AED;
          font-size: 1rem;
          font-weight: 600;
          cursor: pointer;
          padding: 0.5rem;
        }

        .back-button:hover {
          color: #5B21B6;
        }

        .conversation-title {
          flex: 1;
          margin: 0;
          font-size: 1.25rem;
          font-weight: 600;
          color: #1a1a1a;
        }

        .header-spacer {
          width: 80px;
        }

        .messages-area {
          flex: 1;
          overflow-y: auto;
          padding: 2rem;
        }

        .empty-conversation {
          display: flex;
          align-items: center;
          justify-content: center;
          height: 100%;
          color: #999;
        }

        .messages-list {
          display: flex;
          flex-direction: column;
          gap: 1rem;
          max-width: 800px;
          margin: 0 auto;
        }

        .message {
          display: flex;
          flex-direction: column;
          gap: 0.5rem;
          max-width: 70%;
        }

        .message-user {
          align-self: flex-end;
        }

        .message-assistant {
          align-self: flex-start;
        }

        .message-content {
          padding: 1rem 1.25rem;
          border-radius: 16px;
          font-size: 1rem;
          line-height: 1.5;
        }

        .message-user .message-content {
          background: linear-gradient(135deg, #FF6B35 0%, #FF5722 100%);
          color: white;
          border-bottom-right-radius: 4px;
        }

        .message-assistant .message-content {
          background: white;
          color: #1a1a1a;
          border: 1px solid #e0e0e0;
          border-bottom-left-radius: 4px;
        }

        .message-time {
          font-size: 0.75rem;
          color: #999;
          padding: 0 0.5rem;
        }

        .input-area {
          background: white;
          padding: 1rem 1.5rem;
          border-top: 1px solid #e0e0e0;
        }

        .message-form {
          max-width: 800px;
          margin: 0 auto;
        }

        .input-wrapper {
          display: flex;
          gap: 0.75rem;
          align-items: center;
        }

        .message-input {
          flex: 1;
          padding: 0.875rem 1rem;
          border: 1px solid #ddd;
          border-radius: 24px;
          font-size: 1rem;
          transition: border-color 0.2s;
        }

        .message-input:focus {
          outline: none;
          border-color: #7C3AED;
        }

        .message-input:disabled {
          background: #f5f5f5;
          cursor: not-allowed;
        }

        .send-button {
          background: linear-gradient(135deg, #7C3AED 0%, #5B21B6 100%);
          color: white;
          border: none;
          padding: 0.875rem 1.5rem;
          border-radius: 24px;
          font-size: 1rem;
          font-weight: 600;
          cursor: pointer;
          transition: all 0.2s;
        }

        .send-button:hover:not(:disabled) {
          transform: translateY(-2px);
          box-shadow: 0 4px 12px rgba(124, 58, 237, 0.4);
        }

        .send-button:disabled {
          opacity: 0.5;
          cursor: not-allowed;
        }

        @media (max-width: 768px) {
          .messages-area {
            padding: 1rem;
          }

          .message {
            max-width: 85%;
          }

          .input-area {
            padding: 1rem;
          }
        }
      `}</style>
    </div>
  );
}
