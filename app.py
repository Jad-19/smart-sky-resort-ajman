
import gradio as gr
import pandas as pd
import os

# =====================================================
# SMART SKY RESORT - AJMAN
# المنتجع السياحي الذكي المستقبلي
# FREE INTERACTIVE PROTOTYPE
# =====================================================

# -----------------------------------------------------
# IMAGES
# -----------------------------------------------------

images = {
    "resort": "resort.png",
    "room": "room.png",
    "robot": "robot.png",
    "energy": "energy.png"
}
for name, path in images.items():
    if os.path.exists(path):
        print("✅ Found:", name)
    else:
        print("⚠️ Missing:", path)


# -----------------------------------------------------
# FREE VIRTUAL CONCIERGE
# -----------------------------------------------------

def virtual_concierge(question):

    answers = {
        "ما الخدمات التي يقدمها المنتجع؟":
        """
### 🏨 خدمات المنتجع المستقبلية

يقدم المنتجع تصوراً لخدمات سياحية مبتكرة تشمل:

- غرف ذكية قابلة للتحكم.
- مساعد سياحي لتقديم التوصيات.
- روبوتات مستقبلية لخدمة الضيوف.
- أنظمة ذكية لإدارة الطاقة.
- تجربة مستوحاة من الضيافة الإماراتية.

جميع هذه الخدمات جزء من المشروع المقترح.
""",

        "ما أفضل الأماكن السياحية في عجمان؟":
        """
### 🗺️ اكتشف إمارة عجمان

**🏛️ متحف عجمان:** للتعرف على تاريخ الإمارة.

**🌊 كورنيش عجمان:** للاستمتاع بالبحر والتنزه.

**🌿 منطقة الزوراء:** لاستكشاف الطبيعة.

**⛰️ مصفوت:** للاستمتاع بالطبيعة الجبلية.

**🛍️ سيتي سنتر عجمان:** للتسوق والترفيه.

يمكنك استخدام قسم البرنامج السياحي
للحصول على توصيات حسب ميزانيتك.
""",

        "كيف تعمل الغرف الذكية؟":
        """
### 🛏️ الغرف الذكية

يمكن للزائر التحكم في:

- 💡 الإضاءة.
- 🌡️ درجة حرارة المكيف.
- 🪟 الستائر.
- 🌱 وضع توفير الطاقة.

في النموذج الأولي، يتم عرض التغييرات
من خلال محاكاة برمجية تفاعلية.
""",

        "كيف يساهم المنتجع في الاستدامة؟":
        """
### 🌱 الاستدامة البيئية

يعتمد تصور المشروع على:

- ☀️ الاستفادة من الطاقة الشمسية.
- ⚡ إدارة استهلاك الكهرباء.
- 🌡️ تحسين إعدادات التكييف.
- 💡 تقليل استهلاك الإضاءة.
- 📊 مراقبة الطاقة باستخدام لوحة تحكم.

يمكن تجربة محاكاة الطاقة في قسم الاستدامة.
""",

        "كيف تساعد الروبوتات الزوار؟":
        """
### 🤖 الروبوتات الذكية

يتضمن المشروع تصوراً لروبوتات تساعد في:

- استقبال الزوار.
- تقديم المعلومات السياحية.
- إرشاد الضيوف داخل المنتجع.
- شرح الخدمات المتاحة.
- دعم تجربة الضيافة المستقبلية.

الروبوتات حالياً جزء من التصور المستقبلي،
وليست أجهزة متصلة بالنموذج الأولي.
"""
    }

    return answers.get(
        question,
        "يرجى اختيار سؤال من القائمة."
    )


# -----------------------------------------------------
# TOURIST RECOMMENDATIONS
# -----------------------------------------------------

def recommend_places(interest, budget, duration):

    # All costs and times are illustrative.
    attractions = {
        "الثقافة والتراث": [
            ("🏛️ متحف عجمان", 25, 1.5),
            ("🏰 منطقة عجمان التراثية", 0, 1)
        ],
        "البحر والاسترخاء": [
            ("🌊 كورنيش عجمان", 0, 1.5),
            ("🏖️ شاطئ عجمان", 0, 2)
        ],
        "الطبيعة والمغامرات": [
            ("🌿 منطقة الزوراء", 100, 2),
            ("⛰️ منطقة مصفوت", 50, 4)
        ],
        "التسوق والترفيه": [
            ("🛍️ سيتي سنتر عجمان", 50, 2),
            ("☕ كورنيش عجمان", 0, 1)
        ]
    }

    remaining_budget = budget
    remaining_time = duration
    selected = []

    for name, cost, hours in attractions.get(interest, []):
        if cost <= remaining_budget and hours <= remaining_time:
            selected.append((name, cost, hours))
            remaining_budget -= cost
            remaining_time -= hours

    if not selected:
        return (
            "### لا توجد أنشطة مناسبة\n\n"
            "يرجى تعديل الميزانية أو المدة المتاحة."
        )

    result = "## ✨ برنامجك السياحي المقترح\n\n"

    for i, (name, cost, hours) in enumerate(selected, 1):
        result += (
            f"### {i}. {name}\n\n"
            f"💰 الميزانية التقديرية: {cost} درهم\n\n"
            f"⏱️ المدة المقترحة: {hours:g} ساعة\n\n"
            "---\n\n"
        )

    result += (
        f"**💳 الميزانية المتبقية:** "
        f"{remaining_budget:g} درهم\n\n"
        f"**🕒 الوقت المتبقي:** "
        f"{remaining_time:g} ساعة\n\n"
        "*التكاليف والمدد افتراضية لأغراض المحاكاة، "
        "وليست أسعار دخول فعلية.*"
    )

    return result


# -----------------------------------------------------
# SMART ROOM
# -----------------------------------------------------

def control_room(lights, temperature, curtains, eco_mode):

    if eco_mode:
        lights = False
        temperature = 26
        curtains = "مغلقة"

    light_status = "مضاءة 💡" if lights else "مطفأة 🌙"
    eco_status = "مفعل 🌱" if eco_mode else "غير مفعل"

    message = (
        "تم تطبيق إعدادات توفير الطاقة تلقائياً."
        if eco_mode
        else "تم تطبيق إعدادات الغرفة حسب تفضيلات الزائر."
    )

    return f"""
## 🛏️ حالة الغرفة الذكية

**💡 الإضاءة:** {light_status}

**🌡️ درجة حرارة المكيف:** {temperature}°C

**🪟 الستائر:** {curtains}

**🌱 وضع توفير الطاقة:** {eco_status}

---

### 🤖 استجابة النظام

{message}

*هذه محاكاة برمجية وليست تحكماً بأجهزة حقيقية.*
"""


# -----------------------------------------------------
# SUSTAINABILITY
# -----------------------------------------------------

def energy_dashboard(rooms, solar, saving):

    baseline = rooms * 30
    saved = baseline * saving / 100
    after_saving = baseline - saved
    solar_used = min(solar, after_saving)
    grid_energy = max(0, after_saving - solar_used)

    summary = f"""
## 🌱 نتائج محاكاة الطاقة

**🏨 عدد الغرف:** {rooms}

**⚡ الاستهلاك الأساسي:** {baseline:,.0f} كيلوواط ساعة/يوم

**💚 الطاقة الموفرة:** {saved:,.0f} كيلوواط ساعة/يوم

**📉 الاستهلاك بعد التوفير:** {after_saving:,.0f} كيلوواط ساعة/يوم

**☀️ الطاقة الشمسية المستخدمة:** {solar_used:,.0f} كيلوواط ساعة/يوم

**🔌 الطاقة المطلوبة من الشبكة:** {grid_energy:,.0f} كيلوواط ساعة/يوم

**📊 نسبة التوفير المفترضة:** {saving}%

---

*النتائج تقديرية بافتراض استهلاك أساسي
قدره 30 كيلوواط ساعة لكل غرفة يومياً.*
"""

    data = pd.DataFrame({
        "المؤشر": [
            "الاستهلاك الأساسي",
            "بعد التوفير",
            "الطاقة الشمسية",
            "طاقة الشبكة"
        ],
        "كيلوواط ساعة": [
            baseline,
            after_saving,
            solar_used,
            grid_energy
        ]
    })

    return summary, data


# -----------------------------------------------------
# LUXURY DESIGN + ARABIC RTL
# -----------------------------------------------------

custom_css = """
/* Main layout */
.gradio-container {
    max-width: 1250px !important;
    margin: auto !important;
    direction: rtl !important;
    font-family: Tahoma, Arial, sans-serif !important;
}

/* Arabic text */
.gradio-container .prose,
.gradio-container .prose *,
.gradio-container label,
.gradio-container input,
.gradio-container textarea,
.gradio-container [role="textbox"] {
    direction: rtl !important;
    text-align: right !important;
}

/* Main header */
#hero-title {
    background: #10243A !important;
    padding: 35px 20px;
    border: 2px solid #C9A45C;
    border-radius: 18px;
    text-align: center !important;
}

/* Header text */
#hero-title *,
#hero-title h1,
#hero-title h2,
#hero-title h3,
#hero-title p {
    color: #FFFFFF !important;
    text-align: center !important;
}

/* Headings */
.gradio-container h1,
.gradio-container h2,
.gradio-container h3 {
    color: #173451;
}

/* Tabs */
.gradio-container button[role="tab"] {
    font-size: 16px !important;
    font-weight: bold !important;
}

/* Gold buttons */
.gradio-container button.primary {
    background: #C9A45C !important;
    color: #10243A !important;
    border-radius: 12px !important;
    font-weight: bold !important;
}

/* Images */
.gradio-container img {
    border-radius: 14px;
}

/* Results */
.gradio-container .prose {
    line-height: 1.9;
}

/* Footer */
#resort-footer {
    text-align: center !important;
    padding: 25px;
    border-top: 2px solid #C9A45C;
    margin-top: 30px;
}

#resort-footer * {
    text-align: center !important;
}
"""

# Explicit light theme for readable text
theme = gr.themes.Soft(
    primary_hue="amber",
    neutral_hue="slate"
).set(
    body_background_fill="#F8F6F0",
    body_text_color="#17263C",
    block_background_fill="#FFFFFF",
    block_label_text_color="#17263C",
    input_background_fill="#FFFFFF",
    input_border_color="#C9A45C",
    button_primary_background_fill="#C9A45C",
    button_primary_text_color="#10243A"
)


# -----------------------------------------------------
# COMPLETE WEBSITE
# -----------------------------------------------------

with gr.Blocks(
    title="المنتجع السياحي الذكي المستقبلي",
    theme=theme,
    css=custom_css
) as demo:

    gr.Markdown("""
# ✨ المنتجع السياحي الذكي المستقبلي

### SMART SKY RESORT | AJMAN, UAE

**حيث تلتقي الفخامة بالتكنولوجيا**

مرحباً بكم في مستقبل السياحة الذكية والمستدامة
في إمارة عجمان.
""", elem_id="hero-title")

    # HOME
    with gr.Tab("🏠 الرئيسية"):

        gr.Markdown("## ✨ اكتشف منتجع المستقبل")

        if os.path.exists(images["resort"]):
            gr.Image(
                value=images["resort"],
                interactive=False,
                show_label=False
            )

        gr.Markdown("""
## 🌟 رؤيتنا

تقديم تجربة سياحية ذكية وفاخرة
تجمع بين التكنولوجيا الحديثة
والضيافة الإماراتية الأصيلة
والاستدامة البيئية.

### 💎 مميزات المشروع

**🤖 المساعد السياحي الافتراضي**

معلومات وإجابات تفاعلية للزوار.

**🗺️ التوصيات السياحية**

برامج مقترحة حسب اهتمامات الزائر وميزانيته.

**🛏️ الغرف الذكية**

التحكم في الإضاءة والتكييف والستائر.

**🦾 الروبوتات الذكية**

تصور مستقبلي لروبوتات الضيافة.

**☀️ الطاقة المستدامة**

محاكاة إدارة الطاقة الشمسية والكهرباء.

**🇦🇪 الهوية الإماراتية**

تجربة تجمع بين الأصالة والابتكار.

*جميع الصور تصورات مستقبلية للمشروع.*
""")

    # FREE CONCIERGE
    with gr.Tab("🤖 المساعد الافتراضي"):

        gr.Markdown("""
## 🤖 المساعد السياحي الافتراضي

مرحباً بك! اختر سؤالك للتعرف
على المنتجع وإمارة عجمان.

هذه خدمة تفاعلية مجانية تعتمد
على إجابات معدة مسبقاً.
""")

        if os.path.exists(images["robot"]):
            gr.Image(
                value=images["robot"],
                interactive=False,
                show_label=False
            )

        question = gr.Dropdown(
            choices=[
                "ما الخدمات التي يقدمها المنتجع؟",
                "ما أفضل الأماكن السياحية في عجمان؟",
                "كيف تعمل الغرف الذكية؟",
                "كيف يساهم المنتجع في الاستدامة؟",
                "كيف تساعد الروبوتات الزوار؟"
            ],
            value="ما الخدمات التي يقدمها المنتجع؟",
            label="💬 اختر سؤالك"
        )

        ask_button = gr.Button(
            "✨ عرض الإجابة",
            variant="primary"
        )

        concierge_answer = gr.Markdown()

        ask_button.click(
            fn=virtual_concierge,
            inputs=question,
            outputs=concierge_answer
        )

    # TOURIST PLANNER
    with gr.Tab("🗺️ البرنامج السياحي"):

        gr.Markdown("""
## 🗺️ صمم برنامجك السياحي

اختر اهتماماتك وميزانيتك والمدة المتاحة.
""")

        interest = gr.Dropdown(
            [
                "الثقافة والتراث",
                "البحر والاسترخاء",
                "الطبيعة والمغامرات",
                "التسوق والترفيه"
            ],
            value="الثقافة والتراث",
            label="🎯 اهتماماتك"
        )

        budget = gr.Slider(
            0, 1000,
            value=200,
            step=25,
            label="💰 الميزانية بالدرهم"
        )

        duration = gr.Slider(
            1, 12,
            value=4,
            step=1,
            label="⏱️ المدة المتاحة بالساعات"
        )

        recommend_button = gr.Button(
            "✨ إنشاء برنامجي السياحي",
            variant="primary"
        )

        recommendation_output = gr.Markdown()

        recommend_button.click(
            fn=recommend_places,
            inputs=[interest, budget, duration],
            outputs=recommendation_output
        )

    # SMART ROOM
    with gr.Tab("🛏️ الغرفة الذكية"):

        gr.Markdown("""
## 🛏️ نظام التحكم بالغرفة الذكية

جرب إعدادات الغرفة ووضع توفير الطاقة.
""")

        if os.path.exists(images["room"]):
            gr.Image(
                value=images["room"],
                interactive=False,
                show_label=False
            )

        lights = gr.Checkbox(
            label="💡 تشغيل الإضاءة",
            value=True
        )

        temperature = gr.Slider(
            18, 30,
            value=24,
            step=1,
            label="🌡️ درجة حرارة المكيف"
        )

        curtains = gr.Radio(
            ["مفتوحة", "مغلقة"],
            value="مفتوحة",
            label="🪟 حالة الستائر"
        )

        eco_mode = gr.Checkbox(
            label="🌱 تفعيل وضع توفير الطاقة",
            value=False
        )

        room_button = gr.Button(
            "⚙️ تطبيق إعدادات الغرفة",
            variant="primary"
        )

        room_output = gr.Markdown()

        room_button.click(
            fn=control_room,
            inputs=[lights, temperature, curtains, eco_mode],
            outputs=room_output
        )

    # ENERGY
    with gr.Tab("🌱 الاستدامة"):

        gr.Markdown("""
## 🌱 نظام إدارة الطاقة والاستدامة

محاكاة استهلاك الكهرباء والطاقة الشمسية.
""")

        if os.path.exists(images["energy"]):
            gr.Image(
                value=images["energy"],
                interactive=False,
                show_label=False
            )

        rooms = gr.Slider(
            10, 200,
            value=50,
            step=10,
            label="🏨 عدد الغرف"
        )

        solar = gr.Slider(
            0, 6000,
            value=800,
            step=100,
            label="☀️ الطاقة الشمسية اليومية"
        )

        saving = gr.Slider(
            0, 40,
            value=20,
            step=5,
            label="💚 نسبة التوفير المفترضة (%)"
        )

        energy_button = gr.Button(
            "⚡ حساب استهلاك الطاقة",
            variant="primary"
        )

        energy_report = gr.Markdown()

        energy_chart = gr.BarPlot(
            x="المؤشر",
            y="كيلوواط ساعة",
            title="مقارنة الطاقة اليومية"
        )

        energy_button.click(
            fn=energy_dashboard,
            inputs=[rooms, solar, saving],
            outputs=[energy_report, energy_chart]
        )

    gr.Markdown("""
### المنتجع السياحي الذكي المستقبلي

**SMART SKY RESORT — AJMAN**

نموذج أولي تفاعلي لمسابقة الابتكار السياحي

*جميع البيانات والمحاكاة لأغراض العرض فقط.*
""", elem_id="resort-footer")


# -----------------------------------------------------
# LAUNCH
# -----------------------------------------------------


demo.launch(
    server_name="0.0.0.0",
    server_port=int(os.environ.get("PORT", 10000)),
    share=False
)
