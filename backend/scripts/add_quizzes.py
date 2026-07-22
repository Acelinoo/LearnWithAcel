import json
import os

filepath = os.path.join(os.path.dirname(__file__), "content", "web_content.py")

namespace = {}
with open(filepath, "r", encoding="utf-8") as f:
    exec(f.read(), namespace)

web_content = namespace["WEB_CONTENT"]

for role, categories in web_content.items():
    for category in categories:
        for lesson in category["lessons"]:
            if "## Quiz" not in lesson["content"]:
                quiz_template = f"""

## Quiz

### Soal 1

Apa topik utama yang dibahas pada materi ini?

- A. Topik lain yang tidak relevan
- B. {lesson['title']}
- C. Tidak ada topik
- D. Rahasia perusahaan

Jawaban benar: B

Penjelasan: Materi ini difokuskan pada pemahaman tentang {lesson['title']}.
"""
                lesson["content"] += quiz_template

with open(filepath, "w", encoding="utf-8") as f:
    f.write("WEB_CONTENT = ")
    f.write(json.dumps(web_content, indent=4, ensure_ascii=False))
