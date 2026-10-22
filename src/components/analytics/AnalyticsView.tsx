import React, { useMemo } from 'react';
import { useQuizStore } from '../../store/useQuizStore';
import { 
  BarChart3, 
  Trophy, 
  Calendar, 
  Download, 
  Layers,
  ArrowRight
} from 'lucide-react';

export const AnalyticsView: React.FC = () => {
  const { 
    questions, 
    studyAttempts, 
    mistakeIds, 
    testHistory, 
    clearTestHistory, 
    setLastTestSession,
    setActiveView 
  } = useQuizStore();

  const totalQuestions = questions.length; // 120
  const masteredCount = Object.values(studyAttempts).filter((a) => a.isCorrect).length;
  const attemptedCount = Object.keys(studyAttempts).length;
  const masteryPercentage = Math.round((masteredCount / totalQuestions) * 100);

  // Week-by-Week Progress Map
  const weekProgress = useMemo(() => {
    const map = new Map<number, { total: number; mastered: number; attempted: number }>();
    for (let w = 1; w <= 12; w++) {
      map.set(w, { total: 0, mastered: 0, attempted: 0 });
    }

    questions.forEach((q) => {
      const stats = map.get(q.assignmentWeek);
      if (stats) {
        stats.total += 1;
        const att = studyAttempts[q.id];
        if (att) {
          stats.attempted += 1;
          if (att.isCorrect) stats.mastered += 1;
        }
      }
    });

    return map;
  }, [questions, studyAttempts]);

  // Average test score
  const avgTestPercentage = useMemo(() => {
    if (testHistory.length === 0) return 0;
    const sum = testHistory.reduce((acc, t) => acc + t.percentage, 0);
    return Math.round(sum / testHistory.length);
  }, [testHistory]);

  const handleExportData = () => {
    const exportObj = {
      timestamp: Date.now(),
      masteredCount,
      totalQuestions,
      studyAttempts,
      mistakeIds,
      testHistory,
    };
    const blob = new Blob([JSON.stringify(exportObj, null, 2)], { type: 'application/json' });
    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = `dihci_practice_backup_${new Date().toISOString().slice(0, 10)}.json`;
    document.body.appendChild(a);
    a.click();
    a.remove();
  };

  return (
    <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8 animate-in fade-in duration-300">
      
      {/* Top Banner */}
      <div className="glass-panel rounded-3xl p-6 sm:p-8 border-slate-200 dark:border-slate-800 shadow-2xl flex flex-col sm:flex-row items-center justify-between gap-6">
        <div className="flex items-center gap-4 text-center sm:text-left">
          <div className="w-14 h-14 rounded-2xl bg-blue-500/10 border border-blue-500/20 text-blue-600 dark:text-blue-400 flex items-center justify-center shrink-0 shadow-lg shadow-blue-500/10">
            <BarChart3 className="w-7 h-7" />
          </div>
          <div>
            <h1 className="text-2xl font-extrabold text-slate-900 dark:text-white tracking-tight">Performance Analytics</h1>
            <p className="text-xs sm:text-sm text-slate-600 dark:text-slate-400 mt-1">
              Track your course completion rate, mastery percentage, and mock test trends.
            </p>
          </div>
        </div>

        <button
          onClick={handleExportData}
          className="flex items-center gap-2 px-4 py-2.5 rounded-xl border border-slate-200 dark:border-slate-700 hover:border-slate-300 dark:hover:border-slate-600 bg-white dark:bg-slate-900 text-slate-700 dark:text-slate-300 text-xs font-semibold hover:text-slate-900 dark:hover:text-white transition-colors shrink-0 shadow-sm"
        >
          <Download className="w-4 h-4 text-blue-600 dark:text-blue-400" />
          <span>Export Progress JSON</span>
        </button>
      </div>

      {/* KPI Cards */}
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
        <div className="glass-panel rounded-3xl p-5 border-slate-200 dark:border-slate-800 space-y-2">
          <span className="text-xs font-bold text-slate-500 dark:text-slate-400 uppercase tracking-wider block">
            Overall Mastery
          </span>
          <div className="text-3xl font-extrabold text-emerald-600 dark:text-emerald-400">
            {masteryPercentage}%
          </div>
          <span className="text-xs text-slate-500">
            {masteredCount} of {totalQuestions} questions
          </span>
        </div>

        <div className="glass-panel rounded-3xl p-5 border-slate-200 dark:border-slate-800 space-y-2">
          <span className="text-xs font-bold text-slate-500 dark:text-slate-400 uppercase tracking-wider block">
            Attempted
          </span>
          <div className="text-3xl font-extrabold text-blue-600 dark:text-blue-400">
            {attemptedCount}
          </div>
          <span className="text-xs text-slate-500">
            {totalQuestions - attemptedCount} unattempted
          </span>
        </div>

        <div className="glass-panel rounded-3xl p-5 border-slate-200 dark:border-slate-800 space-y-2">
          <span className="text-xs font-bold text-slate-500 dark:text-slate-400 uppercase tracking-wider block">
            Active Mistakes
          </span>
          <div className="text-3xl font-extrabold text-rose-600 dark:text-rose-400">
            {mistakeIds.length}
          </div>
          <span className="text-xs text-slate-500">
            In Mistake Notebook
          </span>
        </div>

        <div className="glass-panel rounded-3xl p-5 border-slate-200 dark:border-slate-800 space-y-2">
          <span className="text-xs font-bold text-slate-500 dark:text-slate-400 uppercase tracking-wider block">
            Avg Mock Test Score
          </span>
          <div className="text-3xl font-extrabold text-indigo-600 dark:text-indigo-400">
            {avgTestPercentage}%
          </div>
          <span className="text-xs text-slate-500">
            Across {testHistory.length} test sessions
          </span>
        </div>
      </div>

      {/* Assignment Week Matrix */}
      <div className="glass-panel rounded-3xl p-6 sm:p-8 border-slate-200 dark:border-slate-800 shadow-xl space-y-6">
        <div className="flex items-center gap-2 border-b border-slate-200 dark:border-slate-800 pb-3">
          <Layers className="w-5 h-5 text-blue-600 dark:text-blue-400" />
          <h2 className="text-base font-bold text-slate-900 dark:text-white tracking-tight">
            Week-by-Week Mastery (Assignments 1 to 12)
          </h2>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          {Array.from({ length: 12 }, (_, i) => i + 1).map((week) => {
            const stats = weekProgress.get(week) || { total: 10, mastered: 0, attempted: 0 };
            const pct = Math.round((stats.mastered / (stats.total || 1)) * 100);

            return (
              <div
                key={week}
                className="p-4 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-2.5 shadow-sm"
              >
                <div className="flex items-center justify-between text-xs font-bold">
                  <span className="text-slate-800 dark:text-slate-200">Assignment {week}</span>
                  <span className={pct === 100 ? 'text-emerald-600 dark:text-emerald-400' : pct >= 50 ? 'text-blue-600 dark:text-blue-400' : 'text-slate-500 dark:text-slate-400'}>
                    {stats.mastered} / {stats.total} Mastered
                  </span>
                </div>

                {/* Progress Bar */}
                <div className="w-full h-2 rounded-full bg-slate-100 dark:bg-slate-800 overflow-hidden">
                  <div
                    className={`h-full rounded-full transition-all duration-300 ${
                      pct === 100
                        ? 'bg-emerald-500'
                        : pct >= 50
                        ? 'bg-blue-500'
                        : 'bg-indigo-500'
                    }`}
                    style={{ width: `${pct}%` }}
                  />
                </div>

                <div className="flex items-center justify-between text-[11px] text-slate-500">
                  <span>{stats.attempted} attempted</span>
                  <span>{pct}%</span>
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {/* Mock Test History */}
      <div className="glass-panel rounded-3xl p-6 sm:p-8 border-slate-200 dark:border-slate-800 shadow-xl space-y-6">
        <div className="flex items-center justify-between border-b border-slate-200 dark:border-slate-800 pb-3">
          <div className="flex items-center gap-2">
            <Trophy className="w-5 h-5 text-indigo-600 dark:text-indigo-400" />
            <h2 className="text-base font-bold text-slate-900 dark:text-white tracking-tight">Mock Test History</h2>
          </div>

          {testHistory.length > 0 && (
            <button
              onClick={clearTestHistory}
              className="text-xs text-rose-600 dark:text-rose-400 hover:text-rose-700 dark:hover:text-rose-300 transition-colors"
            >
              Clear History
            </button>
          )}
        </div>

        {testHistory.length > 0 ? (
          <div className="overflow-x-auto">
            <table className="w-full text-left text-xs text-slate-700 dark:text-slate-300">
              <thead className="bg-slate-100 dark:bg-slate-900/90 text-slate-500 dark:text-slate-400 font-bold uppercase tracking-wider border-b border-slate-200 dark:border-slate-800">
                <tr>
                  <th className="py-3 px-4">Date</th>
                  <th className="py-3 px-4">Score</th>
                  <th className="py-3 px-4">Accuracy</th>
                  <th className="py-3 px-4">Weeks</th>
                  <th className="py-3 px-4">Time</th>
                  <th className="py-3 px-4 text-right">Action</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-200 dark:divide-slate-800">
                {testHistory.map((sess) => (
                  <tr key={sess.id} className="hover:bg-slate-50 dark:hover:bg-slate-900/50 transition-colors">
                    <td className="py-3.5 px-4 font-medium text-slate-900 dark:text-white flex items-center gap-2">
                      <Calendar className="w-3.5 h-3.5 text-slate-400 dark:text-slate-500" />
                      <span>{sess.date}</span>
                    </td>
                    <td className="py-3.5 px-4 font-bold text-slate-900 dark:text-white">
                      {sess.score} / {sess.maxScore}
                    </td>
                    <td className="py-3.5 px-4">
                      <span className={`px-2 py-0.5 rounded-full font-bold text-[10px] ${
                        sess.percentage >= 80
                          ? 'bg-emerald-500/20 text-emerald-700 dark:text-emerald-400'
                          : sess.percentage >= 50
                          ? 'bg-blue-500/20 text-blue-700 dark:text-blue-400'
                          : 'bg-rose-500/20 text-rose-700 dark:text-rose-400'
                      }`}>
                        {sess.percentage}%
                      </span>
                    </td>
                    <td className="py-3.5 px-4 text-slate-500 dark:text-slate-400">
                      {sess.assignmentWeeks.length === 12
                        ? 'All 12 Weeks'
                        : `Weeks ${sess.assignmentWeeks.join(', ')}`}
                    </td>
                    <td className="py-3.5 px-4 text-slate-500 dark:text-slate-400">
                      {Math.floor(sessionTime(sess.timeSpentSeconds) / 60)}m {sess.timeSpentSeconds % 60}s
                    </td>
                    <td className="py-3.5 px-4 text-right">
                      <button
                        onClick={() => {
                          setLastTestSession(sess);
                          setActiveView('test');
                        }}
                        className="text-blue-600 dark:text-blue-400 hover:text-blue-700 dark:hover:text-blue-300 font-bold text-xs inline-flex items-center gap-1"
                      >
                        <span>Review</span>
                        <ArrowRight className="w-3 h-3" />
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        ) : (
          <div className="text-center py-12 text-slate-400 text-xs">
            No mock tests completed yet. Take a test in Test Mode to see performance trends here!
          </div>
        )}
      </div>
    </div>
  );
};

function sessionTime(sec: number) {
  return isNaN(sec) ? 0 : sec;
}
