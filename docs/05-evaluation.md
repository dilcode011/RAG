# 05 - RAG Evaluation

## Why Evaluation Matters

Without proper evaluation, you cannot know if your improvements are real or just placebo.

## Evaluation Dimensions

1. **Retrieval Quality**
   - Recall
   - Precision
   - Mean Reciprocal Rank (MRR)
   - Normalized Discounted Cumulative Gain (NDCG)

2. **Generation Quality**
   - Faithfulness (no hallucination)
   - Answer Relevancy
   - Contextual Precision & Recall
   - Groundedness

3. **End-to-End Metrics**
   - Overall correctness
   - User satisfaction (human eval)
   - Latency & Cost

## Popular Evaluation Frameworks (2026)

| Framework     | Focus                     | Open Source | Best For                     |
|---------------|---------------------------|-------------|------------------------------|
| RAGAS         | LLM-as-Judge              | Yes         | Most popular                 |
| DeepEval      | Production monitoring     | Yes         | End-to-end testing           |
| ARES          | Automated evaluation      | Yes         | Research-grade               |
| LangSmith     | Tracing + evaluation      | No          | LangChain users              |
| Phoenix       | Observability             | Yes         | Tracing & visualization      |

## Key Metrics Explained

- **Faithfulness**: Does the answer stick to the provided context?
- **Answer Relevancy**: Is the answer relevant to the question?
- **Contextual Precision**: Are all retrieved chunks actually useful?
- **Contextual Recall**: Did we retrieve all necessary information?

## Best Practices for Evaluation
- Create a golden dataset (questions + reference answers + ground truth contexts)
- Use multiple LLMs as judges for robustness
- Track metrics over time as you improve the pipeline
- Combine automated + human evaluation

## Recommended Workflow
1. Build baseline RAG
2. Create evaluation dataset (50–200 samples)
3. Run automated evaluation
4. Identify weak areas (retrieval vs generation)
5. Iterate with advanced techniques
6. Re-evaluate

---

**Congratulations!**  
You have completed the core documentation set for your RAG learning journey.

**Next Actions:**
- Read all 5 docs
- Start implementing from `notebooks/01-naive-rag`
- Track your progress in `ROADMAP.md`

Happy Learning! 🚀