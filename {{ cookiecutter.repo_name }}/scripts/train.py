import os

import click
import mlflow
import mlflow.pytorch
import pytorch_lightning as pl
from dotenv import load_dotenv

"""
from {{ cookiecutter.module_name }}.data import DataModule
from {{ cookiecutter.module_name }}.models import Module
"""

load_dotenv()


@click.command()
@click.option('-r', '--dataset-root', type=click.Path(exists=True), default='datasets/final', required=True,
              help='The root path to dataset. Default: datasets/final')
@click.option('--batch-size', type=int, default=16, help='Batch size. Default: 16')
@click.option('--max-epochs', type=int, default=10, help='Training epochs. Default: 10')
@click.option('--num-workers',
              type=int,
              default=os.cpu_count() // 4,
              help=f'Number of workers. #CPU of this machine: {os.cpu_count()}. Default: {os.cpu_count() // 4}')
@click.option('--seed', type=int, default=168, help='Random seed of train/test split. Default: 168')
@click.option('--model-type', type=str, default='resnet50', help='The types of model. Default: resnet50')
@click.option('--accelerator',
              type=str,
              default='auto',
              help='Supports passing different accelerator types ("cpu", "gpu", "tpu", "ipu", "auto") '
                   'as well as custom accelerator instances. Default: auto')
@click.option('--output-path',
              type=str,
              default='logs',
              help='Path to output model weight. Default: logs')
@click.option('--fast-dev-run', type=bool, is_flag=True, help='Run fast develop loop of pytorch lightning')
def main(
        dataset_root,
        batch_size,
        max_epochs,
        num_workers,
        seed,
        model_type,
        accelerator,
        output_path,
        fast_dev_run,
):
    pl.seed_everything(seed)
    mlflow.set_tracking_uri(os.environ['MLFLOW_URL'])
    mlflow.set_experiment(experiment_name=os.environ['MLFLOW_EXPERIMENT_NAME'])

    """
    Setup data augmentation.
    """

    """
    Setup datamodule in {{ cookiecutter.module_name }}.data.
    """
    datamodule = None
    print(datamodule)

    """
    Setup datamodule in {{ cookiecutter.module_name }}.models.
    """
    model = None

    with mlflow.start_run() as run:
        print(run.info.run_id)
        output_path = os.path.join(output_path, run.info.run_id)
        os.makedirs(output_path)

        mlflow.log_param('model_type', model_type)
        mlflow.pytorch.autolog()

        trainer = pl.Trainer(
            accelerator=accelerator,
            max_epochs=max_epochs,
            fast_dev_run=fast_dev_run,
            default_root_dir=output_path
        )
        trainer.fit(model, datamodule=datamodule)
        result = trainer.test(model, datamodule=datamodule)
        print(result)

        trainer.save_checkpoint(os.path.join(output_path, 'model.ckpt'))


if __name__ == '__main__':
    main()
