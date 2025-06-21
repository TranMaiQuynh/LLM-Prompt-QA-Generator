import os

# Danh sách các thư mục và file cần tạo
structure = {
    "04_auto_evaluation": {
        "evaluation_scripts": [
            "metric_calculator.py",
            "bleu_rouge.py",
            "bert_factcheck.py",
            "diversity_analyzer.py",
            "consistency_evaluator.py"
        ],
        "phase1_results": {
            "per_model": [
                "gpt_metrics.feather",
                "gemini_metrics.feather"
            ],
            "comparative_analysis": [
                "prompt_technique_comparison.csv",
                "domain_performance.xlsx",
                "radar_chart.png"
            ],
            "files": [
                "model_prompt_matrix.csv"
            ]
        },
        "phase2_results": {
            "dataset_quality": [
                "full_100k_metrics.feather",
                "domain_breakdown.csv",
                "quality_report.pdf"
            ],
            "comparison_with_phase1": {
                "files": [
                    "quality_delta.csv",
                    "statistical_test.ipynb"
                ],
                "improvement_visualization": []
            }
        }
    },
    "05_metadata_management": [
        "qa_metadata.db",
        "metadata_schema.sql",
        "metadata_loader.py",
        {
            "data_lineage": [
                "lineage_graph.gml",
                "provenance_tracker.py"
            ]
        },
        {
            "bias_detection": [
                "bias_analysis.ipynb",
                "gender_bias_report.html",
                "cultural_bias_metrics.csv"
            ]
        }
    ],
    "06_final_outputs": {
        "phase1_findings": {
            "files": [
                "technical_report.md",
                "optimal_pairings.csv"
            ],
            "presentation": [
                "research_slides.pptx",
                "demo_video.mp4"
            ]
        },
        "phase2_dataset": {
            "full_dataset": [
                "100k_qa_dataset.jsonl",
                "100k_qa_dataset.parquet",
                "dataset_card.md"
            ],
            "statistics": [
                "question_length_dist.png",
                "answer_quality.csv",
                "token_distribution.pdf"
            ],
            "quality_certification": [
                "auto_validation_report.pdf",
                "compliance_checklist.yml"
            ]
        }
    }
}

# Hàm tạo folder và file
def create_structure(base_path, tree):
    if isinstance(tree, dict):
        for folder, content in tree.items():
            folder_path = os.path.join(base_path, folder)
            os.makedirs(folder_path, exist_ok=True)
            create_structure(folder_path, content)
    elif isinstance(tree, list):
        for item in tree:
            if isinstance(item, str):
                file_path = os.path.join(base_path, item)
                open(file_path, 'w').close()
            elif isinstance(item, dict):
                create_structure(base_path, item)

# Gọi hàm
if __name__ == "__main__":
    create_structure(".", structure)
    print("✅ Cấu trúc thư mục và file đã được tạo.")
