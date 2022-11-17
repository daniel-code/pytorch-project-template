"""
Inference single sample with trained model
"""

import click
import pytorch_lightning as pl
import torch
from tqdm import tqdm

DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'


@click.command()
@click.option('--input-path', type=click.Path(exists=True), required=True, help='Path to input sample.')
@click.option('--model-path', type=click.Path(exists=True), required=True, help='Path to model weight.')
def main(
        input_path,
        model_path,
):
    """
    Pre-processing input sample.
    """
    x = None
    x = x.to(DEVICE)
    """
    Load trained model from model path.
    """
    model: pl.LightningModule = None

    model = model.load_from_checkpoint(model_path)
    model.eval()
    model.to(DEVICE)

    """
    Inference.
    """
    y_pred = model(x)
    print(y_pred)


if __name__ == '__main__':
    main()
