# Relation Patterns

Use this file to identify the report's internal logic before writing the image prompt.

## Core relation types

Extract relations explicitly. Do not collapse them into a single generic “flow”.

- `background -> problem`: motivation leads to a sharper scientific question
- `problem -> objective`: the problem defines the overall target
- `objective -> module`: the target is decomposed into research modules
- `module -> method`: each module has its own technical approach
- `module -> output`: each module yields an intermediate result
- `parallel modules -> integration`: multiple lines of work converge into a unified system or conclusion
- `evaluation -> refinement`: validation feeds back into optimization
- `theory -> experiment`: theoretical analysis supports experimental design
- `data -> model -> validation`: data supports modeling, then verification
- `hardware/software/co-design`: parallel subsystems interact bidirectionally

## Common structural patterns

### 1. Linear staged pattern

Use when the report has a clear sequence:

- background
- objective
- method stage 1
- method stage 2
- validation
- outcome

Recommended layout:

- left to right or top to bottom
- few branches
- clear milestone arrows

### 2. Parallel module pattern

Use when the report splits the problem into several subtopics or work packages.

Recommended layout:

- one top-level objective area
- two to four parallel module boxes in the middle
- one integration or expected-result area at the bottom or right

### 3. Layered abstraction pattern

Use when the report spans different layers, such as:

- theory
- algorithm
- system
- application

Recommended layout:

- stacked bands from abstract to concrete
- vertical dependencies
- side arrows only for cross-layer feedback

### 4. Input-process-output pattern

Use when the report naturally organizes into source conditions, technical pipeline, and outputs.

Recommended layout:

- left input region
- middle processing pipeline
- right output region

### 5. Closed-loop optimization pattern

Use when the report emphasizes iteration, evaluation, and refinement.

Recommended layout:

- main forward path
- one visible feedback arrow
- evaluation node placed near the lower right or lower center

## Prioritization rules

- Choose one dominant reading path.
- Keep no more than one secondary feedback loop unless the source strongly requires more.
- Merge adjacent text fragments when they express the same function.
- Separate nodes that belong to different logical levels even if the source mentions them in one sentence.

## Text extraction heuristics

- Objectives usually start with “面向…”, “针对…”, “实现…”, “构建…”, or “揭示…”.
- Methods often contain verbs such as “设计”, “提出”, “构建”, “优化”, “融合”, “建模”, “重建”, “生成”, or “验证”.
- Outputs often contain “提升”, “实现”, “形成”, “获得”, “支撑”, or explicit metric/result language.
- Scientific problems often contain “关键问题”, “核心挑战”, “机理”, “映射关系”, “瓶颈”, or “约束”.

## Visual translation rules

- Put the most general statement in the most visually dominant anchor position.
- Put peer modules at the same size and visual level.
- Put methods inside or directly beneath their corresponding modules.
- Put expected outputs in a convergence block, not scattered among methods.
- Use grouped pale-blue containers when one module contains several tightly linked substeps.
