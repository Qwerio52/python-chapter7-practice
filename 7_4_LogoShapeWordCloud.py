import jieba
from wordcloud import WordCloud
import numpy as np
from PIL import Image

def logo_mask_wordcloud(mask_img_path, poem_txt, out_img="logo_wordcloud.png"):
    mask = np.array(Image.open(mask_img_path))
    with open(poem_txt, "r", encoding="utf-8") as f:
        text = f.read()
    words = jieba.lcut(text)
    cut_text = " ".join(words)
    wc = WordCloud(
        font_path="simhei.ttf",
        mask=mask,
        background_color="white",
        width=800,
        height=600
    )
    wc.generate(cut_text)
    wc.to_file(out_img)
    print(f"Logo wordcloud saved: {out_img}")

if __name__ == "__main__":
    logo_mask_wordcloud("logo.png", "poem.txt")