from .vision_analyzer import analyze_ui


def review_ui(image_path: str):

    result = analyze_ui(image_path)
    print("Review Result:", result)
    return result