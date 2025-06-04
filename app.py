import streamlit as st
from logic import parse_followers, parse_following, get_non_followers

st.set_page_config(page_title="Instagram Non-Followback Checker", layout="wide")
st.title("📉 Instagram Non-Followback Checker")

# Introduction and explanation
st.markdown("""
# 🔍 Cari Tahu Siapa yang Nggak Follow Balik Kamu di Instagram!

FYI: Web App ini tidak menggunakan database sama sekali. Artinya, tidak ada data yang disimpan. Semua dilakukan di perangkat kamu, aman & privat.
Tujuannya hanya untuk membantumu membaca data followers & following, biar kamu nggak bingung lagi siapa yang nggak follow balik. 😄
""")

st.subheader("✨ Langkah-Langkah Mudah:")
with st.expander("Lihat instruksi lengkap"):
    st.markdown("""
    1. Masuk ke Instagram kamu
    2. Buka Profil > Garis tiga (☰) / Pengaturan
    3. Pilih Pusat Akun
    4. Klik Informasi dan Izin Anda
    5. Pilih Unduh Informasi Anda
    6. Klik Mengunduh atau Mentransfer informasi
    7. Pilih akun Instagram yang ingin dicek
    8. Klik Beberapa Informasi Anda
    9. Scroll ke bagian Koneksi, lalu pilih ✅ Pengikut & Mengikuti
    10. Pilih Unduh ke perangkat
    11. Di bagian Rentang Tanggal, pilih: Sepanjang Waktu
    12. Di bagian Format, pilih: JSON
    13. Klik Buat File dan tunggu ± 3–10 menit (tergantung jumlah followers)
    14. Setelah file siap, unduh file dari bagian Unduh Informasi Anda
    15. File akan berbentuk ZIP
    16. Ekstrak file tersebut (pakai ZArchiver, RAR, dll di HP kamu)
    17. Upload 2 file hasil ekstrak: `followers_1.json` dan `following.json`
    """)

st.markdown("---")

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

# Add footer information
st.markdown("---")
st.markdown("""
        ### 💬 Butuh Bantuan?
        DM aja langsung ke [@panggilgaaaja](https://www.instagram.com/panggilgaaaja) di Instagram!

        ### 💡 Catatan:
        Web app ini akan terus di-update dengan fitur-fitur baru!

        Jangan lupa bagikan ke teman-temanmu, supaya makin banyak yang terbantu ✨
        """)