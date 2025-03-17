from image_processing_ferreedu import process_image

def test_process_image():
    result = process_image("path/to/image.jpg")
    assert result is not None