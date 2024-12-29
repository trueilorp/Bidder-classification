# Structure

- note1: dataset evaluation in his orignal form.
- note2: Feature Extraction Pipeline for Data Processing

## note1: Dataset Evaluation in his orignal form

### Purpose

The purpose of **note1** is to assess the dataset in its original form, without any preprocessing or feature engineering. This initial step evaluates the quality and relevance of the features provided and determines their impact on the model's performance.

## Key Insights

1. **Overfitting Demonstration**: 
   - By training a model on the raw dataset, Note1 shows how the given features contribute to overfitting. This is indicated by a low score on test set.
   
2. **Feature Utility**: 
   - The experiment highlights that the features provided in the dataset are not suitable for solving the problem effectively. 

This analysis sets the stage for further preprocessing, feature selection, or engineering to improve model generalization.

## note2: Feature Extraction Pipeline for Data Processing

### Purpose

The purpose of **note2** is to provide a pipeline for storing and loading extracted features, ensuring that the features are not recalculated every time they are needed. This notebook includes an example of how to use the pipeline, while the class implementation is stored in a separate Python file (**fep.py**).

## note3: Feature engineering part 1

### Purpose

In this notebook is to extract some features that could be helpful in bot classification task. 

## note3: Feature engineering part 2

### Purpose

In this notebook is to extract features related to the time. 