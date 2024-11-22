from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "resume.pdf"
profile_pic = current_dir / "assets" / "cropped_image_陳本瑜.jpg"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital Resume | Ben Chen"
PAGE_ICON = ":wave:"
NAME = "Ben Chen"
DESCRIPTION = """
Motivated learner transitioning from Geological Engineering to Data Science, with skills in data analysis, machine learning, and deep learning using Python, TensorFlow, and PyTorch.
"""
EMAIL = "ben.chen968@gmail.com"
SOCIAL_MEDIA = {
    "GitHub": "https://github.com/benintw",
    "LinkedIn": "https://www.linkedin.com/in/chen-ben968/",
}
PROJECTS = {
    "🐍 Chip Anomaly Detection Using PatchCore Model": "empty",
    "🔍 Retrieval-Augmented Generation (RAG) Model QA Interface": "empty",
    "👁️ Implementing Grad-CAM for Classification Explainability": "empty",
    "🎯 Human Image Segmentation with U-Net and EfficientNet": "empty",
    "📦 Object Localization for Fruits Using EfficientNet": "empty",
    "😀 Facial Expression Recognition Using EfficientNet": "empty",
    "🛣️ Aerial Road Segmentation Using U-Net": "empty",
    "👥 Person Re-Identification Using Triplet Loss": "empty",
    "📊 Facial Keypoint Detection Using ResNet": "empty",
    "🔎 Instagram Fake Account Detection": "empty",
    "📰 Fake News Detection Using BiLSTM": "empty",
    "🖥️ GPT-2 Model Demonstration Web App": "empty",
    "🖥️ Transformer Architecture Visualization Web App": "empty",
    "💪 Gym Member Management System with Facial Recognition": "empty",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

st.title("Hello there!")

# --- LOAD ASSETS ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" ⬇️  Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

# --- SOCIAL LINKS ---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- EDUCATION ---
st.write("#")
st.subheader("Education")
st.write(
    """
- National Taipei University of Technology, Master of Science in Artificial Intelligence Technology (2023-present)
- University of British Columbia, Bachelor of Applied Science in Geological Engineering (2011-2016)
"""
)

# --- EXPERIENCE & QUALIFICATIONS ---
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    """
- ABC
- DEF
- GHI
"""
)

# --- SKILLS ---
st.write("#")
st.subheader("Skills")
st.write(
    """
- Python
- TensorFlow
- PyTorch
- Machine Learning
- Deep Learning
"""
)

# --- WORK HISTORY ---
st.write("#")
st.subheader("Work History")
st.write("---")

# --- JOB 1 ---
st.write("Research Assistant, National Taipei University of Technology")
st.write("2022-2023")
st.write(
    """
- ABC
- DEF
- GHI
"""
)

# --- JOB 2 ---
st.write("Project Engineer, All Roads Construction Co., Ltd.")
st.write("2022-2023")
st.write(
    """
- ABC
- DEF
- GHI
"""
)

# --- JOB 3 ---
st.write("Project Engineer, Primo Stone Works Co., Ltd.")
st.write("2022-2023")
st.write(
    """
- ABC
- DEF
- GHI
"""
)

# --- PROJECTS ---
st.write("#")
st.subheader("Projects")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"{project} | [Source Code]({link})")
