import React, { useState, useMemo } from 'react';
import { useQuizStore } from '../../store/useQuizStore';
import { 
  AlertCircle, 
  CheckCircle2, 
  Trash2, 
  Check, 
  XCircle, 
  Sparkles,
  BookOpen
} from 'lucide-react';
import confetti from 'canvas-confetti';

export const MistakeNotebookView: React.FC = () => {
  const { 
    questions, 
    mistakeIds, 
    removeMistake, 
    clearMistakes, 
    setActiveView,
    setStudyWeekFilter
  } = useQuizStore();

  const [selectedOptions, setSelectedOptions] = useState<Record<string, string[]>>({});
  const [revealedResults, setRevealedResults] = useState<Record<string, boolean>>({});

  const mistakeQuestions = useMemo(() => {
    const map = new Map(questions.map((q) => [q.id, q]));
    return mistakeIds.map((id) => map.get(id)!).filter(Boolean);
  }, [questions, mistakeIds]);

  const handleSelectOption = (q: typeof questions[0], optionId: string) => {
    if (revealedResults[q.id]) return;

    if (q.type === 'multiple') {
      const current = selectedOptions[q.id] || [];
      const updated = current.includes(optionId)
        ? current.filter((id) => id !== optionId)
        : [...current, optionId];
      setSelectedOptions((prev) => ({ ...prev, [q.id]: updated }));
    } else {
      // 1-Click Instant Check for single choice!
      const updated = [optionId];
      setSelectedOptions((prev) => ({ ...prev, [q.id]: updated }));
      setRevealedResults((prev) => ({ ...prev, [q.id]: true }));

      const isCorrect =
        updated.length === q.correctAnswers.length &&
        updated.every((ans) => q.correctAnswers.includes(ans));

      if (isCorrect) {
        confetti({
          particleCount: 40,
          spread: 60,
          origin: { y: 0.8 },
          colors: ['#10b981', '#3b82f6']
        });
      }
    }
  };

  const handleMsqCheck = (q: typeof questions[0]) => {
    const userAns = selectedOptions[q.id] || [];
    if (userAns.length === 0) return;

    setRevealedResults((prev) => ({ ...prev, [q.id]: true }));

    const isCorrect =
      userAns.length === q.correctAnswers.length &&
      userAns.every((ans) => q.correctAnswers.includes(ans));

    if (isCorrect) {
      confetti({
        particleCount: 40,
        spread: 60,
        origin: { y: 0.8 },
        colors: ['#10b981', '#3b82f6']
      });
    }
  };

  const handleMastered = (qId: string) => {
    removeMistake(qId);
  };

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
      
      {/* Top Banner */}
      <div className="glass-panel rounded-3xl p-6 sm:p-8 border-slate-200 dark:border-slate-800 shadow-2xl flex flex-col sm:flex-row items-center justify-between gap-6">
        <div className="flex items-center gap-4 text-center sm:text-left">
          <div className="w-14 h-14 rounded-2xl bg-rose-500/10 border border-rose-500/20 text-rose-600 dark:text-rose-400 flex items-center justify-center shrink-0 shadow-lg shadow-rose-500/10">
            <AlertCircle className="w-7 h-7" />
          </div>
          <div>
            <h1 className="text-2xl font-extrabold text-slate-900 dark:text-white tracking-tight">Mistake Notebook</h1>
            <p className="text-xs sm:text-sm text-slate-600 dark:text-slate-400 mt-1">
              Target and eliminate your weak spots. Questions missed during study or tests are saved here for deliberate practice.
            </p>
          </div>
        </div>

        <div className="flex items-center gap-3 shrink-0">
          {mistakeQuestions.length > 0 && (
            <button
              onClick={clearMistakes}
              className="flex items-center gap-1.5 px-4 py-2.5 rounded-xl border border-slate-300 dark:border-slate-700 hover:border-rose-500/40 text-xs font-semibold text-slate-600 dark:text-slate-400 hover:text-rose-600 dark:hover:text-rose-300 transition-colors"
            >
              <Trash2 className="w-4 h-4" />
              <span>Clear All</span>
            </button>
          )}

          <button
            onClick={() => {
              setStudyWeekFilter(0);
              setActiveView('study');
            }}
            className="flex items-center gap-1.5 px-4 py-2.5 rounded-xl bg-blue-600 hover:bg-blue-500 text-white text-xs font-bold shadow-md shadow-blue-600/30 transition-all"
          >
            <BookOpen className="w-4 h-4" />
            <span>Study All 120</span>
          </button>
        </div>
      </div>

      {/* Mistake Questions List */}
      {mistakeQuestions.length > 0 ? (
        <div className="space-y-6">
          <div className="flex items-center justify-between">
            <span className="text-xs font-bold text-slate-500 dark:text-slate-400 uppercase tracking-wider">
              {mistakeQuestions.length} Questions Requiring Attention
            </span>
          </div>

          {mistakeQuestions.map((q) => {
            const userAns = selectedOptions[q.id] || [];
            const isRevealed = !!revealedResults[q.id];
            const isCorrect =
              isRevealed &&
              userAns.length === q.correctAnswers.length &&
              userAns.every((ans) => q.correctAnswers.includes(ans));

            return (
              <div
                key={q.id}
                className="glass-panel rounded-3xl p-6 sm:p-7 border border-slate-200 dark:border-slate-800 shadow-xl space-y-5"
              >
                {/* Card Meta */}
                <div className="flex items-center justify-between border-b border-slate-200 dark:border-slate-800 pb-3">
                  <div className="flex items-center gap-2">
                    <span className="px-2.5 py-1 rounded-lg bg-rose-500/10 text-rose-700 dark:text-rose-400 border border-rose-500/20 text-xs font-bold">
                      Week {q.assignmentWeek} • Question {q.questionNumber}
                    </span>
                    <span className="text-xs px-2 py-0.5 rounded-lg bg-slate-100 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 text-slate-600 dark:text-slate-400">
                      {q.type === 'multiple' ? 'Multiple Choice' : 'Single Choice (Click to Answer)'}
                    </span>
                  </div>

                  <button
                    onClick={() => handleMastered(q.id)}
                    className="flex items-center gap-1 px-3 py-1 rounded-xl text-xs font-semibold text-slate-500 dark:text-slate-400 hover:text-emerald-600 dark:hover:text-emerald-400 hover:bg-emerald-50 dark:hover:bg-emerald-950/30 transition-colors"
                    title="Remove from notebook if you already know this"
                  >
                    <Check className="w-3.5 h-3.5" />
                    <span>Mastered (Remove)</span>
                  </button>
                </div>

                {/* Prompt */}
                <p className="text-base font-semibold text-slate-900 dark:text-slate-100 leading-relaxed">
                  {q.prompt}
                </p>

                {/* Interactive Options */}
                <div className="space-y-2.5">
                  {q.options.map((opt) => {
                    const isSelected = userAns.includes(opt.id);
                    const isOfficialCorrect = q.correctAnswers.includes(opt.id);

                    let itemClass = 'border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900/60 hover:bg-slate-50 dark:hover:bg-slate-800/80 text-slate-800 dark:text-slate-300';
                    let badgeClass = 'bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400 border-slate-300 dark:border-slate-700';

                    if (isRevealed) {
                      if (isOfficialCorrect) {
                        itemClass = 'border-emerald-500 bg-emerald-50 dark:bg-emerald-950/40 text-emerald-950 dark:text-emerald-200 font-medium';
                        badgeClass = 'bg-emerald-500 text-white font-bold border-emerald-400';
                      } else if (isSelected && !isOfficialCorrect) {
                        itemClass = 'border-rose-500 bg-rose-50 dark:bg-rose-950/40 text-rose-950 dark:text-rose-200 font-medium';
                        badgeClass = 'bg-rose-500 text-white font-bold border-rose-400';
                      } else {
                        itemClass = 'opacity-50 border-slate-200 dark:border-slate-800 text-slate-400 dark:text-slate-500';
                      }
                    } else if (isSelected) {
                      itemClass = 'border-blue-500 bg-blue-50 dark:bg-blue-950/40 text-blue-900 dark:text-blue-100';
                      badgeClass = 'bg-blue-600 text-white border-blue-400';
                    }

                    return (
                      <button
                        key={opt.id}
                        disabled={isRevealed}
                        onClick={() => handleSelectOption(q, opt.id)}
                        className={`w-full text-left p-3.5 rounded-2xl border transition-all flex items-start gap-3.5 ${itemClass}`}
                      >
                        <div className={`w-6 h-6 rounded-lg text-xs font-bold flex items-center justify-center shrink-0 border transition-colors ${badgeClass}`}>
                          {opt.id.toUpperCase()}
                        </div>
                        <span className="text-sm leading-relaxed pt-0.5">{opt.text}</span>
                      </button>
                    );
                  })}
                </div>

                {/* MSQ Confirm Button if needed */}
                {q.type === 'multiple' && !isRevealed && (
                  <div>
                    <button
                      disabled={userAns.length === 0}
                      onClick={() => handleMsqCheck(q)}
                      className={`px-4 py-2 rounded-xl text-xs font-bold transition-all ${
                        userAns.length > 0
                          ? 'bg-blue-600 text-white hover:bg-blue-500'
                          : 'bg-slate-200 dark:bg-slate-800 text-slate-400 dark:text-slate-600 cursor-not-allowed'
                      }`}
                    >
                      Confirm MSQ Answer
                    </button>
                  </div>
                )}

                {/* Explanation Banner if revealed */}
                {isRevealed && (
                  <div className={`p-5 rounded-2xl border space-y-3 text-xs shadow-sm ${
                    isCorrect
                      ? 'bg-emerald-50 dark:bg-emerald-950/40 border-emerald-300 dark:border-emerald-500/50 text-emerald-950 dark:text-emerald-200'
                      : 'bg-slate-50 dark:bg-slate-900 border-slate-200 dark:border-slate-800 text-slate-800 dark:text-slate-300'
                  }`}>
                    <div className="flex items-center justify-between border-b border-slate-200 dark:border-slate-800 pb-2">
                      <div className="flex items-center gap-1.5 font-bold">
                        {isCorrect ? (
                          <>
                            <CheckCircle2 className="w-4 h-4 text-emerald-600 dark:text-emerald-400" />
                            <span className="text-emerald-700 dark:text-emerald-400 text-sm">Correct! Mastered.</span>
                          </>
                        ) : (
                          <>
                            <XCircle className="w-4 h-4 text-rose-600 dark:text-rose-400" />
                            <span className="text-rose-700 dark:text-rose-400 text-sm">Incorrect</span>
                          </>
                        )}
                      </div>
                      <span className="font-bold text-xs px-2.5 py-0.5 rounded-full bg-slate-200 dark:bg-slate-800 text-slate-700 dark:text-slate-300">
                        Accepted: Option {q.correctAnswers.map(a => a.toUpperCase()).join(', ')}
                      </span>
                    </div>

                    {renderExplanationSections(q.explanation)}

                    <div className="pt-2 flex justify-end">
                      {isCorrect ? (
                        <button
                          onClick={() => handleMastered(q.id)}
                          className="px-4 py-2 rounded-xl bg-emerald-600 text-white text-xs font-bold hover:bg-emerald-500 shadow-md shadow-emerald-600/20 transition-all flex items-center gap-1.5"
                        >
                          <Sparkles className="w-3.5 h-3.5" />
                          <span>Remove from Notebook</span>
                        </button>
                      ) : (
                        <button
                          onClick={() => {
                            setRevealedResults((prev) => ({ ...prev, [q.id]: false }));
                            setSelectedOptions((prev) => ({ ...prev, [q.id]: [] }));
                          }}
                          className="px-4 py-2 rounded-xl bg-slate-200 dark:bg-slate-800 text-slate-700 dark:text-slate-300 text-xs font-semibold hover:bg-slate-300 dark:hover:bg-slate-700 transition-colors"
                        >
                          Try Again
                        </button>
                      )}
                    </div>
                  </div>
                )}
              </div>
            );
          })}
        </div>
      ) : (
        <div className="text-center py-20 glass-panel rounded-3xl border-slate-200 dark:border-slate-800 space-y-4">
          <div className="w-16 h-16 rounded-2xl bg-emerald-500/10 border border-emerald-500/20 text-emerald-600 dark:text-emerald-400 flex items-center justify-center mx-auto">
            <CheckCircle2 className="w-8 h-8" />
          </div>
          <h3 className="text-xl font-bold text-slate-900 dark:text-white">Your Mistake Notebook is Clean!</h3>
          <p className="text-sm text-slate-500 dark:text-slate-400 max-w-md mx-auto">
            Any questions answered incorrectly during Study Mode or Mock Tests will appear here for targeted practice.
          </p>
        </div>
      )}
    </div>
  );
};
