import streamlit as st
from logic import parse_followers, parse_following, get_non_followers

st.set_page_config(page_title="Instagram Non-Followback Checker", layout="wide")
st.title("📉 Instagram Non-Followback Checker")

st.markdown("Upload file `followers_1.json` dan `following.json` dari data Instagram-mu.")

f1 = st.file_uploader("Upload followers_1.json", type="json")
f2 = st.file_uploader("Upload following.json", type="json")

if f1 and f2:
    try:
        followers = parse_followers(f1)
        following = parse_following(f2)
        non_followers = get_non_followers(followers, following)

        st.success(f"Ditemukan {len(non_followers)} akun yang tidak follow kamu balik.")

        if non_followers:
            st.subheader("👻 Akun yang tidak follow balik:")
            for user in non_followers:
                st.markdown(f"- [@{user}](https://www.instagram.com/{user})")
    except Exception as e:
        st.error(f"Terjadi kesalahan saat memproses: {e}")
