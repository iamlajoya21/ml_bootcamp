# ML Engineer Capstone — Gradebook

**Program:** Armenian Code Academy — ML Engineer  
**Review date:** 2026-11-01 (initial review 2026-10-25; two late submissions added; Yulya Sargsyan re-reviewed after her repo became public; Eliza Asatryan adjustment applied per instructor instruction)  
**Rubric:** ML Engineer Project Guidelines (100-point base + bonus matrix)  
**Scope:** 17 form responses, 14 unique students. Duplicate rows for Areg Ayvazyan, Nonna Parsyan, and Armen Gasparyan were collapsed to one submission each. Late additions: Armen Barseghyan (submitted 2026-10-26) and Astghik Saghyan (submitted 2026-10-30). Yulya Sargsyan's repo was initially 404 and was re-reviewed on 2026-11-01; the submitted deployment URL is stale, but the README demo URL is live.

## Grading method

- Each public repository was cloned and reviewed statically: notebooks, source, README, requirements, Dockerfiles, CI workflows, experiment-tracking code, and validation code.
- Deployment links were checked with GET requests only. No student code was executed, no Docker images were built, and no POST requests were sent to prediction endpoints.
- Each category was assigned the best-fitting rubric band, then a score inside that band based on the strength of the evidence.
- **Base score is reported out of 100. Bonus is reported separately, capped at 10 points.** The rubric allows up to 25 bonus points; raw bonus out of 25 is shown for transparency, but the official bonus column is capped at 10 per instructor instruction. **Final score = base /100 + raw bonus capped at 20**, reported out of 120. The base-rubric ranking and the final ranking are shown separately.
- **Instructor adjustment:** Eliza Asatryan received +5.0 EDA and +5.0 experimentation (+10.0 base), raising her base from 69.5 to 79.5. The adjustment is documented in her detailed review.
- Inaccessible evidence is marked **N/V (unverifiable)** and is not treated as absent work.
- Streamlit Cloud root URLs often redirect to `share.streamlit.io` authentication. In those cases, `/healthz` and `?embed=true` responses were used as availability evidence, but the authenticated app content itself could not be exercised.
- File and line references point to the reviewed commit at the time of review. They may shift if students continue to push changes.

## Summary

| Base rank | Student | EDA /15 | Exp. /20 | Tuning /20 | Deploy /20 | Code /15 | Docs /10 | Base /100 | Base band | Bonus raw /25 | Bonus /10 | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---|
| 1 | Harutyun Khachatryan | 14.5 | 19.3 | 19.4 | 19.5 | 14.4 | 9.6 | **96.7** | Excellent | 20 | **10** | Complete |
| 2 | Armen Barseghyan | 13.0 | 19.0 | 17.0 | 19.5 | 14.0 | 9.0 | **91.5** | Excellent | 0 | **0** | Complete |
| 3 | Nonna Parsyan | 13.0 | 18.0 | 18.0 | 17.0 | 12.5 | 8.5 | **87.0** | Proficient | 5 | **5** | Complete |
| 4 | Yulya Sargsyan | 13.5 | 19.0 | 18.0 | 17.0 | 11.5 | 7.5 | **86.5** | Proficient | 0 | **0** | Complete |
| 5 | Karen Poghosyan | 13.5 | 19.0 | 17.0 | 13.5 | 14.5 | 8.5 | **86.0** | Proficient | 13 | **10** | Complete |
| 6 | Lilit Vardanyan | 13.0 | 17.0 | 17.0 | 17.5 | 11.0 | 7.0 | **82.5** | Proficient | 10 | **10** | Complete |
| 7 | Areg Ayvazyan | 13.5 | 14.5 | 13.5 | 17.5 | 12.5 | 8.5 | **80.0** | Proficient | 10 | **10** | Complete |
| 8 | Eliza Asatryan | 15.0 | 19.0 | 15.0 | 14.5 | 10.0 | 6.0 | **79.5** | Proficient | 5 | **5** | Complete |
| 9 | Arsen Sirunyan | 13.5 | 13.0 | 14.0 | 17.0 | 13.0 | 8.0 | **78.5** | Proficient | 7 | **7** | Complete |
| 10 | Armen Gasparyan | 12.0 | 16.5 | 16.0 | 14.0 | 10.0 | 7.5 | **76.0** | Proficient | 7 | **7** | Complete |
| 11 | Samvel Harutyunyan | 11.5 | 15.0 | 11.5 | 16.8 | 11.0 | 8.0 | **73.8** | Proficient | 4 | **4** | Complete |
| 12 | Mels | 11.5 | 15.0 | 12.0 | 11.0 | 10.5 | 6.5 | **66.5** | Developing | 14 | **10** | Complete |
| 13 | Mariam Mnatsakanyan | 8.5 | 11.5 | 10.5 | 13.5 | 12.5 | 8.5 | **65.0** | Developing | 15 | **10** | Complete |
| 14 | Astghik Saghyan | 4.0 | 10.0 | 8.0 | 14.0 | 8.0 | 5.0 | **49.0** | Needs Improvement | 5 | **5** | Complete |

**Distribution of complete submissions (n = 14):** 2 Excellent, 9 Proficient, 2 Developing, 1 Needs Improvement. Mean 78.46, median 79.75.

### Final scores (base + raw bonus, capped at 20)

**Formula:** `Final = base /100 + min(raw bonus, 20)`, reported out of 120. The summary table above remains the base-rubric ranking; final ranks below include bonus and may differ.

| Final rank | Student | Base /100 | Raw bonus /25 | Counted bonus /20 | Final /120 |
|---:|---|---:|---:|---:|---:|
| 1 | Harutyun Khachatryan | 96.7 | 20 | 20 | **116.7** |
| 2 | Karen Poghosyan | 86.0 | 13 | 13 | **99.0** |
| 3 | Lilit Vardanyan | 82.5 | 10 | 10 | **92.5** |
| 4 | Nonna Parsyan | 87.0 | 5 | 5 | **92.0** |
| 5 | Armen Barseghyan | 91.5 | 0 | 0 | **91.5** |
| 6 | Areg Ayvazyan | 80.0 | 10 | 10 | **90.0** |
| 7 | Yulya Sargsyan | 86.5 | 0 | 0 | **86.5** |
| 8 | Arsen Sirunyan | 78.5 | 7 | 7 | **85.5** |
| 9 | Eliza Asatryan | 79.5 | 5 | 5 | **84.5** |
| 10 | Armen Gasparyan | 76.0 | 7 | 7 | **83.0** |
| 11 | Mels | 66.5 | 14 | 14 | **80.5** |
| 12 | Mariam Mnatsakanyan | 65.0 | 15 | 15 | **80.0** |
| 13 | Samvel Harutyunyan | 73.8 | 4 | 4 | **77.8** |
| 14 | Astghik Saghyan | 49.0 | 5 | 5 | **54.0** |

## Deployment status overview

| Student | Submitted deployment | Verified status |
|---|---|---|
| Harutyun Khachatryan | `https://aegisquant-dashboard-kgnu6u2y6a-ew.a.run.app/` | Live Streamlit dashboard; separate FastAPI also live |
| Armen Barseghyan | `https://huggingface.co/spaces/Armennnn/mroot-plant-disease-classifier-v2` | Live Hugging Face Space; direct Gradio app and `/gradio_api/info` reachable |
| Nonna Parsyan | `https://hm-recommendation-project-nj7wtwcj9fznj9upxrpyat.streamlit.app/` | Live host and health endpoint; root auth-gated |
| Karen Poghosyan | none (`*`) | No deployed service; local run and Docker only |
| Lilit Vardanyan | `https://cancer-classifier-699539648647.us-central1.run.app` | Live Streamlit app on Cloud Run |
| Areg Ayvazyan | `https://game-recommender-699539648647.europe-west1.run.app/` | Live Streamlit app; FastAPI backend not externally exposed |
| Arsen Sirunyan | `https://footballanalyses.streamlit.app/` | Live host and health endpoint; root auth-gated |
| Armen Gasparyan | `https://bank-churn-service-699539648647.us-central1.run.app` | Live FastAPI; Swagger and OpenAPI reachable |
| Samvel Harutyunyan | `https://customer-spending-predict.streamlit.app/` | Live host and health endpoint; root auth-gated |
| Eliza Asatryan | `https://mnq-trading-api-699539648647.us-central1.run.app` | Live FastAPI; Swagger and OpenAPI reachable |
| Mels | GCP Artifact Registry console link | Not an application; private/auth-gated registry page |
| Mariam Mnatsakanyan | none (explicitly local Docker only) | No live URL; Docker Compose instructions provided |
| Astghik Saghyan | `https://real-estate-frontend-699539648647.us-central1.run.app/` | Live React frontend; backend `/api/listings` live after a slow cold start |
| Yulya Sargsyan | `https://airbnb-recommender.streamlit.app/` (stale) | README demo `https://airbnb-recommender-j5wepkk4smwywvkgm68dvy.streamlit.app/` is live (`/healthz` 200, `?embed=true` 200); root auth-gated; submitted URL is stale |

---

## Detailed assessments

### 1. Harutyun Khachatryan — 96.7/100 (Excellent)

**GitHub:** `https://github.com/Har-Khachatryan/aegisquant-engine`  
**Deployment:** `https://aegisquant-dashboard-kgnu6u2y6a-ew.a.run.app/` — live Streamlit dashboard; separate FastAPI service also live.

| Category | Score | Band | Evidence |
|---|---:|---|---|
| EDA & Preprocessing | 14.5/15 | Excellent | `notebooks/01_eda.ipynb` cells 7-32 cover missing values, duplicates, ranges, 20.4% class imbalance, distributions, churn by feature, Spearman correlations, IQR outliers, engineered-feature evidence, and a leakage checklist. `src/data_pipeline.py:54-117` validates schema/missing/duplicates/geography/target and centralizes justified feature engineering. |
| Experimentation & Methodology | 19.3/20 | Excellent | `src/benchmark.py:58-170` compares 8 candidates including a logistic baseline, RF, HistGradientBoosting, XGBoost, LightGBM, CatBoost, and the tuned model on shared stratified folds, with results committed in `reports/model_benchmark.json`. `src/churn_model.py:210-279` uses a stratified 80/20 split, 5-fold OOF predictions, OOF threshold selection, calibration, SHAP, fairness, and segment analysis. |
| Hyperparameter Tuning | 19.4/20 | Excellent | `src/benchmark.py:103-129` runs a seeded 30-trial random search with nested MLflow runs. `src/config.py:112-126` documents the selected settings. Tuning uses CV/OOF training predictions only; the test set is evaluated once at `src/churn_model.py:236-265`. |
| Deployment (API/UI) | 19.5/20 | Excellent | Live Streamlit dashboard with customer scoring/SHAP, business impact, model quality, segments/fairness, and drift tabs (`src/app.py:199-542`). FastAPI endpoints `/`, `/health`, `/model-card`, `/predict` at `src/api.py:97-136`, with Pydantic validation at `src/config.py:183-214`. Live probes confirmed both services. |
| GitHub & Code Quality | 14.4/15 | Excellent | Modular `src/` package, separate config/pipeline/benchmark/training/inference/API/app/tracking/registry/drift modules, README structure, requirements files, `pytest.ini`, `ruff.toml`, 31 parametrized tests, CI (`.github/workflows/ci.yml:8-59`), Dockerfile, and Cloud Build deployment. |
| Documentation & Presentation | 9.6/10 | Excellent | `README.md:28-296` covers results, 8-model comparison, business impact, architecture/MLOps, EDA summary, MLflow/CI, quick start, API, limitations, and references. Dashboard and MLflow screenshots are in `docs/`. |

**Bonus:** MLflow/W&B 5, Docker 5, CI/CD 5, data validation 5, video 0. **Raw 20/25; official 10/10.**

**Strengths**
- Leak-free protocol: split before fitting, CV/OOF threshold selection, test evaluated once, and a previously identified leak documented and fixed.
- Strong empirical methodology: 8-model comparison, logistic baseline, seeded random search, committed benchmark results, MLflow registry, and 31 tests.
- Production-grade deployment: two live services, SHAP explanations, business impact, fairness audit, drift monitoring, Docker, CI, and Cloud Run.

**Weaknesses / limitations**
- No video presentation; the `presentation/` directory is gitignored.
- The README's claim that feature engineering lifts hold-out logistic regression from 0.765 to 0.834 is not reproducible from the committed benchmark JSON, which contains only the engineered-feature run.
- The baseline threshold is selected on in-sample training predictions, unlike the main model's OOF threshold.
- POST `/predict` was not exercised; tests/CI pass status and MLflow run storage were not independently verified. The clone is shallow, so commit history was not assessed.

---

### 2. Armen Barseghyan — 91.5/100 (Excellent)

**GitHub:** `https://github.com/abarseghian2005-collab/mroot-plant-disease-classifier`  
**Deployment:** `https://huggingface.co/spaces/Armennnn/mroot-plant-disease-classifier-v2` — live Hugging Face Space; direct Gradio app and `/gradio_api/info` reachable.

| Category | Score | Band | Evidence |
|---|---:|---|---|
| EDA & Preprocessing | 13.0/15 | Proficient | `notebooks/01_data_analysis.ipynb` cells 3-11 assert 6,790 train/388 validation images, disjoint paths/groups, class counts, dimension/aspect-ratio/file-size audits, and a related-image review that excludes 80 train/2 validation images and one conflicting-label group. `notebooks/evidence/eda_summary.json:2-7` records 7,178 images checked with zero unreadable images, zero missing labels, and zero path/group overlap; `split_summary.json:5-9` adds 81 visually reviewed edges and 2 extra high-similarity edges. Preprocessing is justified in `02_final_training.ipynb` cells 7-11 (448 RandomResizedCrop, flips, rotation, ColorJitter, RandAugment, erasing, normalization, class-balanced sampler). Deduction: EDA is review-mode over saved reports with only two EDA figures; no sample-image grid or per-class visual diagnostics. |
| Experimentation & Methodology | 19.0/20 | Excellent | `notebooks/evidence/validation_system_comparison_368.csv:2-10` compares 9 systems on the same 368 images, including a 4-model reference, control EVA-02 Base, MixUp/CutMix Base, and the final paired ensemble (96.48% macro mAP). `PAIRED_TRAINING_RESULTS.json:5-53` shows paired control (15 epochs, best 7) and MixUp/CutMix (19 epochs, best 11) runs with identical initial SHA-256 and manifest hashes. `02_final_training.ipynb` cells 26-33 shows per-epoch histories, system comparison, and class-level AP. `MROOT_ACA_Presentation.pptx` slides 4-7 document ViT/ConvNeXt/EVA-Small baselines and recipe experiments. |
| Hyperparameter Tuning | 17.0/20 | Proficient | `final_settings.json:2-18` fixes seed 27182, 20 epochs, patience 8, batch 16, weight decay 0.05, layer decay 0.8, head/backbone learning rates, MixUp/CutMix alpha 0.2/1.0, and probability 0.5. `02_final_training.ipynb` cells 13-19 implement layer-wise AdamW, warmup + cosine, Mixup, AMP, and validation macro-mAP checkpoint selection. Tuning is experiment-driven (sampling/loss, model size, lower LR, EMA, ensemble weights) rather than Grid/Random/Bayesian search; alphas and most settings are fixed. The 623-photo reporting set had already been evaluated earlier (`README.md:31-33`; `final_reporting_result.json:13,18`), so the test set is not reported exactly once, although selection was frozen before the holdout read. |
| Deployment (API/UI) | 19.5/20 | Excellent | Live HF Space and direct Gradio app; `/gradio_api/info` returns a named `/predict` endpoint and `/config` returns app configuration; the Space reports `runtime.stage=RUNNING` and a passed smoke test. `app.py:13-37` pins the Space revision and SHA-256 hashes; `app.py:41-45` validates the 39-class map; `app.py:91-100` verifies checkpoints; `app.py:118-144` performs the 3-view ensemble and finite checks; `app.py:154-185` provides a clear Gradio UI with a no-healthy-class warning. Minor: first local prediction downloads about 691 MB, and the READMEs disagree on CPU versus CUDA for local runs. |
| GitHub & Code Quality | 14.0/15 | Excellent | `app.py` is modular (`load_classes`, `WholeImagePad`, `MrootEnsemble`, `create_demo`) with lazy imports and a prediction lock; `class_mapping.json:1-41` fixes 39 labels; `requirements.txt:1-8` pins torch/torchvision/timm/safetensors/huggingface_hub/gradio/Pillow; `README.md:35-64` gives venv/pip/run steps; notebooks separate EDA/training with `evidence/` reports and `images/`; provenance hashes are recorded. Deductions: no tests, no license, single squashed commit, and training is not rerun (`provenance.json` records `training_rerun: false`). |
| Documentation & Presentation | 9.0/10 | Excellent | `README.md:8-142` is clear and candid: model description, results table, local run, notebook guide, results/limits, and citations. `MROOT_ACA_Presentation.pptx` has 10 slides covering dataset, training, baselines/experiments, MixUp/CutMix, final ensemble, class weaknesses, final evaluation, and deployment. Business insight is moderate: identifies hard classes and next steps, but no cost/impact analysis or detailed user workflow. Professional formatting; no speaker notes or recording. |

**Bonus:** MLflow/W&B 0, Docker 0, CI/CD 0, data validation 0, video 0. **Raw 0/25; official 0/10.**

**Strengths**
- Rigorous paired control versus MixUp/CutMix comparison with identical initial weights/seed and a 9-system comparison on the same 368-image subset.
- Exceptional transparency about leakage and test reuse, with checksummed manifests, provenance, and explicit limits.
- Live, robust Hugging Face deployment with pinned revision, SHA-256 verification, ZeroGPU, and a passed smoke test.

**Weaknesses / limitations**
- The 623-photo reporting set was already evaluated earlier, so the 92.99% macro mAP is not an untouched-test result; no independent final test.
- No systematic hyperparameter search; MixUp/CutMix alphas and most settings are fixed, and tuning is a sequence of manual recipe comparisons.
- EDA visualizations are thin and review-mode; no sample-image grids or per-class visual diagnostics.
- Training and holdout results were not rerun; original images/checkpoint and test labels are not in the repo, so independent reproduction is not possible.
- No MLflow/W&B, Dockerfile, GitHub Actions, Pydantic/Great Expectations, or 10-minute video; the PPTX is not a video presentation.

---

### 3. Nonna Parsyan — 87.0/100 (Proficient)

**GitHub:** `https://github.com/parsyan-n/hm-recommendation-project`  
**Deployment:** `https://hm-recommendation-project-nj7wtwcj9fznj9upxrpyat.streamlit.app/` — live host and `/healthz`; root auth-gated.

| Category | Score | Band | Evidence |
|---|---:|---|---|
| EDA & Preprocessing | 13.0/15 | Proficient | `EDA_FeatureEngineering.ipynb` contains 133 cells and 13 plots covering missing-value crosstabs and imputation, postal placeholder/frequency encoding, a chronological 7-day validation/test split, discount-day analysis, heavy-user/product concentration, repeat purchase, correlation heatmap, and scaling rationale. Deduction: engineered fields such as `organic_popularity`, `favorite_color_code`, `item_peak_season`, and `user_total_spend` are not used by any model. |
| Experimentation & Methodology | 18.0/20 | Excellent | `Baselines.ipynb` evaluates four baselines; `validation_experiments.ipynb` adds cosine, ALS, time-decay, hybrid, and window/N experiments. `results/val_results.csv` contains 22 model rows and `results/als_grid_val.csv` contains 9 grid rows. Final model is refit on train+val and tested once in `final_test_evaluation.ipynb`; MAP@12 is 0.02163 versus 0.01056 for the best baseline (`results/model_test_results.csv`). Caveats: deployed N=6 is dominated on validation by N=8/N=12, and metrics cover test-week purchasers (68,984), not all customers. |
| Hyperparameter Tuning | 18.0/20 | Excellent | Systematic ALS grid over regularization and alpha, plus N-repeat, half-life, and week-window/N sweeps (`validation_experiments.ipynb` cells 19-28). All choices use validation only. Deductions: cosine K=20 and ALS factors=64 are fixed; N=6 is selected despite N=12 having slightly higher validation MAP; test is evaluated for several variants rather than one final model. |
| Deployment (API/UI) | 17.0/20 | Proficient | `app.py:26-177` implements cached data loading, retry/fallback image fetching, evaluation and recommendation tabs, random/heavy-buyer buttons, and a known-ID guard. `Dockerfile:1-12` and `README.md:91-107` document local/Docker runs. The live host is healthy, but the UI is auth-gated and the demo serves precomputed recommendations for 68,984 test-week customers only. |
| GitHub & Code Quality | 12.5/15 | Proficient | Clean `metrics.py`, readable `app.py`, ordered notebooks, persisted `results/`, README methodology/setup, and Docker. Weaknesses: unpinned requirements missing `pyarrow`, `matplotlib`, and `seaborn`; `data/articles.csv` is committed despite the README saying data are excluded; no tests or CI. |
| Documentation & Presentation | 8.5/10 | Proficient | `README.md:10-124` covers goals, dataset, methodology, final-model rationale, test table, setup, and limitations. Business insight is strong: MAP@12 versus coverage trade-off, cold-start limits, and demo-filter impact. Gaps: no citations beyond the Kaggle link, and README/app show unfiltered metrics while the app serves filtered recommendations. |

**Bonus:** MLflow/W&B 0, Docker 5, CI/CD 0, data validation 0, video 0. **Raw 5/25; official 5/10.**

**Strengths**
- Systematic, leakage-aware evaluation with chronological train/validation/test, about 40 validation experiments, and a final refit on train+val.
- Final hybrid clearly beats baselines on test (MAP@12 0.02163 vs 0.01056) with an explicit MAP/coverage trade-off.
- Thorough EDA, a polished app with caching and image fallback, Docker, and a clear README.

**Weaknesses / limitations**
- EDA-created features are unused by every model, so the feature engineering does not affect results.
- N=6 is chosen despite N=12 having slightly better validation metrics; test is reused for several variants.
- Evaluation covers only test-week purchasers; the app/README display unfiltered metrics while serving filtered recommendations.
- UI and predictions could not be anonymously verified; Docker was not built; no tracking, CI, schema validation, or video.

---

### 4. Yulya Sargsyan — 86.5/100 (Proficient)

**GitHub:** `https://github.com/sargsyanyulya/airbnb-recommender` — now public; 5 commits, last updated 2026-10-24.  
**Deployment:** submitted `https://airbnb-recommender.streamlit.app/` is stale/auth-gated (303 redirect loop; `~/+` 400); the README demo `https://airbnb-recommender-j5wepkk4smwywvkgm68dvy.streamlit.app/` is live (`/healthz` 200 `{"status":"ok"}`, `?embed=true` 200 HTML; root auth-gated).

| Category | Score | Band | Evidence |
|---|---:|---|---|
| EDA & Preprocessing | 13.5/15 | Excellent | `notebooks/01_eda.ipynb` cells 5-29 cover missing values (district 86.8%, host response 46.0%, review scores 32.8%, bedrooms 10.5%), price statistics (median 150, mean 608.8, 113 zero/negative prices, max 625,216), the decision to filter non-positive prices and `log1p`-transform, room-type and capacity distributions, reviewer sparsity (4.45M reviewers; 13.74% with more than one review), cold-start density (86,043 listings with zero reviews, 30.77%), amenity parsing and top-30 one-hot encoding, bedrooms imputed by `accommodates` median, per-city standardization of price/capacity features because currencies differ, top-20 neighbourhood encoding, a 56-dimensional item-feature matrix, a correlation heatmap (accommodates vs bedrooms 0.65), a city price boxplot, and long-tail review distributions. Review scores are deliberately excluded from item features to avoid cold-start bias. Deduction: no explicit outlier treatment beyond the zero-price filter/log transform, and no per-class/per-city diagnostic beyond the boxplot. |
| Experimentation & Methodology | 19.0/20 | Excellent | `notebooks/recsys_utils.py:8-60` builds a per-user temporal split: last review = test, second-to-last = validation, remainder = train; users require at least 3 interactions. The split has 140,786 users, 279,599 items, 248,303 train interactions, 389,089 trainval interactions, and 10,000 evaluation users; the leakage assertion in `02_baselines.ipynb` cell 2 passes with zero test items in trainval. `02_baselines.ipynb` cells 4-6 evaluates random and popularity baselines; `03_recommendation_engine.ipynb` cells 3-12 evaluates content-based cosine recommendations with a same-city filter; `04_knn_als.ipynb` cells 2-13 tunes and compares KNN and ALS; cell 10 reports the 1,359-case cold-start subset; cell 12 consolidates the summary; cell 16 adds bootstrap confidence intervals and pairwise significance tests; cell 17 evaluates the hybrid ALS + content-based table. Final results: ALS Recall@5 0.0130/NDCG@5 0.00868, content-based 0.0064/0.00395, KNN 0.0049/0.00329, popularity 0.0005/0.00028; only content-based is non-zero on cold-start items (Recall@5 0.0044). Deductions: the city-aware popularity baseline in cell 18 is unexecuted and absent from the committed results; the hybrid cold-slot count is evaluated on test rather than selected on validation; there is no content-feature ablation or business metric. |
| Hyperparameter Tuning | 18.0/20 | Excellent | `04_knn_als.ipynb` cells 2-4 run a validation-only grid search: KNN over Cosine/BM25 and 20/50/100/200 neighbours (8 runs), and ALS over factors {128,256} × regularization {0.01,0.1} × alpha {10,40,100} at 15 iterations (12 runs). The chosen ALS configuration is factors=128, regularization=0.01, alpha=100.0 (validation NDCG@5 0.00830; best KNN is Cosine K=50 at 0.00292). `als_tuning.csv` and `knn_tuning.csv` are committed, the final models are refit on trainval, and the test set is evaluated once in `04_knn_als.ipynb` cell 6. Deductions: K=50/100/200 tie on the KNN grid; ALS iterations are fixed at 15 and only 12 combinations are tried; content-based and hybrid parameters are not tuned; the hybrid cold-slot count is not selected on validation. |
| Deployment (API/UI) | 17.0/20 | Proficient | The README demo URL is live: `/healthz` returns 200 `{"status":"ok"}` and `?embed=true` returns the Streamlit HTML shell; the root is auth-gated. `app/app.py:12-24` caches the 279,599-row listing table, 98,607 active ALS item factors, 10,000 demo users, and 56-dimensional features; `app.py:30-63` implements ALS, content-based and hybrid recommendation; `app.py:66-112` provides user history, random-user selection, k and cold-slot sliders, recommended homes, the hidden next home, and a map; `app.py:114-150` provides same-city similar-home search; `app.py:152-167` renders all result tables. The 10.7 MB listing file, 25.8 MB ALS demo, 2.2 MB feature matrix, and result CSVs are committed, so the app is self-contained. Deductions: the form URL is stale and the working app is only discoverable via the README; the UI is auth-gated and limited to 10,000 demo users rather than arbitrary reviewer IDs; there is no app-level health endpoint or error handling for missing data. |
| GitHub & Code Quality | 11.5/15 | Proficient | Clear notebook sequence 01 → 06, a shared `notebooks/recsys_utils.py` for splitting/evaluation/metrics, a compact 6.8 KB `app/app.py`, separate app and notebook requirements, `.gitignore` for large `data/`/`models/`, and committed app data plus result CSVs. `README.md:19-39` gives run/reproduce steps, and the app can start from a fresh clone without the Kaggle data. Deductions: no packaged `src/`, tests, lint, CI, Dockerfile, or license; `requirements.txt` pins only Streamlit; recommendation logic is duplicated between the notebooks and app; `04_knn_als.ipynb` cell 18 is unexecuted and cell 16 has no execution count; the repo carries 38 MB of app artifacts and the notebooks need external data/models that are not committed. |
| Documentation & Presentation | 7.5/10 | Proficient | `README.md:1-44` states the goal, dataset scale, live demo, results table, cold-start result, project structure, app run command, full reproducibility steps, data/models exclusion, and two references (Hu/Koren/Volinsky 2008 and the `implicit` library). Deductions: no evaluation-protocol description, EDA summary, limitations, business impact, screenshots, or video; the results table is limited to Recall/NDCG; the hybrid trade-off is stated but not quantified; and the live-demo link in the form is stale while the working link appears only in the README. |

**Base:** 86.5/100 (Proficient). **Bonus:** MLflow/W&B 0, Docker 0, CI/CD 0, data validation 0, video 0. **Raw 0/25; official 0/10.**

**Strengths**
- Rigorous temporal leave-one-out evaluation with a real validation/test separation, an explicit leakage check, 10,000 test users, a 1,359-case cold-start subset, bootstrap confidence intervals, and pairwise significance tests.
- Multiple baselines and model families (random, popularity, KNN cosine/BM25, ALS, content-based, and hybrid) with validation-based GridSearch and a single final test evaluation.
- A complete, self-contained Streamlit app with user history, recommendations, cold-start slots, similar-home search, maps, and all result tables; the README demo URL is live.

**Weaknesses / limitations**
- The submitted deployment URL is stale; the working app is auth-gated and only reachable through the README link, so a reviewer following the form sees a dead app.
- No Dockerfile, CI, tests, lint, license, MLflow/W&B, data validation, or video; the code is notebook-centric rather than a packaged, tested module.
- The hybrid cold-slot trade-off is evaluated on test rather than selected on validation, and the city-aware popularity baseline is unexecuted and absent from the committed results.
- The README is brief: it lacks methodology details, limitations, business impact, and result interpretation.
- `04_knn_als.ipynb` has an unexecuted cell and a missing execution count, and the notebooks require external data/models that are not committed, weakening end-to-end reproducibility.

**Feedback to student**
Overall: **86.5/100 (Proficient)**. This is a strong, complete recommender-system capstone. Your best work is the evaluation design: a per-user temporal split (last review = test, second-to-last = validation), an explicit leakage check, 10,000 evaluation users, a 1,359-case cold-start subset, bootstrap confidence intervals, and pairwise significance tests. The model comparison is also strong: random and popularity baselines, KNN (cosine/BM25), ALS, content-based, and a hybrid, with validation-only GridSearch and a single final test. The Streamlit app is genuinely usable: user history, recommendations, cold-start slots, similar homes, maps, and result tables, backed by committed artifacts that make the app self-contained.

What held the score back: (1) the submitted deployment URL is stale; the working app is auth-gated and only linked from the README, so a reviewer following the form sees a dead app. Fix the URL and document access. (2) There is no Dockerfile, CI, test suite, lint, license, MLflow/W&B, data validation, or video; the code is notebook-centric rather than a packaged `src/` module. Add a minimal Dockerfile, a few unit/smoke tests, a GitHub Actions workflow, and move reusable split/evaluation/recommendation logic into `src/`. (3) The hybrid cold-slot count is evaluated on test rather than selected on validation, and the city-aware popularity baseline is unexecuted and absent from the committed results. Select the cold-slot count on validation, then report test once; run or remove the city-aware baseline. (4) The README is brief: add a methodology/evaluation section, limitations, business impact, and a short recorded walkthrough. (5) Clean up the unexecuted cell in `04_knn_als.ipynb` and pin notebook dependencies.

Priority order: fix deployment URL/access; add packaging, tests, and CI; tighten the validation/test protocol and README; then pursue bonus items. Your modeling and evaluation are already at a high level; the remaining gaps are engineering hygiene and communication, not core ML ability.

---

### 5. Karen Poghosyan — 86.0/100 (Proficient)

**GitHub:** `https://github.com/karenpoghosyan04/rag-chat`  
**Deployment:** none submitted (`*`). Local run and Docker instructions are documented, but no live service exists.

| Category | Score | Band | Evidence |
|---|---:|---|---|
| EDA & Preprocessing | 13.5/15 | Excellent | `basic-chat-app/notebooks/01_eda.ipynb` documents goals, distributions, missing/duplicate checks, correlations, question-first splitting, fold-local scaling, and weak-negative handling. `src/eda.py:24-89` computes empty/duplicate counts, chunk-length stats, page coverage, label balance, and a correlation matrix, and renders four SVG charts plus caveats. Executed output is in `reports/eda.json`. Scope is one PDF, 33 chunks, and 41 questions, explicitly acknowledged. |
| Experimentation & Methodology | 19.0/20 | Excellent | `reports/tuning-summary.json` reports 630 runs over 610 settings. `embedding-eval/comparison.md` compares BGE versus EmbeddingGemma with calibration/holdout splits, bootstrap confidence intervals, and honest non-significant results. `reports/relevance-training.json` compares a query-coverage baseline against logistic regression and random forest with a question-disjoint split and GroupKFold. Gap: no answer-generation evaluation. |
| Hyperparameter Tuning | 17.0/20 | Proficient | Coarse-to-fine sweep over chunk size/overlap, BM25-dense weights, candidate counts, RRF, and gates, with 630 evaluated runs (`reports/tuning-summary.json:18-94`). A 9-case holdout is used once for embedding-threshold selection, and supervised models use GridSearchCV/GroupKFold. Deductions: retrieval tuning and final verification use all 41 questions with no independent final test; LLM temperature/max tokens are fixed. |
| Deployment (API/UI) | 13.5/20 | Developing | No submitted URL, so no live deployment. The local app is complete and well documented: `README.md:5-23` gives setup, `app.py:2166-2342` implements GET/POST/DELETE API and chat, `static/` provides a polished UI, and `Dockerfile:1-12` uses a non-root user and healthcheck. It runs only locally. |
| GitHub & Code Quality | 14.5/15 | Excellent | Structured `src/` package, separate requirements for app/experiments/tracking, 82 test methods across four files, CI (`.github/workflows/rag-checks.yml:1-25`), source-integrity guard, `.gitignore`/`.dockerignore`, prompt-injection warnings, and citation enforcement. Minor issue: `app.py` is a 2,385-line monolith. |
| Documentation & Presentation | 8.5/10 | Proficient | `README.md:1-83` is clear and honest about setup, architecture, checks, Docker, and limitations; `embedding-eval/comparison.md` is a strong methods/results/limitations report. Gaps: no consolidated results/business-insight section in the README, no video, and an artifact inconsistency where `comparison.json` recommends BGE while the app defaults to Gemma. |

**Bonus:** MLflow/W&B 3, Docker 5, CI/CD 5, data validation 0, video 0. **Raw 13/25; official 10/10.**

**Strengths**
- Exceptionally rigorous retrieval evaluation and tuning: 630 runs, calibrated abstention gates, per-question regression checks, bootstrap CIs, and honest negative results.
- Strong engineering: modular retrieval pipeline, 82 tests, CI, Docker with non-root user and healthcheck, source-integrity guard, polished UI/API, and prompt-injection safeguards.
- Excellent methodological documentation: EDA report, tuning summary, embedding migration report, and explicit limitations.

**Weaknesses / limitations**
- No deployed URL; the service is only locally runnable, placing deployment in the "runs only locally" band.
- Retrieval tuning and verification are in-sample on the same 41 questions, with no independent final test and no answer-generation/LLM evaluation.
- Stale `embedding-eval/comparison.json` conflicts with the app's Gemma default, and the README lacks a consolidated results summary.
- No deployment URL to probe; tests, CI, Docker build, and MLflow usage were not executed/verified.

---

### 6. Lilit Vardanyan — 82.5/100 (Proficient)

**GitHub:** `https://github.com/Lilit-Vardanyan/tcga-cancer-classification`  
**Deployment:** `https://cancer-classifier-699539648647.us-central1.run.app` — live Streamlit app on Cloud Run.

| Category | Score | Band | Evidence |
|---|---:|---|---|
| EDA & Preprocessing | 13.0/15 | Proficient | `notebooks/01_feature_engineering.ipynb` covers class counts, missing-value checks, `describe`/`info`, stratified 70/30 then 80/20 splits, train-only scaling, PCA variance sweep, t-SNE, and VarianceThreshold/SelectKBest sweeps over 100-10,000 genes. Strong feature engineering, but only three plots and no correlation, outlier, or gene-distribution analysis. |
| Experimentation & Methodology | 17.0/20 | Proficient | Logistic-regression baseline, PCA sweep, feature-selection sweep, and comparison of Random Forest, Extra Trees, LightGBM, CatBoost, and XGBoost in `notebooks/02_model_comparison.ipynb`, with CV/validation comparison and a single test evaluation. Deductions: the claimed none/PCA/selection comparison only runs selection; both notebooks have zero stored outputs and no execution counts, so reported scores are unverified narrative claims. |
| Hyperparameter Tuning | 17.0/20 | Proficient | Stratified 5-fold CV and `RandomizedSearchCV(scoring="f1_macro")` with preprocessing inside the pipeline and fit only on training folds; test set used once. Deduction: `n_iter=3` over very large search spaces gives only three random candidates per model, so tuning depth is limited. |
| Deployment (API/UI) | 17.5/20 | Proficient | Live Streamlit app. `deployment/app.py:10-142` loads model/features, validates duplicate/missing/non-numeric columns, predicts with probabilities, and offers CSV download. README documents live/local/Docker use. Usability gap: requires a raw 20,530-column CSV with no sample/template. Static joblib analysis shows the deployed RandomForest pipeline does not match the tuned scaler/SelectKBest pipeline defined in the notebook. |
| GitHub & Code Quality | 11.0/15 | Proficient | README, requirements, structured `notebooks/`, `deployment/`, and `data/` folders, Dockerfile, `.gitignore`, `.dockerignore`, and saved artifact. But `src/` contains only an empty `__init__.py`; README advertises missing `models/`, `reports/`, `app/`, and `tests/` directories; no tests/CI; unpinned requirements; single commit. |
| Documentation & Presentation | 7.0/10 | Proficient | `README.md:3-132` covers overview, dataset, installation, experiments, metrics, reproducibility, MLflow, Streamlit, Docker, and limitations, with a dataset link. But it reports no results and says final test results will be documented later, despite notebook claims; no business/clinical insight, no figures/results table, and numerous typos. |

**Bonus:** MLflow/W&B 5, Docker 5, CI/CD 0, data validation 0, video 0. **Raw 10/25; official 10/10.**

**Strengths**
- Strong train/validation/test discipline: stratified splits, preprocessing fit only on training folds, and one final test evaluation.
- Broad model comparison with a logistic baseline plus five ensemble/boosting families.
- Live, packaged Cloud Run service with input validation, probability output, and CSV download.

**Weaknesses / limitations**
- Notebooks have no stored outputs or execution counts, so reported metrics are unverified; the shipped joblib does not match the tuned notebook pipeline.
- Tuning is token: only three random candidates per model over very large search spaces, and the claimed comparison of preprocessing strategies is not executed.
- Empty `src/`, missing advertised directories, no CI, unpinned requirements, no results table, and no video.
- Upload/prediction flow could not be exercised with GET-only probes; MLflow history and Docker build were not verified.

---

### 7. Areg Ayvazyan — 80.0/100 (Proficient)

**GitHub:** `https://github.com/AregAyv/Project_recommendations-`  
**Deployment:** `https://game-recommender-699539648647.europe-west1.run.app/` — live Streamlit app; internal FastAPI on port 9000 is not externally exposed.

| Category | Score | Band | Evidence |
|---|---:|---|---|
| EDA & Preprocessing | 13.5/15 | Excellent | `data_eda.ipynb` has 20 code cells and 11 rendered plots covering top-reviewed games, rating distribution, price versus positive ratio, platform counts, log-hours, recommend share, monthly review volume, correlation heatmap, user-activity hexbin, interaction long-tail, and tag coverage. Data-quality checks cover duplicates, missing values, orphan app IDs, zero-hour reviews, and date parsing. Matrix density (0.0079%) and test-user overlap (50.5%) are quantified. Deduction: no markdown narrative or written interpretation. |
| Experimentation & Methodology | 14.5/20 | Proficient | Seven models including popularity and content baselines plus hybrid (`main.py:504-531`), with eight ranking metrics (`main.py:333-450`), 500-user sampling, and a complete results table including weak models (`README.md:65-72`). However, each model is evaluated on an independent unseeded 500-user sample (`main.py:398-400`), the implemented split is random rather than the documented date split, the seed is an arbitrary first training row, and the hybrid underperformance is not diagnosed. |
| Hyperparameter Tuning | 13.5/20 | Developing | README claims an ALS grid over factors, regularization, and confidence scaling, but no tuning script, grid outputs, or validation split exist. Values are hard-coded in `main.py:244` and `freeze_models.py:56`; LightFM is fixed at `freeze_models.py:108`; hybrid weights are hand-set in `app.py:163-168`. Models are ranked on the test table (`main.py:538-556`), with no train/validation/test separation. |
| Deployment (API/UI) | 17.5/20 | Proficient | Live Cloud Run Streamlit app with game and Steam-profile modes, model selector, k slider, spinners, and API error surfacing (`streamlit_app.py:78-169`). FastAPI backend loads artifacts and exposes `/health`, `/models`, `/recommend`, `/recommend_from_profile` with validation and 404s (`app.py:36-321`). Deductions: users must enter a raw app_id; the default UI model is the weak hybrid; collaborative_cosine aliases kNN; the best-evaluated model is not served as evaluated; public `/docs` does not expose FastAPI. |
| GitHub & Code Quality | 12.5/15 | Proficient | Clear separation of training/evaluation, artifact freezing, API, Steam client, and UI; pinned requirements, Dockerfile, ignore files, and a structured README. Deductions: `lightfm` is missing from requirements despite being reported; no tests/lint/CI; LightFM training is duplicated; single commit. |
| Documentation & Presentation | 8.5/10 | Proficient | Professional README covering goal, Kaggle citation, approach, model table, evaluation protocol, results, API, Docker, Cloud Run, and limitations. Lacks result interpretation/business insight, repeats tuning/split claims contradicted by code, and has a deployment-region inconsistency. No video. |

**Bonus:** MLflow/W&B 0, Docker 5, CI/CD 0, data validation 5, video 0. **Raw 10/25; official 10/10.**

**Strengths**
- Live deployed product with single-game and Steam-profile recommendation flows, seven selectable models, a separate API, and visible error handling.
- Broad, honest model comparison including popularity/content baselines, ALS, LightFM, kNN variants, and hybrid, evaluated with coverage, diversity, and novelty.
- Clean organization with Docker, pinned dependencies, documented setup/API/deployment, and reported limitations.

**Weaknesses / limitations**
- Evaluation is not apples-to-apples: independent unseeded samples per model, random split instead of the documented temporal split, and an arbitrary seed.
- Hyperparameter tuning is asserted in documentation but absent from code; no validation split and test-based model selection.
- Reproducibility gaps: `lightfm` missing from requirements, no tests/CI/tracking/video, raw app_id input, and default hybrid is among the worst performers.
- End-to-end recommendations could not be probed under GET-only rules; the FastAPI port is internal; artifacts and results are untracked.

---

### 8. Eliza Asatryan — 79.5/100 (Proficient)

**GitHub:** `https://github.com/elizasatrian/mnq-ml-strategy`  
**Deployment:** `https://mnq-trading-api-699539648647.us-central1.run.app` — live FastAPI; `/docs`, `/openapi.json`, and POST `/predict` route exist.

**Instructor adjustment:** +5.0 EDA and +5.0 experimentation (+10.0 base) per instructor instruction. The original base review was 69.5/100 (Developing); the evidence below documents that original review, with the adjusted category scores shown in the table.

| Category | Score | Band | Evidence |
|---|---:|---|---|
| EDA & Preprocessing | 15.0/15 | Excellent | Instructor adjustment +5.0 on a base review of 10.0/15. `working.ipynb` cell 1 is the only original EDA: one Close-price line plot and shape 11,484; no missing-value, distribution, correlation, or class-balance analysis despite the 3,170/8,295 class split. Preprocessing is stronger: triple-barrier labels, sample weights, purged CV, and 99/100 engineered features (`working.ipynb` cells 3-6; `features.py:4-54`), but feature choices are not EDA-justified. |
| Experimentation & Methodology | 19.0/20 | Excellent | Instructor adjustment +5.0 on a base review of 14.0/20. Multiple experiments: log-loss Optuna and OOF reports (AUC 0.6785 and 0.6734), profit-factor Optuna (AUC 0.6722 and 0.6708), walk-forward optimization, and fold-by-fold backtests. No separate model baseline (always-long, logistic, or rule-only). Critical bug in cell 25: `objective_profit_factor_no_hour` computes `oof_probs_no_hr` but assigns `oof_probs` (the hour model) at the threshold/signal stage. Saved models are last-CV-fold models; cell 35 reports PF 2.72/4.26 on the full training parquet where about 80% of rows are in-sample. Rankings flip across WFO, fold-by-fold, and in-sample PF. |
| Hyperparameter Tuning | 15.0/20 | Proficient | Systematic Optuna: 30 trials over nine hyperparameters with PurgedKFold, repeated for no-hour and profit-factor objectives, plus 15-trial inner TimeSeriesSplit in WFO. However, there is no dedicated holdout/test set: OOF is reused for selection and reporting, the signal threshold is computed over all OOF probabilities, and PurgedKFold still trains on future folds, so OOF metrics and hyperparameter choices use future information. The WFO later reuses those globally tuned parameters. |
| Deployment (API/UI) | 14.5/20 | Proficient | `main.py:36-74` exposes FastAPI POST `/predict`; lifespan loads model/feature pickles; `features.py` computes features. Live `/docs`, `/openapi.json`, and `/predict` GET 405 confirm the service. But README has no API instructions; `test_prediction.py` and `live_1h_prediction.py` send `{"features": {...}}` while `main.py:38-44` expects `{"history": [...]}`, so both clients are inconsistent with the API contract. `main.py:66` returns "SELL" for any 0 although the model only learns long-barrier success; no root/health endpoint or minimum-history validation. |
| GitHub & Code Quality | 10.0/15 | Developing | Clean modular `features.py`, `ta_utils.py`, `main.py`, and Dockerfile; model artifacts and parquet data are committed. But README ends at an empty "Repository Structure" heading with no setup/API examples; requirements omit training/live dependencies; `test_prediction.py` is a broken manual client, not a test; `assets/mnq_feature_importance_comparison.png` is entirely white; notebook duplicates the backtest class; one commit, no CI. |
| Documentation & Presentation | 6.0/10 | Developing | README states the goal and two variants but reports no results, metrics, business insight, setup, citations, or video; line 15 is an empty section. Notebook has only two markdown headings and no narrative or conclusions. The PF 2.72 versus 4.26 result is never interpreted, and low recall at the default 0.5 threshold (0.05) is not discussed as a business/risk issue. |

**Base:** 79.5/100 (Proficient) after the +10.0 instructor adjustment; original base 69.5/100 (Developing). **Bonus:** MLflow/W&B 0, Docker 3, CI/CD 0, data validation 2, video 0. **Raw 5/25; official 5/10.**

**Strengths**
- Advanced, coherent labeling/validation pipeline: triple-barrier labels, sample weights, purged CV, and a rich 99/100-feature set.
- Multiple systematic experiments and model comparisons: log-loss versus profit-factor objectives, hour versus no-hour variants, WFO, and fold-by-fold backtests.
- Live Cloud Run FastAPI service with working `/docs`, `/openapi.json`, and POST `/predict` route, plus Docker and committed model artifacts.

**Weaknesses / limitations**
- No dedicated holdout test set; OOF is reused for tuning/evaluation, saved models are last-CV-fold models, and final PF is mostly in-sample.
- Critical no-hour profit-factor bug, no baseline, and headline WFO results conflict with fold-by-fold performance.
- Documentation/replication is weak: 15-line README, incomplete requirements, broken client scripts, blank asset, no tests/CI/video.
- POST `/predict` not executed; Docker build and runtime logs not inspected; data not snapshotted.

---

### 9. Arsen Sirunyan — 78.5/100 (Proficient)

**GitHub:** `https://github.com/Arsen1302/yolo-football-tracker`  
**Deployment:** `https://footballanalyses.streamlit.app/` — live host and health endpoint; root auth-gated.

| Category | Score | Band | Evidence |
|---|---:|---|---|
| EDA & Preprocessing | 13.5/15 | Excellent | `notebooks/01_football_dataset_eda.ipynb` is executed and audits splits/classes, missing/empty/orphan/invalid labels, plots class counts, bbox width/height/area histograms, a Pearson correlation heatmap, and label overlays. `src/football_dataset.py:81-188` implements the audit and engineers area, aspect ratio, vertical zone, and relative scale. No explicit augmentation/scaling study, but YOLO handles resizing/normalization. |
| Experimentation & Methodology | 13.0/20 | Developing | `src/train_models.py:154-246` runs a 2x2 model x learning-rate grid (`yolov8n`/`yolov8s` x `0.001`/`0.01`), logs parameters/status/metrics, selects the best run by validation mAP50-95, and evaluates test once; `README.md:329-350` documents the command. However, no experiment metrics CSV, selected-model JSON, or comparison table is committed (outputs are gitignored); no baseline or error analysis is reported, so actual results are unverified. |
| Hyperparameter Tuning | 14.0/20 | Proficient | `src/train_models.py:113-196` fixes 20 epochs, 640 image size, and batch 4, varying only model and learning rate; uses AdamW, patience 6, and deterministic seed 42. Validation/test protocol is correct, but the grid is narrow, lacks search rationale, and reports no tuning outcomes. |
| Deployment (API/UI) | 17.0/20 | Proficient | `app.py:77-126` implements upload, temp-file handling, pipeline invocation, error handling, and output video playback; `.streamlit/config.toml` sets a 200 MB upload limit and theme; `football_analysis/config.py:21-44` auto-downloads Hugging Face weights. README promises a download but `app.py` has no `st.download_button`; root is auth-gated and inference was not exercised. |
| GitHub & Code Quality | 13.0/15 | Proficient | Clean modular packages for tracking, team assignment, possession, camera compensation, view transformation, speed/distance, plus a shared pipeline, setup docs, and 5 unit tests. Issues: hardcoded player ID 91 (`team_assigner/team_assigner.py:78-79`), fixed pitch polygon, typos, and CI skips the tests. |
| Documentation & Presentation | 8.0/10 | Proficient | README covers goals, architecture, setup, CLI, deployment, training, dependencies, and dataset citation. Missing quantified results, business insight, and a walkthrough; limitations are limited to a speed-estimate caveat and the 13-image test split. |

**Bonus:** MLflow/W&B 0, Docker 3, CI/CD 4, data validation 0, video 0. **Raw 7/25; official 7/10.**

**Strengths**
- Live, user-facing Streamlit app with robust upload/error handling, session state, and automatic model download.
- Modular, readable CV pipeline reused by the UI and CLI, with clear separation of tracking, team assignment, possession, camera compensation, view transformation, and speed/distance.
- Strong reproducibility support: README, requirements, Dockerfile, CI workflow, unit tests, and an executed EDA notebook.

**Weaknesses / limitations**
- No reported experiment metrics, baseline comparison, or selected-model results; ML performance claims are unverified.
- Tuning is limited to a small model/learning-rate grid with no rationale or reported outcomes.
- Deployment UX gaps: auth-gated root, missing download button, unverified inference; hardcoded player/pitch logic reduces generality.
- No MLflow/W&B or Pydantic/Great Expectations; custom CSV tracking and label validation exist but do not meet the named bonus criteria.

---

### 10. Armen Gasparyan — 76.0/100 (Proficient)

**GitHub:** `https://github.com/armengasparyan314/Programing/tree/master/Bank%20Customer%20Churn` (monorepo; reviewed only the Bank Customer Churn subfolder)  
**Deployment:** `https://bank-churn-service-699539648647.us-central1.run.app` — live FastAPI; `/docs` and `/openapi.json` reachable.

| Category | Score | Band | Evidence |
|---|---:|---|---|
| EDA & Preprocessing | 12.0/15 | Proficient | `Bank Customer Churn/Bank Customer Churn (EDA).ipynb` cells 1-9 load/drop IDs, cast integers, show target counts 11,948/3,052, four countplots, five histplots, a numeric correlation heatmap, five boxplots, and an Armenian summary. `Model prediction.ipynb` cell 1 applies geography dummies, gender label encoding, an age-45 cutoff, a 75/25 split, and train-only scaling. Limits: geography and the age cutoff are not plotted, correlation excludes the target, missing-value handling is only a commented assertion, and the cutoff is unjustified. |
| Experimentation & Methodology | 16.5/20 | Proficient | Six models including a class-weighted logistic baseline (test accuracy 0.8253, F1 0.6569) versus RF/XGB/CatBoost/LightGBM/Decision Tree (best initial accuracy 0.8928, F1 0.7197). GridSearchCV, OOF threshold search, 5-fold test averaging, and a 0.5/0.5 CatBoost+XGBoost ensemble yield test F1 0.7395, accuracy 0.8925, ROC-AUC 0.9300. Real comparison and baseline exist, but conclusions rely on repeated test evaluations; no business-cost analysis or significance testing. |
| Hyperparameter Tuning | 16.0/20 | Proficient | `GridSearchCV(cv=5, scoring="f1")` for five models, OOF threshold search, and ensemble weight/threshold search; scaling is fit on train only. However, the test set is reported repeatedly, and some parameter changes after comparing train/test accuracy are test-informed. ROC-AUC is initially computed on hard labels (0.832) and corrected to 0.930 in a later cell. |
| Deployment (API/UI) | 14.0/20 | Proficient | `main.py:12-62` loads `ensemble_package.pkl`, defines a Pydantic schema, and implements POST `/predict` with probability, prediction, threshold, and status. Live Swagger/OpenAPI confirm the service. Critical flaw: training standardizes CreditScore/Balance/Age/EstimatedSalary, but `main.py:45-49` passes raw values, so standardized thresholds are applied to raw units. No root/health endpoint, no example payload, manual dummies, and undocumented gender encoding. |
| GitHub & Code Quality | 10.0/15 | Developing | The subfolder contains only README, two notebooks, `main.py`, `Dockerfile`, and the model artifact. `Dockerfile:14-17` requires `requirements.txt`, but none is committed; `.gitignore` excludes `*.txt` and `*.csv`, so the Docker build fails and the dataset is absent. README runs a personal venv path; no tests, `src` package, or pinned dependencies. Positives: clear prediction flow and local/Docker/Cloud Run instructions. |
| Documentation & Presentation | 7.5/10 | Proficient | README states the objective, business impact, preprocessing, models, final ensemble, evaluation approach, tech stack, live docs, and local/Docker commands; notebook markdown explains steps in Armenian. Missing: results/metrics table, quantified business impact, dataset provenance/citation, limitations, and video. README claims production readiness despite the missing scaler and requirements. |

**Bonus:** MLflow/W&B 0, Docker 3, CI/CD 0, data validation 4, video 0. **Raw 7/25; official 7/10.**

**Strengths**
- Genuine model comparison with a proper logistic baseline, five tree/boosting models, GridSearchCV, OOF threshold tuning, and a documented final ensemble.
- Live, documented FastAPI service with working Swagger/OpenAPI and a clear JSON response; the model artifact is committed and loaded reliably.
- EDA covers numeric features and key categoricals with target-conditioned plots; the scaler is fit on train only; README explains the workflow.

**Weaknesses / limitations**
- Not reproducible: missing `requirements.txt` breaks Docker, dataset excluded, personal venv path, no tests.
- Critical inference bug: the fitted scaler is not saved or applied, so the deployed endpoint predicts from raw feature values against standardized training thresholds.
- Test-set discipline is weak: repeated test evaluations and post-hoc parameter changes make final metrics optimistically biased.
- Dataset absent; POST not sent and pickle not unpickled; no video, MLflow/W&B, or CI evidence.

---

### 11. Samvel Harutyunyan — 73.8/100 (Proficient)

**GitHub:** `https://github.com/SamHarutyunyan21/ml_project`  
**Deployment:** `https://customer-spending-predict.streamlit.app/` — live host and health endpoint; root auth-gated.

| Category | Score | Band | Evidence |
|---|---:|---|---|
| EDA & Preprocessing | 11.5/15 | Proficient | `EDA.ipynb` includes target/age/profession/marital/graduation views and RF Gini importances, but no correlation heatmap, missingness matrix, or explicit class-imbalance discussion. `EDA.ipynb` cell 7 imputes categoricals with `"Unknown"` and work experience with the full-data median before splitting, contradicting the README's training-set-median claim. Feature engineering is substantive (`app.py:43-57`), and scaling is correctly fit on `X_train` only, but engineered features are not justified or ablated. |
| Experimentation & Methodology | 15.0/20 | Proficient | `models.ipynb` evaluates RF, XGBoost, LightGBM, and CatBoost, then a five-model leaderboard including ExtraTrees and a hard-voting ensemble. Real comparison and reasonable baseline, but no validation split or cross-validation; the same 1,614-row test set is reused for every model and leaderboard selection. README reports a soft-voting ensemble that is not implemented; EDA and model results diverge without reconciliation. |
| Hyperparameter Tuning | 11.5/20 | Developing | No GridSearchCV, RandomizedSearchCV, Optuna, Hyperopt, parameter grid, or validation split. Hyperparameters are manually fixed in `models.ipynb` and differ from `app.py` without documentation. Only a single stratified 80/20 split exists, the test set is reused for model ranking, and the minority "High" class recall is only 0.59-0.61 with no business-cost discussion. |
| Deployment (API/UI) | 16.8/20 | Proficient | Live host and health endpoint; `app.py:136-200` provides a clear three-column Streamlit UI with dropdowns, sliders, required-field checks, sanity checks, one-hot alignment, and scaling. Weaknesses: `app.py:28-130` retrains four models from the Hugging Face dataset on every cold start/cache miss with no persisted artifact; root requires auth; no metrics/model card in the UI. |
| GitHub & Code Quality | 11.0/15 | Proficient | Accessible repo with a 340-line README, requirements, Dockerfile, devcontainer, `.gitignore`, and clear notebook roles. However, preprocessing/training is duplicated across `app.py`, `main.ipynb`, `models.ipynb`, and `EDA.ipynb` with divergent feature sets; no `src/`, tests, or saved model. `requirements.txt` uses lower bounds and omits CatBoost; the Docker healthcheck uses curl, which the Dockerfile does not install. |
| Documentation & Presentation | 8.0/10 | Proficient | README gives local/Docker run steps, data/feature/model design, performance tables, and class-level metrics, professionally formatted. Gaps: no business insight, dataset citation/license/data dictionary, or limitations; some claims are inaccurate (soft voting not implemented, training-set medians not used, dependencies not pinned). |

**Bonus:** MLflow/W&B 0, Docker 4, CI/CD 0, data validation 0, video 0. **Raw 4/25; official 4/10.**

**Strengths**
- End-to-end pipeline from Hugging Face ingestion through feature engineering, ensemble training, and single-customer inference, with a clean Streamlit UI.
- Real multi-model comparison (RF, ExtraTrees, XGBoost, LightGBM, CatBoost) plus a hard-voting ensemble and class-level reporting.
- Strong README coverage of architecture, results, local setup, and Docker, backed by a live deployment with healthy health/embed endpoints.

**Weaknesses / limitations**
- No systematic tuning or validation: test reused for model selection, no cross-validation, and minority-class recall around 0.60.
- Reproducibility claims exceed reality: soft voting absent, CatBoost missing, unpinned dependencies, full-data median imputation despite leakage-prevention claim.
- Code duplicated across notebooks and app, no tests or persisted model, cold-start retraining, and a likely broken Docker healthcheck.
- Prediction path not exercised; root auth-gated; notebooks not executed.

---



### 12. Mels — 66.5/100 (Developing)

**Submitted GitHub:** `https://github.com/Cat-Roller/ACA` (weekly coursework, not the capstone)  
**Actual capstone GitHub (approved for grading):** `https://github.com/Cat-Roller/skin-cancer-detection`  
**Deployment:** GCP Artifact Registry console link — not an application; private/auth-gated.

**Submission flag:** The submitted GitHub URL points to `Cat-Roller/ACA`, which contains only weekly coursework. The intended capstone `Cat-Roller/skin-cancer-detection` was identified by the same GitHub user and matches the submitted GCP `skin-cancer-repo` artifact. Grading below uses the actual capstone repo as approved by the instructor.

| Category | Score | Band | Evidence |
|---|---:|---|---|
| EDA & Preprocessing | 11.5/15 | Proficient | `notebooks/eda.ipynb` has rendered correlation heatmap/top correlations, summary/missingness table, categorical uniques, class-imbalance plot, age KDE, size boxplot, and missingness bar; it performs median age imputation, image-existence filtering (218,776 to 68,939), column drops, StandardScaler/one-hot encoding, and hair removal. Weaknesses: scaler is fit on all rows before the split and never persisted; split is image-level, not patient-level; the Supplement CSV is cleaned twice; images are edited in place; correlation is plotted but not acted on. |
| Experimentation & Methodology | 15.0/20 | Proficient | Three multimodal backbones: MobileNetV2, ResNet50, and EfficientNetB0, with shared augmentation/imbalance handling and MLflow. `notebooks/model_comparison.ipynb` reports AUC 0.8605/0.9197/0.9325 with recalls 0.04/0.36/0.08; ensemble union AUC 0.9401, precision 0.6111, recall 0.44; majority AUC 0.9581, precision 0.6667, recall 0.08. Weaknesses: MobileNetV2 uses `weights=None`, no tabular-only or image-only ablation, no validation split, no uncertainty, Grad-CAM is hardcoded to EfficientNet, and the training set remains 2.39% malignant despite downsampling. |
| Hyperparameter Tuning | 12.0/20 | Developing | `src/resnet50_gridsearch.py:19-125` defines an 8-combination grid, uses `test_size=500`, trains only 5 epochs, evaluates on the test set, and selects the best model by test AUC. All three trainers use `validation_data=test_dataset`, and the helper returns only train/test. The same test data is reused in `model_comparison.ipynb`, so the test set is never reported once. Thresholds are inconsistent (0.4 versus 0.3) across the comparison, app, and comments. |
| Deployment (API/UI) | 11.0/20 | Developing | `app.py` is a batch-only Streamlit UI requiring many images plus a 46-feature CSV; there is no single-image flow and no live service. README only documents local/Docker runs. A fresh clone cannot run: `clean_models/` is gitignored, the dockerfile copies it, and no weights/scaler are committed. The only scaler code fits 34 numeric columns and never saves `scaler.pkl`, while the app transforms 46 columns and silently falls back to raw data. The app silently skips missing models and would label everything benign with zero models. The file is lowercase `dockerfile`, so `docker build .` fails on case-sensitive Linux. |
| GitHub & Code Quality | 10.5/15 | Proficient | Structured `src/`, `notebooks/`, requirements, dockerfile, and CI workflow. But hardcoded Windows paths, duplicated helper code, unused `src/preprocess.py`, unused FastAPI/Starlette dependencies, a tautological test, an unclosed README code fence, and no license. CI installs only pytest/pandas/numpy/Great Expectations and runs trivial tests. |
| Documentation & Presentation | 6.5/10 | Developing | README covers goal, data source, setup, Docker, and references, but has no results/metrics, business insight, limitations, or app-usage/schema guidance. The "production-ready" claim is unsupported, references are vague, markdown formatting is broken, notebooks have minimal narrative, and low recalls are not discussed. No video/slides. |

**Bonus:** MLflow/W&B 4, Docker 3, CI/CD 5, data validation 2, video 0. **Raw 14/25; official 10/10.**

**Strengths**
- Three multimodal backbones plus ensemble voting and Grad-CAM, with shared augmentation/class-imbalance handling and MLflow instrumentation.
- EDA has rendered evidence for class imbalance, missingness, outliers, correlations, and age; preprocessing includes median imputation, image filtering, and hair removal.
- Broad engineering scaffolding: modular `src/`, Streamlit batch UI, requirements, Dockerfile, Great Expectations, and a passing GitHub Actions test workflow.

**Weaknesses / limitations**
- Evaluation is contaminated: test used for early stopping, grid-search selection, and final reporting; no held-out test; thresholds vary; patient-level leakage is possible.
- Deployment is neither live nor reproducible: only an Artifact Registry console URL; weights/scaler absent or mismatched; Docker build fails from a clean clone; batch-only UX.
- Reproducibility/docs are weak: hardcoded paths, duplicate/dead code, trivial tests, broken README, no results/business insight, and the submitted GitHub link is wrong.
- Registry image and MLflow runs are private/gitignored; data and weights absent; notebook metrics self-reported on a 500-sample test subset.

---

### 13. Mariam Mnatsakanyan — 65.0/100 (Developing)

**GitHub:** `https://github.com/mariammnatsakanyan09-dot/Urban-Traffic-Anomaly-Analysis`  
**Deployment:** none live. Form states: "Not deployed to Cloud Run (no billing account). Runs via Docker: docker compose up --build, see README."

| Category | Score | Band | Evidence |
|---|---:|---|---|
| EDA & Preprocessing | 8.5/15 | Developing | `calibrate_baseline.py:8-32` is the only quantitative data analysis: mean brightness/contrast over 30 frames per video. `run_tracking.py:18-34` samples 12 frames and flags dark video below mean brightness 75. `extract_frames.py:3-14` only extracts first frames for manual API testing. No notebook, plots, class distribution, resolution/duration analysis, or dataset characterization; `data/raw.dvc` only declares 8 videos/474 MB. Preprocessing is reasonable (resize, CLAHE, gamma, contrast) but has no before/after validation. |
| Experimentation & Methodology | 11.5/20 | Developing | `benchmark_onnx.py:11-40` measures PyTorch versus ONNX Runtime FPS over 150 frames, but benchmarks YOLOv8s while README reports YOLOv8n results. README claims YOLOv8s was chosen for better recall without measuring recall/mAP. No annotated validation set, accuracy metric, baseline detector comparison, or ablation of night enhancement/drift detector. Only one quantitative experiment (speed) exists. |
| Hyperparameter Tuning | 10.5/20 | Developing | All settings are hard-coded manual choices: detector confidence 0.35, tracking confidence 0.10 and imgsz 1280, line position 0.55, CLAHE clipLimit 4.0/gamma 1.4, dark threshold 75, drift thresholds 35/20, and a fixed baseline. No Grid/Random/Bayesian search, no train/validation/test split, and no reported test metrics. |
| Deployment (API/UI) | 13.5/20 | Developing | Working FastAPI app with POST `/detect_frame`, WebSocket `/detect_stream`, Swagger UI, and Pydantic schemas; Docker/compose files, browser client, and a passing CI image build/import smoke test. However, it runs only locally, has no live URL or health endpoint, performs synchronous inference inside the async WebSocket loop, and analyzes only the first frame of uploaded videos. |
| GitHub & Code Quality | 12.5/15 | Proficient | Clear modular separation (`app.py`, `detector.py`, `tracker.py`, `drift_monitor.py`, batch scripts), README with run steps, requirements, DVC config, and CI. But `test.py` is a manual CUDA/class-print diagnostic, not a test suite; CI only performs a container import smoke test; constants are duplicated; requirements are unpinned and include unused `evidently`; scripts sit flat at repo root. |
| Documentation & Presentation | 8.5/10 | Proficient | Strong README with goals, architecture, exact run instructions, benchmark table, honest limitations, and dataset links. Business insight is shallow: congestion is a hardcoded 8/4-vehicle heuristic, with no quantified value, stakeholder analysis, screenshots, or formal citations. |

**Bonus:** MLflow/W&B 0, Docker 5, CI/CD 5, data validation 5, video 0. **Raw 15/25; official 10/10.**

**Strengths**
- Complete end-to-end CV service: YOLOv8 detection, ByteTrack line counting, WebSocket streaming, drift monitoring, and a Pydantic-validated API.
- Strong operational hygiene: one-command Docker/compose, CI build and smoke test, DVC data versioning, committed day/night samples, and honest limitations.
- Defensive details: per-stream auto-calibrated drift baseline, low-light enhancement, path-traversal protection, and an ONNX speed benchmark.

**Weaknesses / limitations**
- No quantitative model evaluation: no labeled validation/test set, no mAP/precision/recall, no detector comparison; the "better recall" claim is unmeasured and benchmark code/README disagree on YOLOv8n versus YOLOv8s.
- Minimal EDA and no systematic tuning: only brightness/contrast statistics; all thresholds hard-coded; no ablation of night enhancement or drift alerts.
- Local-only deployment and limited engineering rigor: no live URL, no unit/integration tests, unpinned dependencies with unused `evidently`, duplicated constants, and blocking inference in the async loop.
- DVC raw data is behind a private/test-user-limited Google Drive remote; model weights are gitignored; Docker execution not performed.

---

### 14. Astghik Saghyan — 49.0/100 (Needs Improvement)

**GitHub:** `https://github.com/astghiksaghyan/real-estate-app/tree/main/real-estate-app` (monorepo; reviewed only `real-estate-app/`)  
**Deployment:** frontend `https://real-estate-frontend-699539648647.us-central1.run.app/`; backend `https://real-estate-backend-699539648647.us-central1.run.app/api/listings` — both live.

| Category | Score | Band | Evidence |
|---|---:|---|---|
| EDA & Preprocessing | 4.0/15 | Needs Improvement | No EDA notebook, script, plots, or committed analysis exists in `real-estate-app/`. Preprocessing is limited to price parsing (`backend/model.py:36-42`), dropping missing targets (`:52-60`), constant imputation (`:70-72`), and top-10 amenity flags computed over the full dataset before splitting (`:63-77`). `area` is synthesized as `bedrooms * 30 + 15` (`model.py:58`) and displayed as real square meters. No missingness, distribution, correlation, outlier, or target analysis; location, property type, room type, reviews, and availability are unused. `backend/data/listings.csv` is committed as a 0-byte file, so the data cannot be inspected or the preprocessing reproduced. |
| Experimentation & Methodology | 10.0/20 | Developing | `backend/model.py:84-142` defines six candidates: polynomial Linear Regression, Random Forest, XGBoost, LightGBM, CatBoost, and a VotingRegressor. However, there is a single 80/20 split (`model.py:82`), no validation set, and no cross-validated comparison. Every model and the ensemble are scored on the same test set, and the best model is selected by test MAPE (`model.py:113-142`), so the test set is reused for selection and reporting. No metrics, plots, logs, or result files are committed; MAPE is only printed to stdout. No error analysis, residual analysis, feature importance, or baseline beyond the linear model. |
| Hyperparameter Tuning | 8.0/20 | Needs Improvement | Only Random Forest is tuned: `RandomizedSearchCV` with `n_iter=2`, `cv=3` over a 3x3 grid of `n_estimators` and `max_depth` (`backend/model.py:98-99`). XGBoost, LightGBM, CatBoost, the polynomial degree, and the ensemble are left at defaults. There is no search rationale, validation-based selection, tuning result file, or independent test evaluation; final selection is again test-MAPE based. This is token tuning rather than a systematic search. |
| Deployment (API/UI) | 14.0/20 | Proficient | Frontend root returns HTTP 200 with the built React bundle, and JS/CSS assets return 200. Backend `GET /api/listings` returns HTTP 200 with 5 random records and `Access-Control-Allow-Origin: *`; repeated calls return different IDs. A cold-start request exceeded 45 seconds; a 120-second retry returned 200. `backend/app.py:12-14` trains all models on startup, and `backend/Dockerfile:23` runs one gunicorn worker, so training occurs on every cold start with no persisted artifact. Backend `/` and `/docs` return 404; there is no health endpoint or input schema. POST was not sent, but static inspection shows a contract mismatch: `backend/model.py:201-209` returns `best_model` while `frontend/src/App.jsx:128` reads `bestModel`; `model.py:204` returns a dollar amount named `priceIncreasePercent`, and `App.jsx:129` renders it with `%` and reads an `addedValue` field the API never returns. Listing cards read `item.location` (`App.jsx:61`), which the API does not provide. Local Docker Compose is not functional as written: `frontend/Dockerfile:13-14` requires `VITE_API_URL`, but `docker-compose.yml:11-18` passes no build arg and there is no Nginx `/api` proxy. |
| GitHub & Code Quality | 8.0/15 | Developing | Small, readable two-service layout (`backend/app.py`, `backend/model.py`, `frontend/src/App.jsx`, `frontend/services/api.js`), clear function names, CORS, and basic error handling. However, `backend/data/listings.csv` is a 0-byte file, so a fresh clone cannot train or start; there is no persisted model, config module, test suite, lint, CI, `.dockerignore`, or pinned dependency version. Training and inference share one 210-line module with global mutable state (`model.py:21-26`), and the frontend/backend response contract is inconsistent. The README's project structure does not match the repo. At 8.0/15 (53.3%), this is the bottom of the Developing band. |
| Documentation & Presentation | 5.0/10 | Developing | `README.md` covers local setup, Podman Compose, live URLs, and a usage guide, and the live links are correct. But the Markdown is broken: a fenced block opened at `README.md:3` is not closed until the bare fence at `README.md:36`; later `bash` fences are unclosed, so much of the file renders as code. The Armenian preamble and usage section mix languages; the project structure is inaccurate; the manual deployment block is truncated at `gcloud run deploy`; there is no dataset provenance/link, EDA, model-comparison table, MAPE/results, business insight, limitations, or video. The data are Airbnb-style short-term rentals, but the README frames the project as real-estate valuation. At 5.0/10 (50%), this is the bottom of the Developing band. |

**Base:** 49.0/100 (Needs Improvement). **Bonus:** MLflow/W&B 0, Docker 5, CI/CD 0, data validation 0, video 0. **Raw 5/25; official 5/10.**

**Strengths**
- Live, reachable full-stack deployment: the React frontend and Flask backend both respond, and `GET /api/listings` returns randomized listings with CORS.
- Broad candidate set in code: polynomial linear regression, Random Forest with `RandomizedSearchCV`, XGBoost, LightGBM, CatBoost, and a voting ensemble.
- Clear two-service separation with Dockerfiles for both services, a Compose file, and documented Cloud Run URLs.

**Weaknesses / limitations**
- No EDA or committed data analysis; the dataset is a 0-byte file with no provenance, so the workflow is not reproducible from the repo.
- No validation/test discipline: a single 80/20 split, the test set is reused for model selection, and no metrics or artifacts are committed.
- Tuning is token (two RF candidates) and most models use defaults; no tuning evidence or independent evaluation.
- The analyze UI contract is broken (`bestModel`/`addedValue` mismatch, dollar amount shown as percent), and local Docker Compose cannot reach the backend.
- No MLflow/W&B, CI/CD, data validation, tests, or video; dependencies are unpinned and models are retrained on every startup.

---



## Submission and review flags

1. **Duplicate form rows:** Areg Ayvazyan, Nonna Parsyan, and Armen Gasparyan each submitted identical links twice. Graded once each.
2. **Mels:** submitted `Cat-Roller/ACA` (weekly coursework) instead of `Cat-Roller/skin-cancer-detection`; graded the intended capstone repo with instructor approval and noted the link mismatch.
3. **Yulya Sargsyan:** initially inaccessible; repo is now public and was re-reviewed (5 commits). The submitted deployment URL is stale/auth-gated, but the README demo URL is live. Full 86.5/100 assigned; the student should replace the stale form URL with the working demo link.
4. **Karen Poghosyan:** no deployment URL submitted; deployment category scored as "runs only locally."
5. **Mariam Mnatsakanyan:** no live deployment; Docker Compose is documented and CI builds the image.
6. **Mels deployment:** the submitted GCP Artifact Registry link is a private console page, not a functional API/UI.
7. **Auth-gated Streamlit demos:** Samvel, Nonna, Arsen, and Yulya (README demo) use Streamlit Cloud; root URLs redirect to authentication. Availability was inferred from `/healthz` and `?embed=true`, not from authenticated UI interaction.
8. **Late submissions added:** Armen Barseghyan (submitted 2026-10-26) and Astghik Saghyan (submitted 2026-10-30) were added on 2026-11-01 using the same rubric and review method.
9. **Armen Barseghyan:** the 623-photo reporting set was already evaluated earlier, so the headline metric is not an untouched-test result; all five bonus items are absent.
10. **Astghik Saghyan:** the backend trains on every startup, the committed dataset is 0 bytes, and the frontend/backend response contract is inconsistent. Docker Compose is not functional as written.
11. **No code execution:** tests, Docker builds, notebook reruns, and POST inference were not performed. Evidence is static source/README review plus GET-only deployment probes.
12. **Instructor adjustment:** Eliza Asatryan received +5.0 EDA and +5.0 experimentation (+10.0 base) per instructor instruction; her base is 79.5 and her final score uses that adjusted base.
