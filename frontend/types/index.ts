export interface Course {
  id: number;
  title: string;
  description: string;
  category: string;
  level: string;
  lesson_count: number;
  estimated_minutes: number;
  progress_percent?: number;
}

export interface Lesson {
  id: number;
  course_id: number;
  title: string;
  summary?: string;
  objectives?: string[];
  content: string;
  analogy?: string;
  example_code?: string;
  line_by_line_explanation?: Array<{ line: number; explanation: string }>;
  common_errors?: Array<{ error: string; explanation: string }>;
  order_index: number;
  estimated_minutes: number;
  is_completed?: boolean;
  next_lesson_id?: number;
}

export interface Exercise {
  id: number;
  lesson_id: number;
  type: 'choice' | 'judge' | 'fill_blank' | 'code_completion' | 'code_fix' | 'programming';
  title: string;
  description: string;
  options?: Array<{ label: string; text: string }>;
  difficulty: string;
  tags: string[];
  is_completed?: boolean;
}

export interface User {
  id: number;
  username: string;
  email: string;
  avatar_url?: string;
  learning_goal: string;
  level: string;
}

export interface DashboardStats {
  completed_lessons: number;
  total_lessons: number;
  completed_exercises: number;
  total_exercises: number;
  wrong_questions: number;
  completed_projects: number;
  total_projects: number;
  study_days: number;
  accuracy_rate: number;
}

export interface CodeRunResult {
  stdout: string;
  stderr: string;
  exit_code: number;
  execution_time_ms: number;
}
