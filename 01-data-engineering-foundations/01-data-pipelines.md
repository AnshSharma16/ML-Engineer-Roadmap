# 1.1 What is a Data Pipeline

## What is a Pipeline?
A data pipeline is a system that moves data from source to destination while cleaning, transforming, and validating it so it can be used reliably for analytics and machine learning.

## Why Pipelines Exist
- Raw data is messy and inconsistent  
- ML models require clean, structured data  
- Manual data handling does not scale  
- Pipelines enable automation, reliability, and reproducibility  

## High-Level Flow
Data Source → Ingestion → Processing → Storage → Consumption

## Batch vs Streaming (High Level)
- Batch: data processed periodically (e.g., daily model training)
- Streaming: data processed continuously (e.g., real-time predictions)

## Role in ML Systems
Data pipelines feed both training and inference data. Poor pipelines often cause model failures, not algorithms.
