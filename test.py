import pytest
import model

def test_model_train():
    assert model.train_data.shape[0] == model.train_labels.shape[0]
    assert model.test_data.shape[0] == model.test_labels.shape[0]
    assert model.train_data.shape[1] == model.test_data.shape[1]

def test_model_evaluation():
    assert model.accuracy >= 0.0
    assert model.accuracy <= 1.0
