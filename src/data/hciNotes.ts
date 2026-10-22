import { HciNote } from '../types/question';

export const HCI_NOTES: HciNote[] = [
  {
    id: 'fitts-law',
    title: "Fitts' Law (Movement Time Model)",
    category: 'Empirical Laws',
    weekReference: 3,
    summary: "Models the time required to rapidly move to a target area as a function of the distance to the target and the target's width.",
    formula: "MT = a + b \\cdot \\log_2\\left(\\frac{2D}{W}\\right) \\quad \\text{or} \\quad MT = a + b \\cdot \\log_2\\left(\\frac{D}{W} + 1\\right)",
    keyPoints: [
      "D = Distance (amplitude) to target center; W = Width of target along movement axis.",
      "Index of Difficulty (ID) = log2(2D/W) or Shannon formulation log2(D/W + 1), measured in bits.",
      "Index of Performance (IP) or Throughput (TP) = ID / MT (bits per second).",
      "Constants 'a' (start/stop intercept) and 'b' (slope) are empirical coefficients determined by linear regression.",
      "Screen corners and edges have effectively infinite width (W = ∞), making them the fastest clickable targets (Mac OS top menu bar)."
    ],
    examTip: "If distance D is doubled while target width W is also doubled, the Index of Difficulty ID remains identical!"
  },
  {
    id: 'hick-hyman-law',
    title: "Hick-Hyman Law (Choice Reaction Time)",
    category: 'Empirical Laws',
    weekReference: 3,
    summary: "Predicts the cognitive decision time required for a user to choose one alternative from a set of n equally probable options.",
    formula: "T = b \\cdot \\log_2(n + 1) \\quad \\text{or} \\quad T = b \\cdot \\sum p_i \\log_2\\left(\\frac{1}{p_i} + 1\\right)",
    keyPoints: [
      "Decision time increases logarithmically with the number of choices 'n'.",
      "Applies when users must identify or choose an option without prior training (novice scanning).",
      "For expert users who already know shortcuts or spatial layout, Hick's law does not apply—retrieval is direct recognition memory.",
      "Used to justify shallow menu hierarchies vs. excessively wide menus (grouping items into categories)."
    ],
    examTip: "Equal probability choices simplify Hick's formula to logarithmic growth. Grouping menus into meaningful sub-menus reduces search time."
  },
  {
    id: 'klm-goms',
    title: "KLM (Keystroke-Level Model) & GOMS",
    category: 'Cognitive Models',
    weekReference: 4,
    summary: "Card, Moran, and Newell's quantitative predictive model of task execution time for expert users performing routine cognitive and physical tasks.",
    formula: "T_{execute} = T_K + T_P + T_H + T_D + T_M + T_R",
    keyPoints: [
      "GOMS Components: Goals (what user wants), Operators (elementary perceptual/motor actions), Methods (sub-goal sequences), Selection Rules (rules deciding method).",
      "KLM Standard Operators & Times: K (Keystroke / press key: 0.2s - 0.28s), P (Point mouse to target: ~1.10s based on Fitts' law), H (Homing hands between keyboard & mouse: ~0.40s), D (Drawing straight lines), M (Mental preparation: ~1.35s), R (System response time).",
      "Rule for inserting 'M': Insert M in front of all K and P operators requiring cognitive decision, then apply heuristic pruning rules (e.g., remove M if next operator is anticipated)."
    ],
    examTip: "KLM only models expert task execution time without errors; it does not model problem solving, learning curve, or error recovery."
  },
  {
    id: 'normans-action-cycle',
    title: "Norman's 7 Stages of Action",
    category: 'Cognitive Models',
    weekReference: 2,
    summary: "Donald Norman's fundamental conceptual framework describing how humans translate mental goals into physical device actions and interpret the results.",
    keyPoints: [
      "Stage 1: Forming the Goal (Mental intent).",
      "Execution Phase (Bridge to world): 2. Forming the Intention, 3. Specifying the Action Sequence, 4. Executing the Action.",
      "Evaluation Phase (Bridge from world): 5. Perceiving the World State, 6. Interpreting the Perception, 7. Evaluating Outcome against the original Goal.",
      "Gulf of Execution: Distance between user's internal goals and allowable physical actions on the system ('How do I do it?').",
      "Gulf of Evaluation: Distance between system's physical presentation and user's mental interpretation ('What did it just do?')."
    ],
    examTip: "Feedforward bridges the Gulf of Execution (signifiers, affordances). Feedback bridges the Gulf of Evaluation (status indicators, sounds, visuals)."
  },
  {
    id: 'norman-design-principles',
    title: "Norman's Core Design Concepts",
    category: 'Design Principles',
    weekReference: 2,
    summary: "Six foundational principles for intuitive, error-resistant everyday and interactive systems.",
    keyPoints: [
      "Affordance: The fundamental actual and perceived properties of an artifact that determine how it can possibly be used (e.g., a chair affords sitting, a button affords pressing).",
      "Signifier: Any perceivable indicator that communicates where action should take place (e.g., 'Push' sign on a door, embossed bevel on a button).",
      "Mapping: The relationship between controls and their movements vs. the resulting effect in the real world (e.g., stove burners mapped spatially to stove knobs).",
      "Feedback: Sending information back to the user about what action has actually been done and what result was achieved.",
      "Constraints: Physical, semantic, cultural, and logical limits that restrict possible user actions to prevent errors.",
      "Conceptual Model: The user's internal mental model of how the system operates under the hood."
    ],
    examTip: "Affordances exist even if invisible; Signifiers are deliberately visible signals showing where and how to interact."
  },
  {
    id: 'nielsen-heuristics',
    title: "Nielsen's 10 Usability Heuristics",
    category: 'Evaluation & Usability',
    weekReference: 6,
    summary: "Jacob Nielsen's ten broad rules of thumb for user interface design and discount heuristic evaluation.",
    keyPoints: [
      "1. Visibility of system status (timely feedback within reasonable time).",
      "2. Match between system and the real world (user's language, familiar concepts).",
      "3. User control and freedom (emergency exit, undo/redo).",
      "4. Consistency and standards (platform conventions, same words for same actions).",
      "5. Error prevention (eliminate error-prone conditions or confirm before action).",
      "6. Recognition rather than recall (make objects, actions, options visible).",
      "7. Flexibility and efficiency of use (accelerators, keyboard shortcuts for experts).",
      "8. Aesthetic and minimalist design (no irrelevant or rarely needed info).",
      "9. Help users recognize, diagnose, and recover from errors (plain language, constructive solution).",
      "10. Help and documentation (searchable, concrete steps, concise)."
    ],
    examTip: "Heuristic evaluation typically requires 3 to 5 independent evaluators to find ~75-80% of usability problems."
  },
  {
    id: 'shneiderman-rules',
    title: "Shneiderman's 8 Golden Rules of Interface Design",
    category: 'Design Principles',
    weekReference: 5,
    summary: "Ben Shneiderman's universal principles derived from empirical experience with interactive systems.",
    keyPoints: [
      "1. Strive for consistency (identical terminology, layouts, fonts, icons).",
      "2. Seek universal usability (cater to novices and experts, diverse abilities).",
      "3. Offer informative feedback (substantial feedback for major actions).",
      "4. Design dialogs to yield closure (sequences organized into beginning, middle, and end).",
      "5. Prevent errors (gray out invalid options, validate form inputs inline).",
      "6. Permit easy reversal of actions (relieves anxiety, encourages exploration).",
      "7. Support internal locus of control (users initiate actions, not the system surprising them).",
      "8. Reduce short-term memory load (humans can only retain 7 ± 2 chunks of info)."
    ],
    examTip: "Closure provides satisfaction of accomplishment and signals the user to drop contingency plans from memory."
  },
  {
    id: 'usability-metrics',
    title: "Usability Metrics & System Usability Scale (SUS)",
    category: 'Evaluation & Usability',
    weekReference: 7,
    summary: "ISO 9241-11 quantitative measurement dimensions: Effectiveness, Efficiency, and Satisfaction.",
    formula: "SUS = 2.5 \\times \\left( \\sum (Q_{odd} - 1) + \\sum (5 - Q_{even}) \\right)",
    keyPoints: [
      "Effectiveness: Task completion rate (%), error frequency.",
      "Efficiency: Time-on-task, time-to-first-click, cognitive workload.",
      "Satisfaction: Subjective ratings via standardized questionnaires (SUS, NASA-TLX, QUIS, CSUQ).",
      "SUS Scoring: 10 questions on a 5-point Likert scale (1 to 5). For odd questions (1, 3, 5, 7, 9), subtract 1. For even questions (2, 4, 6, 8, 10), subtract rating from 5. Sum all converted values and multiply by 2.5. Range is 0 to 100.",
      "Average industry benchmark for SUS is 68. Scores > 80 represent excellent usability."
    ],
    examTip: "A SUS score of 68 is the 50th percentile (Grade C). An 80+ is Grade A."
  },
  {
    id: 'experimental-design',
    title: "Empirical Evaluation & Experimental Design",
    category: 'Evaluation & Usability',
    weekReference: 8,
    summary: "Rigorous scientific evaluation methodologies for comparing interface designs and input techniques.",
    keyPoints: [
      "Independent Variables (IV): Factors manipulated by the experimenter (e.g., interface type A vs B, mouse vs touchpad).",
      "Dependent Variables (DV): Metrics measured to test the hypothesis (e.g., task completion time, error count, subjective rating).",
      "Between-Subjects Design: Each participant tests ONLY one condition. Advantage: No learning/carryover effects. Disadvantage: Requires more participants; high individual variability.",
      "Within-Subjects Design: Every participant tests ALL conditions. Advantage: Fewer participants required; higher statistical power. Disadvantage: Order effects and fatigue (mitigated by Latin Square counterbalancing).",
      "Null Hypothesis ($H_0$): Assumes no significant difference between conditions. p-value < 0.05 rejects $H_0$."
    ],
    examTip: "Counterbalancing is essential in within-subjects experiments to neutralize learning effects across test conditions."
  },
  {
    id: 'interaction-styles',
    title: "Interaction Styles & Dialog Design",
    category: 'Interaction Styles',
    weekReference: 9,
    summary: "Primary paradigms through which users communicate intent to a computer system.",
    keyPoints: [
      "1. Command Line Interface (CLI): High expert efficiency, low cognitive screen space, but steep learning curve (recall over recognition).",
      "2. Menu-Driven Interface: Fast learning for novices (recognition over recall), structured options, but slow navigation for experts.",
      "3. Direct Manipulation: Coined by Shneiderman; continuous representation of objects, rapid reversible incremental actions, direct physical interaction instead of syntax.",
      "4. Form Fill-in: Ideal for structured data entry; requires clear field labels, logical tab order, inline validation.",
      "5. Natural Language: Flexible, hands-free (voice UI), but high ambiguity and failure to convey system boundary/capabilities."
    ],
    examTip: "Direct manipulation delivers immediate visual feedback and syntactic correctness (impossible actions are physically restricted)."
  }
];
