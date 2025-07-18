from transformers import pipeline

# pipe = pipeline("text-classification", model="Shubh0904/autotrain-ot52s-j6gen", truncation=True)


def analyse_raw_email(email_text) -> dict:
    return {"probability": 0.23, "text": "result['label']"}
    # texts = [email_text]
    # results = pipe(texts)
    # result = results[0]
    # # print(result['label'].lower() == "safe email")
    # if result['label'].lower() == "safe email":
    #     probability = 1 - result['score']
    # else:
    #     probability = result['score']
    # return {"probability": probability, "text": result['label']}
