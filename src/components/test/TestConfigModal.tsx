import React, { useState } from 'react';
import { useQuizStore } from '../../store/useQuizStore';
import { Clock, Play, Shuffle, CheckSquare, Square, X } from 'lucide-react';

interface TestConfigModalProps {
  isOpen: boolean;
  onClose: () => void;
}

export const TestConfigModal: React.FC<TestConfigModalProps> = ({ isOpen, onClose }) => {
  const { startTest } = useQuizStore();

  const [selectedWeeks, setSelectedWeeks] = useState<number[]>(
    Array.from({ length: 12 }, (_, i) => i + 1)
  );
  const [questionCount, setQuestionCount] = useState<number>(120);
  const [timerMinutes, setTimerMinutes] = useState<number | null>(60);
  const [shuffleQuestions, setShuffleQuestions] = useState<boolean>(true);

  if (!isOpen) return null;

  const toggleWeek = (week: number) => {
    setSelectedWeeks((prev) =>
      prev.includes(week) ? prev.filter((w) => w !== week) : [...prev, week]
    );
  };

  const selectAllWeeks = () => {
    setSelectedWeeks(Array.from({ length: 12 }, (_, i) => i + 1));
  };

  const deselectAllWeeks = () => {
    setSelectedWeeks([]);
  };

  const handleStart = () => {
    if (selectedWeeks.length === 0) return;
    const maxPossible = selectedWeeks.length * 10;
    const count = Math.min(questionCount, maxPossible);
    startTest(selectedWeeks, count, timerMinutes, shuffleQuestions);
    onClose();
  };

  const maxAvailable = selectedWeeks.length * 10;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-md">
      <div className="w-full max-w-xl glass-panel rounded-3xl p-6 sm:p-8 space-y-6 border border-slate-200 dark:border-slate-700/80 shadow-2xl relative animate-in fade-in zoom-in-95 duration-200">
        
        {/* Header */}
        <div className="flex items-center justify-between border-b border-slate-200 dark:border-slate-800 pb-4">
          <div>
            <h2 className="text-xl font-bold text-slate-900 dark:text-white tracking-tight">Configure Mock Test</h2>
            <p className="text-xs text-slate-500 dark:text-slate-400 mt-1">
              Test your exam readiness with authentic NPTEL assignment MCQs & MSQs.
            </p>
          </div>
          <button
            onClick={onClose}
            className="p-2 rounded-xl text-slate-400 hover:text-slate-900 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Week Selection */}
        <div className="space-y-3">
          <div className="flex items-center justify-between">
            <label className="text-xs font-bold text-slate-700 dark:text-slate-300 uppercase tracking-wide">
              Select Assignment Weeks ({selectedWeeks.length}/12)
            </label>
            <div className="flex items-center gap-3 text-xs">
              <button
                type="button"
                onClick={selectAllWeeks}
                className="text-blue-600 dark:text-blue-400 hover:underline font-medium"
              >
                Select All
              </button>
              <span className="text-slate-400 dark:text-slate-600">•</span>
              <button
                type="button"
                onClick={deselectAllWeeks}
                className="text-slate-500 dark:text-slate-400 hover:underline font-medium"
              >
                Clear
              </button>
            </div>
          </div>

          <div className="grid grid-cols-3 sm:grid-cols-4 gap-2">
            {Array.from({ length: 12 }, (_, i) => i + 1).map((week) => {
              const isChecked = selectedWeeks.includes(week);
              return (
                <button
                  key={week}
                  type="button"
                  onClick={() => toggleWeek(week)}
                  className={`flex items-center justify-between px-3 py-2 rounded-xl border text-xs font-semibold transition-all ${
                    isChecked
                      ? 'bg-blue-500/15 border-blue-500 text-blue-700 dark:text-blue-300 font-bold'
                      : 'bg-white dark:bg-slate-900 border-slate-200 dark:border-slate-800 text-slate-600 dark:text-slate-400 hover:border-slate-300 dark:hover:border-slate-700'
                  }`}
                >
                  <span>Week {week}</span>
                  {isChecked ? (
                    <CheckSquare className="w-3.5 h-3.5 text-blue-600 dark:text-blue-400 shrink-0" />
                  ) : (
                    <Square className="w-3.5 h-3.5 text-slate-400 dark:text-slate-600 shrink-0" />
                  )}
                </button>
              );
            })}
          </div>
        </div>

        {/* Question Count & Presets */}
        <div className="space-y-3">
          <label className="text-xs font-bold text-slate-700 dark:text-slate-300 uppercase tracking-wide">
            Number of Questions: <strong className="text-blue-600 dark:text-blue-400">{Math.min(questionCount, maxAvailable)}</strong>
          </label>
          <div className="flex items-center gap-2">
            {[10, 20, 30, 60, 120].map((num) => (
              <button
                key={num}
                type="button"
                onClick={() => setQuestionCount(num)}
                className={`flex-1 py-1.5 rounded-xl text-xs font-bold transition-all border ${
                  questionCount === num
                    ? 'bg-blue-600 border-blue-500 text-white'
                    : 'bg-white dark:bg-slate-900 border-slate-200 dark:border-slate-800 text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
                }`}
              >
                {num === 120 ? 'All 120' : num}
              </button>
            ))}
          </div>
        </div>

        {/* Time Limit */}
        <div className="space-y-3">
          <label className="text-xs font-bold text-slate-700 dark:text-slate-300 uppercase tracking-wide flex items-center gap-1.5">
            <Clock className="w-4 h-4 text-slate-400" />
            Timer Duration
          </label>
          <div className="grid grid-cols-4 gap-2">
            {[
              { label: 'Untimed', value: null },
              { label: '30 Mins', value: 30 },
              { label: '60 Mins', value: 60 },
              { label: '90 Mins', value: 90 },
            ].map((t) => (
              <button
                key={t.label}
                type="button"
                onClick={() => setTimerMinutes(t.value)}
                className={`py-2 rounded-xl text-xs font-bold transition-all border ${
                  timerMinutes === t.value
                    ? 'bg-indigo-600 border-indigo-500 text-white'
                    : 'bg-white dark:bg-slate-900 border-slate-200 dark:border-slate-800 text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
                }`}
              >
                {t.label}
              </button>
            ))}
          </div>
        </div>

        {/* Shuffle Option */}
        <div className="flex items-center justify-between p-3 rounded-2xl bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800">
          <div className="flex items-center gap-2.5">
            <Shuffle className="w-4 h-4 text-blue-600 dark:text-blue-400" />
            <div>
              <div className="text-xs font-semibold text-slate-800 dark:text-slate-200">Shuffle Question Order</div>
              <div className="text-[11px] text-slate-500 dark:text-slate-400">Randomizes presentation sequence</div>
            </div>
          </div>
          <input
            type="checkbox"
            checked={shuffleQuestions}
            onChange={(e) => setShuffleQuestions(e.target.checked)}
            className="w-4 h-4 text-blue-600 rounded bg-white dark:bg-slate-800 border-slate-300 dark:border-slate-700"
          />
        </div>

        {/* Start Button */}
        <div className="pt-2">
          <button
            type="button"
            disabled={selectedWeeks.length === 0}
            onClick={handleStart}
            className={`w-full py-3.5 rounded-2xl font-bold text-sm tracking-wide flex items-center justify-center gap-2 transition-all shadow-lg ${
              selectedWeeks.length > 0
                ? 'bg-blue-600 hover:bg-blue-500 text-white shadow-blue-600/30 hover:scale-[1.01]'
                : 'bg-slate-200 dark:bg-slate-800 text-slate-400 dark:text-slate-600 cursor-not-allowed'
            }`}
          >
            <Play className="w-4 h-4 fill-white" />
            <span>Start Test Session</span>
          </button>
        </div>
      </div>
    </div>
  );
};
