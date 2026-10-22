import React, { useState, useEffect } from 'react';
import { useQuizStore } from './store/useQuizStore';
import { Header } from './components/layout/Header';
import { Footer } from './components/layout/Footer';
import { ShortcutsModal } from './components/layout/ShortcutsModal';
import { StudyView } from './components/study/StudyView';
import { TestView } from './components/test/TestView';
import { MistakeNotebookView } from './components/mistakes/MistakeNotebookView';
import { ShortNotesView } from './components/notes/ShortNotesView';
import { AnalyticsView } from './components/analytics/AnalyticsView';

export const App: React.FC = () => {
  const { activeView, theme } = useQuizStore();
  const [isShortcutsOpen, setIsShortcutsOpen] = useState(false);

  // Sync dark class on mount and theme change
  useEffect(() => {
    if (theme === 'dark') {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }, [theme]);

  // Global listener for '?' key
  useEffect(() => {
    const handleGlobalKeyDown = (e: KeyboardEvent) => {
      if (['INPUT', 'TEXTAREA'].includes((e.target as HTMLElement)?.tagName)) return;
      if (e.key === '?') {
        setIsShortcutsOpen((prev) => !prev);
      }
    };
    window.addEventListener('keydown', handleGlobalKeyDown);
    return () => window.removeEventListener('keydown', handleGlobalKeyDown);
  }, []);

  return (
    <div className="min-h-screen flex flex-col bg-slate-50 dark:bg-slate-950 text-slate-900 dark:text-slate-100 transition-colors duration-200 selection:bg-blue-600 selection:text-white">
      <Header onOpenShortcuts={() => setIsShortcutsOpen(true)} />

      <main className="flex-1 w-full">
        {activeView === 'study' && <StudyView />}
        {activeView === 'test' && <TestView />}
        {activeView === 'mistakes' && <MistakeNotebookView />}
        {activeView === 'notes' && <ShortNotesView />}
        {activeView === 'analytics' && <AnalyticsView />}
      </main>

      <Footer />

      <ShortcutsModal
        isOpen={isShortcutsOpen}
        onClose={() => setIsShortcutsOpen(false)}
      />
    </div>
  );
};

export default App;
