import jieba
from wordcloud import WordCloud

def generate_gov_wordcloud(txt_path, out_img="gov_wordcloud.png"):
    with open(txt_path, "r", encoding="utf-8") as f:
        text = f.read()
    words = jieba.lcut(text)
    stop_words = {"的","和","是","在","要","我们","也","对","为","把","等","与","有","将","不"}
    word_list = [w for w in words if len(w)>=2 and w not in stop_words]
    text_cut = " ".join(word_list)
    wc = WordCloud(
        font_path="simhei.ttf",
        background_color="white",
        max_words=100,
        width=800,
        height=600
    )
    wc.generate(text_cut)
    wc.to_file(out_img)
    print(f"Wordcloud saved: {out_img}")

if __name__ == "__main__":
    generate_gov_wordcloud("report.txt")