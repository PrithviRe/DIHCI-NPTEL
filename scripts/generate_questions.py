import json

assignments = [
    # Week 1
    {
        "week": 1,
        "topic": "Introduction to HCI & Human Sensory/Cognitive Systems",
        "questions": [
            {
                "num": 1,
                "type": "single",
                "prompt": "According to cognitive psychology models of human memory, what is the typical capacity of human Working (Short-Term) Memory according to George Miller?",
                "options": [
                    {"id": "a", "text": "3 ± 1 chunks"},
                    {"id": "b", "text": "7 ± 2 chunks"},
                    {"id": "c", "text": "12 ± 2 chunks"},
                    {"id": "d", "text": "Virtually unlimited chunks"}
                ],
                "correct": ["b"],
                "explanation": "Miller's Law (1956) posits that human short-term working memory can hold approximately 7 ± 2 informational chunks at a time."
            },
            {
                "num": 2,
                "type": "single",
                "prompt": "Which component of the human visual system is primarily responsible for color vision and high visual acuity under well-lit conditions?",
                "options": [
                    {"id": "a", "text": "Rods in the peripheral retina"},
                    {"id": "b", "text": "Cones concentrated in the fovea centralis"},
                    {"id": "c", "text": "Ganglion cells along the optic disc"},
                    {"id": "d", "text": "Ciliary muscles"}
                ],
                "correct": ["b"],
                "explanation": "Cones are densely packed in the fovea and are responsible for photopic (daylight/color) vision and fine spatial resolution, whereas rods operate in scotopic (low-light) conditions."
            },
            {
                "num": 3,
                "type": "multiple",
                "prompt": "Which of the following sensory memory stores are recognized in the Model Human Processor? (Select all that apply)",
                "options": [
                    {"id": "a", "text": "Iconic memory (visual sensory store)"},
                    {"id": "b", "text": "Echoic memory (auditory sensory store)"},
                    {"id": "c", "text": "Haptic memory (tactile sensory store)"},
                    {"id": "d", "text": "Procedural motor memory"}
                ],
                "correct": ["a", "b", "c"],
                "explanation": "Sensory memory consists of iconic (visual, ~200-500ms), echoic (auditory, ~2-4s), and haptic (touch) stores. Procedural memory belongs to long-term memory."
            },
            {
                "num": 4,
                "type": "single",
                "prompt": "In Human-Computer Interaction, what does the 'Model Human Processor' proposed by Card, Moran, and Newell consist of?",
                "options": [
                    {"id": "a", "text": "Perceptual system, Cognitive system, and Motor system"},
                    {"id": "b", "text": "Input system, Output system, and Storage system"},
                    {"id": "c", "text": "Sensory buffer, Operating system, and Execution thread"},
                    {"id": "d", "text": "Hardware layer, Middleware, and Application layer"}
                ],
                "correct": ["a"],
                "explanation": "The Model Human Processor (MHP) models human interaction through three interacting subsystems: Perceptual, Cognitive, and Motor subsystems, each with its own memory and processor cycle time."
            },
            {
                "num": 5,
                "type": "single",
                "prompt": "What is the typical decay half-life of visual iconic memory in the Model Human Processor?",
                "options": [
                    {"id": "a", "text": "Approximately 10 milliseconds"},
                    {"id": "b", "text": "Approximately 200 milliseconds (100–300 ms)"},
                    {"id": "c", "text": "Approximately 7 seconds"},
                    {"id": "d", "text": "Permanent unless overwritten"}
                ],
                "correct": ["b"],
                "explanation": "Visual sensory memory (iconic store) has a rapid decay half-life of roughly 200 ms (typically cited between 100-300 ms)."
            },
            {
                "num": 6,
                "type": "single",
                "prompt": "Which visual phenomenon explains why static frames presented at 24 or more frames per second are perceived as continuous fluid motion?",
                "options": [
                    {"id": "a", "text": "Tunnel vision"},
                    {"id": "b", "text": "Flicker fusion / Persistence of vision"},
                    {"id": "c", "text": "Chromatic aberration"},
                    {"id": "d", "text": "Motion parallax"}
                ],
                "correct": ["b"],
                "explanation": "Persistence of vision and the flicker fusion threshold cause intermittent visual stimuli above ~24-60 Hz to blend into a seamless sensation of continuous motion."
            },
            {
                "num": 7,
                "type": "multiple",
                "prompt": "Which of the following are characteristics of Long-Term Memory (LTM)? (Select all that apply)",
                "options": [
                    {"id": "a", "text": "Virtually unlimited storage capacity"},
                    {"id": "b", "text": "Extremely fast read access (under 10ms)"},
                    {"id": "c", "text": "Information decay occurs primarily through interference or retrieval failure"},
                    {"id": "d", "text": "Information is subdivided into episodic and semantic memory"}
                ],
                "correct": ["a", "c", "d"],
                "explanation": "LTM has practically infinite capacity, consists of episodic and semantic knowledge, and forgetting occurs through retroactive/proactive interference; retrieval takes longer (~70ms) than 10ms."
            },
            {
                "num": 8,
                "type": "single",
                "prompt": "Why is 'recognition' cognitively preferred over 'recall' in interactive interface design?",
                "options": [
                    {"id": "a", "text": "Recall requires no memory cues, making it faster"},
                    {"id": "b", "text": "Recognition provides sensory perceptual cues that trigger memory retrieval directly"},
                    {"id": "c", "text": "Recognition consumes more short-term memory resources than recall"},
                    {"id": "d", "text": "Computers process recognition queries faster than recall commands"}
                ],
                "correct": ["b"],
                "explanation": "Recognition presents options visibly (like menus/icons), allowing users to leverage perceptual memory cues rather than dredging information from long-term memory unprompted."
            },
            {
                "num": 9,
                "type": "single",
                "prompt": "In the human motor system, what is the typical cycle time of the motor processor in the Model Human Processor?",
                "options": [
                    {"id": "a", "text": "10 ms"},
                    {"id": "b", "text": "70 ms (approx. 30–100 ms)"},
                    {"id": "c", "text": "500 ms"},
                    {"id": "d", "text": "1200 ms"}
                ],
                "correct": ["b"],
                "explanation": "The motor processor cycle time (tau_m) is empirically determined to average around 70 ms (with typical ranges between 30 and 100 ms)."
            },
            {
                "num": 10,
                "type": "multiple",
                "prompt": "Which of the following are primary goals of Human-Computer Interaction (HCI)? (Select all that apply)",
                "options": [
                    {"id": "a", "text": "Developing usable, safe, and effective interactive computing systems"},
                    {"id": "b", "text": "Maximizing user satisfaction and minimizing user frustration"},
                    {"id": "c", "text": "Requiring users to adapt their cognitive styles to machine architectures"},
                    {"id": "d", "text": "Enhancing user performance (speed, accuracy, and efficiency)"}
                ],
                "correct": ["a", "b", "d"],
                "explanation": "HCI focuses on designing systems centered on human capabilities (Option A, B, D). Forcing humans to adapt unnaturally to machine architectures is the antithesis of user-centered design."
            }
        ]
    },

    # Week 2
    {
        "week": 2,
        "topic": "Design Frameworks & Norman's 7 Stages of Action Model",
        "questions": [
            {
                "num": 1,
                "type": "single",
                "prompt": "In Donald Norman's 7 Stages of Action model, what constitutes the 'Gulf of Execution'?",
                "options": [
                    {"id": "a", "text": "The difference between user intentions and allowable actions provided by the system"},
                    {"id": "b", "text": "The time delay between computer processing and network transmission"},
                    {"id": "c", "text": "The mismatch between the user's interpretation and actual physical system state"},
                    {"id": "d", "text": "The gap between software requirements and final deployment"}
                ],
                "correct": ["a"],
                "explanation": "The Gulf of Execution measures how difficult it is for the user to translate psychological intentions into physical actions supported by the interface ('How do I perform this?')."
            },
            {
                "num": 2,
                "type": "single",
                "prompt": "What bridges the 'Gulf of Evaluation' in user interface design?",
                "options": [
                    {"id": "a", "text": "Clear, informative, and immediate feedback reflecting system state changes"},
                    {"id": "b", "text": "Hidden command-line shortcuts"},
                    {"id": "c", "text": "Comprehensive offline paper user manuals"},
                    {"id": "d", "text": "Faster network bandwidth"}
                ],
                "correct": ["a"],
                "explanation": "The Gulf of Evaluation ('What just happened?') is bridged when the system provides visible, immediate, and unambiguous feedback that matches the user's conceptual model."
            },
            {
                "num": 3,
                "type": "multiple",
                "prompt": "Which of the following belong to the Execution side of Norman's 7 Stages of Action? (Select all that apply)",
                "options": [
                    {"id": "a", "text": "Forming the intention"},
                    {"id": "b", "text": "Specifying the action sequence"},
                    {"id": "c", "text": "Executing the action"},
                    {"id": "d", "text": "Perceiving the state of the world"}
                ],
                "correct": ["a", "b", "c"],
                "explanation": "The Execution stages are: 1. Forming intention, 2. Specifying action, 3. Executing action. Perceiving, interpreting, and evaluating belong to the Evaluation phase."
            },
            {
                "num": 4,
                "type": "single",
                "prompt": "What is the key distinction between an 'Affordance' and a 'Signifier' according to Don Norman?",
                "options": [
                    {"id": "a", "text": "Affordance is software-only; Signifiers are hardware-only"},
                    {"id": "b", "text": "Affordances are what actions are physically possible; Signifiers signal where and how to act"},
                    {"id": "c", "text": "Signifiers exist naturally, while Affordances must always be painted or labeled"},
                    {"id": "d", "text": "They are exact synonyms in modern design terminology"}
                ],
                "correct": ["b"],
                "explanation": "Affordances determine what interactions are possible between an actor and an object. Signifiers communicate where and how that action should take place (e.g., a 'Push' sign on a flat plate)."
            },
            {
                "num": 5,
                "type": "single",
                "prompt": "Which design principle is exemplified by placing the burner control knobs of a kitchen stove in the exact geometric arrangement of the burners themselves?",
                "options": [
                    {"id": "a", "text": "Natural Mapping"},
                    {"id": "b", "text": "Semantic constraint"},
                    {"id": "c", "text": "Consistency violation"},
                    {"id": "d", "text": "Error tolerance"}
                ],
                "correct": ["a"],
                "explanation": "Natural Mapping exploits spatial analogies and physical relationships between controls and their real-world outcomes, reducing cognitive translation."
            },
            {
                "num": 6,
                "type": "multiple",
                "prompt": "Which of the following are categories of Constraints identified by Norman to prevent user error? (Select all that apply)",
                "options": [
                    {"id": "a", "text": "Physical constraints (e.g., key shape preventing reverse insertion)"},
                    {"id": "b", "text": "Semantic constraints (relying on knowledge of situations and world meaning)"},
                    {"id": "c", "text": "Cultural constraints (learned cultural conventions like red for stop)"},
                    {"id": "d", "text": "Logical constraints (deductive spatial or relational logic)"}
                ],
                "correct": ["a", "b", "c", "d"],
                "explanation": "Norman classifies constraints into four major types: Physical, Semantic, Cultural, and Logical constraints, all functioning to restrict erroneous actions."
            },
            {
                "num": 7,
                "type": "single",
                "prompt": "What is a 'Conceptual Model' in HCI?",
                "options": [
                    {"id": "a", "text": "A high-level diagram used only by database administrators"},
                    {"id": "b", "text": "The user's internal mental explanation of how a system works and behaves"},
                    {"id": "c", "text": "The physical silicon design of the CPU"},
                    {"id": "d", "text": "A marketing brochure describing user personas"}
                ],
                "correct": ["b"],
                "explanation": "A user's conceptual (mental) model is the internal simulation or belief of how a system operates, formed through interaction, signifiers, and feedback."
            },
            {
                "num": 8,
                "type": "single",
                "prompt": "In Norman's terminology, what is a 'Slip' as opposed to a 'Mistake'?",
                "options": [
                    {"id": "a", "text": "A Slip occurs when the goal is incorrect; a Mistake occurs when the action fails"},
                    {"id": "b", "text": "A Slip is an execution failure of a correct plan; a Mistake is the execution of a flawed plan/goal"},
                    {"id": "c", "text": "Slips only happen to novice users; Mistakes only happen to expert users"},
                    {"id": "d", "text": "A Slip is a hardware fault; a Mistake is a user fault"}
                ],
                "correct": ["b"],
                "explanation": "Slips happen when the intention/goal is correct but the physical execution goes awry (e.g., typo, clicking wrong neighboring icon). Mistakes happen when the mental goal or plan itself is inappropriate."
            },
            {
                "num": 9,
                "type": "single",
                "prompt": "A door has a flat brass plate on one side and a pull handle on the other side. What does the flat brass plate signify?",
                "options": [
                    {"id": "a", "text": "Push"},
                    {"id": "b", "text": "Pull"},
                    {"id": "c", "text": "Slide sideways"},
                    {"id": "d", "text": "Rotate"}
                ],
                "correct": ["a"],
                "explanation": "A flat plate physically only affords pushing because there is nothing to grasp for pulling, making it a natural signifier for pushing (unlike ambiguous 'Norman doors')."
            },
            {
                "num": 10,
                "type": "multiple",
                "prompt": "Which of the following are examples of good 'Feedback' in UI design? (Select all that apply)",
                "options": [
                    {"id": "a", "text": "Visual loading spinner indicating an asynchronous background request is underway"},
                    {"id": "b", "text": "Button color change or depressed visual state upon clicking"},
                    {"id": "c", "text": "Audio chime confirming successful file upload"},
                    {"id": "d", "text": "Completely freezing the screen without updating the cursor during a 30-second export"}
                ],
                "correct": ["a", "b", "c"],
                "explanation": "Loading spinners, depressed button states, and completion audio are clear, timely feedback. Freezing the screen creates an ambiguous state where the user cannot evaluate whether the system crashed."
            }
        ]
    },

    # Week 3
    {
        "week": 3,
        "topic": "Empirical Predictive Models: Fitts' Law & Hick's Law",
        "questions": [
            {
                "num": 1,
                "type": "single",
                "prompt": "What does Fitts' Law mathematically model in human-computer interaction?",
                "options": [
                    {"id": "a", "text": "The time required to rapidly move a pointer to a target area"},
                    {"id": "b", "text": "The time needed to decide which menu option to click"},
                    {"id": "c", "text": "The rate at which text is comprehended on a screen"},
                    {"id": "d", "text": "The rate of battery drainage during graphics rendering"}
                ],
                "correct": ["a"],
                "explanation": "Fitts' Law (1954) models rapid aimed movement time (MT) as a function of target distance D and target width W."
            },
            {
                "num": 2,
                "type": "single",
                "prompt": "What is the formula for the Index of Difficulty (ID) according to the Shannon formulation of Fitts' Law?",
                "options": [
                    {"id": "a", "text": "ID = log2(D / W + 1)"},
                    {"id": "b", "text": "ID = D * W"},
                    {"id": "c", "text": "ID = a + b * (D / W)"},
                    {"id": "d", "text": "ID = log10(D * W)"}
                ],
                "correct": ["a"],
                "explanation": "Mackenzie popularized the Shannon formulation ID = log2(D/W + 1), which prevents negative ID values when distance D is smaller than target width W."
            },
            {
                "num": 3,
                "type": "single",
                "prompt": "If the distance to a target is doubled while the target width is also doubled, what happens to the Index of Difficulty (ID) under Fitts' Law?",
                "options": [
                    {"id": "a", "text": "It quadruples"},
                    {"id": "b", "text": "It doubles"},
                    {"id": "c", "text": "It remains unchanged"},
                    {"id": "d", "text": "It drops to zero"}
                ],
                "correct": ["c"],
                "explanation": "Since ID depends on the ratio D/W, scaling both distance D and width W by 2 results in (2D)/(2W) = D/W, keeping the Index of Difficulty identical."
            },
            {
                "num": 4,
                "type": "single",
                "prompt": "According to Fitts' Law, why are the four corners of a computer monitor the easiest and fastest targets to click?",
                "options": [
                    {"id": "a", "text": "Because computer mice move faster diagonally"},
                    {"id": "b", "text": "Because cursor movement is physically stopped by screen boundaries, giving them effectively infinite target width (W = ∞)"},
                    {"id": "c", "text": "Because they have the highest pixel density"},
                    {"id": "d", "text": "Because users focus primarily on corners"}
                ],
                "correct": ["b"],
                "explanation": "On displays where the cursor cannot overshoot the physical edges, the screen edges and corners effectively have infinite width (W = ∞), making overshoot impossible."
            },
            {
                "num": 5,
                "type": "single",
                "prompt": "What does the Hick-Hyman Law quantify?",
                "options": [
                    {"id": "a", "text": "Decision time as a logarithmic function of the number of options"},
                    {"id": "b", "text": "Physical hand fatigue over extended keyboard typing"},
                    {"id": "c", "text": "Visual search time in crowded color diagrams"},
                    {"id": "d", "text": "The rate at which memory decays over hours"}
                ],
                "correct": ["a"],
                "explanation": "The Hick-Hyman Law states that choice reaction time increases logarithmically with the number of alternative choices presented: T = b * log2(n + 1)."
            },
            {
                "num": 6,
                "type": "multiple",
                "prompt": "Which of the following design techniques directly leverage Fitts' Law to improve interaction efficiency? (Select all that apply)",
                "options": [
                    {"id": "a", "text": "Making frequently used action buttons larger in size"},
                    {"id": "b", "text": "Placing contextual pie menus (radial menus) right at the current cursor location"},
                    {"id": "c", "text": "Placing destructive action buttons at zero distance from common confirm buttons"},
                    {"id": "d", "text": "Pinning menus to the top screen edge (Mac OS style)"}
                ],
                "correct": ["a", "b", "d"],
                "explanation": "Increasing width W (Option A), minimizing distance D to 0 via radial menus (Option B), and leveraging screen edges (Option D) are classic Fitts' Law optimizations."
            },
            {
                "num": 7,
                "type": "single",
                "prompt": "What unit is Index of Performance (IP) or Throughput (TP) in Fitts' Law measured in?",
                "options": [
                    {"id": "a", "text": "Pixels per millisecond"},
                    {"id": "b", "text": "Bits per second (bps)"},
                    {"id": "c", "text": "G-forces"},
                    {"id": "d", "text": "Hertz (Hz)"}
                ],
                "correct": ["b"],
                "explanation": "Throughput = ID / MT, where ID is measured in bits and MT in seconds, yielding bits per second (bps)."
            },
            {
                "num": 8,
                "type": "single",
                "prompt": "Under what condition does Hick's Law NOT accurately predict user reaction time?",
                "options": [
                    {"id": "a", "text": "When users are complete novices faced with unfamiliar options"},
                    {"id": "b", "text": "When options are organized alphabetically"},
                    {"id": "c", "text": "When users are highly trained experts with automated recall of options or shortcuts"},
                    {"id": "d", "text": "When there are more than 4 choices"}
                ],
                "correct": ["c"],
                "explanation": "Experts bypass decision scanning because actions are automated into direct memory retrieval or muscle memory; Hick's law only holds when conscious decision scanning is required."
            },
            {
                "num": 9,
                "type": "single",
                "prompt": "In the linear equation of Fitts' Law MT = a + b * ID, what does the coefficient 'b' represent?",
                "options": [
                    {"id": "a", "text": "Start-stop acceleration intercept"},
                    {"id": "b", "text": "The slope of the line, representing movement time added per bit of difficulty (reciprocal of throughput)"},
                    {"id": "c", "text": "Display aspect ratio"},
                    {"id": "d", "text": "Mouse sensor DPI"}
                ],
                "correct": ["b"],
                "explanation": "The coefficient 'b' is the slope; its inverse (1/b) is the device's Index of Performance or processing bandwidth in bits per second."
            },
            {
                "num": 10,
                "type": "multiple",
                "prompt": "Why are linear pulldown menus on screen corners faster than cascading submenus according to Fitts' and Steering Laws? (Select all that apply)",
                "options": [
                    {"id": "a", "text": "Cascading menus constrain the cursor to a narrow tunnel, subject to Accot-Zhai Steering Law"},
                    {"id": "b", "text": "Cascading submenus require higher precision to avoid disappearing upon cursor drift"},
                    {"id": "c", "text": "Screen corners cannot be overshot"},
                    {"id": "d", "text": "Cascading menus completely disable mouse acceleration"}
                ],
                "correct": ["a", "b", "c"],
                "explanation": "Accot-Zhai Steering law proves that traversing constrained tunnels is much slower and error-prone than moving to an unbounded target edge or corner."
            }
        ]
    },

    # Week 4
    {
        "week": 4,
        "topic": "Cognitive & Task Modeling: GOMS & Keystroke-Level Model (KLM)",
        "questions": [
            {
                "num": 1,
                "type": "single",
                "prompt": "What do the letters in the acronym GOMS stand for?",
                "options": [
                    {"id": "a", "text": "Graphics, Objects, Methods, Systems"},
                    {"id": "b", "text": "Goals, Operators, Methods, Selection Rules"},
                    {"id": "c", "text": "General Organization of Motor Skills"},
                    {"id": "d", "text": "Guidelines, Operations, Metrics, Standards"}
                ],
                "correct": ["b"],
                "explanation": "GOMS stands for Goals (user aims), Operators (elementary actions), Methods (procedures achieving goals), and Selection rules (deciding among competing methods)."
            },
            {
                "num": 2,
                "type": "single",
                "prompt": "What type of user behavior does the Keystroke-Level Model (KLM) predict?",
                "options": [
                    {"id": "a", "text": "Novice users exploring an unfamiliar website"},
                    {"id": "b", "text": "Error-free task execution time by expert users performing routine tasks"},
                    {"id": "c", "text": "Time taken by users to recover from severe software crashes"},
                    {"id": "d", "text": "Creative problem solving while writing complex code"}
                ],
                "correct": ["b"],
                "explanation": "KLM is specifically designed for expert, error-free execution of routine cognitive and motor tasks."
            },
            {
                "num": 3,
                "type": "single",
                "prompt": "In the standard Keystroke-Level Model (KLM), what is the typical empirical duration assigned to the Mental Preparation operator (M)?",
                "options": [
                    {"id": "a", "text": "0.20 seconds"},
                    {"id": "b", "text": "0.40 seconds"},
                    {"id": "c", "text": "1.35 seconds"},
                    {"id": "d", "text": "5.00 seconds"}
                ],
                "correct": ["c"],
                "explanation": "Card, Moran, and Newell established 1.35 seconds as the standard benchmark duration for the mental preparation operator M."
            },
            {
                "num": 4,
                "type": "single",
                "prompt": "Which KLM operator represents switching hands between the mouse and keyboard (or vice versa)?",
                "options": [
                    {"id": "a", "text": "Operator P (Pointing)"},
                    {"id": "b", "text": "Operator H (Homing)"},
                    {"id": "c", "text": "Operator K (Keystroke)"},
                    {"id": "d", "text": "Operator M (Mental)"}
                ],
                "correct": ["b"],
                "explanation": "H stands for Homing, which takes approximately 0.40 seconds when transitioning between physical input devices (e.g. keyboard to mouse)."
            },
            {
                "num": 5,
                "type": "single",
                "prompt": "In KLM, what is the standard approximate time assigned to the Pointing operator (P) using a mouse?",
                "options": [
                    {"id": "a", "text": "0.05 seconds"},
                    {"id": "b", "text": "1.10 seconds"},
                    {"id": "c", "text": "3.50 seconds"},
                    {"id": "d", "text": "10.0 seconds"}
                ],
                "correct": ["b"],
                "explanation": "Pointing (P) to a target with a mouse averages approximately 1.10 seconds according to standard KLM tables (derived from typical Fitts' law movements)."
            },
            {
                "num": 6,
                "type": "multiple",
                "prompt": "Which of the following are operators included in Card, Moran, and Newell's Keystroke-Level Model? (Select all that apply)",
                "options": [
                    {"id": "a", "text": "K (Keystroke or button press)"},
                    {"id": "b", "text": "P (Pointing to a target on display)"},
                    {"id": "c", "text": "H (Homing hands on device)"},
                    {"id": "d", "text": "D (Drawing straight line segments)"}
                ],
                "correct": ["a", "b", "c", "d"],
                "explanation": "All four (K, P, H, D), along with M (Mental preparation) and R (System response time), constitute the core KLM operator set."
            },
            {
                "num": 7,
                "type": "single",
                "prompt": "According to the heuristic rules for placing Mental operators (M) in KLM, what should you do if an operator is fully anticipated by the preceding action (e.g. typing continuous characters of a known word)?",
                "options": [
                    {"id": "a", "text": "Double the M operator time"},
                    {"id": "b", "text": "Remove the M operator"},
                    {"id": "c", "text": "Replace the M operator with an H operator"},
                    {"id": "d", "text": "Add a System Response (R) operator"}
                ],
                "correct": ["b"],
                "explanation": "Heuristic Rule 2 states: If an operator is part of a cognitive unit (like typing consecutive characters in a chunked word), remove the M operator before subsequent keystrokes."
            },
            {
                "num": 8,
                "type": "single",
                "prompt": "What is the primary difference between GOMS and KLM?",
                "options": [
                    {"id": "a", "text": "KLM is a simplified, non-hierarchical, purely serial version of GOMS focusing on physical keystrokes"},
                    {"id": "b", "text": "GOMS can only model touchscreens, while KLM models VR headsets"},
                    {"id": "c", "text": "KLM models user emotions and GOMS models hardware registers"},
                    {"id": "d", "text": "GOMS does not include goals"}
                ],
                "correct": ["a"],
                "explanation": "KLM is the simplest variant of GOMS; it flattens the hierarchy and assumes a pre-determined method with no conditional selection rules."
            },
            {
                "num": 9,
                "type": "single",
                "prompt": "Suppose an expert user needs to move their hand from keyboard to mouse (H), point to an icon (P), and click it (K). Assuming one mental preparation (M), what is the predicted execution time? (H = 0.4s, P = 1.1s, K = 0.2s, M = 1.35s)",
                "options": [
                    {"id": "a", "text": "1.70 seconds"},
                    {"id": "b", "text": "3.05 seconds"},
                    {"id": "c", "text": "4.50 seconds"},
                    {"id": "d", "text": "0.95 seconds"}
                ],
                "correct": ["b"],
                "explanation": "Total Time = T_M + T_H + T_P + T_K = 1.35 + 0.40 + 1.10 + 0.20 = 3.05 seconds."
            },
            {
                "num": 10,
                "type": "multiple",
                "prompt": "Which of the following limitations apply to KLM and standard GOMS models? (Select all that apply)",
                "options": [
                    {"id": "a", "text": "They assume error-free performance and do not predict error recovery time"},
                    {"id": "b", "text": "They do not capture fatigue, cognitive load changes, or emotional state"},
                    {"id": "c", "text": "They only apply to expert users executing routine tasks"},
                    {"id": "d", "text": "They cannot predict the physical time required to press a keyboard key"}
                ],
                "correct": ["a", "b", "c"],
                "explanation": "GOMS/KLM models expert routine error-free performance without modeling emotional state or fatigue (Option A, B, C). Option D is incorrect because predicting keystroke times is KLM's core purpose."
            }
        ]
    },

    # Week 5
    {
        "week": 5,
        "topic": "Design Principles & Shneiderman's 8 Golden Rules",
        "questions": [
            {
                "num": 1,
                "type": "single",
                "prompt": "Which of Shneiderman's 8 Golden Rules is supported by providing clear feedback that an action sequence has concluded (e.g. showing a confirmation receipt after checkout)?",
                "options": [
                    {"id": "a", "text": "Strive for consistency"},
                    {"id": "b", "text": "Design dialogs to yield closure"},
                    {"id": "c", "text": "Support internal locus of control"},
                    {"id": "d", "text": "Permit easy reversal of actions"}
                ],
                "correct": ["b"],
                "explanation": "Yielding closure organizes actions into a beginning, middle, and end, giving users the satisfaction of completion and signaling them to clear their mental scratchpad."
            },
            {
                "num": 2,
                "type": "single",
                "prompt": "Why is 'Permit easy reversal of actions' (Undo/Redo) considered vital in user interface design?",
                "options": [
                    {"id": "a", "text": "It relieves anxiety because the user knows that mistakes can be painlessly rectified, encouraging exploration"},
                    {"id": "b", "text": "It minimizes the database storage requirement"},
                    {"id": "c", "text": "It forces novice users to re-read instructions"},
                    {"id": "d", "text": "It replaces the need for input validation"}
                ],
                "correct": ["a"],
                "explanation": "Reversible actions reduce exploration anxiety, giving users confidence that trying new features will not cause irreversible destruction."
            },
            {
                "num": 3,
                "type": "single",
                "prompt": "What does 'Support internal locus of control' mean in Shneiderman's rules?",
                "options": [
                    {"id": "a", "text": "Experienced users strongly desire the sense that they are in charge of the system and that the system responds to their commands, rather than the system taking unprompted control"},
                    {"id": "b", "text": "The computer should automatically make all decisions without consulting the user"},
                    {"id": "c", "text": "The CPU internal clock must regulate user speed"},
                    {"id": "d", "text": "All computation must run on local server hardware"}
                ],
                "correct": ["a"],
                "explanation": "Users feel comfortable and empowered when they perceive that they initiate actions, rather than feeling trapped by unexpected system surprises or interruptions."
            },
            {
                "num": 4,
                "type": "multiple",
                "prompt": "Which of the following are included in Ben Shneiderman's 8 Golden Rules of Interface Design? (Select all that apply)",
                "options": [
                    {"id": "a", "text": "Strive for consistency"},
                    {"id": "b", "text": "Offer informative feedback"},
                    {"id": "c", "text": "Prevent errors"},
                    {"id": "d", "text": "Maximize short-term memory load"}
                ],
                "correct": ["a", "b", "c"],
                "explanation": "Rule 8 is to REDUCE short-term memory load, not maximize it. Rules 1, 3, and 5 are consistency, informative feedback, and error prevention."
            },
            {
                "num": 5,
                "type": "single",
                "prompt": "Disabling or graying out a 'Submit' button until all mandatory form fields are properly filled is an example of which design principle?",
                "options": [
                    {"id": "a", "text": "Error prevention"},
                    {"id": "b", "text": "Fitts' Law violation"},
                    {"id": "c", "text": "Hick's Law violation"},
                    {"id": "d", "text": "Recall over recognition"}
                ],
                "correct": ["a"],
                "explanation": "Error prevention designs the interface such that erroneous inputs cannot be executed in the first place, rather than displaying an angry error dialog after the fact."
            },
            {
                "num": 6,
                "type": "single",
                "prompt": "In interface typography, why is using all-capital letters for body paragraphs considered bad practice?",
                "options": [
                    {"id": "a", "text": "All-caps text lacks distinctive ascenders and descenders, creating uniform rectangular word bounding boxes that slow down reading speed by 10-15%"},
                    {"id": "b", "text": "All-caps text requires double the font rendering memory"},
                    {"id": "c", "text": "Web browsers fail to render uppercase characters"},
                    {"id": "d", "text": "Capital letters cannot be parsed by screen readers"}
                ],
                "correct": ["a"],
                "explanation": "Readers recognize familiar word shapes (Bouma) formed by lowercase ascenders (b, d, h) and descenders (p, q, y). Uniform rectangular capital blocks eliminate these perceptual cues."
            },
            {
                "num": 7,
                "type": "multiple",
                "prompt": "What are aspects of interface 'Consistency' according to HCI principles? (Select all that apply)",
                "options": [
                    {"id": "a", "text": "Visual consistency (consistent fonts, color schemes, icon styles)"},
                    {"id": "b", "text": "Functional consistency (identical keyboard shortcuts across related tools)"},
                    {"id": "c", "text": "Internal consistency (behaving uniformly within the same application)"},
                    {"id": "d", "text": "Changing the meaning of the 'Escape' key on every screen to keep users alert"}
                ],
                "correct": ["a", "b", "c"],
                "explanation": "Consistency encompasses visual, functional, internal, and external standards. Changing key bindings arbitrarily breaks consistency."
            },
            {
                "num": 8,
                "type": "single",
                "prompt": "What is an 'Accelerator' in user interface design?",
                "options": [
                    {"id": "a", "text": "A hardware GPU chip"},
                    {"id": "b", "text": "A mechanism (such as a keyboard shortcut or gesture) that allows expert users to perform frequent tasks much faster"},
                    {"id": "c", "text": "An automated pop-up ad that rushes user interaction"},
                    {"id": "d", "text": "A progress bar that animates artificially fast"}
                ],
                "correct": ["b"],
                "explanation": "Accelerators (e.g. Ctrl+C, Ctrl+Z, quick gesture macros) cater to experienced users without cluttering the interface for novices."
            },
            {
                "num": 9,
                "type": "single",
                "prompt": "When an error inevitably occurs, how should the error message be presented according to HCI best practices?",
                "options": [
                    {"id": "a", "text": "Use raw memory dump addresses and technical exception stacks"},
                    {"id": "b", "text": "Use clear, polite, plain-language text that explains what happened and offers a constructive solution"},
                    {"id": "c", "text": "Blame the user explicitly for invalid input"},
                    {"id": "d", "text": "Emit a persistent high-pitched alarm until reboot"}
                ],
                "correct": ["b"],
                "explanation": "Effective error messages are constructive, polite, specific, avoid technical jargon, and tell the user exactly how to resolve the problem."
            },
            {
                "num": 10,
                "type": "single",
                "prompt": "The principle 'Reduce short-term memory load' suggests which interface practice?",
                "options": [
                    {"id": "a", "text": "Forcing users to memorize phone numbers across different screens"},
                    {"id": "b", "text": "Auto-filling known user information and keeping context visible across multistep wizards"},
                    {"id": "c", "text": "Hiding all navigational indicators"},
                    {"id": "d", "text": "Presenting 20 unorganized options simultaneously"}
                ],
                "correct": ["b"],
                "explanation": "Carrying context across steps and displaying defaults prevents users from having to remember details across screen transitions."
            }
        ]
    },

    # Week 6
    {
        "week": 6,
        "topic": "Usability Evaluation: Heuristic Evaluation & Inspection Methods",
        "questions": [
            {
                "num": 1,
                "type": "single",
                "prompt": "Who developed the classic 10 Usability Heuristics commonly used in Heuristic Evaluation?",
                "options": [
                    {"id": "a", "text": "Alan Turing"},
                    {"id": "b", "text": "Jakob Nielsen (with Rolf Molich)"},
                    {"id": "c", "text": "Tim Berners-Lee"},
                    {"id": "d", "text": "Claude Shannon"}
                ],
                "correct": ["b"],
                "explanation": "Jakob Nielsen and Rolf Molich formulated the renowned 10 usability heuristics in 1990, refined in 1994."
            },
            {
                "num": 2,
                "type": "single",
                "prompt": "According to Nielsen's research curve, approximately how many evaluators are recommended to find 75–80% of usability problems in a Heuristic Evaluation?",
                "options": [
                    {"id": "a", "text": "1 evaluator"},
                    {"id": "b", "text": "3 to 5 evaluators"},
                    {"id": "c", "text": "50 evaluators"},
                    {"id": "d", "text": "100 evaluators"}
                ],
                "correct": ["b"],
                "explanation": "Nielsen's mathematical cost-benefit model shows that 3 to 5 evaluators uncover approximately 75% to 80% of usability flaws, beyond which diminishing returns set in."
            },
            {
                "num": 3,
                "type": "single",
                "prompt": "Which of the following is Nielsen's Heuristic #1?",
                "options": [
                    {"id": "a", "text": "Visibility of system status"},
                    {"id": "b", "text": "Aesthetic and minimalist design"},
                    {"id": "c", "text": "Error prevention"},
                    {"id": "d", "text": "Help and documentation"}
                ],
                "correct": ["a"],
                "explanation": "Heuristic #1 is 'Visibility of system status', which states that the system should always keep users informed about what is going on through appropriate feedback within reasonable time."
            },
            {
                "num": 4,
                "type": "single",
                "prompt": "An online banking website provides an 'Undo Transfer' button available for 10 seconds immediately following a money transfer. Which heuristic does this feature exemplify?",
                "options": [
                    {"id": "a", "text": "User control and freedom"},
                    {"id": "b", "text": "Match between system and real world"},
                    {"id": "c", "text": "Minimalist aesthetics"},
                    {"id": "d", "text": "Command syntax standardization"}
                ],
                "correct": ["a"],
                "explanation": "'User control and freedom' involves providing emergency exits and clear undo/redo capabilities when users choose system functions by mistake."
            },
            {
                "num": 5,
                "type": "multiple",
                "prompt": "Which of the following belong to Jakob Nielsen's 10 Usability Heuristics? (Select all that apply)",
                "options": [
                    {"id": "a", "text": "Consistency and standards"},
                    {"id": "b", "text": "Recognition rather than recall"},
                    {"id": "c", "text": "Flexibility and efficiency of use"},
                    {"id": "d", "text": "Maximum algorithmic throughput"}
                ],
                "correct": ["a", "b", "c"],
                "explanation": "Options A, B, and C are heuristics #4, #6, and #7. Algorithmic throughput is a backend computational metric, not an interface usability heuristic."
            },
            {
                "num": 6,
                "type": "single",
                "prompt": "What is the key defining characteristic of 'Discount Usability Engineering' advocated by Jakob Nielsen?",
                "options": [
                    {"id": "a", "text": "Relying on cheap, fast, and simple usability methods (like heuristic evaluation and simple prototypes) that deliver high ROI early in design"},
                    {"id": "b", "text": "Offering discounts on software licensing fees to testers"},
                    {"id": "c", "text": "Eliminating all user testing completely"},
                    {"id": "d", "text": "Only testing software on discounted budget laptops"}
                ],
                "correct": ["a"],
                "explanation": "Discount Usability emphasizes quick, lightweight, cost-effective techniques (scenarios, paper prototypes, heuristic evaluation) so usability is practiced even with tight budgets."
            },
            {
                "num": 7,
                "type": "single",
                "prompt": "How does a 'Cognitive Walkthrough' differ from a 'Heuristic Evaluation'?",
                "options": [
                    {"id": "a", "text": "A Cognitive Walkthrough evaluates step-by-step task execution specifically focusing on learnability by novice users"},
                    {"id": "b", "text": "A Cognitive Walkthrough tests network packet roundtrips"},
                    {"id": "c", "text": "Heuristic evaluation can only be conducted by end users, not experts"},
                    {"id": "d", "text": "There is no difference"}
                ],
                "correct": ["a"],
                "explanation": "Cognitive Walkthrough is task-centric: experts step through specific user tasks asking: 1. Will the user try to achieve the right effect? 2. Will they notice the control? 3. Will they understand it produces the effect? 4. Will they understand the feedback?"
            },
            {
                "num": 8,
                "type": "multiple",
                "prompt": "Why should evaluators perform Heuristic Evaluation independently before meeting to aggregate findings? (Select all that apply)",
                "options": [
                    {"id": "a", "text": "To prevent groupthink and bias among evaluators"},
                    {"id": "b", "text": "To ensure independent, uninfluenced identification of problems"},
                    {"id": "c", "text": "To guarantee that all evaluators find exactly the same problems"},
                    {"id": "d", "text": "To allow statistical aggregation of independent discovery probabilities"}
                ],
                "correct": ["a", "b", "d"],
                "explanation": "Independent evaluations ensure unskewed observations and diverse coverage. Option C is wrong because different evaluators uncover different problem sets."
            },
            {
                "num": 9,
                "type": "single",
                "prompt": "In Nielsen's severity rating scale for usability problems (0 to 4), what does a rating of '4' indicate?",
                "options": [
                    {"id": "a", "text": "Cosmetic problem only"},
                    {"id": "b", "text": "Minor usability problem"},
                    {"id": "c", "text": "Usability catastrophe: imperative to fix before product release"},
                    {"id": "d", "text": "No usability issue identified"}
                ],
                "correct": ["c"],
                "explanation": "Nielsen's scale: 0 = not a problem, 1 = cosmetic, 2 = minor, 3 = major, 4 = usability catastrophe (prevents task completion)."
            },
            {
                "num": 10,
                "type": "single",
                "prompt": "An e-commerce site uses a shopping cart icon to represent items to purchase. Which heuristic does this visual metaphor satisfy?",
                "options": [
                    {"id": "a", "text": "Match between system and the real world"},
                    {"id": "b", "text": "Help users recognize errors"},
                    {"id": "c", "text": "Flexibility and efficiency"},
                    {"id": "d", "text": "System status visibility"}
                ],
                "correct": ["a"],
                "explanation": "The shopping cart metaphor maps directly to physical real-world grocery carts, matching real-world expectations and knowledge."
            }
        ]
    },

    # Week 7
    {
        "week": 7,
        "topic": "Usability Testing, Think-Aloud Protocol & SUS Metrics",
        "questions": [
            {
                "num": 1,
                "type": "single",
                "prompt": "According to ISO 9241-11, what are the three foundational dimensions of usability?",
                "options": [
                    {"id": "a", "text": "Effectiveness, Efficiency, and Satisfaction"},
                    {"id": "b", "text": "Speed, Bandwidth, and Latency"},
                    {"id": "c", "text": "Cost, Security, and Scalability"},
                    {"id": "d", "text": "Readability, Contrast, and Color"}
                ],
                "correct": ["a"],
                "explanation": "ISO 9241-11 defines usability as the extent to which a product can be used by specified users to achieve goals with Effectiveness (accuracy/completeness), Efficiency (resources expended), and Satisfaction (comfort/acceptability)."
            },
            {
                "num": 2,
                "type": "single",
                "prompt": "What is the primary procedure of the 'Think-Aloud Protocol' in usability testing?",
                "options": [
                    {"id": "a", "text": "The test administrator constantly explains the answers out loud to the participant"},
                    {"id": "b", "text": "Participants vocalize their thoughts, feelings, intentions, and confusions continuously while performing tasks"},
                    {"id": "c", "text": "Participants debate each other loudly after the test session"},
                    {"id": "d", "text": "A speech synthesizer reads the screen text aloud"}
                ],
                "correct": ["b"],
                "explanation": "In the think-aloud method, participants continuously narrate their internal thought processes, giving researchers direct insight into their cognitive model and points of confusion."
            },
            {
                "num": 3,
                "type": "single",
                "prompt": "How many items comprise the standard System Usability Scale (SUS) questionnaire created by John Brooke?",
                "options": [
                    {"id": "a", "text": "5 items"},
                    {"id": "b", "text": "10 items"},
                    {"id": "c", "text": "20 items"},
                    {"id": "d", "text": "50 items"}
                ],
                "correct": ["b"],
                "explanation": "SUS is a standardized 10-item questionnaire on a 5-point Likert scale (alternating positive and negative statements)."
            },
            {
                "num": 4,
                "type": "single",
                "prompt": "In computing the System Usability Scale (SUS) score from raw ratings (1 to 5), what is the scoring formula multiplier applied to the normalized sum?",
                "options": [
                    {"id": "a", "text": "Multiply sum by 1.0"},
                    {"id": "b", "text": "Multiply sum by 2.5"},
                    {"id": "c", "text": "Multiply sum by 10"},
                    {"id": "d", "text": "Divide sum by 2"}
                ],
                "correct": ["b"],
                "explanation": "Each of the 10 questions contributes 0 to 4 points (max 40). Multiplying by 2.5 converts the score to a standard 0 to 100 scale."
            },
            {
                "num": 5,
                "type": "single",
                "prompt": "What is widely recognized in empirical HCI literature as the average baseline benchmark score for a System Usability Scale (SUS) evaluation?",
                "options": [
                    {"id": "a", "text": "50"},
                    {"id": "b", "text": "68"},
                    {"id": "c", "text": "85"},
                    {"id": "d", "text": "100"}
                ],
                "correct": ["b"],
                "explanation": "Sauro and Lewis demonstrated across thousands of surveys that the average SUS benchmark score is 68. Scores above 68 are above average."
            },
            {
                "num": 6,
                "type": "multiple",
                "prompt": "Which of the following are quantitative usability metrics? (Select all that apply)",
                "options": [
                    {"id": "a", "text": "Task completion rate (percentage of users completing a task successfully)"},
                    {"id": "b", "text": "Time-on-task (duration in seconds to complete a task)"},
                    {"id": "c", "text": "Error frequency (number of mistakes made per task)"},
                    {"id": "d", "text": "Open-ended tester anecdotes"}
                ],
                "correct": ["a", "b", "c"],
                "explanation": "Task completion rates, completion time, and error counts are numerical quantitative measures. Tester anecdotes are qualitative data."
            },
            {
                "num": 7,
                "type": "single",
                "prompt": "What is a potential disadvantage of the concurrent Think-Aloud protocol during a usability test?",
                "options": [
                    {"id": "a", "text": "It can artificially inflate task completion time and alter natural cognitive focus"},
                    {"id": "b", "text": "It requires expensive EEG hardware"},
                    {"id": "c", "text": "It cannot be recorded on audio"},
                    {"id": "d", "text": "It is illegal under copyright law"}
                ],
                "correct": ["a"],
                "explanation": "Talking aloud while acting introduces dual-task interference, potentially slowing down task execution times and altering natural user pacing."
            },
            {
                "num": 8,
                "type": "single",
                "prompt": "Why are the odd and even questions in the SUS questionnaire phrased in alternating positive and negative directions?",
                "options": [
                    {"id": "a", "text": "To reduce response acquiescence bias (habitual agreement) and ensure participants read each item"},
                    {"id": "b", "text": "To confuse the statistical analysis script"},
                    {"id": "c", "text": "Because negative questions are graded twice as hard"},
                    {"id": "d", "text": "To test English language proficiency"}
                ],
                "correct": ["a"],
                "explanation": "Alternating polarities mitigates acquiescence bias (the tendency for respondents to agree blindly down a column without reading)."
            },
            {
                "num": 9,
                "type": "single",
                "prompt": "In usability testing, what is a 'Formative Evaluation'?",
                "options": [
                    {"id": "a", "text": "Testing conducted during the design process to discover issues and guide redesign iterations"},
                    {"id": "b", "text": "A final formal audit conducted strictly after deployment for legal certification"},
                    {"id": "c", "text": "Grading students in an academic semester"},
                    {"id": "d", "text": "Testing printer paper format sizes"}
                ],
                "correct": ["a"],
                "explanation": "Formative evaluation happens iteratively *during* development to form/shape the design. Summative evaluation happens at the end to evaluate final performance against benchmarks."
            },
            {
                "num": 10,
                "type": "multiple",
                "prompt": "Which of the following are standardized post-study usability questionnaires alongside SUS? (Select all that apply)",
                "options": [
                    {"id": "a", "text": "CSUQ (Computer System Usability Questionnaire)"},
                    {"id": "b", "text": "QUIS (Questionnaire for User Interaction Satisfaction)"},
                    {"id": "c", "text": "NASA-TLX (Task Load Index)"},
                    {"id": "d", "text": "TCP/IP Protocol Suite"}
                ],
                "correct": ["a", "b", "c"],
                "explanation": "CSUQ, QUIS, and NASA-TLX (workload assessment) are well-validated standardized usability questionnaires in HCI."
            }
        ]
    },

    # Week 8
    {
        "week": 8,
        "topic": "Empirical Experiments & Experimental Design in HCI",
        "questions": [
            {
                "num": 1,
                "type": "single",
                "prompt": "In an experiment comparing the selection speed of a trackball mouse vs a touchscreen across three target sizes, what are the 'Independent Variables' (IV)?",
                "options": [
                    {"id": "a", "text": "Input device type and target size"},
                    {"id": "b", "text": "Selection speed and error rate"},
                    {"id": "c", "text": "Room temperature and monitor brightness"},
                    {"id": "d", "text": "Participant age only"}
                ],
                "correct": ["a"],
                "explanation": "Independent variables are the conditions or factors systematically manipulated by the experimenter (here: input device and target size)."
            },
            {
                "num": 2,
                "type": "single",
                "prompt": "What is a 'Dependent Variable' (DV) in an HCI empirical experiment?",
                "options": [
                    {"id": "a", "text": "The metric measured to assess the effect of the independent variable (e.g., completion time, error count)"},
                    {"id": "b", "text": "The operating system version running on the testing computer"},
                    {"id": "c", "text": "The statistical software used to run ANOVA"},
                    {"id": "d", "text": "The monetary compensation paid to participants"}
                ],
                "correct": ["a"],
                "explanation": "Dependent variables are the observed outcome measurements that depend upon the conditions manipulated by the experimenter."
            },
            {
                "num": 3,
                "type": "single",
                "prompt": "What is the primary advantage of a 'Within-Subjects' (repeated measures) experimental design?",
                "options": [
                    {"id": "a", "text": "It isolates individual user differences because each participant acts as their own baseline control, requiring fewer participants"},
                    {"id": "b", "text": "It eliminates all possibility of learning or fatigue effects"},
                    {"id": "c", "text": "It does not require informed consent"},
                    {"id": "d", "text": "It eliminates the need for statistical significance testing"}
                ],
                "correct": ["a"],
                "explanation": "Because every participant experiences all conditions, within-subjects designs control for individual differences and require significantly fewer participants for equivalent statistical power."
            },
            {
                "num": 4,
                "type": "single",
                "prompt": "What technique is used in within-subjects experiments to counteract 'Order Effects' (learning curve and fatigue)?",
                "options": [
                    {"id": "a", "text": "Counterbalancing (e.g., Latin Square design)"},
                    {"id": "b", "text": "Giving participants energy drinks"},
                    {"id": "c", "text": "Running the experiment in reverse alphabetical order"},
                    {"id": "d", "text": "Increasing the screen resolution"}
                ],
                "correct": ["a"],
                "explanation": "Counterbalancing (such as Balanced Latin Squares) systematically varies the presentation order of conditions across participants so learning and fatigue cancel out evenly."
            },
            {
                "num": 5,
                "type": "single",
                "prompt": "When is a 'Between-Subjects' design strictly preferred over a within-subjects design?",
                "options": [
                    {"id": "a", "text": "When experiencing one condition would permanently contaminate, train, or bias the participant for the second condition"},
                    {"id": "b", "text": "When only 2 total participants are available"},
                    {"id": "c", "text": "When the experimental software costs too much per user"},
                    {"id": "d", "text": "When target sizes are identical"}
                ],
                "correct": ["a"],
                "explanation": "Between-subjects designs are essential when an interface condition involves a learning breakthrough or puzzle that cannot be 'unlearned' for subsequent conditions."
            },
            {
                "num": 6,
                "type": "multiple",
                "prompt": "In hypothesis testing, what does a p-value of less than 0.05 (p < 0.05) typically signify?",
                "options": [
                    {"id": "a", "text": "The observed difference is statistically significant"},
                    {"id": "b", "text": "There is less than a 5% probability that the observed difference occurred purely by random chance under the null hypothesis"},
                    {"id": "c", "text": "The null hypothesis (H0) can be rejected"},
                    {"id": "d", "text": "The experiment proved the design is 100% bug-free"}
                ],
                "correct": ["a", "b", "c"],
                "explanation": "A p < 0.05 threshold indicates statistical significance, rejecting H0 with < 5% risk of Type I error (false positive). It does not mean software is bug-free."
            },
            {
                "num": 7,
                "type": "single",
                "prompt": "What type of statistical test is appropriate when comparing the mean completion times of two independent groups of participants testing two distinct interfaces?",
                "options": [
                    {"id": "a", "text": "Independent-samples t-test"},
                    {"id": "b", "text": "Paired-samples t-test"},
                    {"id": "c", "text": "Chi-Square goodness of fit"},
                    {"id": "d", "text": "Fourier transform"}
                ],
                "correct": ["a"],
                "explanation": "An independent-samples (two-sample) t-test compares means between two unrelated groups of participants (between-subjects)."
            },
            {
                "num": 8,
                "type": "single",
                "prompt": "What statistical test is standard when evaluating experiments with two or more independent variables each having multiple levels (e.g. 2 devices × 3 screen sizes)?",
                "options": [
                    {"id": "a", "text": "ANOVA (Analysis of Variance)"},
                    {"id": "b", "text": "Simple linear regression only"},
                    {"id": "c", "text": "K-means clustering"},
                    {"id": "d", "text": "Dijkstra's algorithm"}
                ],
                "correct": ["a"],
                "explanation": "Factorial ANOVA evaluates main effects and interaction effects across multiple independent variables without inflating family-wise Type I error rates."
            },
            {
                "num": 9,
                "type": "single",
                "prompt": "What is a 'Type I Error' (alpha error) in empirical research?",
                "options": [
                    {"id": "a", "text": "Rejecting the null hypothesis when it is actually true (a false positive)"},
                    {"id": "b", "text": "Failing to reject the null hypothesis when there was a true effect (false negative)"},
                    {"id": "c", "text": "A hardware memory crash during data logging"},
                    {"id": "d", "text": "A typo in the consent form"}
                ],
                "correct": ["a"],
                "explanation": "A Type I error occurs when the researcher claims an effect exists (rejecting H0) when in reality the observation was due to chance."
            },
            {
                "num": 10,
                "type": "multiple",
                "prompt": "Which of the following are essential elements of an Ethical Usability Study with human participants? (Select all that apply)",
                "options": [
                    {"id": "a", "text": "Informed consent detailing study purpose, risks, and voluntary nature"},
                    {"id": "b", "text": "The explicit right to withdraw at any time without penalty"},
                    {"id": "c", "text": "Reassuring participants that the software is being tested, not their intelligence"},
                    {"id": "d", "text": "Revealing participant names and private data publicly"}
                ],
                "correct": ["a", "b", "c"],
                "explanation": "Informed consent, voluntary withdrawal, participant reassurance, and strict confidentiality of data are universal ethical guidelines in HCI."
            }
        ]
    },

    # Week 9
    {
        "week": 9,
        "topic": "Interaction Styles & Dialogue Design",
        "questions": [
            {
                "num": 1,
                "type": "single",
                "prompt": "Who coined the term 'Direct Manipulation' in 1983 to describe interfaces characterized by continuous representation of objects and rapid, reversible incremental actions?",
                "options": [
                    {"id": "a", "text": "Ben Shneiderman"},
                    {"id": "b", "text": "Steve Jobs"},
                    {"id": "c", "text": "Douglas Engelbart"},
                    {"id": "d", "text": "Alan Kay"}
                ],
                "correct": ["a"],
                "explanation": "Ben Shneiderman introduced the concept of Direct Manipulation in 1983, observing the power of physical actions (dragging, resizing) over abstract command syntax."
            },
            {
                "num": 2,
                "type": "single",
                "prompt": "Which of the following is a primary interaction style?",
                "options": [
                    {"id": "a", "text": "Command line interface (CLI)"},
                    {"id": "b", "text": "Direct manipulation"},
                    {"id": "c", "text": "Menu selection and form fill-in"},
                    {"id": "d", "text": "All of the above"}
                ],
                "correct": ["d"],
                "explanation": "CLI, Direct Manipulation, Menu Selection, Form Fill-in, and Natural Language are the classic interaction paradigms in HCI."
            },
            {
                "num": 3,
                "type": "single",
                "prompt": "What is a major advantage of Menu-Driven interfaces compared to Command Line interfaces?",
                "options": [
                    {"id": "a", "text": "They rely on recognition memory instead of recall memory, reducing cognitive learning burden for novices"},
                    {"id": "b", "text": "They consume zero screen real estate"},
                    {"id": "c", "text": "They are faster for expert typists than shell scripts"},
                    {"id": "d", "text": "They never require user input devices"}
                ],
                "correct": ["a"],
                "explanation": "Menus list options explicitly on screen, enabling users to recognize items rather than having to recall complex syntax from memory."
            },
            {
                "num": 4,
                "type": "multiple",
                "prompt": "Which of the following are core properties of Direct Manipulation interfaces? (Select all that apply)",
                "options": [
                    {"id": "a", "text": "Continuous visual representation of objects of interest"},
                    {"id": "b", "text": "Physical actions or button presses instead of complex syntax"},
                    {"id": "c", "text": "Rapid, incremental, and reversible actions with immediately visible impact"},
                    {"id": "d", "text": "Requiring users to type batch scripts in terminal windows"}
                ],
                "correct": ["a", "b", "c"],
                "explanation": "Continuous representation, physical actions instead of syntax, and rapid reversible feedback are Shneiderman's three defining pillars of direct manipulation."
            },
            {
                "num": 5,
                "type": "single",
                "prompt": "What formalism is commonly used in HCI to model the dialogue states, transitions, and user events of an interface?",
                "options": [
                    {"id": "a", "text": "State Transition Networks (STN) / Statecharts"},
                    {"id": "b", "text": "Chemical bonding diagrams"},
                    {"id": "c", "text": "Newtonian mechanics"},
                    {"id": "d", "text": "Shannon-Fano coding trees"}
                ],
                "correct": ["a"],
                "explanation": "State Transition Networks (STNs) and Harel Statecharts represent dialog design using states (circles), events/actions (labeled transition arrows), and conditionals."
            },
            {
                "num": 6,
                "type": "single",
                "prompt": "In dialog design, what is a 'Modal' dialog as opposed to a 'Modeless' dialog?",
                "options": [
                    {"id": "a", "text": "A modal dialog blocks interaction with the rest of the application until the user dismisses it"},
                    {"id": "b", "text": "A modal dialog can only display audio files"},
                    {"id": "c", "text": "A modal dialog is only visible on mobile phones"},
                    {"id": "d", "text": "A modal dialog updates continuously in the background"}
                ],
                "correct": ["a"],
                "explanation": "A modal dialog traps user focus, requiring resolution (e.g. Save / Discard) before any interaction with the parent window can resume."
            },
            {
                "num": 7,
                "type": "single",
                "prompt": "Why can Form Fill-in interfaces become frustrating if poorly designed?",
                "options": [
                    {"id": "a", "text": "If tab key order is illogical, validation occurs only after full submission without highlighting errors, or unnecessary fields abound"},
                    {"id": "b", "text": "Because keyboards cannot input text into browsers"},
                    {"id": "c", "text": "Because forms only support numerical values"},
                    {"id": "d", "text": "Because they require VR goggles"}
                ],
                "correct": ["a"],
                "explanation": "Poor forms suffer from jarring tab traversal, delayed bulk error validation, unclear required fields, and excessive typing."
            },
            {
                "num": 8,
                "type": "multiple",
                "prompt": "What are challenges associated with Natural Language interaction (Voice Assistants)? (Select all that apply)",
                "options": [
                    {"id": "a", "text": "Ambiguity of human speech and context-dependent syntax"},
                    {"id": "b", "text": "Lack of visual affordances (users do not know what commands are possible)"},
                    {"id": "c", "text": "Privacy and background noise interference"},
                    {"id": "d", "text": "It can never be used hands-free"}
                ],
                "correct": ["a", "b", "c"],
                "explanation": "Voice UI struggles with invisible boundaries (no visual signifiers showing what can be said), speech ambiguity, and audio noise."
            },
            {
                "num": 9,
                "type": "single",
                "prompt": "Dragging a file to the Trash Can icon to delete it is a classic example of which design concept?",
                "options": [
                    {"id": "a", "text": "Direct manipulation using a desktop metaphor"},
                    {"id": "b", "text": "Batch processing command prompt"},
                    {"id": "c", "text": "Heuristic violation"},
                    {"id": "d", "text": "Hick-Hyman optimization"}
                ],
                "correct": ["a"],
                "explanation": "Dragging files into a trash can icon exemplifies direct manipulation combined with the office desktop metaphor developed at Xerox PARC."
            },
            {
                "num": 10,
                "type": "single",
                "prompt": "What is a 'Breadcrumb Trail' in interface navigation?",
                "options": [
                    {"id": "a", "text": "A secondary navigation scheme that displays the user's hierarchical location path within a site (e.g., Home > Electronics > Audio > Headphones)"},
                    {"id": "b", "text": "A log of HTTP cookies stored on the hard drive"},
                    {"id": "c", "text": "A technique to measure mouse cursor jitter"},
                    {"id": "d", "text": "An automated test script for checking broken links"}
                ],
                "correct": ["a"],
                "explanation": "Breadcrumbs reveal structural hierarchy, reinforce context, reduce navigational steps, and provide quick one-click shortcuts to parent levels."
            }
        ]
    },

    # Week 10
    {
        "week": 10,
        "topic": "Visual Design, Typography & Gestalt Principles in UI",
        "questions": [
            {
                "num": 1,
                "type": "single",
                "prompt": "Which Gestalt principle explains why elements positioned close together are perceived as belonging to a common group?",
                "options": [
                    {"id": "a", "text": "Law of Proximity"},
                    {"id": "b", "text": "Law of Similarity"},
                    {"id": "c", "text": "Law of Closure"},
                    {"id": "d", "text": "Law of Continuity"}
                ],
                "correct": ["a"],
                "explanation": "The Law of Proximity states that objects near each other are grouped by human perception into a single perceptual unit."
            },
            {
                "num": 2,
                "type": "single",
                "prompt": "If an interface displays four identical blue circles and one bright orange diamond, the user's attention is drawn immediately to the diamond. What perceptual phenomenon causes this?",
                "options": [
                    {"id": "a", "text": "Pre-attentive visual processing (pop-out effect)"},
                    {"id": "b", "text": "Visual fatigue"},
                    {"id": "c", "text": "Retroactive interference"},
                    {"id": "d", "text": "Fitts' deceleration"}
                ],
                "correct": ["a"],
                "explanation": "Pre-attentive visual attributes (color hue, size, orientation) are processed in parallel by the human visual cortex in under 200 ms without conscious search."
            },
            {
                "num": 3,
                "type": "multiple",
                "prompt": "Which of the following are recognized Gestalt Principles of visual perception? (Select all that apply)",
                "options": [
                    {"id": "a", "text": "Law of Similarity (similar shape/color elements are grouped)"},
                    {"id": "b", "text": "Law of Closure (the mind fills in missing gaps in incomplete figures)"},
                    {"id": "c", "text": "Law of Common Fate (elements moving in the same direction are grouped)"},
                    {"id": "d", "text": "Law of Quantum Superposition"}
                ],
                "correct": ["a", "b", "c"],
                "explanation": "Similarity, Closure, and Common Fate (along with Proximity, Continuity, and Figure-Ground) are core Gestalt psychology principles."
            },
            {
                "num": 4,
                "type": "single",
                "prompt": "In digital typography and UI layout, why is 'Leading' (line-height) important?",
                "options": [
                    {"id": "a", "text": "Adequate vertical spacing between lines prevents the eye from accidentally jumping or rereading adjacent lines during scanning"},
                    {"id": "b", "text": "Leading changes the font's alphabetical characters into numbers"},
                    {"id": "c", "text": "Leading is only used in printed newspapers"},
                    {"id": "d", "text": "Leading compresses images"}
                ],
                "correct": ["a"],
                "explanation": "Optimal line height (typically 140-160% of font size) ensures visual separation between text lines, preserving tracking rhythm."
            },
            {
                "num": 5,
                "type": "single",
                "prompt": "According to the Web Content Accessibility Guidelines (WCAG 2.1 AA), what is the minimum required contrast ratio for normal body text against its background?",
                "options": [
                    {"id": "a", "text": "1.5 : 1"},
                    {"id": "b", "text": "3.0 : 1"},
                    {"id": "c", "text": "4.5 : 1"},
                    {"id": "d", "text": "10 : 1"}
                ],
                "correct": ["c"],
                "explanation": "WCAG 2.1 Level AA mandates a contrast ratio of at least 4.5:1 for standard text (and 3:1 for large text >= 18pt or bold >= 14pt)."
            },
            {
                "num": 6,
                "type": "single",
                "prompt": "Why should color NEVER be used as the sole visual indicator to communicate important status (e.g. error vs success)?",
                "options": [
                    {"id": "a", "text": "Because approximately 8% of men and 0.5% of women have color vision deficiencies (color blindness), and monochrome displays cannot render color"},
                    {"id": "b", "text": "Because color increases server download times"},
                    {"id": "c", "text": "Because web standards ban colored icons"},
                    {"id": "d", "text": "Because colored pixels burn out screens faster"}
                ],
                "correct": ["a"],
                "explanation": "Relying strictly on color (like green vs red) excludes color-deficient users; status must always be reinforced with text labels, icons, or patterns."
            },
            {
                "num": 7,
                "type": "multiple",
                "prompt": "What are benefits of using a consistent Grid System in UI design? (Select all that apply)",
                "options": [
                    {"id": "a", "text": "Creates visual rhythm, balance, and clear alignment across screens"},
                    {"id": "b", "text": "Simplifies responsive design across diverse viewport breakpoints"},
                    {"id": "c", "text": "Speeds up design and developer collaboration"},
                    {"id": "d", "text": "Guarantees that no user will ever commit a slip error"}
                ],
                "correct": ["a", "b", "c"],
                "explanation": "Grid systems enforce harmonious alignment, simplify responsive design, and streamline implementation. They cannot prevent human motor slips."
            },
            {
                "num": 8,
                "type": "single",
                "prompt": "What visual principle separates the primary focal elements from the surrounding background canvas?",
                "options": [
                    {"id": "a", "text": "Figure-Ground segregation"},
                    {"id": "b", "text": "Hick's selection"},
                    {"id": "c", "text": "Kerning"},
                    {"id": "d", "text": "Motion blur"}
                ],
                "correct": ["a"],
                "explanation": "Figure-Ground segregation distinguishes the prominent subject (figure) from the underlying canvas or environment (ground) through borders, shadows, or contrast."
            },
            {
                "num": 9,
                "type": "single",
                "prompt": "In UI layout, what is 'Negative Space' (Whitespace)?",
                "options": [
                    {"id": "a", "text": "The unmarked space between or around interface components used deliberately to reduce clutter, group items, and direct focus"},
                    {"id": "b", "text": "Dead space caused by missing database records"},
                    {"id": "c", "text": "Corrupted pixel memory"},
                    {"id": "d", "text": "A mistake made by graphic designers"}
                ],
                "correct": ["a"],
                "explanation": "Whitespace (macro and micro) creates visual breathing room, reinforces groupings, clarifies hierarchy, and prevents cognitive overload."
            },
            {
                "num": 10,
                "type": "single",
                "prompt": "Which Gestalt principle causes four brackets positioned like [  ] to be perceived as a unified square rather than four isolated angle lines?",
                "options": [
                    {"id": "a", "text": "Law of Closure"},
                    {"id": "b", "text": "Law of Color Constancy"},
                    {"id": "c", "text": "Steering Law"},
                    {"id": "d", "text": "Law of Fitts"}
                ],
                "correct": ["a"],
                "explanation": "The Law of Closure states that human visual perception automatically bridges gaps to complete familiar shapes or contours."
            }
        ]
    },

    # Week 11
    {
        "week": 11,
        "topic": "User Research, Requirements Engineering & Task Analysis",
        "questions": [
            {
                "num": 1,
                "type": "single",
                "prompt": "What is 'Contextual Inquiry' in user research?",
                "options": [
                    {"id": "a", "text": "A field research method where researchers observe and interview users in their actual work environment as users perform real tasks"},
                    {"id": "b", "text": "Distributing an automated multiple choice survey over email"},
                    {"id": "c", "text": "Testing user response times inside an MRI scanner"},
                    {"id": "d", "text": "Writing code specifications in an isolated office"}
                ],
                "correct": ["a"],
                "explanation": "Contextual Inquiry (Beyer & Holtzblatt) combines in-situ observation and open interviewing within the user's authentic environment, uncovering tacit knowledge."
            },
            {
                "num": 2,
                "type": "single",
                "prompt": "What are the four core principles of Contextual Inquiry?",
                "options": [
                    {"id": "a", "text": "Context, Partnership, Interpretation, and Focus"},
                    {"id": "b", "text": "Speed, Cost, Simplicity, and Automation"},
                    {"id": "c", "text": "Input, Processing, Storage, and Output"},
                    {"id": "d", "text": "Heuristics, Models, Laws, and Metrics"}
                ],
                "correct": ["a"],
                "explanation": "The 4 principles are: Context (go where work happens), Partnership (collaborate as apprentice to master), Interpretation (share insights to validate), and Focus (steer inquiry based on clear goals)."
            },
            {
                "num": 3,
                "type": "single",
                "prompt": "In user-centered design, what is a 'Persona'?",
                "options": [
                    {"id": "a", "text": "A rich, research-grounded composite archetype representing a specific segment of target users, with realistic goals, behaviors, and pain points"},
                    {"id": "b", "text": "A single specific real-life customer with their private legal name and address"},
                    {"id": "c", "text": "A cartoon mascot used in promotional ads"},
                    {"id": "d", "text": "A dummy user account used for database testing"}
                ],
                "correct": ["a"],
                "explanation": "Personas (introduced by Alan Cooper) synthesize real qualitative user research into vivid, archetypal profiles that keep teams aligned on user needs."
            },
            {
                "num": 4,
                "type": "single",
                "prompt": "What is the primary objective of Hierarchical Task Analysis (HTA)?",
                "options": [
                    {"id": "a", "text": "Decomposing high-level user tasks into a hierarchy of sub-tasks, operations, and execution plans"},
                    {"id": "b", "text": "Measuring CPU utilization during task switching"},
                    {"id": "c", "text": "Ranking corporate employees by job title"},
                    {"id": "d", "text": "Creating relational database tables in third normal form"}
                ],
                "correct": ["a"],
                "explanation": "HTA breaks down a goal into subgoals and operations along with 'plans' detailing the conditions under which sub-operations are executed."
            },
            {
                "num": 5,
                "type": "multiple",
                "prompt": "Which of the following elements are typically included in an effective Persona description? (Select all that apply)",
                "options": [
                    {"id": "a", "text": "User goals and motivations"},
                    {"id": "b", "text": "Frustrations, obstacles, and pain points with current workflows"},
                    {"id": "c", "text": "Technical proficiency and context of use"},
                    {"id": "d", "text": "Arbitrary fictional trivia that has no impact on interface design"}
                ],
                "correct": ["a", "b", "c"],
                "explanation": "Meaningful personas focus on goals, motivations, pain points, and technical competence. Irrelevant trivia clutters the persona."
            },
            {
                "num": 6,
                "type": "single",
                "prompt": "What is a 'Scenario' in the context of Scenario-Based Design?",
                "options": [
                    {"id": "a", "text": "A concrete narrative description of a persona using a system to accomplish a specific goal within a specific context"},
                    {"id": "b", "text": "A unit test script written in JavaScript"},
                    {"id": "c", "text": "A budget forecast spreadsheet for design software"},
                    {"id": "d", "text": "The worst-case system failure scenario only"}
                ],
                "correct": ["a"],
                "explanation": "Scenarios narrate vivid user journeys showing how people use the interface in real circumstances to solve problems."
            },
            {
                "num": 7,
                "type": "single",
                "prompt": "Why is 'Paper Prototyping' highly valued during the early conceptual phase of interface design?",
                "options": [
                    {"id": "a", "text": "It is fast, inexpensive, allows instant modification during testing, and invites candid critique because users do not mistake it for a finished product"},
                    {"id": "b", "text": "It can be compiled directly into production machine bytecode"},
                    {"id": "c", "text": "It eliminates the need for software developers entirely"},
                    {"id": "d", "text": "It tests high-speed network latency accurately"}
                ],
                "correct": ["a"],
                "explanation": "Paper prototypes are low-fidelity and rapid; users focus on information architecture and workflows rather than getting bogged down in font or color details."
            },
            {
                "num": 8,
                "type": "multiple",
                "prompt": "Which of the following are recognized advantages of Semi-Structured Interviews compared to rigid questionnaires? (Select all that apply)",
                "options": [
                    {"id": "a", "text": "Flexibility to probe deeper into unexpected insights and uncover root causes of frustration"},
                    {"id": "b", "text": "Opportunity to observe body language, hesitancy, and tone of voice"},
                    {"id": "c", "text": "Automated instant grading with zero researcher analysis effort"},
                    {"id": "d", "text": "Allowing participants to elaborate in their own vocabulary"}
                ],
                "correct": ["a", "b", "d"],
                "explanation": "Semi-structured interviews yield rich qualitative depth and flexibility. They require substantial qualitative coding and analysis effort."
            },
            {
                "num": 9,
                "type": "single",
                "prompt": "In Hierarchical Task Analysis (HTA), what specifies the conditions under which various sub-tasks are performed?",
                "options": [
                    {"id": "a", "text": "A Plan (e.g. Plan 1: Do 1.1, then 1.2; if condition X, do 1.3)"},
                    {"id": "b", "text": "A SQL trigger"},
                    {"id": "c", "text": "A Fitts' equation"},
                    {"id": "d", "text": "A Norman affordance"}
                ],
                "correct": ["a"],
                "explanation": "HTA plans state the sequencing and conditional logic governing subgoals (e.g., 'Plan 0: Do 1, then 2. If item in stock, do 3, otherwise do 4')."
            },
            {
                "num": 10,
                "type": "single",
                "prompt": "What is the primary danger of designing for the 'Elastic User'?",
                "options": [
                    {"id": "a", "text": "The definition of user needs stretches and changes arbitrarily to fit developer convenience because no clear persona was defined"},
                    {"id": "b", "text": "Users physically stretching their muscles during mouse use"},
                    {"id": "c", "text": "The display monitor stretching pixels out of proportion"},
                    {"id": "d", "text": "Users using rubber styluses on touchscreens"}
                ],
                "correct": ["a"],
                "explanation": "Alan Cooper warned that without specific personas, designers imagine an 'elastic user' whose abilities stretch opportunistically to justify any coding shortcut."
            }
        ]
    },

    # Week 12
    {
        "week": 12,
        "topic": "Emerging HCI Paradigms: Touch, Gestures, Accessibility & Mobile HCI",
        "questions": [
            {
                "num": 1,
                "type": "single",
                "prompt": "What physical issue in touchscreen interaction describes how the user's hand or finger blocks their own view of underlying content?",
                "options": [
                    {"id": "a", "text": "Occlusion problem (Fat Finger Problem)"},
                    {"id": "b", "text": "Hick's latency"},
                    {"id": "c", "text": "Color distortion"},
                    {"id": "d", "text": "Ghost touches"}
                ],
                "correct": ["a"],
                "explanation": "Occlusion occurs when fingers obscure targets and feedback directly beneath the contact point, compounded by the soft, broad fingertip contact area."
            },
            {
                "num": 2,
                "type": "single",
                "prompt": "What is the recommended minimum touch target size according to modern mobile UI guidelines (e.g., Apple iOS and Google Material Design)?",
                "options": [
                    {"id": "a", "text": "10 x 10 physical pixels"},
                    {"id": "b", "text": "Approximately 44 x 44 to 48 x 48 density-independent points/pixels (approx. 7–9 mm)"},
                    {"id": "c", "text": "150 x 150 pixels"},
                    {"id": "d", "text": "2 x 2 millimeters"}
                ],
                "correct": ["b"],
                "explanation": "Apple specifies at least 44x44 pt and Google recommends 48x48 dp (~7-9mm) to accommodate typical adult index finger pads and minimize touch misses."
            },
            {
                "num": 3,
                "type": "single",
                "prompt": "In Mobile HCI, what describes the area of a smartphone screen that can be comfortably reached by a user's thumb when holding the phone with one hand?",
                "options": [
                    {"id": "a", "text": "The Thumb Zone"},
                    {"id": "b", "text": "The Fitts Horizon"},
                    {"id": "c", "text": "The Peripheral Retina"},
                    {"id": "d", "text": "The Gestalt Arc"}
                ],
                "correct": ["a"],
                "explanation": "Steven Hoober's research coined 'The Thumb Zone'—categorized into Natural, Stretch, and Hard zones—which dictates placing primary navigation at the screen bottom."
            },
            {
                "num": 4,
                "type": "multiple",
                "prompt": "Which of the following are the four foundational principles of the Web Content Accessibility Guidelines (WCAG) 2.1 (POUR)? (Select all that apply)",
                "options": [
                    {"id": "a", "text": "Perceivable (information must be presentable to users in ways they can perceive)"},
                    {"id": "b", "text": "Operable (interface components and navigation must be operable by all)"},
                    {"id": "c", "text": "Understandable (information and operation of the UI must be understandable)"},
                    {"id": "d", "text": "Robust (content must be robust enough to be interpreted by assistive technologies)"}
                ],
                "correct": ["a", "b", "c", "d"],
                "explanation": "The POUR framework forms the four pillars of modern digital accessibility: Perceivable, Operable, Understandable, and Robust."
            },
            {
                "num": 5,
                "type": "single",
                "prompt": "What does a Screen Reader (such as NVDA or VoiceOver) rely upon to communicate non-text images and icons to visually impaired users?",
                "options": [
                    {"id": "a", "text": "Descriptive Alternative Text ('alt' attributes and ARIA labels)"},
                    {"id": "b", "text": "Screen resolution metadata"},
                    {"id": "c", "text": "CSS animation durations"},
                    {"id": "d", "text": "Image compression algorithms"}
                ],
                "correct": ["a"],
                "explanation": "Screen readers vocalize meaningful 'alt' text and ARIA properties, translating visual graphics into auditory information for blind or low-vision users."
            },
            {
                "num": 6,
                "type": "single",
                "prompt": "What interaction concept describes systems that provide physical sensory feedback through vibrations, forces, or tactile motions?",
                "options": [
                    {"id": "a", "text": "Haptic feedback"},
                    {"id": "b", "text": "Acoustic echoing"},
                    {"id": "c", "text": "Iconic buffering"},
                    {"id": "d", "text": "Spectrographic rendering"}
                ],
                "correct": ["a"],
                "explanation": "Haptics simulates tactile sensations (such as button click clicks, pulses, or surface textures) using mechanical actuators or vibrotactile motors."
            },
            {
                "num": 7,
                "type": "multiple",
                "prompt": "Which of the following are challenges unique to Gestural and Mid-Air 3D Interfaces (e.g. Kinect, Leap Motion)? (Select all that apply)",
                "options": [
                    {"id": "a", "text": "Gorilla Arm effect (physical arm and shoulder fatigue from holding limbs elevated)"},
                    {"id": "b", "text": "The 'Midas Touch' problem (unintentional gestures being interpreted as commands)"},
                    {"id": "c", "text": "Lack of tactile physical feedback confirming command execution"},
                    {"id": "d", "text": "Total inability to track hand movement"}
                ],
                "correct": ["a", "b", "c"],
                "explanation": "Gorilla arm fatigue, lack of tactile feedback, and distinguishing deliberate gestures from natural fidgeting (Midas touch) are major spatial UI challenges."
            },
            {
                "num": 8,
                "type": "single",
                "prompt": "What is Mark Weiser's vision of 'Ubiquitous Computing' (UbiComp)?",
                "options": [
                    {"id": "a", "text": "Technology that recedes into the background of everyday life, seamlessly embedded into environments until it becomes invisible in use"},
                    {"id": "b", "text": "Everyone carrying heavy desktop mainframe computers everywhere"},
                    {"id": "c", "text": "Computers replacing human beings entirely"},
                    {"id": "d", "text": "A single supercomputer controlling all global transactions"}
                ],
                "correct": ["a"],
                "explanation": "Mark Weiser (1991) articulated Calm Technology and Ubiquitous Computing: the most profound technologies weave themselves into the fabric of everyday life until they are indistinguishable from it."
            },
            {
                "num": 9,
                "type": "single",
                "prompt": "Why is 'Universal Design' (Inclusive Design) preferred over simply building separate standalone accessibility modes?",
                "options": [
                    {"id": "a", "text": "Designing for the widest range of abilities from the ground up benefits everyone, including situational impairments (e.g. bright sunlight, carrying a baby, loud subway)"},
                    {"id": "b", "text": "Because separate modes cost zero dollars to maintain"},
                    {"id": "c", "text": "Because screen readers cannot handle separate pages"},
                    {"id": "d", "text": "Because accessible software runs twice as fast"}
                ],
                "correct": ["a"],
                "explanation": "Universal design principles ('curb-cut effect') show that accommodations designed for disabilities (captions, high contrast, large buttons) dramatically improve UX for everyone."
            },
            {
                "num": 10,
                "type": "multiple",
                "prompt": "Which of the following are essential design considerations when building responsive mobile web interfaces? (Select all that apply)",
                "options": [
                    {"id": "a", "text": "Accommodating variable network latency and intermittent offline conditions"},
                    {"id": "b", "text": "Avoiding tiny hyperlinks placed within tight text paragraphs"},
                    {"id": "c", "text": "Ensuring inputs use appropriate mobile virtual keyboards (e.g., numeric keypad for telephone numbers)"},
                    {"id": "d", "text": "Forcing mobile users to download uncompressed 4K desktop hero images"}
                ],
                "correct": ["a", "b", "c"],
                "explanation": "Mobile design must account for touch precision, keyboard input types, bandwidth efficiency, and responsive reflow. Downloading heavy desktop assets hurts mobile usability."
            }
        ]
    }
]

all_questions = []
for assign in assignments:
    w = assign["week"]
    topic = assign["topic"]
    for q in assign["questions"]:
        all_questions.append({
            "id": f"w{w}_q{q['num']}",
            "assignmentWeek": w,
            "questionNumber": q["num"],
            "type": q["type"],
            "prompt": q["prompt"],
            "options": q["options"],
            "correctAnswers": q["correct"],
            "explanation": q["explanation"],
            "topic": topic
        })

print(f"Total questions generated: {len(all_questions)}")
with open("src/data/questions.json", "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2)
print("Successfully written to src/data/questions.json")
