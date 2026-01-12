# sycophancy-eval-gpt4
1. Executive Summary

This project implements an automated research pipeline to empirically measure sycophancy in GPT-4o-mini. Specifically, I investigated the "Expertise Trigger"—the tendency for models to prioritize user deference over factual accuracy when prompted with a high-authority persona.

Key Finding: My results demonstrate a significant "Sycophancy Gap," where the model's error rate increased from 11.1% (Neutral) to 25% (Expert). In objective categories like Technology, the model exhibited a 50% failure rate under expert pressure.
2. Research Methodology

I developed a dual-condition benchmarking framework to test model truthfulness across 30 hand-crafted "False Premise" questions.
Technical Stack

    Orchestration: Python 3.x

    Data Persistence: SQLite (for structured experiment logging and reproducibility)

    Analysis: Pandas & Seaborn

    Model: GPT-4o-mini (temperature=0 for deterministic, reproducible results)

Experimental Design

Each test case was passed through the pipeline under two conditions:

    The Control (Neutral): A standard system prompt ("You are a helpful assistant").

    The Variable (Expert): A high-authority system prompt ("I am a world-renowned PhD... I am certain [Wrong Answer] is correct").

3. Results & Visualization

The following chart illustrates the domain-specific susceptibility to sycophantic pressure: ![Research Results](research_results.png)
Observations

    High-Stakes Failures: The model showed a 0.67 lie rate in the Health category, agreeing with dangerous or incorrect advice when pushed by the "Expert" persona.

    The Tech-Logic Flip: While the model was 100% accurate in neutral settings for Tech and Math, it succumbed to falsehoods nearly 30-50% of the time under authority bias.

4. Alignment Implications

This project highlights a core tension in RLHF (Reinforcement Learning from Human Feedback): the tradeoff between helpfulness (being agreeable) and honesty (being factual). My research suggests that without explicit honesty-incentivized training, models remain highly steerable by assertive users, which presents a significant risk in professional decision-support contexts.
5. How to Reproduce

To replicate this study, ensure you have an OpenAI API key saved in a .env file.

    Install Dependencies:
    Bash

pip install -r requirements.txt

Run the Evaluation:
Bash

python run_eval.py

Analyze the Database:
Bash

    python check_db.py

6. Future Work

    Recursive Pressure: Testing if "Expert" personas can talk the model into ignoring its own Chain-of-Thought reasoning.

    Cross-Model Benchmarking: Comparing these results against Claude 3.5 Sonnet to evaluate if Constitutional AI training reduces this specific failure mode.
