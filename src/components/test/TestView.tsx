import React, { useState, useEffect, useMemo, useCallback } from 'react';
import { useQuizStore } from '../../store/useQuizStore';
import { 
  Clock, 
  Flag, 
  ChevronLeft, 
  ChevronRight, 
  Send, 
  AlertTriangle,
} from 'lucide-react';
import { TestConfigModal } from './TestConfigModal';
import { TestResultView } from './TestResultView';

export const TestView: React.FC = () => {
  const {
    questions,
    isTestActive,
    activeTestSession,
    recordTestAnswer,
    toggleTestMarkReview,
    setTestQuestionIndex,
    submitTest,
    cancelTest,
    lastTestSession,
    setLastTestSession
  } = useQuizStore();

  const [isConfigOpen, setIsConfigOpen] = useState(false);
  const [isSubmitModalOpen, setIsSubmitModalOpen] = useState(false);
  const [timeLeft, setTimeLeft] = useState<number | null>(null);

  // Sync timer
  useEffect(() => {
    if (activeTestSession?.timeRemainingSeconds !== undefined) {
      setTimeLeft(activeTestSession.timeRemainingSeconds);
    }
  }, [activeTestSession]);

  // Countdown timer effect
  useEffect(() => {
    if (!isTestActive || timeLeft === null) return;
    if (timeLeft <= 0) {
      handleFinalSubmit();
      return;
    }

    const timer = setInterval(() => {
      setTimeLeft((prev) => (prev !== null && prev > 0 ? prev - 1 : 0));
    }, 1000);

    return () => clearInterval(timer);
  }, [isTestActive, timeLeft]);

  // Map of questions for quick lookup
  const questionsMap = useMemo(() => {
    return new Map(questions.map((q) => [q.id, q]));
  }, [questions]);

  const activeQuestionList = useMemo(() => {
    if (!activeTestSession) return [];
    return activeTestSession.questionIds.map((id) => questionsMap.get(id)!).filter(Boolean);
  }, [activeTestSession, questionsMap]);

  const currentQ = activeTestSession
    ? activeQuestionList[activeTestSession.currentIndex]
    : null;

  const currentSelectedOptions = (currentQ && activeTestSession?.answers[currentQ.id]) || [];
  const isMarked = (currentQ && activeTestSession?.markedForReview.includes(currentQ.id)) || false;

  // Handle Option Toggle
  const handleSelectOption = (optionId: string) => {
    if (!currentQ) return;
    if (currentQ.type === 'multiple') {
      const updated = currentSelectedOptions.includes(optionId)
        ? currentSelectedOptions.filter((id) => id !== optionId)
        : [...currentSelectedOptions, optionId];
      recordTestAnswer(currentQ.id, updated);
    } else {
      recordTestAnswer(currentQ.id, [optionId]);
    }
  };

  const handleClearResponse = () => {
    if (!currentQ) return;
    recordTestAnswer(currentQ.id, []);
  };

  const handleNext = useCallback(() => {
    if (!activeTestSession) return;
    if (activeTestSession.currentIndex < activeQuestionList.length - 1) {
      setTestQuestionIndex(activeTestSession.currentIndex + 1);
    }
  }, [activeTestSession, activeQuestionList.length, setTestQuestionIndex]);

  const handlePrev = useCallback(() => {
    if (!activeTestSession) return;
    if (activeTestSession.currentIndex > 0) {
      setTestQuestionIndex(activeTestSession.currentIndex - 1);
    }
  }, [activeTestSession, setTestQuestionIndex]);

  const handleFinalSubmit = () => {
    setIsSubmitModalOpen(false);
    submitTest();
  };

  // Keyboard navigation inside test
  useEffect(() => {
    if (!isTestActive || !currentQ) return;

    const handleKeyDown = (e: KeyboardEvent) => {
      const key = e.key.toLowerCase();
      if (['1', 'a'].includes(key) && currentQ.options[0]) handleSelectOption(currentQ.options[0].id);
      if (['2', 'b'].includes(key) && currentQ.options[1]) handleSelectOption(currentQ.options[1].id);
      if (['3', 'c'].includes(key) && currentQ.options[2]) handleSelectOption(currentQ.options[2].id);
      if (['4', 'd'].includes(key) && currentQ.options[3]) handleSelectOption(currentQ.options[3].id);
      if (e.key === 'ArrowRight') handleNext();
      if (e.key === 'ArrowLeft') handlePrev();
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [isTestActive, currentQ, currentSelectedOptions, handleNext, handlePrev]);

  // Format time (HH:MM:SS)
  const formatTimer = (seconds: number) => {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  };

  // If viewing previous test results
  if (!isTestActive && lastTestSession) {
    return (
      <TestResultView
        session={lastTestSession}
        onRetake={() => {
          setLastTestSession(null);
          setIsConfigOpen(true);
        }}
      />
    );
  }

  // If idle, show Test Landing Card
  if (!isTestActive) {
    return (
      <div className="max-w-4xl mx-auto px-4 py-16 text-center space-y-8">
        <div className="glass-panel rounded-3xl p-8 sm:p-12 space-y-6 border-slate-200 dark:border-slate-800 shadow-2xl">
          <div className="w-16 h-16 rounded-2xl bg-blue-500/10 border border-blue-500/20 text-blue-600 dark:text-blue-400 flex items-center justify-center mx-auto shadow-lg shadow-blue-500/10">
            <Clock className="w-8 h-8" />
          </div>

          <div className="space-y-3">
            <h1 className="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-white tracking-tight">
              NPTEL DIHCI Exam Simulator
            </h1>
            <p className="text-slate-600 dark:text-slate-400 text-sm sm:text-base max-w-xl mx-auto leading-relaxed">
              Experience the full 120-question mock test or test individual assignment weeks under timed exam conditions with standard NPTEL scoring (+1 / 0).
            </p>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 pt-4 max-w-2xl mx-auto text-left text-xs">
            <div className="p-4 rounded-2xl bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-1">
              <span className="font-bold text-slate-900 dark:text-white block">120 Questions</span>
              <span className="text-slate-500 dark:text-slate-400">Authentic NPTEL Assignments 1 to 12.</span>
            </div>
            <div className="p-4 rounded-2xl bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-1">
              <span className="font-bold text-slate-900 dark:text-white block">Flexible Timer</span>
              <span className="text-slate-500 dark:text-slate-400">Timed 30/60/90 mins or untimed.</span>
            </div>
            <div className="p-4 rounded-2xl bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-1">
              <span className="font-bold text-slate-900 dark:text-white block">Detailed Scorecard</span>
              <span className="text-slate-500 dark:text-slate-400">Week-by-week accuracy & review.</span>
            </div>
          </div>

          <div className="pt-6">
            <button
              onClick={() => setIsConfigOpen(true)}
              className="px-8 py-4 rounded-2xl font-bold text-sm bg-blue-600 hover:bg-blue-500 text-white shadow-xl shadow-blue-600/30 hover:scale-[1.02] transition-all"
            >
              Configure & Start Test
            </button>
          </div>
        </div>

        <TestConfigModal isOpen={isConfigOpen} onClose={() => setIsConfigOpen(false)} />
      </div>
    );
  }

  const totalQuestions = activeQuestionList.length;
  const answeredCount = Object.values(activeTestSession?.answers || {}).filter(
    (arr) => arr.length > 0
  ).length;
  const markedCount = activeTestSession?.markedForReview.length || 0;
  const unattemptedCount = totalQuestions - answeredCount;

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 space-y-6">
      
      {/* Top Test Header Bar */}
      <div className="glass-panel rounded-2xl px-6 py-4 flex items-center justify-between border-slate-200 dark:border-slate-800 shadow-lg">
        <div className="flex items-center gap-3">
          <span className="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse" />
          <div>
            <h2 className="text-sm font-bold text-slate-900 dark:text-white tracking-wide">
              DIHCI Mock Test
            </h2>
            <span className="text-xs text-slate-500 dark:text-slate-400">
              Question {(activeTestSession?.currentIndex || 0) + 1} of {totalQuestions}
            </span>
          </div>
        </div>

        {/* Timer */}
        {timeLeft !== null && (
          <div className={`flex items-center gap-2 px-4 py-1.5 rounded-xl border text-sm font-mono font-bold tracking-wider ${
            timeLeft < 300 
              ? 'bg-rose-50 dark:bg-rose-950/60 border-rose-300 dark:border-rose-500/80 text-rose-700 dark:text-rose-300 animate-pulse' 
              : 'bg-slate-100 dark:bg-slate-900 border-slate-200 dark:border-slate-800 text-blue-700 dark:text-blue-400'
          }`}>
            <Clock className="w-4 h-4" />
            <span>{formatTimer(timeLeft)}</span>
          </div>
        )}

        {/* Finish Button */}
        <button
          onClick={() => setIsSubmitModalOpen(true)}
          className="flex items-center gap-2 px-4 py-2 rounded-xl bg-blue-600 hover:bg-blue-500 text-white text-xs font-bold shadow-md shadow-blue-600/30 transition-all"
        >
          <Send className="w-3.5 h-3.5" />
          <span>Submit Test</span>
        </button>
      </div>

      {/* Main Test Layout (Question Card on left, Palette on right) */}
      <div className="grid grid-cols-1 lg:grid-cols-4 gap-6 items-start">
        
        {/* Question Pane (Cols 1-3) */}
        <div className="lg:col-span-3 glass-panel rounded-3xl p-6 sm:p-8 space-y-6 border-slate-200 dark:border-slate-800 shadow-xl">
          {currentQ && (
            <>
              {/* Question Metadata */}
              <div className="flex items-center justify-between border-b border-slate-200 dark:border-slate-800/80 pb-4">
                <div className="flex items-center gap-2.5">
                  <span className="px-2.5 py-1 rounded-lg bg-blue-500/10 text-blue-600 dark:text-blue-400 border border-blue-500/20 text-xs font-bold">
                    Week {currentQ.assignmentWeek} • Question {currentQ.questionNumber}
                  </span>
                  <span className={`text-xs px-2.5 py-1 rounded-lg border font-medium ${
                    currentQ.type === 'multiple' 
                      ? 'bg-purple-500/10 text-purple-700 dark:text-purple-400 border-purple-500/30' 
                      : 'bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400 border-slate-200 dark:border-slate-700'
                  }`}>
                    {currentQ.type === 'multiple' ? 'Multiple Choice (MSQ)' : 'Single Choice (MCQ)'}
                  </span>
                </div>

                <button
                  onClick={() => toggleTestMarkReview(currentQ.id)}
                  className={`flex items-center gap-1.5 px-3 py-1.5 rounded-xl border text-xs font-medium transition-all ${
                    isMarked
                      ? 'bg-amber-500/20 border-amber-500/50 text-amber-700 dark:text-amber-300 font-bold'
                      : 'bg-slate-100 dark:bg-slate-900 border-slate-200 dark:border-slate-800 text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200'
                  }`}
                >
                  <Flag className="w-3.5 h-3.5" />
                  <span>{isMarked ? 'Marked for Review' : 'Mark for Review'}</span>
                </button>
              </div>

              {/* Prompt */}
              <div className="space-y-4">
                <h3 className="text-lg sm:text-xl font-semibold text-slate-900 dark:text-slate-100 leading-relaxed">
                  {currentQ.prompt}
                </h3>

                {currentQ.imageUrl && (
                  <div className="p-2 rounded-xl bg-slate-100 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 inline-block">
                    <img src={currentQ.imageUrl} alt="Question Diagram" className="max-h-72 rounded-lg object-contain" />
                  </div>
                )}
              </div>

              {/* Options */}
              <div className="space-y-3 pt-2">
                {currentQ.options.map((opt) => {
                  const isSelected = currentSelectedOptions.includes(opt.id);

                  return (
                    <button
                      key={opt.id}
                      onClick={() => handleSelectOption(opt.id)}
                      className={`w-full text-left p-4 rounded-2xl border transition-all flex items-start gap-4 ${
                        isSelected
                          ? 'border-blue-500 bg-blue-50 dark:bg-blue-950/40 text-blue-950 dark:text-blue-100 shadow-sm shadow-blue-500/20 font-medium'
                          : 'border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900/70 hover:border-slate-300 dark:hover:border-slate-700 hover:bg-slate-50 dark:hover:bg-slate-800/80 text-slate-800 dark:text-slate-300'
                      }`}
                    >
                      <div className={`w-7 h-7 rounded-lg flex items-center justify-center text-xs font-bold shrink-0 border transition-colors ${
                        isSelected
                          ? 'bg-blue-600 text-white border-blue-400'
                          : 'bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400 border-slate-300 dark:border-slate-700'
                      }`}>
                        {opt.id.toUpperCase()}
                      </div>
                      <span className="text-sm sm:text-base leading-relaxed pt-0.5">
                        {opt.text}
                      </span>
                    </button>
                  );
                })}
              </div>

              {/* Navigation & Clear Actions */}
              <div className="flex flex-wrap items-center justify-between gap-4 pt-6 border-t border-slate-200 dark:border-slate-800">
                <button
                  disabled={currentSelectedOptions.length === 0}
                  onClick={handleClearResponse}
                  className="px-3.5 py-2 rounded-xl text-xs font-medium text-slate-500 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-800 disabled:opacity-30 disabled:cursor-not-allowed transition-colors"
                >
                  Clear Response
                </button>

                <div className="flex items-center gap-2">
                  <button
                    disabled={(activeTestSession?.currentIndex || 0) === 0}
                    onClick={handlePrev}
                    className="flex items-center gap-1 px-4 py-2.5 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 disabled:opacity-40 disabled:cursor-not-allowed text-xs font-bold transition-colors"
                  >
                    <ChevronLeft className="w-4 h-4" />
                    <span>Previous</span>
                  </button>

                  <button
                    onClick={handleNext}
                    className="flex items-center gap-1 px-5 py-2.5 rounded-xl bg-blue-600 hover:bg-blue-500 text-white text-xs font-bold shadow-md shadow-blue-600/30 transition-all"
                  >
                    <span>Save & Next</span>
                    <ChevronRight className="w-4 h-4" />
                  </button>
                </div>
              </div>
            </>
          )}
        </div>

        {/* Question Palette (Col 4) */}
        <div className="glass-panel rounded-3xl p-5 border-slate-200 dark:border-slate-800 shadow-xl space-y-5">
          <div className="border-b border-slate-200 dark:border-slate-800 pb-3">
            <h4 className="text-xs font-bold text-slate-800 dark:text-slate-300 uppercase tracking-wide">
              Question Palette ({totalQuestions})
            </h4>
            
            {/* Status Legend */}
            <div className="grid grid-cols-2 gap-2 mt-3 text-[11px] text-slate-600 dark:text-slate-400">
              <div className="flex items-center gap-1.5">
                <span className="w-3 h-3 rounded-md bg-emerald-500" />
                <span>Answered ({answeredCount})</span>
              </div>
              <div className="flex items-center gap-1.5">
                <span className="w-3 h-3 rounded-md bg-slate-200 dark:bg-slate-800 border border-slate-300 dark:border-slate-700" />
                <span>Not Visited</span>
              </div>
              <div className="flex items-center gap-1.5">
                <span className="w-3 h-3 rounded-md bg-amber-500" />
                <span>Marked ({markedCount})</span>
              </div>
              <div className="flex items-center gap-1.5">
                <span className="w-3 h-3 rounded-md bg-rose-500/30 border border-rose-500" />
                <span>Unattempted ({unattemptedCount})</span>
              </div>
            </div>
          </div>

          {/* Numbers Grid */}
          <div className="grid grid-cols-5 gap-2 max-h-[380px] overflow-y-auto pr-1">
            {activeQuestionList.map((q, idx) => {
              const ans = activeTestSession?.answers[q.id] || [];
              const isAns = ans.length > 0;
              const isMkd = activeTestSession?.markedForReview.includes(q.id) || false;
              const isCurr = idx === activeTestSession?.currentIndex;

              let btnClass = 'bg-white dark:bg-slate-900 border-slate-200 dark:border-slate-800 text-slate-600 dark:text-slate-400 hover:border-slate-300 dark:hover:border-slate-700';

              if (isMkd) {
                btnClass = 'bg-amber-500/20 border-amber-500/60 text-amber-700 dark:text-amber-300 font-bold';
              } else if (isAns) {
                btnClass = 'bg-emerald-500/20 border-emerald-500/60 text-emerald-700 dark:text-emerald-300 font-bold';
              }

              if (isCurr) {
                btnClass += ' ring-2 ring-blue-500 ring-offset-2 ring-offset-white dark:ring-offset-slate-950';
              }

              return (
                <button
                  key={q.id}
                  onClick={() => setTestQuestionIndex(idx)}
                  className={`h-9 rounded-xl border text-xs font-semibold flex items-center justify-center transition-all ${btnClass}`}
                >
                  {idx + 1}
                </button>
              );
            })}
          </div>

          <div className="pt-2 border-t border-slate-200 dark:border-slate-800">
            <button
              onClick={cancelTest}
              className="w-full py-2 rounded-xl text-xs font-semibold text-rose-600 dark:text-rose-400 hover:bg-rose-50 dark:hover:bg-rose-950/30 transition-colors"
            >
              Exit Test
            </button>
          </div>
        </div>
      </div>

      {/* Submit Confirmation Modal */}
      {isSubmitModalOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-md">
          <div className="w-full max-w-md glass-panel rounded-3xl p-6 sm:p-8 space-y-6 border border-slate-200 dark:border-slate-700/80 shadow-2xl animate-in zoom-in-95">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 rounded-xl bg-amber-500/10 border border-amber-500/30 flex items-center justify-center text-amber-500 shrink-0">
                <AlertTriangle className="w-5 h-5" />
              </div>
              <div>
                <h3 className="text-lg font-bold text-slate-900 dark:text-white">Ready to Submit?</h3>
                <p className="text-xs text-slate-500 dark:text-slate-400">Review your attempt summary below:</p>
              </div>
            </div>

            <div className="grid grid-cols-3 gap-3 p-4 rounded-2xl bg-slate-50 dark:bg-slate-900/90 border border-slate-200 dark:border-slate-800 text-center">
              <div>
                <span className="text-xs text-slate-500 dark:text-slate-400 block">Answered</span>
                <strong className="text-base font-bold text-emerald-600 dark:text-emerald-400">{answeredCount}</strong>
              </div>
              <div>
                <span className="text-xs text-slate-500 dark:text-slate-400 block">Marked</span>
                <strong className="text-base font-bold text-amber-600 dark:text-amber-400">{markedCount}</strong>
              </div>
              <div>
                <span className="text-xs text-slate-500 dark:text-slate-400 block">Unattempted</span>
                <strong className="text-base font-bold text-rose-600 dark:text-rose-400">{unattemptedCount}</strong>
              </div>
            </div>

            <div className="flex items-center gap-3">
              <button
                onClick={() => setIsSubmitModalOpen(false)}
                className="flex-1 py-3 rounded-xl border border-slate-300 dark:border-slate-700 text-xs font-bold text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors"
              >
                Continue Test
              </button>
              <button
                onClick={handleFinalSubmit}
                className="flex-1 py-3 rounded-xl bg-blue-600 hover:bg-blue-500 text-xs font-bold text-white shadow-lg shadow-blue-600/30 transition-all"
              >
                Confirm Submit
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
