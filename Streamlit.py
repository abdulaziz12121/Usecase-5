import streamlit as st

import pandas as pd
import numpy as np

st.image("image.jpg")

st.markdown(
    """
<h1 style="font-weight: bold; direction: rtl;">قصة اختيار تخصص الجامعة</h1>              
    
<p style="direction: rtl;">عمر: اخر سنة في الثانوية وما تعرف وش تدخل تخصص في الجامعة صح</p>
<p style="direction: rtl;">عبدالعزيز: صح، كيف رواتب خرجي الجامعة بشكل عام</p>
<p style="direction: rtl;">عمر: اعطيك العلم</p>
    """,
    unsafe_allow_html=True
)

st.image("image 3.png")


# Using HTML and CSS to set text direction to right-to-left
st.markdown(
    """
    
             <p style="direction: rtl;">عبدالعزيز: جميل</p>
<p style="direction: rtl;">عمر: عطني طلباتك في التخصص</p>
<p style="direction: rtl;">عبدالعزيز: اهم شي يكون مطلوب في سوق العمل</p>
<p style="direction: rtl;">عمر: اكثر التخصصات مطلوبة</p>

<p style="direction: rtl;">1-بائع</p>
<p style="direction: rtl;">2.محاسب</p>
<p style="direction: rtl;">3.أخصائي تسويق</p>
<p style="direction: rtl;">4.مساعد إداري</p>
<p style="direction: rtl;">5.موظف استقبال</p>

   
    """,
    unsafe_allow_html=True
)
st.image("image1.png")
#-----------------------------------------------------------------------

# Using HTML and CSS to set text direction to right-to-left
st.markdown(
    """
<p style="direction: rtl;"> عمر: ابشر وهاذي اعلى 3 مناطق </p>
<ul style="direction: rtl;">
    <li>الرياض</li>
    <li>مكة المكرمة</li>
    <li>المنطقة الشرقية</li>
</ul>
    """,
    unsafe_allow_html=True
)
st.image("image2.png")
st.markdown(
    """
<p style="direction: rtl;">عبدالعزيز: جميل, معلومات مفيدة جدا, بدخل حاسب</p>
    """,
    unsafe_allow_html=True
)

#-----------------------------------------------------------------------