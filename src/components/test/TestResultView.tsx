import React, { useState, useEffect, useMemo } from 'react';
import { useQuizStore } from '../../store/useQuizStore';
import { TestSession } from '../../types/question';
import { 
  Trophy, 
  RotateCcw, 
  CheckCircle2, 
  XCircle, 
  HelpCircle, 
  Bookmark, 
  BookmarkCheck, 
  AlertCircle,
  Layers,
  ArrowRight
} from 'lucide-react';
import confetti from 'canvas-confetti';

interface TestResultViewProps {
  session: TestSession;
  onRetake: () => void;
}

export const TestResultView: React.FC<TestResultViewProps> = ({ session, onRetake }) => {
  const { 
    questions, 
    addMistake, 
    toggleBookmark, 
    isBookmarked,
    setActiveView 
  } = useQuizStore();

  const [reviewFilter, setReviewFilter] = useState<'all' | 'incorrect' | 'unattempted' | 'correct'>('incorrect');

  // Trigger celebration confetti on mount if score is good
  useEffect(() => {
    if (session.percentage >= 70) {
      confetti({
        particleCount: 70,
        spread: 80,
        origin: { y: 0.6 },
        colors: ['#3b82f6', '#10b981', '#f59e0b', '#6366f1']
      });
    }
  }, [session.percentage]);

  const questionsMap = useMemo(() => {
    return new Map(questions.map((q) => [q.id, q]));
  }, [questions]);

  // Breakdown by Week
  const weekBreakdown = useMemo(() => {
    const map = new Map<number, { total: number; correct: number }>();
    session.assignmentWeeks.forEach((w) => map.set(w, { total: 0, correct: 0 }));

    Object.keys(session.answers).forEach((qId) => {
      const q = questionsMap.get(qId);
      if (!q) return;
      const stats = map.get(q.assignmentWeek);
      if (stats) {
        stats.total += 1;
        const userAns = session.answers[qId] || [];
        const isCorrect =
          userAns.length === q.correctAnswers.length &&
          userAns.every((ans) => q.correctAnswers.includes(ans));
        if (isCorrect) stats.correct += 1;
      }
    });

    return map;
  }, [session, questionsMap]);

  // Evaluated question results
  const evaluatedQuestions = useMemo(() => {
    const list = Object.keys(session.answers).map((qId) => {
      const q = questionsMap.get(qId);
      if (!q) return null;

      const userAns = session.answers[qId] || [];
      const isUnattempted = userAns.length === 0;
      const isCorrect =
        !isUnattempted &&
        userAns.length === q.correctAnswers.length &&
        userAns.every((ans) => q.correctAnswers.includes(ans));

      return {
        question: q,
        userAns,
        isCorrect,
        isUnattempted,
      };
    }).filter(Boolean);

    return list as {
      question: typeof questions[0];
      userAns: string[];
      isCorrect: boolean;
      isUnattempted: boolean;
    }[];
  }, [session.answers, questionsMap]);

  const filteredReviewList = useMemo(() => {
    return evaluatedQuestions.filter((item) => {
      if (reviewFilter === 'incorrect') return !item.isCorrect && !item.isUnattempted;
      if (reviewFilter === 'unattempted') return item.isUnattempted;
      if (reviewFilter === 'correct') return item.isCorrect;
      return true;
    });
  }, [evaluatedQuestions, reviewFilter]);

  const handleAddAllMissedToNotebook = () => {
    evaluatedQuestions.forEach((item) => {
      if (!item.isCorrect) addMistake(item.question.id);
    });
  };

  const incorrectCount = evaluatedQuestions.filter((i) => !i.isCorrect && !i.isUnattempted).length;
  const unattemptedCount = evaluatedQuestions.filter((i) => i.isUnattempted).length;
  const correctCount = evaluatedQuestions.filter((i) => i.isCorrect).length;

  const renderExplanationSections = (text?: string) => {
    if (!text) return null;
    const parts = text.split('\n\n');
    return (
      <div className="space-y-2 pt-1 text-xs leading-relaxed">
        {parts.map((p, idx) => {
          if (p.startsWith('**Why it\'s Correct:**')) {
            return (
              <div key={idx} className="p-3 rounded-xl bg-emerald-500/10 border border-emerald-500/20 text-emerald-950 dark:text-emerald-200">
                <strong className="text-emerald-700 dark:text-emerald-300 font-bold block mb-0.5">✓ Why it's Correct:</strong>
                <p>{p.replace('**Why it\'s Correct:**', '').trim()}</p>
              </div>
            );
          }
          if (p.startsWith('**Why Other Options are Incorrect:**')) {
            return (
              <div key={idx} className="p-3 rounded-xl bg-slate-100 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 text-slate-800 dark:text-slate-300">
                <strong className="text-slate-900 dark:text-slate-200 font-bold block mb-0.5">✗ Why Other Options are Incorrect:</strong>
                <p>{p.replace('**Why Other Options are Incorrect:**', '').trim()}</p>
              </div>
            );
          }
          if (p.startsWith('**Course Context:**')) {
            return (
              <div key={idx} className="p-3 rounded-xl bg-blue-500/10 border border-blue-500/20 text-blue-950 dark:text-blue-200">
                <strong className="text-blue-700 dark:text-blue-300 font-bold block mb-0.5">💡 Course Context:</strong>
                <p>{p.replace('**Course Context:**', '').trim()}</p>
              </div>
            );
          }
          return <p key={idx} className="text-slate-700 dark:text-slate-300">{p}</p>;
        })}
      </div>
    );
  };

  return (
    <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8 animate-in fade-in duration-300">
      
      {/* Score Summary Card */}
      <div className="glass-panel rounded-3xl p-8 sm:p-10 border-slate-200 dark:border-slate-800 shadow-2xl space-y-8 relative overflow-hidden">
        
        <div className={`absolute top-0 right-0 w-80 h-80 rounded-full blur-3xl opacity-20 -mr-20 -mt-20 ${
          session.percentage >= 80 ? 'bg-emerald-500' : session.percentage >= 60 ? 'bg-blue-500' : 'bg-rose-500'
        }`} />

        <div className="flex flex-col sm:flex-row items-center sm:items-start justify-between gap-6 relative z-10">
          <div className="flex items-center gap-5 text-center sm:text-left">
            <div className={`w-20 h-20 rounded-2xl flex items-center justify-center shrink-0 shadow-xl ${
              session.percentage >= 70
                ? 'bg-gradient-to-tr from-emerald-600 to-teal-400 text-white shadow-emerald-500/25'
                : 'bg-gradient-to-tr from-blue-600 to-indigo-500 text-white shadow-blue-500/25'
            }`}>
              <Trophy className="w-10 h-10" />
            </div>

            <div className="space-y-1">
              <span className="text-xs font-bold uppercase tracking-wider text-blue-600 dark:text-blue-400">
                Test Completed • {session.date}
              </span>
              <h1 className="text-3xl sm:text-4xl font-extrabold text-slate-900 dark:text-white tracking-tight">
                {session.percentage >= 85 ? 'Outstanding Performance!' : session.percentage >= 60 ? 'Great Practice Attempt!' : 'Keep Practicing!'}
              </h1>
              <p className="text-xs sm:text-sm text-slate-500 dark:text-slate-400">
                You attempted {session.totalQuestions} questions across {session.assignmentWeeks.length} weeks.
              </p>
            </div>
          </div>

          {/* Large Score Pill */}
          <div className="text-center sm:text-right px-6 py-4 rounded-2xl bg-white dark:bg-slate-900/90 border border-slate-200 dark:border-slate-800 shrink-0 shadow-sm">
            <span className="text-xs text-slate-500 dark:text-slate-400 block font-medium">Final Score</span>
            <div className="flex items-baseline justify-center sm:justify-end gap-1">
              <span className="text-4xl font-extrabold text-slate-900 dark:text-white">{session.score}</span>
              <span className="text-slate-400 text-lg">/ {session.maxScore}</span>
            </div>
            <span className={`text-xs font-bold px-2 py-0.5 rounded-full mt-1 inline-block ${
              session.percentage >= 70 ? 'bg-emerald-500/20 text-emerald-700 dark:text-emerald-400' : 'bg-blue-500/20 text-blue-700 dark:text-blue-400'
            }`}>
              {session.percentage}% Accuracy
            </span>
          </div>
        </div>

        {/* Quick Stats Grid */}
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 pt-4 border-t border-slate-200 dark:border-slate-800/80">
          <div className="p-4 rounded-2xl bg-slate-50 dark:bg-slate-900/80 border border-slate-200 dark:border-slate-800 text-center">
            <span className="text-xs text-slate-500 dark:text-slate-400 block">Correct</span>
            <strong className="text-xl font-bold text-emerald-600 dark:text-emerald-400">{correctCount}</strong>
          </div>
          <div className="p-4 rounded-2xl bg-slate-50 dark:bg-slate-900/80 border border-slate-200 dark:border-slate-800 text-center">
            <span className="text-xs text-slate-500 dark:text-slate-400 block">Incorrect</span>
            <strong className="text-xl font-bold text-rose-600 dark:text-rose-400">{incorrectCount}</strong>
          </div>
          <div className="p-4 rounded-2xl bg-slate-50 dark:bg-slate-900/80 border border-slate-200 dark:border-slate-800 text-center">
            <span className="text-xs text-slate-500 dark:text-slate-400 block">Unattempted</span>
            <strong className="text-xl font-bold text-slate-600 dark:text-slate-400">{unattemptedCount}</strong>
          </div>
          <div className="p-4 rounded-2xl bg-slate-50 dark:bg-slate-900/80 border border-slate-200 dark:border-slate-800 text-center">
            <span className="text-xs text-slate-500 dark:text-slate-400 block">Time Spent</span>
            <strong className="text-xl font-bold text-blue-600 dark:text-blue-400">
              {Math.floor(session.timeSpentSeconds / 60)}m {session.timeSpentSeconds % 60}s
            </strong>
          </div>
        </div>

        {/* Action Controls */}
        <div className="flex flex-wrap items-center justify-between gap-4 pt-4 border-t border-slate-200 dark:border-slate-800">
          <button
            onClick={handleAddAllMissedToNotebook}
            className="flex items-center gap-2 px-4 py-2.5 rounded-xl bg-rose-500/10 border border-rose-500/30 text-rose-700 dark:text-rose-300 hover:bg-rose-500/20 text-xs font-bold transition-colors"
          >
            <AlertCircle className="w-4 h-4" />
            <span>Add Missed ({incorrectCount}) to Mistake Notebook</span>
          </button>

          <div className="flex items-center gap-3">
            <button
              onClick={() => setActiveView('study')}
              className="flex items-center gap-1.5 px-4 py-2.5 rounded-xl border border-slate-300 dark:border-slate-700 text-xs font-bold text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors"
            >
              <span>Review in Study Mode</span>
              <ArrowRight className="w-3.5 h-3.5" />
            </button>

            <button
              onClick={onRetake}
              className="flex items-center gap-1.5 px-5 py-2.5 rounded-xl bg-blue-600 hover:bg-blue-500 text-white text-xs font-bold shadow-lg shadow-blue-600/30 transition-all"
            >
              <RotateCcw className="w-3.5 h-3.5" />
              <span>Retake Test</span>
            </button>
          </div>
        </div>
      </div>

      {/* Week-by-Week Accuracy Breakdown */}
      {session.assignmentWeeks.length > 1 && (
        <div className="glass-panel rounded-3xl p-6 sm:p-8 border-slate-200 dark:border-slate-800 space-y-4 shadow-xl">
          <div className="flex items-center gap-2 border-b border-slate-200 dark:border-slate-800 pb-3">
            <Layers className="w-4 h-4 text-blue-600 dark:text-blue-400" />
            <h3 className="text-sm font-bold text-slate-900 dark:text-white uppercase tracking-wider">
              Performance by Assignment Week
            </h3>
          </div>

          <div className="grid grid-cols-2 sm:grid-cols-4 md:grid-cols-6 gap-3 pt-2">
            {session.assignmentWeeks.map((week) => {
              const stats = weekBreakdown.get(week) || { total: 0, correct: 0 };
              const pct = stats.total > 0 ? Math.round((stats.correct / stats.total) * 100) : 0;

              return (
                <div
                  key={week}
                  className="p-3.5 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 text-center space-y-1 shadow-sm"
                >
                  <span className="text-[11px] font-bold text-slate-500 dark:text-slate-400 block uppercase">
                    Week {week}
                  </span>
                  <div className="text-lg font-extrabold text-slate-900 dark:text-white">
                    {stats.correct} <span className="text-xs text-slate-400">/ {stats.total}</span>
                  </div>
                  <span className={`text-[10px] font-bold px-1.5 py-0.2 rounded-full inline-block ${
                    pct >= 80 ? 'bg-emerald-500/20 text-emerald-700 dark:text-emerald-400' : pct >= 50 ? 'bg-blue-500/20 text-blue-700 dark:text-blue-400' : 'bg-rose-500/20 text-rose-700 dark:text-rose-400'
                  }`}>
                    {pct}%
                  </span>
                </div>
              );
            })}
          </div>
        </div>
      )}

      {/* Question Review Section */}
      <div className="space-y-4">
        <div className="flex flex-wrap items-center justify-between gap-3">
          <h3 className="text-lg font-bold text-slate-900 dark:text-white tracking-tight">Question-by-Question Review</h3>

          <div className="flex items-center gap-1.5 p-1 rounded-xl bg-slate-100 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 text-xs">
            {(['incorrect', 'unattempted', 'correct', 'all'] as const).map((mode) => (
              <button
                key={mode}
                onClick={() => setReviewFilter(mode)}
                className={`px-3 py-1.5 rounded-lg font-semibold capitalize transition-colors ${
                  reviewFilter === mode
                    ? 'bg-blue-600 text-white shadow-sm'
                    : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200'
                }`}
              >
                {mode === 'incorrect' ? `Incorrect (${incorrectCount})` : mode}
              </button>
            ))}
          </div>
        </div>

        {/* Filtered Questions List */}
        <div className="space-y-4">
          {filteredReviewList.length > 0 ? (
            filteredReviewList.map(({ question: q, userAns, isCorrect, isUnattempted }) => (
              <div
                key={q.id}
                className={`glass-panel rounded-3xl p-6 sm:p-7 border space-y-4 transition-all shadow-md ${
                  isCorrect
                    ? 'border-emerald-300 dark:border-emerald-500/30'
                    : isUnattempted
                    ? 'border-slate-200 dark:border-slate-800'
                    : 'border-rose-300 dark:border-rose-500/30'
                }`}
              >
                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-2.5">
                    <span className="text-xs px-2.5 py-1 rounded-lg bg-slate-100 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 font-bold text-slate-700 dark:text-slate-300">
                      Week {q.assignmentWeek} • Q{q.questionNumber}
                    </span>
                    <span className={`text-xs px-2.5 py-1 rounded-lg font-bold flex items-center gap-1 ${
                      isCorrect
                        ? 'bg-emerald-500/20 text-emerald-700 dark:text-emerald-400 border border-emerald-500/30'
                        : isUnattempted
                        ? 'bg-slate-200 dark:bg-slate-800 text-slate-600 dark:text-slate-400 border border-slate-300 dark:border-slate-700'
                        : 'bg-rose-500/20 text-rose-700 dark:text-rose-400 border border-rose-500/30'
                    }`}>
                      {isCorrect ? (
                        <>
                          <CheckCircle2 className="w-3.5 h-3.5" />
                          <span>Correct (+1)</span>
                        </>
                      ) : isUnattempted ? (
                        <>
                          <HelpCircle className="w-3.5 h-3.5" />
                          <span>Unattempted (0)</span>
                        </>
                      ) : (
                        <>
                          <XCircle className="w-3.5 h-3.5" />
                          <span>Incorrect (0)</span>
                        </>
                      )}
                    </span>
                  </div>

                  <button
                    onClick={() => toggleBookmark(q.id)}
                    className="p-1.5 rounded-lg text-slate-400 hover:text-amber-500 transition-colors"
                  >
                    {isBookmarked(q.id) ? (
                      <BookmarkCheck className="w-4 h-4 text-amber-500" />
                    ) : (
                      <Bookmark className="w-4 h-4" />
                    )}
                  </button>
                </div>

                <p className="text-base font-semibold text-slate-900 dark:text-slate-100 leading-relaxed">
                  {q.prompt}
                </p>

                <div className="space-y-2 pt-1">
                  {q.options.map((opt) => {
                    const isSelected = userAns.includes(opt.id);
                    const isCorrectAnswer = q.correctAnswers.includes(opt.id);

                    let itemStyle = 'border-slate-200 dark:border-slate-800/80 bg-slate-50 dark:bg-slate-900/60 text-slate-600 dark:text-slate-400';
                    let badgeStyle = 'bg-slate-200 dark:bg-slate-800 text-slate-600 dark:text-slate-400 border-slate-300 dark:border-slate-700';

                    if (isCorrectAnswer) {
                      itemStyle = 'border-emerald-500 bg-emerald-50 dark:bg-emerald-950/30 text-emerald-900 dark:text-emerald-200 font-medium';
                      badgeStyle = 'bg-emerald-500 text-white font-bold border-emerald-400';
                    } else if (isSelected && !isCorrectAnswer) {
                      itemStyle = 'border-rose-500 bg-rose-50 dark:bg-rose-950/30 text-rose-900 dark:text-rose-200 font-medium';
                      badgeStyle = 'bg-rose-500 text-white font-bold border-rose-400';
                    }

                    return (
                      <div
                        key={opt.id}
                        className={`p-3.5 rounded-2xl border text-sm flex items-start gap-3.5 ${itemStyle}`}
                      >
                        <div className={`w-6 h-6 rounded-lg text-xs font-bold flex items-center justify-center shrink-0 border ${badgeStyle}`}>
                          {opt.id.toUpperCase()}
                        </div>
                        <span className="pt-0.5 leading-relaxed">{opt.text}</span>
                      </div>
                    );
                  })}
                </div>

                {/* Rich Explanation */}
                <div className="p-4 rounded-2xl bg-white dark:bg-slate-900/80 border border-slate-200 dark:border-slate-800 text-xs space-y-2 shadow-sm">
                  <span className="font-bold text-slate-900 dark:text-slate-200 block text-xs">
                    Official Accepted: Option {q.correctAnswers.map(a => a.toUpperCase()).join(', ')}
                  </span>
                  {renderExplanationSections(q.explanation)}
                </div>
              </div>
            ))
          ) : (
            <div className="text-center py-12 glass-panel rounded-3xl border-slate-200 dark:border-slate-800 text-slate-500 dark:text-slate-400 text-sm">
              No questions found under the "{reviewFilter}" filter.
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
