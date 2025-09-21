from ml_detector import predict_from_metrics


def test_predict_no_model():
    # If no model file exists, the function should return None (fallback behavior)
    res = predict_from_metrics({})
    assert res is None
