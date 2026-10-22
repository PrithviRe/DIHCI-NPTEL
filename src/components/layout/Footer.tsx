import React, { useState } from 'react';
import { useQuizStore } from '../../store/useQuizStore';
import { RotateCcw, AlertTriangle } from 'lucide-react';

export const Footer: React.FC = () => {
  const { resetAllStudyProgress, clearMistakes, clearTestHistory } = useQuizStore();
  const [isResetConfirmOpen, setIsResetConfirmOpen] = useState(false);

  const handleFullReset = () => {
    resetAllStudyProgress();
    clearMistakes();
    clearTestHistory();
    setIsResetConfirmOpen(false);
  };

  return (
    <footer className="w-full border-t border-slate-200 dark:border-slate-900 bg-white/80 dark:bg-slate-950/80 py-8 mt-16 text-slate-500 text-xs transition-colors">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col sm:flex-row items-center justify-between gap-4">
        
        <div className="space-y-1 text-center sm:text-left">
          <p className="text-slate-600 dark:text-slate-400 font-medium">
            NPTEL Course <span className="text-blue-600 dark:text-blue-400 font-bold">noc26_cs177</span>: Design & Implementation of Human-Computer Interfaces
          </p>
          <p className="text-[11px] text-slate-500">
            Prof. Samit Bhattacharya • Department of Computer Science & Engineering, IIT Guwahati
          </p>
        </div>

        <div className="flex items-center gap-4">
          <button
            onClick={() => setIsResetConfirmOpen(true)}
            className="flex items-center gap-1.5 text-slate-500 hover:text-rose-600 dark:hover:text-rose-400 text-xs transition-colors"
          >
            <RotateCcw className="w-3.5 h-3.5" />
            <span>Reset All Progress</span>
          </button>
        </div>
      </div>

      {isResetConfirmOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-md">
          <div className="w-full max-w-sm glass-panel rounded-3xl p-6 space-y-5 border border-slate-200 dark:border-slate-700 shadow-2xl text-center">
            <div className="w-12 h-12 rounded-2xl bg-rose-500/10 text-rose-500 flex items-center justify-center mx-auto">
              <AlertTriangle className="w-6 h-6" />
            </div>

            <div className="space-y-1.5">
              <h4 className="text-base font-bold text-slate-900 dark:text-white">Reset All Practice Data?</h4>
              <p className="text-xs text-slate-500 dark:text-slate-400">
                This will clear your study attempts, mistake notebook, and mock test scores. This cannot be undone.
              </p>
            </div>

            <div className="flex items-center gap-2 pt-2">
              <button
                onClick={() => setIsResetConfirmOpen(false)}
                className="flex-1 py-2.5 rounded-xl border border-slate-300 dark:border-slate-700 text-xs font-semibold text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800"
              >
                Cancel
              </button>
              <button
                onClick={handleFullReset}
                className="flex-1 py-2.5 rounded-xl bg-rose-600 hover:bg-rose-500 text-xs font-bold text-white shadow-md shadow-rose-600/30"
              >
                Reset Data
              </button>
            </div>
          </div>
        </div>
      )}
    </footer>
  );
};
