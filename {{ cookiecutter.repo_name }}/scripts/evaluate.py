"""
Evaluation model performance and generate reports.
"""

import click
import pytorch_lightning as pl
import torch
from tqdm import tqdm

DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'


@click.command()
@click.option('-r', '--dataset-root', type=click.Path(exists=True), default='datasets/final', required=True,
              help='The root path to dataset. Default: datasets/final')
@click.option('--model-path', type=click.Path(exists=True), required=True, help='Path to model weight.')
@click.option('--seed', type=int, default=168, help='Random seed of train/test split. Default: 168')
def main(
        dataset_root,
        model_path,
        seed,
):
    pl.seed_everything(seed)

    """
    Setup test transform.
    """

    """
    Setup data augmentation.
    """

    """
    Setup datamodule in {{ cookiecutter.module_name }}.data.
    """
    datamodule: pl.LightningDataModule = None
    datamodule.setup('test')
    test_dataloader = datamodule.test_dataloader()

    """
    Setup datamodule in {{ cookiecutter.module_name }}.models.
    """
    model: pl.LightningModule = None

    model = model.load_from_checkpoint(model_path)
    model.eval()
    model.to(DEVICE)

    with tqdm(total=len(test_dataloader)) as pbar:
        with torch.no_grad():
            for x, y in test_dataloader:
                x = x.to(DEVICE)
                y = y.to(DEVICE)
                y_pred = model(x)
                """
                Evaluate performance.
                """

                pbar.update()


if __name__ == '__main__':
    main()
