export type QuestionType = 'single' | 'multiple';

export interface QuestionOption {
  id: string; // 'a', 'b', 'c', 'd'
  text: string;
}

export interface Question {
  id: string; // e.g. "w1_q1"
  assignmentWeek: number; // 1 to 12
  questionNumber: number; // 1 to 10
  type: QuestionType;
  prompt: string;
  imageUrl?: string;
  options: QuestionOption[];
  correctAnswers: string[]; // e.g. ['a'] or ['a', 'c']
  explanation?: string;
  topic?: string;
}

export interface TestSession {
  id: string;
  date: string;
  assignmentWeeks: number[];
  totalQuestions: number;
  timeSpentSeconds: number;
  answers: Record<string, string[]>;
  markedForReview: string[];
  score: number;
  maxScore: number;
  percentage: number;
}

export interface QuestionAttempt {
  questionId: string;
  selectedAnswers: string[];
  isCorrect: boolean;
  timestamp: number;
  mode: 'study' | 'test';
}

export type ViewMode = 'study' | 'test' | 'mistakes' | 'notes' | 'analytics';

export interface HciNote {
  id: string;
  title: string;
  category: 'Empirical Laws' | 'Cognitive Models' | 'Design Principles' | 'Evaluation & Usability' | 'Interaction Styles';
  weekReference?: number;
  summary: string;
  formula?: string;
  keyPoints: string[];
  examTip?: string;
}
