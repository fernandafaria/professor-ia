/**
 * Cliente API para comunicação com o backend FastAPI
 */

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

interface RequestOptions {
  method?: 'GET' | 'POST' | 'PUT' | 'DELETE' | 'PATCH';
  headers?: Record<string, string>;
  body?: any;
}

class ApiClient {
  private baseUrl: string;
  private defaultHeaders: Record<string, string>;

  constructor(baseUrl: string) {
    this.baseUrl = baseUrl;
    this.defaultHeaders = {
      'Content-Type': 'application/json',
    };
  }

  private getAuthToken(): string | null {
    if (typeof window !== 'undefined') {
      return localStorage.getItem('token');
    }
    return null;
  }

  private async request<T>(
    endpoint: string,
    options: RequestOptions = {}
  ): Promise<T> {
    const { method = 'GET', headers = {}, body } = options;

    const token = this.getAuthToken();
    const authHeaders: Record<string, string> = token
      ? { Authorization: `Bearer ${token}` }
      : {};

    const url = `${this.baseUrl}${endpoint}`;
    const config: RequestInit = {
      method,
      headers: {
        ...this.defaultHeaders,
        ...authHeaders,
        ...headers,
      },
    };

    if (body && method !== 'GET') {
      config.body = JSON.stringify(body);
    }

    try {
      const response = await fetch(url, config);

      if (!response.ok) {
        const error = await response.json().catch(() => ({
          detail: response.statusText,
        }));
        throw new Error(error.detail || `HTTP error! status: ${response.status}`);
      }

      // Se a resposta estiver vazia, retorna null
      const contentType = response.headers.get('content-type');
      if (contentType && contentType.includes('application/json')) {
        return await response.json();
      }

      return null as T;
    } catch (error) {
      console.error('API request failed:', error);
      throw error;
    }
  }

  // Auth endpoints
  async login(email: string, password: string) {
    return this.request<{ access_token: string; token_type: string }>(
      '/api/v1/auth/login',
      {
        method: 'POST',
        body: { email, password },
      }
    );
  }

  async register(email: string, password: string, name: string) {
    return this.request<{ id: string; email: string; name: string }>(
      '/api/v1/auth/register',
      {
        method: 'POST',
        body: { email, password, name },
      }
    );
  }

  async getCurrentUser(): Promise<{ id: string; email: string; name: string }> {
    return this.request<{ id: string; email: string; name: string }>('/api/v1/auth/me');
  }

  // Profile endpoints
  async getProfiles(): Promise<any[]> {
    try {
      const result = await this.request<any[]>('/api/v1/profile');
      if (Array.isArray(result)) {
        return result;
      }
      return [];
    } catch (error) {
      console.error('Error fetching profiles:', error);
      return [];
    }
  }

  async createProfile(data: any): Promise<{ id: string; name: string; subject?: string; grade?: string }> {
    return this.request<{ id: string; name: string; subject?: string; grade?: string }>('/api/v1/profile', {
      method: 'POST',
      body: data,
    });
  }

  async updateProfile(id: string, data: any): Promise<{ id: string; name: string; subject?: string; grade?: string }> {
    return this.request<{ id: string; name: string; subject?: string; grade?: string }>(`/api/v1/profile/${id}`, {
      method: 'PUT',
      body: data,
    });
  }

  // Conversation endpoints
  async getConversations(): Promise<any[]> {
    try {
      const result = await this.request<any[]>('/api/v1/conversations');
      if (Array.isArray(result)) {
        return result;
      }
      return [];
    } catch (error) {
      console.error('Error fetching conversations:', error);
      return [];
    }
  }

  async createConversation(data: { title: string }): Promise<{ id: string; title: string; created_at: string }> {
    return this.request<{ id: string; title: string; created_at: string }>('/api/v1/conversations', {
      method: 'POST',
      body: data,
    });
  }

  async getConversation(id: string): Promise<{ id: string; title: string; created_at: string }> {
    return this.request<{ id: string; title: string; created_at: string }>(`/api/v1/conversations/${id}`);
  }

  // Message endpoints
  async sendMessage(conversationId: string, content: string): Promise<{ id: string; content: string; created_at: string }> {
    return this.request<{ id: string; content: string; created_at: string }>(`/api/v1/conversations/${conversationId}/messages`, {
      method: 'POST',
      body: { content },
    });
  }

  async getMessages(conversationId: string): Promise<any[]> {
    try {
      const result = await this.request<any[]>(`/api/v1/conversations/${conversationId}/messages`);
      if (Array.isArray(result)) {
        return result;
      }
      return [];
    } catch (error) {
      console.error('Error fetching messages:', error);
      return [];
    }
  }
}

export const api = new ApiClient(API_URL);
