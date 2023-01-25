import mlflow

with mlflow.start_run():
    for i in range(100):

        mlflow.log_param("x", 1)

        mlflow.log_metric("y", i,step=i)
