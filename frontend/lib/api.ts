const API_BASE = process.env.NEXT_PUBLIC_API_BASE_URL || '/api';

async function fetcher<T>(path: string, options?: RequestInit): Promise<T> {
  const res = await fetch(`${API_BASE}${path}`, {
    headers: {
      'Content-Type': 'application/json',
    },
    ...options,
  });
  if (!res.ok) {
    throw new Error(`API error: ${res.status}`);
  }
  return res.json();
}

export const api = {
  auth: {
    login: (email: string, password: string) =>
      fetcher('/auth/login', {
        method: 'POST',
        body: new URLSearchParams({ username: email, password }),
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      }),
    register: (username: string, email: string, password: string) =>
      fetcher('/auth/register', {
        method: 'POST',
        body: JSON.stringify({ username, email, password }),
      }),
  },
  courses: {
    list: () => fetcher('/courses'),
    get: (id: number) => fetcher(`/courses/${id}`),
  },
  lessons: {
    get: (id: number) => fetcher(`/lessons/${id}`),
    complete: (id: number) =>
      fetcher(`/lessons/${id}/complete`, { method: 'POST' }),
  },
  exercises: {
    list: (lessonId: number) => fetcher(`/lessons/${lessonId}/exercises`),
    submit: (id: number, answer?: string, code?: string) =>
      fetcher(`/exercises/${id}/submit`, {
        method: 'POST',
        body: JSON.stringify({ answer, code }),
      }),
  },
  code: {
    run: (code: string, language = 'python', stdin = '') =>
      fetcher('/code/run', {
        method: 'POST',
        body: JSON.stringify({ language, code, stdin }),
      }),
  },
  users: {
    me: () => fetcher('/users/me'),
    dashboard: () => fetcher('/users/me/dashboard'),
  },
  ai: {
    chat: (message: string, history: Array<{ role: string; content: string }> = [], lessonId?: number) =>
      fetcher('/chat', {
        method: 'POST',
        body: JSON.stringify({ message, history, lesson_id: lessonId }),
      }),
    explainError: (code: string, error: string, lessonId?: number) =>
      fetcher('/explain-error', {
        method: 'POST',
        body: JSON.stringify({ code, error, lesson_id: lessonId }),
      }),
    reviewCode: (code: string, lessonId?: number, exerciseId?: number) =>
      fetcher('/review-code', {
        method: 'POST',
        body: JSON.stringify({ code, lesson_id: lessonId, exercise_id: exerciseId }),
      }),
    generatePractice: (lessonId: number, difficulty = 'easy', count = 3) =>
      fetcher('/generate-practice', {
        method: 'POST',
        body: JSON.stringify({ lesson_id: lessonId, difficulty, count }),
      }),
  },
};
