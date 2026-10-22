import json

with open('src/data/questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# Comprehensive academic explanations for all 120 questions
explanations = {
    # WEEK 1
    "w1_q1": {
        "correct": "Option D (2011 onwards) is correct because in the historical evolution of interactive computing taught in the course, computing eras are segmented into: pre-1985 (batch/mainframe), 1985-1998 (GUI and desktop PC), 1998-2007 (Internet and web age), 2007-2011 (mobile revolution), and 2011 onwards representing the 'modern age' of ubiquitous, cloud-connected, wearable, and AI-assisted smart computing devices.",
        "why_others_wrong": "Options A, B, and C represent earlier transitional milestones (1985 ushered in commercial desktop GUIs; 1998 marked ubiquitous web/browser adoption; 2007 launched the modern multi-touch smartphone era), not the 'modern age'.",
        "context": "Understanding the evolutionary timeline highlights how user expectations shifted from system-centric batch processing to seamless, context-aware ubiquitous interaction."
    },
    "w1_q2": {
        "correct": "Option B ('Super knowledgeable') is correct because it is NOT a recognized generic user category in HCI literature. The three foundational categories of users established by Ben Shneiderman and standard HCI taxonomy are: Novice (first-time/unfamiliar), Intermittent (casual/occasional with knowledge decay), and Expert (frequent, power users seeking high efficiency).",
        "why_others_wrong": "Options A, C, and D are the classic standard user categories defined across software engineering and interaction design.",
        "context": "Different user categories require distinct interface accommodations: novices need visible constraints and signifiers, intermittent users need clear recognition cues, and experts need shortcuts and accelerators."
    },
    "w1_q3": {
        "correct": "Option C is correct because the Second Quadrant of Barry Boehm's Spiral Model is dedicated specifically to 'Risk Analysis and Prototyping'. For interactive software, usability risks (unclear requirements, cognitive mismatch, navigation friction) are the most dangerous hazards, and rapid prototyping in this quadrant resolves them before expensive coding begins.",
        "why_others_wrong": "Option A (UI layout definition) occurs during design/development in Quadrant 3. Option B (finalizing architecture) is an architectural engineering task. Option D (testing and deployment) belongs to Quadrants 3 and 4.",
        "context": "The 4 Spiral Model quadrants are: 1. Determine Objectives, 2. Identify & Mitigate Risks (Prototyping), 3. Develop & Verify (Build), 4. Customer Evaluation & Plan next cycle."
    },
    "w1_q4": {
        "correct": "Option C is correct because 'Utility' in software engineering refers to whether the software provides the features, functionalities, and capabilities that users actually require to accomplish their tasks. Usability, by contrast, is whether users can execute those features easily and pleasantly.",
        "why_others_wrong": "Option A relates to efficiency (a usability metric). Option B relates to visual aesthetics. Option D relates to maintenance release cadence.",
        "context": "Utility + Usability = Usefulness. A system can have high usability (easy to click and navigate) but zero utility (does not do what the user needs)."
    },
    "w1_q5": {
        "correct": "Option D ('None of the above') is correct because every single device listed (Desktop, Digital Pedometer, Smartphone) is indeed an interactive computer. All three contain processing units, memory, input sensors/buttons, and output displays to perform computational tasks.",
        "why_others_wrong": "Desktops, digital pedometers, and smartphones all qualify as computers under modern embedded and ubiquitous computing definitions.",
        "context": "Modern HCI encompasses embedded systems, wearables (pedometers), and mobile terminals, moving far beyond traditional desktop computing."
    },
    "w1_q6": {
        "correct": "Option B ('Iterative') is correct because interactive software development requires continuous cycles of Design, Prototype, and Evaluate. Human cognitive needs and behavioral nuances cannot be completely predicted upfront; they emerge and get refined through iterative user exposure.",
        "why_others_wrong": "Sporadic implies random or disorganized efforts. Variable and discrete do not describe the cyclical feedback loops inherent to user-centered software engineering.",
        "context": "Iterative design is the cornerstone of User-Centered Design (UCD) as codified in ISO 9241-210."
    },
    "w1_q7": {
        "correct": "Option D ('Memorization') is correct because it is NOT one of Nielsen's five quality components. Jakob Nielsen's five usability attributes are: Learnability, Efficiency, Memorability (the ease of re-establishing proficiency after a period of non-use), Errors, and Satisfaction.",
        "why_others_wrong": "Learnability (Option A), Efficiency (Option B), and Satisfaction (Option C) are official pillars of Nielsen's usability framework. 'Memorability' is the official term, not 'Memorization'.",
        "context": "Memorability measures how easily a casual or intermittent user can return to the design without having to learn everything from scratch."
    },
    "w1_q8": {
        "correct": "Option B ('Learnability study') is correct because classical Waterfall models do not include a 'learnability study' phase. The traditional linear phases of the Waterfall model are: Feasibility study, Requirements analysis and specification, Design, Coding and unit testing, Integration and system testing, and Maintenance.",
        "why_others_wrong": "Feasibility study (Option A), System integration and testing (Option C), and Maintenance (Option D) are standard textbook phases of the classic Waterfall lifecycle.",
        "context": "The Waterfall model's lack of explicit usability/learnability phases is the primary reason why User-Centered Design and Agile models superseded it for interactive systems."
    },
    "w1_q9": {
        "correct": "Option A ('First, Fourth') is correct because Quadrant 1 (top-left) of the Spiral Model is dedicated to 'Identify Objectives, alternatives, and constraints', while Quadrant 4 (bottom-left) is dedicated to 'Customer evaluation, review, and planning of the next phase'.",
        "why_others_wrong": "Quadrant 2 is Risk Analysis/Prototyping, and Quadrant 3 is Engineering/Coding/Testing.",
        "context": "Boehm's Spiral Model progresses clockwise through: Q1 (Objectives) -> Q2 (Risk/Prototyping) -> Q3 (Development) -> Q4 (Evaluation/Planning)."
    },
    "w1_q10": {
        "correct": "Option A ('System-Centered Design') is correct because System-Centered Design focuses predominantly on system capabilities, hardware efficiency, or what developers find technically interesting or convenient to construct, rather than focusing on end-user psychology and needs.",
        "why_others_wrong": "User-Centered Design (Option B) prioritizes user goals and cognitive constraints. Participatory Design (Option D) actively involves end-users in the co-design process.",
        "context": "System-Centered Design historically caused severe usability catastrophes because users were expected to adapt unnaturally to internal machine architectures."
    },

    # WEEK 2
    "w2_q1": {
        "correct": "Option C ('Semi-structured interview') is correct because Contextual Inquiry is fundamentally a semi-structured interview method conducted in-situ (the user's actual workplace) combined with contextual observation, where the interviewer follows an open guide while probing deeper into observed user behaviors.",
        "why_others_wrong": "Pure interviews (Option A) lack real-time workplace context and demonstration. Pure passive observation (Option B) misses the user's verbal explanations of why actions are performed.",
        "context": "Introduced by Beyer and Holtzblatt, Contextual Inquiry follows the master-apprentice model to discover unarticulated user needs."
    },
    "w2_q2": {
        "correct": "Option A ('Function name') is correct because in a formal Software Requirements Specification (SRS), a functional requirement is specified by its input, its expected output, and a detailed functional description of the transformation logic—not simply by a code-level function name.",
        "why_others_wrong": "Input (Option B), Output (Option C), and Description (Option D) are the three mandatory structural components required to specify any functional requirement in an SRS.",
        "context": "An SRS focuses on 'WHAT' the system must accomplish from a behavioral standpoint, abstracting away programming identifiers."
    },
    "w2_q3": {
        "correct": "Option A ('active') is correct because Contextual Inquiry can be conducted in Active mode (where the researcher interrupts the user to ask clarifying questions about observed actions) and Passive mode (where the researcher observes silently without interfering, discussing afterward).",
        "why_others_wrong": "'Semi-active' and 'neutral' are informal terms not recognized in the formal Contextual Inquiry methodological taxonomy.",
        "context": "Active inquiry is ideal for deciphering tacit habits, while passive inquiry is essential when user interruption would break critical task timing or safety."
    },
    "w2_q4": {
        "correct": "Option B ('five') is correct because the Contextual Inquiry workflow comprises 5 distinct procedural stages: 1. Plan, 2. Initiate, 3. Execute (the session), 4. Reflect (immediate debrief), and 5. Wrap-up / Consolidate.",
        "why_others_wrong": "Options A, C, and D do not correspond to the five-stage contextual inquiry lifecycle taught in the course modules.",
        "context": "Following all five stages ensures methodological rigor from pre-interview scoping to final requirement consolidation."
    },
    "w2_q5": {
        "correct": "Option A ('Plan Stage') is correct because the Plan stage involves all preparatory logistical and methodological setup: selecting target user profiles, scripting observation protocols, acquiring recording tools/cameras, and securing permissions.",
        "why_others_wrong": "Initiate Stage (Option B) involves establishing rapport with the participant upon arrival. Execute Stage (Option C) is the actual workplace observation. Reflect Stage (Option D) is post-session analysis.",
        "context": "Proper planning prevents observation bias and ensures ethical consent before field visits begin."
    },
    "w2_q6": {
        "correct": "Option D ('Five') is correct because the Affinity Diagram (KJ method) consists of 5 sequential steps: 1. Generate observational notes on cards/sticky notes, 2. Display all notes randomly, 3. Cluster notes into related groups without speaking, 4. Create descriptive header labels for clusters, 5. Draw hierarchical relationships between super-groups.",
        "why_others_wrong": "Options A, B, and C represent incomplete subsets of the five-step affinity synthesis process.",
        "context": "Affinity diagramming is the standard qualitative synthesis technique used in HCI to convert messy qualitative field notes into structured user needs."
    },
    "w2_q7": {
        "correct": "Option B ('Non-functional requirement') is correct because Usability requirements (e.g. task completion time, allowable error rate, ease of learning, user satisfaction) specify quality attributes of the system, which are categorized as non-functional requirements in software engineering.",
        "why_others_wrong": "Functional requirements (Option A) describe specific services, calculations, or data transformations the system must execute.",
        "context": "While functional requirements specify WHAT a system does, non-functional requirements govern HOW WELL and how reliably it does it."
    },
    "w2_q8": {
        "correct": "Option A is correct because the core foundational principle of Contextual Inquiry is 'Context': observing real users performing their authentic day-to-day tasks in their natural physical work setting.",
        "why_others_wrong": "Option B (conducting interviews) is just a technique, not the primary objective. Option C and D describe later downstream artifacts or recording tools.",
        "context": "The 4 core principles of CI are: Context (go where the work is), Partnership (master-apprentice collaboration), Interpretation (assigning shared meaning), and Focus."
    },
    "w2_q9": {
        "correct": "Option B is correct because the 'Reflect' stage takes place immediately following the observation session to analyze collected data, review notes, cross-verify interpretations with the team, and identify preliminary design goals.",
        "why_others_wrong": "Contacting authorities (Option A) belongs to the Plan/Initiate stages. Scripting procedures (Option C) belongs strictly to the Plan stage.",
        "context": "Reflecting immediately after an interview capitalizes on short-term memory before tacit details fade."
    },
    "w2_q10": {
        "correct": "Option B ('One to two hours') is correct because an individual Contextual Inquiry session typically lasts between 1 to 2 hours. This provides sufficient depth to observe task workflows without causing excessive cognitive fatigue to the user or interfering with their business operations.",
        "why_others_wrong": "Options A and C (weeks or months) represent entire project timelines, not the duration of an individual contextual inquiry session.",
        "context": "A 1-2 hour focused observation strikes the perfect balance between depth of contextual immersion and participant comfort."
    },

    # WEEK 3
    "w3_q1": {
        "correct": "Option B ('False') is correct because in an SRS document, functional requirements must describe WHAT output is produced from what input, NOT HOW the system internally computes it. Specifying 'HOW' is the job of detailed code design and algorithmic implementation, not the requirements phase.",
        "why_others_wrong": "Claiming that an SRS should describe 'HOW' violates the fundamental separation between Requirements (What) and Architecture/Implementation (How).",
        "context": "Conflating 'what' with 'how' prematurely restricts developer freedom and biases system design before all constraints are understood."
    },
    "w3_q2": {
        "correct": "Option A ('True') is correct because observing real users during contextual inquiry frequently reveals previously unstated workflows, workarounds, and tacit requirements that necessitate adding brand-new functional requirements to the system specification.",
        "why_others_wrong": "Option B is incorrect because requirements discovery is an iterative process; field research routinely uncovers missing functions.",
        "context": "Users frequently adapt to bad systems with personal workarounds (e.g. sticky notes, manual spreadsheets); noticing these highlights missing functional features."
    },
    "w3_q3": {
        "correct": "Option C ('Code design') is correct because in User-Centered Design (UCD), developers balance two dual concerns: 'Interface Design' (the user-facing interaction, ergonomics, and presentation) and 'Code Design' (the underlying architecture, data structures, and computational algorithms).",
        "why_others_wrong": "Machine design (Option A) and hardware design (Option B) refer to mechanical/electronic engineering. System design (Option D) is an umbrella term encompassing both.",
        "context": "A brilliant interface cannot compensate for broken, buggy backend code; both must be engineered harmoniously."
    },
    "w3_q4": {
        "correct": "Option A ('Interface') is correct because the rapid iterative cycle of 'Design-Prototype-Evaluate' is designed primarily for Interface Design. Prototyping allows teams to test layout, interaction flows, and cognitive friction with users before investing heavy resources in code implementation.",
        "why_others_wrong": "Code design (Option B) and System design (Option C) rely more on formal architectural modeling, refactoring, and automated testing rather than rapid user prototype evaluation.",
        "context": "Throwaway and paper prototypes are interface-specific tools that validate mental models before writing production code."
    },
    "w3_q5": {
        "correct": "Option B ('Formal languages') is correct because software engineering design languages span a spectrum from Natural languages (English), to Semi-formal languages (DFD, UML), to Formal languages (mathematically rigorous notations such as Z, VDM, or algebraic specifications).",
        "why_others_wrong": "Informal languages (Option A) is a synonym for natural language. Context-sensitive languages (Option C) is a Chomsky grammar classification, not a design notation category.",
        "context": "Formal specification languages use mathematical logic (set theory and predicate calculus) to prove system correctness without ambiguity."
    },
    "w3_q6": {
        "correct": "Option B ('Semi-formal') is correct because Data Flow Diagrams (DFDs) use standardized graphical shapes (processes, datastores, external entities, data flows) with defined syntax, but lack rigorous mathematical semantics, classifying them as semi-formal design notations.",
        "why_others_wrong": "Natural (Option A) uses spoken language. Formal languages rely on mathematical proofs. Context-sensitive (Option D) is a formal language theory class.",
        "context": "Most visual software modeling notations (DFD, ERD, UML) are semi-formal because they provide visual structure without mathematical execution proofs."
    },
    "w3_q7": {
        "correct": "Option C ('Eight') is correct because Ben Shneiderman formulated the seminal 'Eight Golden Rules of Interface Design' in 1986.",
        "why_others_wrong": "Five, Seven, and Nine are incorrect counts. Jakob Nielsen proposed 10 heuristics, while Shneiderman proposed 8 rules.",
        "context": "Shneiderman's 8 Golden Rules are: Consistency, Universal Usability, Informative Feedback, Dialog Closure, Error Prevention, Reversal of Actions (Undo), Locus of Control, and Reduced Memory Load."
    },
    "w3_q8": {
        "correct": "Option C ('Reduce short-term memory load') is correct because this directly reflects Shneiderman's 8th Golden Rule. Human working memory is limited to ~7 ± 2 chunks, so interfaces should keep context visible, pre-fill known data, and avoid forcing users to memorize information across screens.",
        "why_others_wrong": "Strive for consistency (Option A) requires uniform terminology. Reversal of actions (Option B) is Undo/Redo. Keep users in control (Option D) relates to internal locus of control.",
        "context": "Minimizing memory load relies on 'recognition rather than recall'—making items visible so users do not have to retrieve them from memory."
    },
    "w3_q9": {
        "correct": "Option B ('Specific') is correct because Apple's Human Interface Guidelines (HIG) are platform-specific design guidelines tailored exclusively to Apple hardware (iOS, macOS, visionOS) and Apple design conventions, unlike generic guidelines (like Shneiderman's rules) which apply across all systems.",
        "why_others_wrong": "Generic guidelines (Option A) apply universally across any device or operating system.",
        "context": "Design guidelines exist at two levels: high-level generic principles (universal) and platform-specific guidelines (e.g. Apple HIG, Google Material Design)."
    },
    "w3_q10": {
        "correct": "Option B ('Detailed design') is correct because selecting specific data structures (arrays, hash maps, trees) and exact algorithms (sorting, search, traversal logic) is performed during the Detailed Design phase. High-level design focuses on module partitioning and interfaces.",
        "why_others_wrong": "Preliminary / High-level design (Option A) defines the overall system architecture, subsystem decomposition, and module communication protocols without descending into algorithmic specifics.",
        "context": "High-level design creates the blueprint of modules; detailed design defines the internal algorithmic engine of each module."
    },

    # WEEK 4
    "w4_q1": {
        "correct": "Option A ('actions') is correct because Donald Norman's 7 Stages of Action model conceptualizes human interaction with interactive devices as an alternating cycle of physical and cognitive actions (forming intentions, specifying actions, executing motor actions, and evaluating feedback).",
        "why_others_wrong": "Selection (Option B) and Manipulation (Option C) are specific sub-types of interaction, but Norman's overarching model is formulated around 'actions'.",
        "context": "Norman's 7 Stages: 1. Goal, 2. Intention, 3. Action Specification, 4. Execution, 5. Perception, 6. Interpretation, 7. Evaluation."
    },
    "w4_q2": {
        "correct": "Option B ('evaluation') is correct because Norman divides interaction into two macro-stages: the 'Execution stage' (bridging the psychological goal to physical device action) and the 'Evaluation stage' (bridging the physical device state back to the psychological interpretation).",
        "why_others_wrong": "Design (Option A) is what creators do. Interaction (Option C) is the broad domain itself, not a sub-stage.",
        "context": "The two macro-stages give rise to the famous concepts: the Gulf of Execution and the Gulf of Evaluation."
    },
    "w4_q3": {
        "correct": "Option C ('evaluation') is correct because 'Perceiving system state' is the first stage on the return cycle of the Evaluation phase (followed by Interpreting perception, and Evaluating outcome against the initial goal).",
        "why_others_wrong": "Execution (Option A) encompasses forming the intention, specifying actions, and physical motor execution.",
        "context": "Feedback (visual, auditory, tactile) is perceived by the human sensory system during this stage to bridge the Gulf of Evaluation."
    },
    "w4_q4": {
        "correct": "Option A ('The gulf of execution') is correct because the Gulf of Execution measures the psychological and physical gap between what the user intends to do and what allowable actions the interface actually provides.",
        "why_others_wrong": "The Gulf of Evaluation (Option B) is the difficulty of assessing the system's state and determining if the goal was achieved. 'Gulf of Interaction' (Option C) is a non-standard hybrid term.",
        "context": "Signifiers, natural mappings, and affordances help users bridge the Gulf of Execution."
    },
    "w4_q5": {
        "correct": "Option B ('mistakes') is correct because in Norman's error classification, human errors during interaction are bifurcated into 'Slips' (execution errors where the goal is right but action execution fails) and 'Mistakes' (planning errors where the mental goal or plan itself is flawed).",
        "why_others_wrong": "'Error' (Option A) and 'Human error' (Option C) are general umbrella categories, not the specific paired counterpart to slips.",
        "context": "Slips occur due to lack of attention or muscle fatigue (e.g. typos, clicking wrong icon); mistakes occur due to incomplete mental models."
    },
    "w4_q6": {
        "correct": "Option B ('False') is correct because depicting the entire interface at the surface level without underlying functionality is the definition of a Horizontal Prototype. A Vertical Prototype, by contrast, implements full, deep functionality for only a narrow slice of features.",
        "why_others_wrong": "The prompt incorrectly attributes the horizontal prototype definition to a vertical prototype.",
        "context": "Horizontal = broad breath, zero depth; Vertical = narrow breadth, deep functionality."
    },
    "w4_q7": {
        "correct": "Option A ('Low fidelity') is correct because paper mock-ups, sketches, and cardboard prototypes are classic examples of Low-Fidelity (Lo-Fi) prototypes. They are fast, cheap, and focus attention on information architecture rather than visual aesthetics.",
        "why_others_wrong": "High fidelity (Option B) prototypes look and behave like finished software (interactive code/clickable Figma). Medium fidelity (Option C) prototypes use digital wireframes without final styling.",
        "context": "Low-fidelity prototypes encourage candid user criticism because users do not assume the design is finished or fragile."
    },
    "w4_q8": {
        "correct": "Option A ('True') is correct because standard Cognitive Walkthrough guidelines (Wharton et al., 1994) recommend a multidisciplinary team of 3 to 5 evaluators to optimize defect discovery and cognitive perspective without logistical gridlock.",
        "why_others_wrong": "Option B is incorrect because literature empirically demonstrates that 3-5 evaluators find the vast majority of learnability issues.",
        "context": "Evaluators role-play novice users stepping through tasks, evaluating action visibility, semantic matching, and feedback."
    },
    "w4_q9": {
        "correct": "Option B ('False') is correct because in a Cognitive Walkthrough, evaluators must NOT simply answer 'yes' or 'no'. They must provide detailed, credible stories justifying why a user would or would not take the right action and record specific failure points.",
        "why_others_wrong": "A binary yes/no response fails to capture the underlying cognitive explanation needed by developers to redesign the interface.",
        "context": "Wharton's 4 walkthrough questions require qualitative justification: 1. Will the user try to achieve effect? 2. Notice control? 3. Associate with action? 4. Understand feedback?"
    },
    "w4_q10": {
        "correct": "Option C ('Wizard of Oz') is correct because the Wizard of Oz technique simulates an intelligent or automated computing system by having a hidden human operator ('the Wizard') behind the scenes manually generating responses, unbeknownst to the test subject.",
        "why_others_wrong": "Vertical (Option B) is a functional prototype. Medium fidelity (Option A) and Incremental (Option D) describe prototype fidelity and process strategies.",
        "context": "Wizard of Oz is widely used to evaluate speech recognition, NLP, and AI assistants before investing in expensive machine learning algorithms."
    },

    # WEEK 5
    "w5_q1": {
        "correct": "Option C ('by evaluating usability') is correct because the primary, comprehensive quality framework for evaluating interactive software interfaces is Usability (defined by ISO 9241-11 through effectiveness, efficiency, and satisfaction).",
        "why_others_wrong": "Evaluating satisfaction (Option A) and memorability (Option B) are individual sub-dimensions of usability, not the overarching evaluation method itself.",
        "context": "Usability evaluation encompasses both inspection methods (heuristic evaluation, walkthroughs) and empirical user testing."
    },
    "w5_q2": {
        "correct": "Option A ('True') is correct because before conducting a Cognitive Walkthrough, the evaluation team must define the user persona, concrete task scenarios, the exact sequence of correct actions, and the four diagnostic usability questions for each step.",
        "why_others_wrong": "Without a pre-defined sequence of actions and structured questions, cognitive walkthroughs lose rigor and turn into unstructured critiques.",
        "context": "Structuring the walkthrough around explicit user tasks ensures evaluators stay focused on novice learnability."
    },
    "w5_q3": {
        "correct": "Option B ('heuristics') is correct because in a Heuristic Evaluation, the guidelines or checklist items used by expert evaluators to inspect an interface are termed 'Heuristics' (rules of thumb, most famously Nielsen's 10 Heuristics).",
        "why_others_wrong": "Checkbox (Option A) is a UI widget. Usability issues (Option C) and problems (Option D) are the resulting discoveries, not the checklist guidelines themselves.",
        "context": "Heuristics act as cognitive lenses that help inspectors spot usability defects systematically."
    },
    "w5_q4": {
        "correct": "Options B and A ('Rating on a scale' and 'Utter the option') are correct because self-report usability methods collect subjective user feedback by asking participants to rate items on structured Likert/semantic scales or to verbalize their choice/opinions directly.",
        "why_others_wrong": "Both rating scales (Likert) and open verbal choices are recognized self-report techniques in usability research.",
        "context": "Self-report metrics quantify subjective user satisfaction, complementing objective measures like task completion times."
    },
    "w5_q5": {
        "correct": "Option A ('Post-task questionnaire') is correct because the ASQ (After-Scenario Questionnaire, developed by Lewis) is administered immediately following the completion of an individual task/scenario to capture immediate task difficulty.",
        "why_others_wrong": "Option B (Post-session) describes questionnaires like the SUS or CSUQ which are administered once at the very end of the entire usability testing session.",
        "context": "ASQ contains 3 items assessing ease of task completion, time required, and satisfaction with support information."
    },
    "w5_q6": {
        "correct": "Option D ('70') is correct because empirical research across thousands of usability surveys (Sauro & Lewis) establishes that a System Usability Scale (SUS) score around 68-70 is the average baseline (50th percentile / Grade C). A score >= 70 is considered acceptable/desirable.",
        "why_others_wrong": "Scores of 10, 20, or 50 represent severe usability failures (50 is in the bottom 15th percentile).",
        "context": "SUS scores above 80 indicate Grade A usability, while scores below 68 indicate below-average usability requiring remediation."
    },
    "w5_q7": {
        "correct": "Option A ('3-5') is correct because research by Jakob Nielsen demonstrated that 3 to 5 expert evaluators uncover roughly 75% to 80% of usability defects, providing the optimal cost-benefit balance in discount usability engineering.",
        "why_others_wrong": "Larger teams (4-7, 5-7, 7-9) incur diminishing returns: additional evaluators find fewer new problems while substantially increasing inspection costs.",
        "context": "A single evaluator finds only ~35% of problems, but pooling 3-5 independent evaluators covers the majority of severe issues."
    },
    "w5_q8": {
        "correct": "Option A ('Heuristics') is correct because the checklist items evaluated in a heuristic evaluation are called Heuristics (rules of thumb for good interface design).",
        "why_others_wrong": "Actions and statements are general linguistic terms, not the specific HCI inspection term.",
        "context": "Using established heuristics allows inspectors to benchmark designs against proven cognitive principles."
    },
    "w5_q9": {
        "correct": "Option D ('System usability scale') is correct because SUS stands for 'System Usability Scale', created by John Brooke at Digital Equipment Corporation in 1986.",
        "why_others_wrong": "Options A, B, and C use incorrect terms ('Software' instead of 'System', and 'Score' instead of 'Scale').",
        "context": "SUS is a 10-item Likert scale questionnaire that is technology-agnostic and widely cited as the industry benchmark for perceived usability."
    },
    "w5_q10": {
        "correct": "Options A and C ('Cognitive walkthrough' and 'Heuristic evaluation') are correct because both are recognized expert usability inspection methods used to evaluate prototypes.",
        "why_others_wrong": "Affinity diagram (Option B) is a qualitative data synthesis and clustering method used during user research, not an interface prototype evaluation technique.",
        "context": "Heuristic evaluation and cognitive walkthroughs form the backbone of 'discount usability' inspection without requiring end-user testing."
    },

    # WEEK 6
    "w6_q1": {
        "correct": "Option D ('Colorful') is correct because being 'Colorful' is an aesthetic choice and NOT a fundamental engineering criterion of good software design. Good software design requires Coverage (addressing all requirements), Correctness (accurate execution), and Understandability (maintainable and clear architecture).",
        "why_others_wrong": "Coverage (Option A), Correctness (Option B), and Understandability (Option C) are essential quality criteria of software architecture.",
        "context": "Excessive color can increase visual cognitive load; aesthetic choices must support usability, not substitute for sound architecture."
    },
    "w6_q2": {
        "correct": "Option A ('Logical') is correct because Logical Cohesion occurs when elements in a module perform tasks that are logically similar or categorized together (e.g., a module that groups all input routines together or all mathematical transformations together).",
        "why_others_wrong": "Temporal cohesion (Option B) groups tasks executed at the same time (e.g. startup initialization). Procedural cohesion (Option C) groups tasks following a sequence of steps. Sequential cohesion (Option D) passes the output of one step as input to the next.",
        "context": "Cohesion levels (from weakest to strongest): Coincidental < Logical < Temporal < Procedural < Communicational < Sequential < Functional."
    },
    "w6_q3": {
        "correct": "Option C ('Content') is correct because Content Coupling is the worst and tightest form of coupling, occurring when one module directly accesses, modifies, or shares the internal implementation code/data of another module.",
        "why_others_wrong": "Data coupling (Option A) is the best and cleanest form (modules pass only primitive data parameters). Control coupling (Option B) occurs when one module passes flags to control the execution logic of another.",
        "context": "High coupling makes software brittle; changes to one module unintentionally break dependent modules."
    },
    "w6_q4": {
        "correct": "Option C ('Object') is correct because the two fundamental architectural design approaches in software engineering are Function-Oriented Design (structured/procedural) and Object-Oriented Design (OOD).",
        "why_others_wrong": "Logic and folder are not software architectural design paradigms.",
        "context": "Function-oriented models view software as a hierarchy of functions processing data; object-oriented models view software as interacting autonomous objects encapsulating state and behavior."
    },
    "w6_q5": {
        "correct": "Option C ('Attribute') is correct because the three foundational building blocks of Entity-Relationship (ER) models are Entities (rectangles), Attributes (ovals), and Relationships (diamonds).",
        "why_others_wrong": "Object, User, and Class belong to object-oriented programming, not classical Chen ER modeling.",
        "context": "Peter Chen introduced ER modeling in 1976 to provide a unified conceptual model for database architectures."
    },
    "w6_q6": {
        "correct": "Option A is correct because Null attributes in relational databases and ER models represent situations where an entity either does not have an applicable value for that attribute or the value is currently unknown/missing.",
        "why_others_wrong": "Option B describes Derived attributes (attributes whose values are computed from other stored attributes, represented by dashed ovals).",
        "context": "Handling null values properly is essential in database schema design to avoid semantic errors during queries."
    },
    "w6_q7": {
        "correct": "Option B ('Many-to-many') is correct because the four cardinality constraints in ER modeling are: One-to-One (1:1), One-to-Many (1:N), Many-to-One (N:1), and Many-to-Many (M:N).",
        "why_others_wrong": "'Binary-to-many' and 'Many-to-binary' confuse degree (binary vs ternary) with cardinality ratios.",
        "context": "Many-to-many relationships require a junction/associative table when translated into physical relational database schemas."
    },
    "w6_q8": {
        "correct": "Options A and B ('Temporal' and 'Functional') are correct because both are recognized types of module cohesion. Functional cohesion is the highest and most desirable form; Temporal cohesion groups routines executed in the same timeframe.",
        "why_others_wrong": "Content (Option C) is a type of module coupling, not cohesion. Option D ('All of the above') is wrong because Content is not cohesion.",
        "context": "Functional cohesion means every element in the module contributes to executing a single, well-defined mathematical or computational task."
    },
    "w6_q9": {
        "correct": "Option B ('Coupling') is correct because Coupling specifically measures the degree of interdependence and interaction BETWEEN different software modules, whereas Cohesion measures how closely related the elements are WITHIN a single module.",
        "why_others_wrong": "Cohesion (Option A) measures internal intra-module strength. Option C is wrong because the two concepts operate at different structural levels.",
        "context": "The golden rule of software engineering architecture is: 'Aim for High Cohesion and Low Coupling'."
    },
    "w6_q10": {
        "correct": "Option D ('Data flow diagram') is correct because DFD stands for Data Flow Diagram, a graphical modeling tool for function-oriented software analysis and design.",
        "why_others_wrong": "Options A, B, and C use incorrect expansions ('design', 'decision', 'development').",
        "context": "DFDs model how data enters a system, transforms across functional processes, and gets stored in datastores."
    },

    # WEEK 7
    "w7_q1": {
        "correct": "Option B ('Functions') is correct because Function-Oriented Design conceptualizes the system as a collection of services or processing steps represented as Functions/procedures that manipulate passive data.",
        "why_others_wrong": "Objects (Option C) are the core abstraction of Object-Oriented design. Data (Option A) represents the input/output passed between functions.",
        "context": "Function-oriented design breaks high-level functions into smaller sub-functions using top-down stepwise refinement."
    },
    "w7_q2": {
        "correct": "Option A ('True') is correct because Object-Oriented Design (OOD) rejects viewing a system as a centralized collection of procedural 'services'; instead, it models the world as autonomous, self-contained objects that collaborate via message passing.",
        "why_others_wrong": "Option B is incorrect because in pure OOD, capabilities are encapsulated as member operations belonging to individual objects rather than monolithic system-wide services.",
        "context": "This fundamental paradigm shift improves modularity, maintainability, and code reuse through encapsulation and polymorphism."
    },
    "w7_q3": {
        "correct": "Option B ('Operations') is correct because in object-oriented modeling, a class encapsulates two essential components: Attributes (data/state variables) and Operations (methods/behavioral functions).",
        "why_others_wrong": "Objects (Option C) are runtime instances of classes. Data (Option A) is represented by attributes.",
        "context": "A UML class diagram box displays three compartments: Class Name, Attributes, and Operations."
    },
    "w7_q4": {
        "correct": "Option A ('True') is correct because Attributes define the state, fields, or properties that instances (objects) of that class can hold at runtime.",
        "why_others_wrong": "Option B is incorrect because attributes are the formal mechanism for declaring data types and variables encapsulated in an object.",
        "context": "Encapsulation restricts direct external access to attributes, forcing interactions through class operations/methods."
    },
    "w7_q5": {
        "correct": "Option C ('object oriented analysis') is correct because OOA stands for Object-Oriented Analysis, the phase focused on modeling the problem domain and identifying objects, classes, and requirements.",
        "why_others_wrong": "Options A, B, and D use incorrect expansions ('assignment', 'assistance', 'attributes').",
        "context": "OOA models WHAT the real-world domain consists of; OOD designs HOW software objects will implement the solution."
    },
    "w7_q6": {
        "correct": "Option B ('Operations') is correct because Operations (methods) define the dynamic behavior, message handling, and state transformations that a class can perform.",
        "why_others_wrong": "Attributes (Option D) and Data (Option A) define static state. Objects (Option C) are instances.",
        "context": "State + Behavior = Object. Attributes represent state; operations represent behavior."
    },
    "w7_q7": {
        "correct": "Option C ('OOD') is correct because the Unified Modeling Language (UML) is a standardized visual modeling language used primarily to represent Object-Oriented Design (and Analysis).",
        "why_others_wrong": "OOP (Option A) refers to actual programming languages (Java, C++). OOA (Option B) is only the analysis subset.",
        "context": "UML was created by Grady Booch, Ivar Jacobson, and James Rumbaugh (the 'Three Amigos') in the mid-1990s."
    },
    "w7_q8": {
        "correct": "Option B ('False') is correct because UML is a graphical modeling language/notation, NOT a design methodology. A methodology prescribes a process, schedule, and team roles (e.g. Scrum, XP, Waterfall); UML simply provides the visual vocabulary to draw diagrams.",
        "why_others_wrong": "Confusing a modeling language with a software development process is a common beginner misconception.",
        "context": "You can use UML with any methodology: Waterfall, Agile, Spiral, or the Rational Unified Process (RUP)."
    },
    "w7_q9": {
        "correct": "Option B ('Component diagram') is correct because the Implementation View of a system depicts software modules, source code files, libraries, and executables, which is modeled using UML Component diagrams.",
        "why_others_wrong": "Deployment diagrams (Option A) capture the physical hardware environment. Class diagrams (Option C) capture logical static structure. Use case diagrams (Option D) capture user behavioral requirements.",
        "context": "In Kruchten's 4+1 View Model, the Implementation (Development) View manages software asset organization."
    },
    "w7_q10": {
        "correct": "Option C ('Entity') is correct because Entity objects (in the BCE - Boundary, Controller, Entity pattern) represent persistent data and domain information (e.g. books, accounts, customer records).",
        "why_others_wrong": "Boundary objects (Option A) handle interactions with external actors (UI forms, API endpoints). Controller objects (Option B) orchestrate workflow logic.",
        "context": "The BCE pattern separates presentation (Boundary), business logic (Controller), and state storage (Entity)."
    },

    # WEEK 8
    "w8_q1": {
        "correct": "Option D ('Readability, understandability, and teamwork') is correct because adhering to standard coding conventions (naming, formatting, indentation) ensures that code is easy to read, simple to understand during debugging, and seamlessly maintainable across collaborative engineering teams.",
        "why_others_wrong": "Options A, B, and C are only partial benefits; coding standards impact all three dimensions simultaneously.",
        "context": "Software is read far more often than it is written; standard coding guidelines drastically reduce cognitive friction during code reviews."
    },
    "w8_q2": {
        "correct": "Option C ('10') is correct because textbook coding guidelines and course lectures recommend keeping individual functions concise—ideally around 10 lines of code—to uphold the Single Responsibility Principle and maintain high readability.",
        "why_others_wrong": "Functions with 50+ or 100+ lines become difficult to comprehend, verify, and unit-test without defects.",
        "context": "Small functions are easier to test, reason about, and reuse without side effects."
    },
    "w8_q3": {
        "correct": "Options A, B, and C ('Using lengthy functions', 'Using the same identifier for multiple purposes', 'Using goto indiscriminately') are correct because all three are notorious code smells and anti-patterns that create spaghetti code and introduce bugs.",
        "why_others_wrong": "Using proper indentation (Option D) is a mandatory best practice, not something to avoid.",
        "context": "Reusing variable names for unrelated purposes breaks referential transparency and confuses static analysis tools."
    },
    "w8_q4": {
        "correct": "Option B ('Execution-based') is correct because software testing methods are broadly partitioned into Review-Based methods (static testing without running code: inspections, walkthroughs) and Execution-Based methods (dynamic testing by running code with test inputs).",
        "why_others_wrong": "Manual testing (Option A) can be both execution-based or review-based. Option D ('1 Point') is a stray OCR label.",
        "context": "Review-based testing catches 50-70% of logical bugs before code ever compiles, saving substantial debugging time."
    },
    "w8_q5": {
        "correct": "Options A and B ('Code inspection' and 'Code walkthrough') are correct because both are the classic review-based (static) software quality assurance methods.",
        "why_others_wrong": "Unit testing (Option C) is dynamic execution-based testing requiring the code to execute with test cases.",
        "context": "Code inspection is formal and checklist-driven (Fagan inspection); code walkthrough is informal and led by the code author."
    },
    "w8_q6": {
        "correct": "Option A ('True') is correct because White-Box (structural/glass-box) testing explicitly uses knowledge of internal program source code, control flow paths, and branch conditions to design test cases.",
        "why_others_wrong": "Option B is incorrect because black-box testing ignores internal code structure, while white-box testing requires it.",
        "context": "White-box testing evaluates statement coverage, branch coverage, condition coverage, and path coverage."
    },
    "w8_q7": {
        "correct": "Option B ('3-5 members') is correct because standard software engineering guidelines recommend a team size of 3 to 5 members for code walkthroughs to facilitate thorough scrutiny without organizational chaos.",
        "why_others_wrong": "Teams with fewer than 3 lack diverse perspective; teams larger than 5 suffer coordination overhead and slower reviews.",
        "context": "A typical walkthrough team includes: the author, a moderator, a scribe, and one or two peer inspectors."
    },
    "w8_q8": {
        "correct": "Option A ('Code walkthrough') is correct because in a code walkthrough, the author guides the review team through the source code, manually stepping through sample test data by hand on a whiteboard to simulate runtime execution.",
        "why_others_wrong": "Code inspection (Option B) is a static checklist audit looking for standard defects (syntax, uninitialized variables) rather than hand simulation. Black/White box testing executes on a computer.",
        "context": "Manual simulation in walkthroughs uncovers algorithmic boundary flaws and off-by-one errors early."
    },
    "w8_q9": {
        "correct": "Option A ('True') is correct because uninitialized variables are static defects that do not require program execution to find; they are easily caught during static code inspection using standard inspection checklists or compiler linting.",
        "why_others_wrong": "Option B is incorrect because static analysis and code inspection checklists explicitly include checks for variable initialization before use.",
        "context": "Uninitialized variables cause unpredictable memory garbage and undefined runtime crashes in languages like C/C++."
    },
    "w8_q10": {
        "correct": "Option D ('Knowledge of the internal structure of the code') is correct because Black-Box testing intentionally treats the software as an opaque black box, relying strictly on requirements specifications without any knowledge of internal code or data structures.",
        "why_others_wrong": "Equivalence class partitioning (Option A), Boundary value analysis (Option B), and Test suite creation (Option C) are core techniques of black-box testing.",
        "context": "Black-box testing verifies that the software delivers the expected outputs for given inputs from the user's perspective."
    },

    # WEEK 9
    "w9_q1": {
        "correct": "Option B ('Test suite') is correct because a collection or set of all test cases intended to test a specific software application or component is formally known as a Test Suite.",
        "why_others_wrong": "A Testcase (Option A) refers to a single individual test input, execution condition, and expected outcome.",
        "context": "Test suites are automated within continuous integration (CI) pipelines to prevent regression bugs."
    },
    "w9_q2": {
        "correct": "Option A ('True') is correct because selecting test inputs completely at random often clusters values in the center of equivalence partitions where bugs rarely hide, offering low defect discovery significance compared to systematic testing.",
        "why_others_wrong": "Option B is incorrect because random testing fails to target boundary values where over 80% of software defects actually reside.",
        "context": "Systematic techniques (BVA, Equivalence Partitioning) guarantee high test significance with minimal test cases."
    },
    "w9_q3": {
        "correct": "Option B ('Boundary value analysis') is correct because the two primary foundational techniques for designing black-box test cases are Equivalence Class Partitioning (ECP) and Boundary Value Analysis (BVA).",
        "why_others_wrong": "Structural analysis (Option A) belongs to white-box testing. Equivalence class analysis and system analysis are informal terms.",
        "context": "BVA tests values right at the borders of equivalence classes (e.g. min-1, min, min+1, max-1, max, max+1)."
    },
    "w9_q4": {
        "correct": "Option A ('One') is correct because the mathematical premise of an equivalence partition is that all input values within that partition are treated identically by the program logic. Therefore, testing any ONE arbitrary representative value from the class is assumed to be as effective as testing all of them.",
        "why_others_wrong": "Testing two, four, or five values from the same equivalence class is redundant and inflates test suite execution time without increasing defect detection.",
        "context": "Equivalence partitioning reduces an infinite set of potential inputs into a small, manageable number of test cases."
    },
    "w9_q5": {
        "correct": "Option B ('Equivalence class') is correct because in black-box testing, the input domain is partitioned into contiguous subsets called Equivalence Classes, where every value in the subset is assumed to produce the same processing outcome.",
        "why_others_wrong": "Partition class and program class are non-standard terminology.",
        "context": "Equivalence classes are divided into Valid Equivalence Classes (normal inputs) and Invalid Equivalence Classes (error-handling inputs)."
    },
    "w9_q6": {
        "correct": "Options A and B ('Code walkthrough' and 'Code inspection') are correct because both are the formal review-based testing methodologies in software quality engineering.",
        "why_others_wrong": "Code analysis (Option C) and Code assessment (Option D) are generic descriptive phrases, not formal review inspection techniques.",
        "context": "Code walkthroughs and inspections verify compliance with coding standards, error handling, and algorithmic correctness."
    },
    "w9_q7": {
        "correct": "Option C ('Suite') is correct because a set of test cases assembled to test software is termed a Test Suite.",
        "why_others_wrong": "Question and Questionnaire are survey tools, not software engineering test terminology.",
        "context": "A test suite organizes test cases logically by module, feature, or testing level (unit, integration, regression)."
    },
    "w9_q8": {
        "correct": "Options A and C ('input' and 'output') are correct because Black-Box test cases are derived strictly from the specification of valid/invalid inputs and their corresponding expected outputs.",
        "why_others_wrong": "Knowledge of design (Option B) and Knowledge of code (Option D) are the domain of white-box and gray-box testing, not black-box testing.",
        "context": "Black-box testing ensures that software satisfies customer requirements without being biased by implementation quirks."
    },
    "w9_q9": {
        "correct": "Option A ('True') is correct because an equivalence class is formally defined as a subset of the input domain where the software's behavior is equivalent for any value chosen from that subset.",
        "why_others_wrong": "Option B is incorrect because this is the fundamental definition of equivalence partitioning in software testing.",
        "context": "If a test fails for one member of an equivalence class, it is assumed to fail for all members of that class."
    },
    "w9_q10": {
        "correct": "Option A ('Black-box testing') is correct because Functional Testing validates system operations against user requirements and functional specifications, making it fundamentally a black-box testing paradigm.",
        "why_others_wrong": "White-box testing (Option B) evaluates structural code execution (branches, paths, conditions), which is structural testing, not functional testing.",
        "context": "Functional testing answers: 'Does the software perform the specific business functions required by the user?'"
    },

    # WEEK 10
    "w10_q1": {
        "correct": "Option A ('True') is correct because White-Box (glass-box/structural) testing inherently requires access to and knowledge of internal source code, control logic, and variable states to create test cases.",
        "why_others_wrong": "Option B is incorrect because testing without internal knowledge is black-box testing.",
        "context": "White-box testing allows developers to inspect untested conditional branches and exception blocks."
    },
    "w10_q2": {
        "correct": "Option A ('CFG') is correct because a Control Flow Graph (CFG) is the standard visual graph representation of program control flow, where nodes represent statements and directed edges represent control jumps.",
        "why_others_wrong": "DFD (Option B) models data movement. ERD (Option C) models database relationships. Class diagrams (Option D) model object-oriented static class hierarchies.",
        "context": "CFGs are the mathematical foundation for calculating cyclomatic complexity and designing path coverage test suites."
    },
    "w10_q3": {
        "correct": "Option B ('Add edges') is correct because constructing a CFG requires: 1. Numbering all basic statements, 2. Creating a node for each statement, and 3. Adding directed edges between nodes that represent possible transfers of control.",
        "why_others_wrong": "Complementing (Option A) and sorting (Option C) are not steps in standard CFG construction.",
        "context": "Branches (e.g. if-else, while loops) generate multiple outgoing edges from decision nodes."
    },
    "w10_q4": {
        "correct": "Option A ('True') is correct because Branch Coverage requires that every decision branch (both TRUE and FALSE outcomes of every conditional statement) is executed at least once. Satisfying branch coverage guarantees that every statement lying along those branches is also executed, thereby guaranteeing Statement Coverage.",
        "why_others_wrong": "Option B is incorrect because Statement coverage does NOT guarantee branch coverage (e.g. an unstated 'else' branch can be missed), but branch coverage ALWAYS guarantees statement coverage.",
        "context": "Branch coverage is strictly stronger than statement coverage in the subsumption hierarchy of structural testing."
    },
    "w10_q5": {
        "correct": "Option A ('Linearly independent paths') is correct because Path Coverage aims to execute all linearly independent paths (basis paths) through the program's control flow graph.",
        "why_others_wrong": "Linearly dependent paths (Option B) are redundant linear combinations of basis paths and do not add test coverage.",
        "context": "The number of linearly independent paths in a program is mathematically equal to McCabe's Cyclomatic Complexity."
    },
    "w10_q6": {
        "correct": "Option A ('E-N+2') is correct because McCabe's formula for Cyclomatic Complexity of a connected control flow graph is V(G) = E - N + 2P, where E is the number of edges, N is the number of nodes, and P is connected components (P = 1 for a single procedure, giving E - N + 2).",
        "why_others_wrong": "Options B, C, and D are algebraic variants with incorrect signs or constants.",
        "context": "Cyclomatic complexity can also be calculated as: Number of Closed Predicate Nodes + 1, or the total number of bounded regions + 1."
    },
    "w10_q7": {
        "correct": "Option C ('Acceptance testing') is correct because the three standard sequential phases of system validation and deployment testing are: Alpha testing (in-house with simulated users), Beta testing (field testing with actual end-users in real environments), and Final Acceptance testing (sign-off against contractual requirements).",
        "why_others_wrong": "Gama, Sigma, and Omega testing are fictitious or non-standard testing names.",
        "context": "Acceptance testing determines whether the customer formally accepts delivery and authorizes payment."
    },
    "w10_q8": {
        "correct": "Option B ('Large') is correct because Volume Testing tests the system's performance, stability, and memory degradation when subjected to massive, heavy volumes of data (e.g. millions of database records or continuous massive file uploads).",
        "why_others_wrong": "Small inputs (Option A) evaluate basic functional correctness, not volume stress.",
        "context": "Volume testing uncovers database index bottlenecks, disk capacity limits, and buffer overflow memory leaks."
    },
    "w10_q9": {
        "correct": "Option B ('Four') is correct because empirical research in HCI and software engineering progresses across 4 fundamental stages: 1. Formulate testable research questions and hypotheses, 2. Design the experimental protocol, 3. Execute observation and collect data, 4. Perform statistical analysis and draw conclusions.",
        "why_others_wrong": "Three, Five, and Six do not match the standard 4-stage empirical research framework taught in the course.",
        "context": "Following the four stages prevents post-hoc data dredging and ensures statistical validity."
    },
    "w10_q10": {
        "correct": "Option B ('Empirical') is correct because data acquired directly through systematic sensory observation, experimental testing, or measurement in the physical world is termed Empirical Data.",
        "why_others_wrong": "Option A is a stray OCR artifact. Authoritative (Option C) relies on dogma/authority. Experiential (Option D) refers to subjective personal perception.",
        "context": "Empirical data forms the foundation of scientific evaluation in HCI, superseding subjective designer intuition."
    },

    # WEEK 11
    "w11_q1": {
        "correct": "Option C ('empirical research') is correct because conducting controlled laboratory experiments to systematically observe, record, and statistically evaluate user behavior across interface conditions is the definition of Empirical Research.",
        "why_others_wrong": "Programmable, hypothetical, and theoretical research describe mathematical proofs or simulations, not controlled human experiments.",
        "context": "Empirical research tests causal relationships between interface designs and user performance."
    },
    "w11_q2": {
        "correct": "Option C ('four') is correct because empirical research consists of 4 broad stages: 1. Research Question & Hypothesis Formulation, 2. Experimental Design, 3. Data Collection, 4. Statistical Analysis & Interpretation.",
        "why_others_wrong": "Two, three, and five are incorrect counts for the course's empirical research stages.",
        "context": "Methodological rigor across all 4 stages is required to achieve high internal and external validity."
    },
    "w11_q3": {
        "correct": "Option A ('testable, non-testable') is correct because RQ3 ('Does the new interface let me enter text faster than MS Word?') is a Testable research question because 'faster' can be quantitatively measured in words-per-minute (WPM) or seconds. RQ1 ('Is the new technique good?') is Non-testable because 'good' is vague, subjective, and undefined.",
        "why_others_wrong": "Alternative and null hypotheses (Option B) are statistical formalizations of testable questions, not classifications of research questions.",
        "context": "A valid scientific research question must be operationalized with measurable metrics."
    },
    "w11_q4": {
        "correct": "Option A ('null hypothesis') is correct because the Null Hypothesis (H0) is the baseline proposition stating that the manipulated independent variable will have NO effect on the outcome (any observed difference is due purely to random sampling error).",
        "why_others_wrong": "The Alternative Hypothesis (Option B, H1) predicts that there IS a real, significant difference caused by the experimental treatment.",
        "context": "In significance testing, statistical tests evaluate whether the evidence is strong enough to reject the null hypothesis."
    },
    "w11_q5": {
        "correct": "Option A ('1 Point' - Nominal scale) is correct because assigning arbitrary numerical or symbolic codes to observational attributes without any mathematical order or magnitude (e.g. 1 = Male, 2 = Female, or 1 = Mouse, 2 = Touchpad) is the definition of a Nominal Measurement Scale. (Note: Option A is the official accepted key in NPTEL).",
        "why_others_wrong": "Ordinal data (Option B) conveys ranked order (e.g. 1st, 2nd, 3rd). Interval data (Option C) has equal distances between points. Ratio data (Option D) has a true zero point.",
        "context": "Stevens' four levels of measurement are: Nominal, Ordinal, Interval, and Ratio."
    },
    "w11_q6": {
        "correct": "Option A is correct because temperature measured on a thermometer (Celsius or Fahrenheit) is the textbook definition of Interval Scaled Data: distances between degrees are equal, but the zero point (0°C) is arbitrary and does not represent the complete absence of heat.",
        "why_others_wrong": "Option B ('False') is incorrect because Celsius/Fahrenheit temperature is universally classified as interval data (unlike Kelvin which is ratio scale).",
        "context": "Because interval data lacks an absolute zero, you can state that 30°C is 10° warmer than 20°C, but NOT that 30°C is 'twice as hot' as 15°C."
    },
    "w11_q7": {
        "correct": "Option C ('Confounding variables') is correct because Confounding Variables are extraneous, uncontrolled factors that correlate with both the independent and dependent variables, introducing systematic bias and misleading causal conclusions.",
        "why_others_wrong": "Dependent variables (Option A) are the measured metrics. Independent variables (Option B) are the factors manipulated by researchers. Control variables (Option D) are variables deliberately held constant.",
        "context": "For example, in comparing typing speed across two interfaces, participant prior typing expertise is a major confound that must be controlled through counterbalancing."
    },
    "w11_q8": {
        "correct": "Option A ('True') is correct because in qualitative pilot usability studies and formative testing, Jakob Nielsen's mathematical research curve demonstrated that 5 participants uncover approximately 85% of usability flaws.",
        "why_others_wrong": "Option B is incorrect because testing 5 users is the gold standard for quick discount pilot iterations.",
        "context": "Running multiple small tests with 5 participants each and iterating between runs is far more effective than running one massive test with 25 users at the end."
    },
    "w11_q9": {
        "correct": "Option C ('12, 25') is correct because in quantitative empirical experiments in HCI, achieving statistical significance and adequate statistical power (power >= 0.80) typically requires between 12 and 25 participants per experimental group.",
        "why_others_wrong": "1 to 5 participants (Options A and B) are far too few for quantitative inferential statistics (t-tests, ANOVA) due to high variance. 10 to 12 is borderline.",
        "context": "Using 12 to 24 participants allows standard counterbalancing designs (e.g. Balanced Latin Square) to eliminate order effects."
    },
    "w11_q10": {
        "correct": "Option A ('between-subject') is correct because when participants are partitioned into separate distinct groups such that each group tests ONLY ONE interface condition, the experimental design is classified as a Between-Subjects (independent measures) study.",
        "why_others_wrong": "Within-subject (Option B) occurs when EVERY participant tests ALL conditions. Uni-subject and center-subject are non-existent terms.",
        "context": "Between-subjects designs eliminate learning and fatigue carryover effects between conditions, but require larger sample sizes."
    },

    # WEEK 12
    "w12_q1": {
        "correct": "Option B ('Refute') is correct because in inferential statistical significance testing, the scientific method attempts to REFUTE (reject) the null hypothesis (H0). If H0 is rejected (p < 0.05), we accept the alternative hypothesis (H1) that the design change produced a real effect.",
        "why_others_wrong": "Scientists never set out to 'accept' the null hypothesis (Option A); statistically, we either reject H0 or fail to reject H0.",
        "context": "Rejecting the null hypothesis confirms that the observed performance improvement is unlikely to have occurred by random luck."
    },
    "w12_q2": {
        "correct": "Option A ('False positive') is correct because a Type I Error (alpha error) occurs when the researcher rejects a true null hypothesis—claiming that an effect or difference exists when in reality it was purely random chance (a False Positive).",
        "why_others_wrong": "Type II Error (beta error) is a False Negative (failing to detect a real effect). True positive and true negative represent correct statistical decisions.",
        "context": "Standard significance level alpha is set at 0.05, meaning we accept a maximum 5% risk of committing a Type I error."
    },
    "w12_q3": {
        "correct": "Option B ('False') is correct because the t-statistic (t-test) is NOT the only way to test for significance. Researchers widely use ANOVA (F-test), Chi-Square tests, Mann-Whitney U tests, Wilcoxon signed-rank tests, and Kruskal-Wallis tests depending on data distribution and variable levels.",
        "why_others_wrong": "Claiming t-test is the ONLY technique is mathematically incorrect.",
        "context": "When evaluating more than two conditions or factorial designs, ANOVA is required to avoid inflating family-wise error rates."
    },
    "w12_q4": {
        "correct": "Option A ('Parametric and Non-parametric') is correct because statistical significance testing techniques are broadly classified into Parametric tests (which assume data follows a specific distribution, usually normal, e.g. t-test, ANOVA) and Non-Parametric tests (distribution-free tests used for ranked or skewed data, e.g. Mann-Whitney, Chi-Square).",
        "why_others_wrong": "'t-test and non t-test' (Option B) is an informal, non-scientific dichotomy.",
        "context": "Parametric tests offer higher statistical power when assumptions are met, while non-parametric tests protect against skewed outliers."
    },
    "w12_q5": {
        "correct": "Option A ('True') is correct because project planning in software engineering fundamentally revolves around estimating four core interdependent parameters: Project Size (KLOC, Function Points), Cost (budget), Duration (calendar time/schedule), and Effort (person-months).",
        "why_others_wrong": "Option B is incorrect because these four parameters constitute the classic project estimation quadruple.",
        "context": "Effort estimation directly drives project cost and team staffing schedules."
    },
    "w12_q6": {
        "correct": "Option B ('Constructive Cost Estimation Model') is correct because COCOMO stands for Constructive Cost Estimation Model, an algorithmic software cost estimation model developed by Barry Boehm in 1981.",
        "why_others_wrong": "Options A, C, and D invent incorrect words ('Conducive', 'Category') instead of 'Constructive Cost'.",
        "context": "COCOMO uses regression formulas based on project size (KLOC) to estimate development effort and schedule duration."
    },
    "w12_q7": {
        "correct": "Option B ('Three') is correct because Barry Boehm structured COCOMO into 3 distinct hierarchical levels of estimation: 1. Basic COCOMO (quick, single-variable calculation), 2. Intermediate COCOMO (incorporates 15 cost driver cost multipliers), 3. Detailed COCOMO (assesses cost drivers at each subsystem and module phase).",
        "why_others_wrong": "Two, Four, and Five are incorrect counts of the COCOMO estimation hierarchy.",
        "context": "Progressing from Basic to Detailed COCOMO improves estimation accuracy as architectural details crystallize."
    },
    "w12_q8": {
        "correct": "Option A ('True') is correct because Agile development methods emphasize short, iterative timeboxed sprints (typically 1 to 4 weeks), continuous integration, and frequent customer feedback, ensuring rapid turnaround of working software increments.",
        "why_others_wrong": "Option B is incorrect because fast turnaround and adaptability to changing requirements are the defining hallmarks of the Agile manifesto.",
        "context": "Agile eliminates the multi-month delivery delays typical of rigid Waterfall projects."
    },
    "w12_q9": {
        "correct": "Option B ('Agile') is correct because Scrum is the world's most widely adopted Agile project management framework, featuring Sprints, Product Backlogs, Daily Standups, and Sprint Retrospectives.",
        "why_others_wrong": "Traditional SDLC (Option A) refers to sequential models like Waterfall. Option D ('1 Point') is a stray OCR label.",
        "context": "Scrum empowers cross-functional self-organizing teams to iteratively inspect and adapt."
    },
    "w12_q10": {
        "correct": "Option A ('Duration planned') is correct because in a Gantt Chart, horizontal bars represent project activities, and the horizontal length of each bar is directly proportional to the planned calendar duration (start date to end date) of that activity along the timeline.",
        "why_others_wrong": "Effort (Option B, person-hours) and Cost (Option C, money) are resource parameters, not the physical horizontal timeline axis of a Gantt chart.",
        "context": "Gantt charts visually illustrate project milestones, dependencies, and critical path schedules."
    }
}

# Update questions with enriched explanations
updated_count = 0
for q in questions:
    q_id = q['id']
    if q_id in explanations:
        info = explanations[q_id]
        enriched_text = f"**Why it's Correct:** {info['correct']}\n\n**Why Other Options are Incorrect:** {info['why_others_wrong']}\n\n**Course Context:** {info['context']}"
        q['explanation'] = enriched_text
        updated_count += 1
    else:
        # Fallback if somehow missing
        q['explanation'] = f"The official accepted answer is Option {', '.join(q['correctAnswers']).toUpperCase()}."

with open('src/data/questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, indent=2)

print(f"Enriched {updated_count} / {len(questions)} questions with comprehensive academic explanations!")
