import React, { useState, useEffect, useMemo, useCallback } from 'react';
import { useQuizStore } from '../../store/useQuizStore';
import { 
  CheckCircle2, 
  XCircle, 
  Bookmark, 
  BookmarkCheck, 
  RotateCcw, 
  ChevronLeft, 
  ChevronRight, 
  Shuffle, 
  Lightbulb, 
  Check, 
  Layers,
  Sparkles,
  ArrowRight
} from 'lucide-react';
import confetti from 'canvas-confetti';

export const StudyView: React.FC = () => {
  const {
    questions,
    studyWeekFilter,
    setStudyWeekFilter,
    studyAttempts,
    recordStudyAttempt,
    resetStudyQuestion,
    bookmarkedIds,
    toggleBookmark,
    isBookmarked,
    shuffleStudyOptions,
    toggleShuffleStudyOptions
  } = useQuizStore();

  const [currentIndex, setCurrentIndex] = useState(0);
  const [selectedOptions, setSelectedOptions] = useState<string[]>([]);
  const [showAnswerForced, setShowAnswerForced] = useState(false);
  const [filterType, setFilterType] = useState<'all' | 'unattempted' | 'incorrect' | 'bookmarked'>('all');

  // Filter questions based on week and status
  const filteredQuestions = useMemo(() => {
    return questions.filter((q) => {
      if (studyWeekFilter !== 0 && q.assignmentWeek !== studyWeekFilter) return false;

      const attempt = studyAttempts[q.id];
      if (filterType === 'unattempted') return !attempt;
      if (filterType === 'incorrect') return attempt && !attempt.isCorrect;
      if (filterType === 'bookmarked') return bookmarkedIds.includes(q.id);
      return true;
    });
  }, [questions, studyWeekFilter, filterType, studyAttempts, bookmarkedIds]);

  useEffect(() => {
    if (currentIndex >= filteredQuestions.length) {
      setCurrentIndex(Math.max(0, filteredQuestions.length - 1));
    }
  }, [filteredQuestions.length, currentIndex]);

  const currentQ = filteredQuestions[currentIndex] || null;
  const currentAttempt = currentQ ? studyAttempts[currentQ.id] : null;
  const isSubmitted = !!currentAttempt || showAnswerForced;

  // Sync selected options when viewing previously attempted question
  useEffect(() => {
    if (currentAttempt) {
      setSelectedOptions(currentAttempt.selectedOptions);
      setShowAnswerForced(false);
    } else {
      setSelectedOptions([]);
      setShowAnswerForced(false);
    }
  }, [currentQ?.id, currentAttempt]);

  // Navigate Questions
  const handleNext = useCallback(() => {
    if (currentIndex < filteredQuestions.length - 1) {
      setCurrentIndex((prev) => prev + 1);
    }
  }, [currentIndex, filteredQuestions.length]);

  const handlePrev = useCallback(() => {
    if (currentIndex > 0) {
      setCurrentIndex((prev) => prev - 1);
    }
  }, [currentIndex]);

  // Option Click Handler (1-Click Instant Check for single choice)
  const handleSelectOption = (optionId: string) => {
    if (isSubmitted || !currentQ) return;

    if (currentQ.type === 'multiple') {
      // For MSQ: toggle selection
      setSelectedOptions((prev) =>
        prev.includes(optionId) ? prev.filter((id) => id !== optionId) : [...prev, optionId]
      );
    } else {
      // 1-CLICK INSTANT CHECK FOR SINGLE CHOICE!
      const newSelected = [optionId];
      setSelectedOptions(newSelected);

      const isCorrect =
        newSelected.length === currentQ.correctAnswers.length &&
        newSelected.every((opt) => currentQ.correctAnswers.includes(opt));

      recordStudyAttempt(currentQ.id, newSelected, isCorrect);

      if (isCorrect) {
        confetti({
          particleCount: 35,
          spread: 60,
          origin: { y: 0.8 },
          colors: ['#10b981', '#3b82f6', '#6366f1']
        });
      }
    }
  };

  // Submit Answer for Multiple Choice
  const handleMsqSubmit = useCallback(() => {
    if (!currentQ || selectedOptions.length === 0 || isSubmitted) return;

    const correct = currentQ.correctAnswers;
    const isCorrect =
      selectedOptions.length === correct.length &&
      selectedOptions.every((opt) => correct.includes(opt));

    recordStudyAttempt(currentQ.id, selectedOptions, isCorrect);

    if (isCorrect) {
      confetti({
        particleCount: 40,
        spread: 60,
        origin: { y: 0.8 },
        colors: ['#10b981', '#3b82f6']
      });
    }
  }, [currentQ, selectedOptions, isSubmitted, recordStudyAttempt]);

  // Keyboard Shortcuts
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (['INPUT', 'TEXTAREA'].includes((e.target as HTMLElement)?.tagName)) return;
      const key = e.key.toLowerCase();

      // Number keys 1-4 or A-D to select options
      if (!isSubmitted && currentQ) {
        if (['1', 'a'].includes(key) && currentQ.options[0]) handleSelectOption(currentQ.options[0].id);
        if (['2', 'b'].includes(key) && currentQ.options[1]) handleSelectOption(currentQ.options[1].id);
        if (['3', 'c'].includes(key) && currentQ.options[2]) handleSelectOption(currentQ.options[2].id);
        if (['4', 'd'].includes(key) && currentQ.options[3]) handleSelectOption(currentQ.options[3].id);
      }

      // Enter key: advances to next question when submitted
      if (e.key === 'Enter') {
        if (isSubmitted) {
          handleNext();
        } else if (currentQ?.type === 'multiple' && selectedOptions.length > 0) {
          handleMsqSubmit();
        }
      }

      if (e.key === 'ArrowRight') handleNext();
      if (e.key === 'ArrowLeft') handlePrev();

      if (key === 'f' && currentQ) {
        toggleBookmark(currentQ.id);
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [isSubmitted, currentQ, selectedOptions, handleMsqSubmit, handleNext, handlePrev, toggleBookmark]);

  // Week Selector counts
  const weekStats = useMemo(() => {
    const map = new Map<number, { total: number; correct: number }>();
    for (let w = 1; w <= 12; w++) map.set(w, { total: 0, correct: 0 });

    questions.forEach((q) => {
      const stats = map.get(q.assignmentWeek);
      if (stats) {
        stats.total += 1;
        if (studyAttempts[q.id]?.isCorrect) stats.correct += 1;
      }
    });
    return map;
  }, [questions, studyAttempts]);

  // Helper to format explanation markdown
  const renderFormattedExplanation = (text?: string) => {
    if (!text) return null;
    const parts = text.split('\n\n');
    return (
      <div className="space-y-3 pt-1 text-xs sm:text-sm leading-relaxed">
        {parts.map((p, idx) => {
          if (p.startsWith('**Why it\'s Correct:**')) {
            return (
              <div key={idx} className="p-3.5 rounded-2xl bg-emerald-500/10 border border-emerald-500/20 text-emerald-900 dark:text-emerald-200">
                <strong className="text-emerald-700 dark:text-emerald-300 font-bold block mb-1">✓ Why it's Correct:</strong>
                <p className="text-emerald-950 dark:text-emerald-100">{p.replace('**Why it\'s Correct:**', '').trim()}</p>
              </div>
            );
          }
          if (p.startsWith('**Why Other Options are Incorrect:**')) {
            return (
              <div key={idx} className="p-3.5 rounded-2xl bg-slate-100 dark:bg-slate-900/90 border border-slate-200 dark:border-slate-800 text-slate-800 dark:text-slate-300">
                <strong className="text-slate-900 dark:text-slate-200 font-bold block mb-1">✗ Why Other Options are Incorrect:</strong>
                <p className="text-slate-700 dark:text-slate-300">{p.replace('**Why Other Options are Incorrect:**', '').trim()}</p>
              </div>
            );
          }
          if (p.startsWith('**Course Context:**')) {
            return (
              <div key={idx} className="p-3.5 rounded-2xl bg-blue-500/10 border border-blue-500/20 text-blue-900 dark:text-blue-200">
                <strong className="text-blue-700 dark:text-blue-300 font-bold block mb-1">💡 Course Context & Key Takeaway:</strong>
                <p className="text-blue-950 dark:text-blue-100">{p.replace('**Course Context:**', '').trim()}</p>
              </div>
            );
          }
          return <p key={idx} className="text-slate-700 dark:text-slate-300">{p}</p>;
        })}
      </div>
    );
  };

  return (
    <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
      
      {/* Week Selector Chips */}
      <div className="space-y-3">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2">
            <Layers className="w-5 h-5 text-blue-600 dark:text-blue-400" />
            <h2 className="text-sm font-bold text-slate-800 dark:text-slate-200 tracking-wide uppercase">Select Assignment Week</h2>
          </div>
          <span className="text-xs text-slate-500 dark:text-slate-400">
            {studyWeekFilter === 0 ? 'All 120 Questions' : `Assignment ${studyWeekFilter} (10 Questions)`}
          </span>
        </div>

        <div className="flex items-center gap-2 overflow-x-auto pb-2 scrollbar-none">
          <button
            onClick={() => { setStudyWeekFilter(0); setCurrentIndex(0); }}
            className={`px-3.5 py-2 rounded-xl text-xs font-semibold whitespace-nowrap transition-all duration-150 border ${
              studyWeekFilter === 0
                ? 'bg-blue-600 border-blue-500 text-white shadow-md shadow-blue-500/25'
                : 'bg-white dark:bg-slate-900 border-slate-200 dark:border-slate-800 text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200 hover:border-slate-300 dark:hover:border-slate-700'
            }`}
          >
            All Weeks (120)
          </button>

          {Array.from({ length: 12 }, (_, i) => i + 1).map((week) => {
            const stats = weekStats.get(week) || { total: 10, correct: 0 };
            const isCompleted = stats.correct === stats.total && stats.total > 0;
            const isSelected = studyWeekFilter === week;

            return (
              <button
                key={week}
                onClick={() => { setStudyWeekFilter(week); setCurrentIndex(0); }}
                className={`flex items-center gap-1.5 px-3 py-2 rounded-xl text-xs font-semibold whitespace-nowrap transition-all border ${
                  isSelected
                    ? 'bg-blue-600 border-blue-500 text-white shadow-md shadow-blue-500/25'
                    : isCompleted
                    ? 'bg-emerald-50 dark:bg-emerald-950/40 border-emerald-300 dark:border-emerald-500/40 text-emerald-700 dark:text-emerald-400 hover:border-emerald-400'
                    : 'bg-white dark:bg-slate-900 border-slate-200 dark:border-slate-800 text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200 hover:border-slate-300 dark:hover:border-slate-700'
                }`}
              >
                <span>Week {week}</span>
                {isCompleted ? (
                  <Check className="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400 stroke-[3]" />
                ) : (
                  <span className={`text-[10px] px-1.5 py-0.2 rounded-full font-bold ${
                    isSelected ? 'bg-blue-800 text-blue-100' : 'bg-slate-100 dark:bg-slate-800 text-slate-500 dark:text-slate-400'
                  }`}>
                    {stats.correct}/{stats.total}
                  </span>
                )}
              </button>
            );
          })}
        </div>
      </div>

      {/* Filter Tabs & Toolbar */}
      <div className="flex flex-wrap items-center justify-between gap-3 p-3 rounded-2xl bg-white/70 dark:bg-slate-900/60 border border-slate-200 dark:border-slate-800/80 shadow-sm">
        <div className="flex items-center gap-1.5 overflow-x-auto">
          {(['all', 'unattempted', 'incorrect', 'bookmarked'] as const).map((mode) => (
            <button
              key={mode}
              onClick={() => { setFilterType(mode); setCurrentIndex(0); }}
              className={`px-3 py-1.5 rounded-lg text-xs font-medium capitalize transition-colors ${
                filterType === mode
                  ? 'bg-slate-200 dark:bg-slate-800 text-blue-700 dark:text-blue-400 font-bold border border-blue-400/30'
                  : 'text-slate-500 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200'
              }`}
            >
              {mode}
            </button>
          ))}
        </div>

        <div className="flex items-center gap-3 text-xs text-slate-500 dark:text-slate-400">
          <button
            onClick={toggleShuffleStudyOptions}
            className={`flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg border transition-colors ${
              shuffleStudyOptions
                ? 'bg-indigo-50 dark:bg-indigo-950/60 border-indigo-300 dark:border-indigo-500/50 text-indigo-700 dark:text-indigo-300 font-semibold'
                : 'border-slate-200 dark:border-slate-800 hover:bg-slate-100 dark:hover:bg-slate-800/60 text-slate-600 dark:text-slate-400'
            }`}
            title="Randomize option order to prevent positional memorization"
          >
            <Shuffle className="w-3.5 h-3.5" />
            <span>Shuffle Options</span>
          </button>
        </div>
      </div>

      {/* Main Question Card Area */}
      {currentQ ? (
        <div className="glass-panel rounded-3xl p-6 sm:p-8 space-y-6 shadow-xl relative border-slate-200 dark:border-slate-800">
          
          {/* Card Top Meta */}
          <div className="flex items-center justify-between border-b border-slate-200 dark:border-slate-800/80 pb-4">
            <div className="flex items-center gap-3">
              <span className="px-2.5 py-1 rounded-lg bg-blue-500/10 text-blue-600 dark:text-blue-400 border border-blue-500/20 text-xs font-bold">
                Assignment {currentQ.assignmentWeek} • Question {currentQ.questionNumber}
              </span>
              <span className={`text-xs px-2.5 py-1 rounded-lg border font-medium ${
                currentQ.type === 'multiple' 
                  ? 'bg-purple-500/10 text-purple-700 dark:text-purple-400 border-purple-500/30' 
                  : 'bg-slate-100 dark:bg-slate-800/80 text-slate-600 dark:text-slate-400 border-slate-200 dark:border-slate-700/60'
              }`}>
                {currentQ.type === 'multiple' ? 'Multiple Choice (MSQ)' : 'Single Choice (Click to Answer)'}
              </span>
            </div>

            <div className="flex items-center gap-2">
              <button
                onClick={() => toggleBookmark(currentQ.id)}
                className={`p-2 rounded-xl transition-all ${
                  isBookmarked(currentQ.id)
                    ? 'text-amber-500 bg-amber-500/10 border border-amber-500/30'
                    : 'text-slate-400 hover:text-slate-600 dark:hover:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-800'
                }`}
                title="Bookmark for revision (Hotkey: F)"
              >
                {isBookmarked(currentQ.id) ? (
                  <BookmarkCheck className="w-5 h-5 fill-amber-500/20" />
                ) : (
                  <Bookmark className="w-5 h-5" />
                )}
              </button>

              <button
                onClick={() => resetStudyQuestion(currentQ.id)}
                className="p-2 rounded-xl text-slate-400 hover:text-slate-600 dark:hover:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors"
                title="Reset question attempt"
              >
                <RotateCcw className="w-4 h-4" />
              </button>
            </div>
          </div>

          {/* Question Prompt */}
          <div className="space-y-4">
            <h3 className="text-lg sm:text-xl font-semibold text-slate-900 dark:text-slate-100 leading-relaxed tracking-normal">
              {currentQ.prompt}
            </h3>

            {currentQ.imageUrl && (
              <div className="p-2 rounded-xl bg-slate-100 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 inline-block">
                <img src={currentQ.imageUrl} alt="Question Diagram" className="max-h-72 rounded-lg object-contain" />
              </div>
            )}

            {currentQ.type === 'multiple' && (
              <p className="text-xs font-medium text-purple-600 dark:text-purple-300 flex items-center gap-1.5">
                <Sparkles className="w-3.5 h-3.5" />
                Multiple correct options: Select all options that apply, then click "Confirm Answer".
              </p>
            )}
          </div>

          {/* Options List */}
          <div className="space-y-3 pt-2">
            {currentQ.options.map((opt) => {
              const isSelected = selectedOptions.includes(opt.id);
              const isCorrectAnswer = currentQ.correctAnswers.includes(opt.id);

              let optionClasses = 'border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900/70 hover:border-slate-300 dark:hover:border-slate-700 hover:bg-slate-50 dark:hover:bg-slate-800/80 text-slate-800 dark:text-slate-200';
              let badgeClasses = 'bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400 border-slate-300 dark:border-slate-700';

              if (isSubmitted) {
                if (isCorrectAnswer) {
                  optionClasses = 'border-emerald-500 bg-emerald-50 dark:bg-emerald-950/40 text-emerald-950 dark:text-emerald-100 shadow-sm shadow-emerald-500/10 font-medium';
                  badgeClasses = 'bg-emerald-500 text-white font-bold border-emerald-400';
                } else if (isSelected && !isCorrectAnswer) {
                  optionClasses = 'border-rose-500 bg-rose-50 dark:bg-rose-950/40 text-rose-950 dark:text-rose-100 font-medium';
                  badgeClasses = 'bg-rose-500 text-white font-bold border-rose-400';
                } else {
                  optionClasses = 'opacity-50 border-slate-200 dark:border-slate-800/50 bg-slate-50/50 dark:bg-slate-950/30 text-slate-400 dark:text-slate-500';
                }
              } else if (isSelected) {
                optionClasses = 'border-blue-500 bg-blue-50 dark:bg-blue-950/40 text-blue-900 dark:text-blue-100 shadow-sm shadow-blue-500/20';
                badgeClasses = 'bg-blue-600 text-white border-blue-400';
              }

              return (
                <button
                  key={opt.id}
                  onClick={() => handleSelectOption(opt.id)}
                  className={`w-full text-left p-4 rounded-2xl border transition-all duration-150 flex items-start gap-4 ${optionClasses} ${
                    !isSubmitted ? 'cursor-pointer active:scale-[0.99]' : ''
                  }`}
                >
                  <div className={`w-7 h-7 rounded-lg flex items-center justify-center text-xs font-bold shrink-0 border transition-colors ${badgeClasses}`}>
                    {isSubmitted && isCorrectAnswer ? (
                      <Check className="w-4 h-4 stroke-[3]" />
                    ) : isSubmitted && isSelected && !isCorrectAnswer ? (
                      <XCircle className="w-4 h-4 stroke-[2.5]" />
                    ) : (
                      opt.id.toUpperCase()
                    )}
                  </div>

                  <span className="text-sm sm:text-base leading-relaxed pt-0.5">
                    {opt.text}
                  </span>
                </button>
              );
            })}
          </div>

          {/* Action Row for MSQ or Next */}
          {currentQ.type === 'multiple' && !isSubmitted && (
            <div className="pt-2">
              <button
                disabled={selectedOptions.length === 0}
                onClick={handleMsqSubmit}
                className={`px-5 py-2.5 rounded-xl font-bold text-xs tracking-wide transition-all shadow-md ${
                  selectedOptions.length > 0
                    ? 'bg-blue-600 hover:bg-blue-500 text-white shadow-blue-600/30 hover:scale-[1.02]'
                    : 'bg-slate-200 dark:bg-slate-800 text-slate-400 dark:text-slate-600 cursor-not-allowed'
                }`}
              >
                Confirm Answer ({selectedOptions.length} selected)
              </button>
            </div>
          )}

          {/* Explanation Banner (Shows immediately after click / submit) */}
          {isSubmitted && (
            <div className={`p-6 rounded-3xl border transition-all space-y-4 shadow-md ${
              currentAttempt?.isCorrect
                ? 'bg-emerald-50/80 dark:bg-emerald-950/30 border-emerald-300 dark:border-emerald-500/40'
                : 'bg-slate-50 dark:bg-slate-900/90 border-slate-300 dark:border-slate-700/80'
            }`}>
              <div className="flex items-center justify-between border-b border-slate-200 dark:border-slate-800 pb-3">
                <div className="flex items-center gap-2.5 text-sm font-bold">
                  {currentAttempt?.isCorrect ? (
                    <>
                      <CheckCircle2 className="w-5 h-5 text-emerald-600 dark:text-emerald-400" />
                      <span className="text-emerald-700 dark:text-emerald-400 text-base">Correct!</span>
                    </>
                  ) : (
                    <>
                      <XCircle className="w-5 h-5 text-rose-600 dark:text-rose-400" />
                      <span className="text-rose-700 dark:text-rose-400 text-base">Incorrect</span>
                    </>
                  )}
                </div>

                <div className="text-xs font-bold px-3 py-1 rounded-full bg-slate-200 dark:bg-slate-800 text-slate-800 dark:text-slate-200">
                  Accepted: Option {currentQ.correctAnswers.map(a => a.toUpperCase()).join(', ')}
                </div>
              </div>

              {/* Render the rich 3-part explanation */}
              {renderFormattedExplanation(currentQ.explanation)}

              {/* Quick Next Button */}
              <div className="pt-2 flex justify-end">
                <button
                  onClick={handleNext}
                  className="flex items-center gap-2 px-5 py-2.5 rounded-xl bg-blue-600 hover:bg-blue-500 text-white text-xs font-bold shadow-md shadow-blue-600/20 transition-all hover:scale-[1.02]"
                >
                  <span>Next Question (Enter)</span>
                  <ArrowRight className="w-4 h-4" />
                </button>
              </div>
            </div>
          )}

          {/* Action Footer Navigation */}
          <div className="flex flex-wrap items-center justify-between gap-4 pt-4 border-t border-slate-200 dark:border-slate-800">
            <div className="flex items-center gap-2">
              {!isSubmitted ? (
                <button
                  onClick={() => setShowAnswerForced(true)}
                  className="px-3.5 py-2 rounded-xl text-xs font-semibold text-slate-500 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-800/60 transition-colors"
                >
                  Show Answer & Explanation
                </button>
              ) : (
                <button
                  onClick={() => {
                    resetStudyQuestion(currentQ.id);
                    setShowAnswerForced(false);
                    setSelectedOptions([]);
                  }}
                  className="px-3.5 py-2 rounded-xl text-xs font-semibold bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700 transition-colors"
                >
                  Try Again
                </button>
              )}
            </div>

            {/* Navigation Controls */}
            <div className="flex items-center gap-3">
              <span className="text-xs font-medium text-slate-500 dark:text-slate-400">
                {currentIndex + 1} of {filteredQuestions.length}
              </span>

              <div className="flex items-center gap-1.5">
                <button
                  disabled={currentIndex === 0}
                  onClick={handlePrev}
                  className="p-2 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 disabled:opacity-40 disabled:cursor-not-allowed transition-colors"
                  title="Previous question (ArrowLeft)"
                >
                  <ChevronLeft className="w-4 h-4" />
                </button>

                <button
                  disabled={currentIndex === filteredQuestions.length - 1}
                  onClick={handleNext}
                  className="p-2 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 disabled:opacity-40 disabled:cursor-not-allowed transition-colors"
                  title="Next question (ArrowRight)"
                >
                  <ChevronRight className="w-4 h-4" />
                </button>
              </div>
            </div>
          </div>
        </div>
      ) : (
        <div className="text-center py-16 space-y-4 glass-panel rounded-3xl">
          <p className="text-slate-500 dark:text-slate-400 text-base">No questions found matching this filter.</p>
          <button
            onClick={() => setFilterType('all')}
            className="px-4 py-2 rounded-xl bg-blue-600 text-white text-xs font-bold hover:bg-blue-500 transition-colors"
          >
            Reset Filters
          </button>
        </div>
      )}
    </div>
  );
};
