from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()

model = ChatGroq(  model="llama-3.3-70b-versatile", temperature=0)

# Schema
class Review(TypedDict):

    key_themes: Annotated[list[str], "Write down all the key thems discussed in the review in a list"]
    summary: Annotated[str, "a brif summary of the review"]
    sentiment: Annotated[Literal["pos","neg"],"Return the review either negative,positive or neutral"]
    pros : Annotated[Optional[list[str]], "Write down the pros inside a list"]
    cons : Annotated[Optional[list[str]], "Write down the cons inside a list"]
    name: Annotated[Optional[str], "Write the name of the reviewer"]

structured_mode = model.with_structured_output(Review)


result = structured_mode.invoke("""The Vivo V3 is a mid-range smartphone that combines a sleek metallic design with reliable performance. It features a 5-inch HD display, Snapdragon 616 processor, 3GB RAM, and a fingerprint sensor for quick unlocking. While it shines in terms of audio quality and build, it runs on an older Android version and has a modest battery.

✅ Pros:
Premium metallic design

Fast fingerprint sensor

Excellent audio with AK4375 Hi-Fi chip

Good camera performance for its class

❌ Cons:
Outdated Android version (Lollipop)

Small battery (2550 mAh)

Low screen resolution (720p).""")


print(result['name'])