from backend.analyzer import analyze_video_bytes


def test_size_bias_reduced():
    # Very small synthetic file
    small = b'\x00' * 2000  # ~0.002 MB
    small_result = analyze_video_bytes(small, filename='normal.mp4', ignore_size=False)

    # Very large synthetic file
    large = b'\x00' * (1024 * 1024 * 200)  # 200 MB
    large_result = analyze_video_bytes(large, filename='normal.mp4', ignore_size=False)

    # Confidence should not be wildly different solely due to size (log scale)
    assert 0 <= small_result['confidence'] <= 1
    assert 0 <= large_result['confidence'] <= 1
    # They should be different but within a reasonable bound (size contrib limited)
    assert abs(small_result['confidence'] - large_result['confidence']) < 0.5


def test_ignore_size_flag():
    # Create a file in the 'suspicious' size range but with no other indicators
    suspicious = b'\x01' * (1024 * 1024 * 10)  # 10 MB

    res_with_size = analyze_video_bytes(suspicious, filename='video.mp4', ignore_size=False)
    res_ignored = analyze_video_bytes(suspicious, filename='video.mp4', ignore_size=True)

    # When size is ignored, confidence should be less than or equal to when size is considered
    assert res_ignored['confidence'] <= res_with_size['confidence']
