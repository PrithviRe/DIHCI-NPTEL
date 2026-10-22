import { create } from 'zustand';
import { persist, createJSONStorage } from 'zustand/middleware';
import { Question, TestSession, ViewMode } from '../types/question';
import rawQuestions from '../data/questions.json';

interface StudyAttempt {
  selectedOptions: string[];
  isSubmitted: boolean;
  isCorrect: boolean;
}

interface QuizState {
  // Questions Bank
  questions: Question[];
  
  // Navigation
  activeView: ViewMode;
  setActiveView: (view: ViewMode) => void;

  // Bookmarks & Mistakes
  bookmarkedIds: string[];
  toggleBookmark: (questionId: string) => void;
  isBookmarked: (questionId: string) => boolean;

  mistakeIds: string[];
  addMistake: (questionId: string) => void;
  removeMistake: (questionId: string) => void;
  clearMistakes: () => void;

  // Study Mode State
  studyWeekFilter: number; // 0 = all weeks, 1..12 = specific week
  setStudyWeekFilter: (week: number) => void;
  studyQuestionIndex: number;
  setStudyQuestionIndex: (index: number) => void;
  studyAttempts: Record<string, StudyAttempt>; // questionId -> attempt
  recordStudyAttempt: (questionId: string, selectedOptions: string[], isCorrect: boolean) => void;
  resetStudyQuestion: (questionId: string) => void;
  resetAllStudyProgress: () => void;

  // Test Mode State
  isTestActive: boolean;
  activeTestSession: {
    selectedWeeks: number[];
    questionIds: string[];
    currentIndex: number;
    answers: Record<string, string[]>;
    markedForReview: string[];
    timeRemainingSeconds: number | null;
    totalTimeSeconds: number;
  } | null;
  startTest: (weeks: number[], questionCount?: number, timeLimitMinutes?: number | null, shuffle?: boolean) => void;
  recordTestAnswer: (questionId: string, selectedOptions: string[]) => void;
  toggleTestMarkReview: (questionId: string) => void;
  setTestQuestionIndex: (index: number) => void;
  submitTest: () => TestSession;
  cancelTest: () => void;

  // Completed Test History & Last Result
  lastTestSession: TestSession | null;
  setLastTestSession: (session: TestSession | null) => void;
  testHistory: TestSession[];
  clearTestHistory: () => void;

  // Preferences
  theme: 'dark' | 'light';
  toggleTheme: () => void;
  shuffleStudyOptions: boolean;
  toggleShuffleStudyOptions: () => void;
}

export const useQuizStore = create<QuizState>()(
  persist(
    (set, get) => ({
      questions: rawQuestions as Question[],
      activeView: 'study',
      setActiveView: (view) => set({ activeView: view }),

      bookmarkedIds: [],
      toggleBookmark: (id) => {
        const { bookmarkedIds } = get();
        if (bookmarkedIds.includes(id)) {
          set({ bookmarkedIds: bookmarkedIds.filter((item) => item !== id) });
        } else {
          set({ bookmarkedIds: [...bookmarkedIds, id] });
        }
      },
      isBookmarked: (id) => get().bookmarkedIds.includes(id),

      mistakeIds: [],
      addMistake: (id) => {
        const { mistakeIds } = get();
        if (!mistakeIds.includes(id)) {
          set({ mistakeIds: [...mistakeIds, id] });
        }
      },
      removeMistake: (id) => {
        set({ mistakeIds: get().mistakeIds.filter((item) => item !== id) });
      },
      clearMistakes: () => set({ mistakeIds: [] }),

      // Study Mode
      studyWeekFilter: 1, // default to Week 1
      setStudyWeekFilter: (week) => set({ studyWeekFilter: week, studyQuestionIndex: 0 }),
      studyQuestionIndex: 0,
      setStudyQuestionIndex: (index) => set({ studyQuestionIndex: index }),
      studyAttempts: {},
      recordStudyAttempt: (questionId, selectedOptions, isCorrect) => {
        const attempts = { ...get().studyAttempts };
        attempts[questionId] = {
          selectedOptions,
          isSubmitted: true,
          isCorrect,
        };
        const updates: Partial<QuizState> = { studyAttempts: attempts };
        if (!isCorrect) {
          const mistakeIds = get().mistakeIds;
          if (!mistakeIds.includes(questionId)) {
            updates.mistakeIds = [...mistakeIds, questionId];
          }
        }
        set(updates);
      },
      resetStudyQuestion: (questionId) => {
        const attempts = { ...get().studyAttempts };
        delete attempts[questionId];
        set({ studyAttempts: attempts });
      },
      resetAllStudyProgress: () => set({ studyAttempts: {} }),

      // Test Mode
      isTestActive: false,
      activeTestSession: null,
      lastTestSession: null,
      setLastTestSession: (session) => set({ lastTestSession: session }),
      testHistory: [],
      clearTestHistory: () => set({ testHistory: [], lastTestSession: null }),

      startTest: (weeks, questionCount, timeLimitMinutes, shuffle = false) => {
        const allQuestions = get().questions;
        let pool = allQuestions.filter((q) => weeks.includes(q.assignmentWeek));

        if (shuffle) {
          pool = [...pool].sort(() => Math.random() - 0.5);
        }

        if (questionCount && questionCount < pool.length) {
          pool = pool.slice(0, questionCount);
        }

        const totalTime = timeLimitMinutes ? timeLimitMinutes * 60 : 0;

        set({
          isTestActive: true,
          activeTestSession: {
            selectedWeeks: weeks,
            questionIds: pool.map((q) => q.id),
            currentIndex: 0,
            answers: {},
            markedForReview: [],
            timeRemainingSeconds: timeLimitMinutes ? totalTime : null,
            totalTimeSeconds: totalTime,
          },
        });
      },

      recordTestAnswer: (questionId, selectedOptions) => {
        const session = get().activeTestSession;
        if (!session) return;
        set({
          activeTestSession: {
            ...session,
            answers: {
              ...session.answers,
              [questionId]: selectedOptions,
            },
          },
        });
      },

      toggleTestMarkReview: (questionId) => {
        const session = get().activeTestSession;
        if (!session) return;
        const exists = session.markedForReview.includes(questionId);
        set({
          activeTestSession: {
            ...session,
            markedForReview: exists
              ? session.markedForReview.filter((id) => id !== questionId)
              : [...session.markedForReview, questionId],
          },
        });
      },

      setTestQuestionIndex: (index) => {
        const session = get().activeTestSession;
        if (!session) return;
        set({
          activeTestSession: {
            ...session,
            currentIndex: index,
          },
        });
      },

      submitTest: () => {
        const state = get();
        const session = state.activeTestSession;
        if (!session) throw new Error('No active test session');

        const allQuestionsMap = new Map(state.questions.map((q) => [q.id, q]));
        let score = 0;
        const mistakesToAdd: string[] = [];

        session.questionIds.forEach((qId) => {
          const q = allQuestionsMap.get(qId);
          if (!q) return;

          const userAns = session.answers[qId] || [];
          const correct = q.correctAnswers || [];

          // Compare set equality
          const isCorrect =
            userAns.length === correct.length &&
            userAns.every((ans) => correct.includes(ans));

          if (isCorrect) {
            score += 1;
          } else {
            mistakesToAdd.push(qId);
          }
        });

        const totalQuestions = session.questionIds.length;
        const percentage = Math.round((score / totalQuestions) * 100);

        const newSessionRecord: TestSession = {
          id: `test_${Date.now()}`,
          date: new Date().toLocaleDateString('en-US', {
            month: 'short',
            day: 'numeric',
            hour: '2-digit',
            minute: '2-digit',
          }),
          assignmentWeeks: session.selectedWeeks,
          totalQuestions,
          timeSpentSeconds: session.totalTimeSeconds - (session.timeRemainingSeconds ?? 0),
          answers: session.answers,
          markedForReview: session.markedForReview,
          score,
          maxScore: totalQuestions,
          percentage,
        };

        // Combine mistakes
        const updatedMistakes = Array.from(new Set([...state.mistakeIds, ...mistakesToAdd]));

        set({
          isTestActive: false,
          activeTestSession: null,
          lastTestSession: newSessionRecord,
          testHistory: [newSessionRecord, ...state.testHistory],
          mistakeIds: updatedMistakes,
          activeView: 'test',
        });

        return newSessionRecord;
      },

      cancelTest: () => {
        set({ isTestActive: false, activeTestSession: null });
      },

      // Preferences
      theme: 'dark',
      toggleTheme: () => {
        const newTheme = get().theme === 'dark' ? 'light' : 'dark';
        if (newTheme === 'dark') {
          document.documentElement.classList.add('dark');
        } else {
          document.documentElement.classList.remove('dark');
        }
        set({ theme: newTheme });
      },
      shuffleStudyOptions: false,
      toggleShuffleStudyOptions: () =>
        set({ shuffleStudyOptions: !get().shuffleStudyOptions }),
    }),
    {
      name: 'dihci-practice-storage',
      storage: createJSONStorage(() => localStorage),
      partialize: (state) => ({
        bookmarkedIds: state.bookmarkedIds,
        mistakeIds: state.mistakeIds,
        studyAttempts: state.studyAttempts,
        testHistory: state.testHistory,
        studyWeekFilter: state.studyWeekFilter,
        theme: state.theme,
        shuffleStudyOptions: state.shuffleStudyOptions,
      }),
    }
  )
);
