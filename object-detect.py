from llm_axe import OllamaChat, ObjectDetectorAgent, safe_read_json

llm = OllamaChat(model = "llava-7b")

detector = ObjectDetectorAgent(llm, llm)

with open('my-img.jpg.png', 'rb') as image_file:
    image_data = image_file.read()

print(type(image_data))

res = detector.detect(
    images= [image_data],
    detection_criteria = "Detect all objects in the image."
)

print(res)

json = safe_read_json(res)
print(json)



