from textSummarizer.pipeline.stage_01_data_ingestion import TrainingPipeline
from textSummarizer.logging import logger

STAGE_NAME = "Data_ingestion_Stage"

try:
    logger.info(f">>>>>>>>>>>>>>>>>>stage  {STAGE_NAME} started <<<<<<<<<<<")
    pipeline_obj = TrainingPipeline()
    pipeline_obj.main()
    logger.info(f">>>>>>>>>>>>>   stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<")
except Exception as e:
    raise e
