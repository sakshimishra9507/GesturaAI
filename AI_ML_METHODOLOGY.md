# AI/ML Methodology
1. Capture RGB frame.
2. Detect 21 hand landmarks.
3. Translate landmarks so wrist is origin.
4. Scale coordinates for hand-size invariance.
5. Flatten to 63 features.
6. Train Random Forest baseline.
7. Evaluate with accuracy, precision, recall, F1 and confusion matrix.

For research-quality results, use cross-user splits so the same person's frames do not appear in both train and test sets. Compare KNN, SVM, Random Forest and neural sequence models for advanced work. Test different users, lighting, backgrounds, distances and partial occlusion.
