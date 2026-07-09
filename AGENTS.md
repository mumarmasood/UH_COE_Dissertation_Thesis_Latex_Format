# AGENTS.md

## Project Identity

This repository is for Umar Masood’s Ph.D. thesis writing project. The thesis is centered on bio-inspired underwater robotic fish systems, with emphasis on 3D robotic fish development, variable buoyancy control, perception and environmental sensing, and a path toward cooperative/swarm underwater monitoring.

The thesis should be treated as a system-level robotics thesis, not merely a collection of separate papers. The main story should connect the work as:

**robotic fish platform → 3D buoyancy/depth control → perception and environmental sensing → toward cooperative/swarm monitoring**

The current working theme is:

**Design, control, perception, and environmental sensing of bio-inspired robotic fish for underwater monitoring applications.**

This framing is a starting point and may evolve. Do not treat the current structure as final unless Umar explicitly confirms it.

---

## General Writing Rules

* Maintain a professional Ph.D.-level academic tone.
* Be technically precise, but avoid unnecessarily complicated language.
* Do not exaggerate claims.
* Do not invent results, citations, experiments, equations, figures, tables, or parameter values.
* Clearly distinguish between:

  * proposed work,
  * designed hardware,
  * implemented algorithms,
  * simulation results,
  * benchtop validation,
  * pool experiments,
  * full robotic fish experiments,
  * future work.
* Do not write as if preliminary or controlled-environment experiments prove full field deployment.
* Do not use vague phrases such as “highly efficient,” “intelligent,” “robust,” or “autonomous” unless the surrounding text explains exactly what is meant.
* Avoid turning the thesis into generic background writing. Each paragraph should support the thesis story.
* Preserve LaTeX formatting, labels, citations, equations, figure references, and table references.
* If citation keys are missing, mark them clearly as TODO rather than inventing references.
* If information is uncertain, insert a clear placeholder such as `[TODO: confirm experimental value]`.

---

## LaTeX and File Editing Rules

* Before editing, inspect the relevant `.tex`, `.bib`, figure, and chapter files.
* Make small, reviewable edits.
* Do not restructure the whole thesis unless asked.
* Do not delete existing content unless it is clearly duplicate, misplaced, or Umar explicitly asks.
* Preserve existing labels such as `\label{...}`, `\ref{...}`, `\eqref{...}`, and `\cite{...}` unless there is a clear reason to change them.
* Keep figure captions technically specific and not exaggerated.
* Keep tables consistent in units, notation, and formatting.
* Use consistent terminology across chapters.
* Prefer thesis-style integration over paper-copy-paste style.
* When adapting text from papers, rewrite it so it fits the thesis narrative and avoids unnecessary repetition.

---

## Core Thesis Terms

Use terminology consistently.

Preferred terms include:

* bio-inspired robotic fish
* underwater robotic fish
* variable buoyancy device
* buoyancy control system
* 3D underwater motion
* depth regulation
* perception and environmental sensing
* vision-based pipeline tracking
* CO2 monitoring
* oil-spill sensing
* RSS-based relative localization
* cooperative underwater monitoring
* robotic fish swarm, only when framed carefully as future/toward-swarm work

Avoid overusing “AI” or “intelligent” unless the section clearly explains the intelligence in terms of sensing, control, autonomy, perception, decision-making, or system integration.

---

## Working Thesis Architecture

The following seven-part structure is a starting point, not a fixed final outline. Use it as the default guide unless Umar provides a different structure.

### 1. Introduction

Purpose: introduce the overall research problem and thesis story.

Include:

* underwater environmental and infrastructure monitoring motivation,
* limitations of conventional underwater monitoring approaches,
* motivation for bio-inspired robotic fish,
* need for 3D underwater motion,
* need for sensing and perception,
* motivation for future cooperative/swarm monitoring,
* research objectives,
* main contributions,
* thesis organization.

Do not include detailed derivations, full experimental results, or paper-level methods here.

---

### 2. Development of a 3D Bio-Inspired Robotic Fish Platform with Variable Buoyancy

Purpose: explain the robotic fish platform and its physical/mechatronic realization.

This chapter should answer:

**What robotic platform was developed, and how does it enable 3D underwater operation?**

Include:

* robotic fish body and mechanical design,
* tail/propulsion mechanism,
* buoyancy control device as hardware,
* actuator and sensor integration,
* embedded electronics at system level,
* communication and control interface at system level,
* basic platform specifications,
* swimming and buoyancy-device validation,
* role of the platform as the foundation for later chapters.

Mention the buoyancy control device physically and mechanically here, but leave detailed controller formulation for the control chapter.

Do not over-focus on MPC, ESC, CO2 sensing, oil-spill sensing, or swarm localization in this chapter.

---

### 3. Modeling and Control of Variable Buoyancy for 3D Underwater Motion

Purpose: explain the control methodologies developed for buoyancy/depth regulation.

This chapter should answer:

**How can the variable buoyancy system be modeled and controlled for vertical motion and depth regulation?**

Include:

* buoyancy dynamics,
* depth-control problem formulation,
* actuator/device constraints,
* model assumptions,
* constrained control methodology from the AIM paper,
* recent ESC-related control work,
* comparison of the control approaches,
* simulation and/or experimental validation,
* limitations and practical implementation considerations.

Be very clear about whether each result is simulation, benchtop experiment, pool experiment, or full robotic fish experiment.

Do not repeat all mechanical design details from Chapter 2. Refer back to the platform chapter when needed.

---

### 4. Perception and Environmental Sensing with Bio-Inspired Robotic Fish

Purpose: show how the robotic fish functions as a mobile perception and sensing platform.

This chapter should answer:

**How can the robotic fish be used to perceive underwater features and collect environmental sensing data?**

Include:

* vision-based pipeline tracking,
* image processing and line/pipeline detection,
* visual error calculation and tracking concept,
* CO2 sensing/monitoring work,
* oil-spill sensing work,
* sensing payloads and data collection,
* experimental setup,
* sensing results,
* limitations of controlled-environment sensing.

This chapter should unify pipeline tracking, CO2 monitoring, and oil-spill sensing under the broader theme of robotic fish-based underwater perception and environmental monitoring.

Do not claim full industrial pipeline deployment or open-water field validation unless the thesis files explicitly support that.

---

### 5. Toward Cooperative Robotic Fish Swarms Using RSS-Based Relative Localization

Purpose: present the step from a single robotic fish toward cooperative multi-robot underwater monitoring.

This chapter should answer:

**How can relative localization support future cooperative robotic fish/swarm monitoring?**

Include:

* motivation for multi-robot underwater monitoring,
* limitations of a single robotic fish,
* need for relative localization,
* RSS-based localization work,
* IMU/EKF details if they are part of the actual work,
* experimental or simulation setup,
* localization results,
* connection to future robotic fish swarm operation.

Use “toward swarm” language carefully. Do not claim a complete robotic fish swarm exists unless it was actually built and demonstrated.

---

### 6. Integrated Discussion

Purpose: connect the technical chapters into one thesis-level argument.

This chapter should not simply repeat chapter summaries. It should discuss the thesis as a whole.

Include:

* how the robotic fish platform supports the later control and sensing work,
* how buoyancy control enables 3D environmental monitoring,
* how perception and sensing demonstrate the usefulness of the platform,
* how RSS localization extends the work toward cooperative monitoring,
* technical limitations across the whole thesis,
* system-level tradeoffs,
* what was learned from integrating hardware, control, sensing, and localization.

This chapter should be analytical and integrative.

---

### 7. Conclusions and Future Work

Purpose: close the thesis clearly.

Include:

* concise restatement of the thesis problem,
* summary of main contributions,
* final conclusions from the work,
* future work directions.

Future work may include:

* improved onboard autonomy,
* onboard camera/edge processing,
* more advanced depth and trajectory control,
* better underwater localization,
* multi-robot experiments,
* field testing,
* improved sensor payloads,
* longer-duration operation,
* full integration of perception, sensing, and cooperative monitoring.

Do not introduce new technical results in the conclusion.

---

## Results and Discussion Placement

For technical chapters, include chapter-level results and discussion inside the same chapter where the method is introduced.

Preferred pattern for Chapters 2–5:

1. Chapter introduction
2. Related background specific to that chapter
3. System/model/method
4. Experimental or simulation setup
5. Results
6. Discussion
7. Chapter summary

Do not move all results to the end of the thesis. That would make the thesis hard to follow because the work spans hardware, control, sensing, and localization.

The final discussion chapter should integrate results across chapters, not replace the individual results sections.

---

## Chapter-Specific Cautions

### Platform chapter cautions

* Do not overclaim autonomy if the system was operated through a GUI or external computer.
* Do not bury the buoyancy control device; it is one of the key links to 3D operation.
* Do not overload the chapter with control theory.

### Control chapter cautions

* Do not blur simulation and hardware validation.
* Do not hide actuator constraints or physical limitations.
* Do not present PID, MPC, ESC, or any controller as better without explaining the metric or evidence.
* Do not change equations without checking notation consistency.

### Perception and sensing chapter cautions

* Do not make CO2, oil-spill sensing, and pipeline tracking feel like unrelated projects.
* Connect them as examples of robotic fish-based perception and environmental monitoring.
* Be careful with sensor calibration, response time, spatial mapping, and controlled-environment limitations.
* Do not claim ocean-scale deployment unless supported.

### Swarm chapter cautions

* Use “toward swarm” or “toward cooperative monitoring” unless a complete swarm was demonstrated.
* Clearly distinguish RSS localization from full swarm autonomy.
* Connect the localization work back to robotic fish monitoring, but do not force unsupported claims.

### Discussion/conclusion cautions

* Do not repeat abstracts from each paper.
* Explain the unified contribution.
* Be honest about limitations.
* Make future work concrete and technically grounded.

---

## Known Work That Should Not Be Lost

When organizing or editing the thesis, do not accidentally omit major work areas that belong in the thesis narrative:

* 3D robotic fish platform development,
* variable buoyancy device,
* buoyancy/depth-control methodologies,
* AIM paper work,
* recent ESC paper work,
* vision-based pipeline tracking / IBVS-related work,
* CO2 sensing paper,
* oil-spill sensing paper,
* RSS-based relative localization / toward-swarm work,
* Python GUI and system integration where relevant,
* pool testing and experimental validation where supported.

Older non-Ph.D. robotics work, such as NUST/NCRA projects, UGVs, industrial automation projects, or unrelated robotics prototypes, should generally not be included in the main technical thesis chapters unless Umar explicitly asks or they are needed briefly for background.

---

## Editing Behavior for Codex

When asked to edit thesis text:

1. First identify which chapter and thesis role the text belongs to.
2. Check whether the text supports the chapter’s purpose.
3. Improve clarity, flow, technical accuracy, and thesis-level connection.
4. Remove or flag overclaims.
5. Preserve evidence-backed claims.
6. Keep terminology consistent.
7. Add TODO markers where information must be confirmed.
8. Summarize what was changed.

When asked to create new thesis text:

* Ask for missing technical details if needed.
* Do not invent missing results.
* Use placeholders for missing citations, values, figures, or experimental details.
* Write in a style suitable for a Ph.D. dissertation.
* Make the text connect to the overall thesis story.

When asked to reorganize chapters:

* Do not assume the current structure is fixed.
* Treat the seven-part structure as a starting point.
* Recommend changes based on coherence, committee expectations, and evidence available in the thesis files.
* Explain why a section should move, merge, or be split.

---

## Final Principle

The thesis should read as one coherent research contribution:

**a bio-inspired robotic fish platform was developed for 3D underwater operation, controlled through variable buoyancy methodologies, applied to perception and environmental sensing tasks, and extended conceptually and experimentally toward cooperative multi-robot monitoring.**

Every chapter, section, figure, and result should support this central thesis story.
