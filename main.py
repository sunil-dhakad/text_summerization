from textSummarizer.pipeline.stage_01_data_ingestion import TrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.logging import logger

STAGE_NAME = "Data_ingestion_Stage"

try:
    logger.info(f">>>>>>>>>>>>>>>>>>stage  {STAGE_NAME} started <<<<<<<<<<<")
    pipeline_obj = TrainingPipeline()
    pipeline_obj.main()
    logger.info(f">>>>>>>>>>>>>   stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<")
except Exception as e:
    raise e


STAGE_NAME = "data_validation_stage"

try:
    logger.info(f" >>>>>>>>>>>>>>  stage : {STAGE_NAME} started  <<<<<<<<<<<<<<<<<<<<<<")
    validation_pipeline_obj = DataValidationTrainingPipeline()
    validation_pipeline_obj.main()
    logger.info(f">>>>>>>>>>>>>>>>>> STAGE: {STAGE_NAME}  started   <<<<<<<<<<<<<<<<<<<")
except Exception as e:
    raise e 