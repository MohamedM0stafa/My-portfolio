# app.py
import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(page_title="Mohamed Mostafa", layout="wide")


# Sidebar navigation
menu = st.sidebar.radio("Navigate", ["Home", "SQL", "Power BI", "Excel"])
if menu == "Home":
    # 1. تحديد مسار ملف الـ PDF الحقيقي على جهازك أو السيرفر
    # نفترض أن الملف موجود في مجلد assets واسمه Mohamed_Mostafa_Resume.pdf
    resume_path = r"Pictures/Mohamed_Mostafa.pdf"

    # 2. التأكد من وجود الملف أولاً وقراءته بصيغة الـ Bytes (rb) لضمان عدم حدوث خطأ
    if os.path.exists(resume_path):
        with open(resume_path, "rb") as f:
            pdf_data = f.read()

        # 3. زر التحميل النظيف
        st.download_button(
            label="📄 Download My Resume",
            data=pdf_data,  # نمرر البيانات التي قرأناها وليس مسار الملف كـ String
            file_name="Mohamed_Mostafa_Resume.pdf",
            mime="application/pdf",
        )
    else:
        # رسالة تظهر لك أنت فقط أثناء البرمجة إذا نسيت وضع الملف في مكانه
        st.warning("تنبيه للمطور: ملف الـ PDF غير موجود في المسار المحدّد.")

    col1, col2 = st.columns([1, 3])
    with col1:
        st.image(
            "Pictures/WhatsApp Image 2026-06-28 at 9.36.22 PM.jpeg",
            width=200,
        )  # صورتك هنا
    with col2:
        st.title("Hi, I am Mohamed Mostafa")
        st.write("Data Analyst | Turning Raw Data into Actionable Business Insights")
        st.info("Experience: SQL | Power BI | Excel")
        st.header("About Me")
        st.write(
            "Detail-oriented Data Analyst with 1 year of experience in data analytics, research, andreporting.Proficient in transforming"
            "raw data into actionable insights using Excel, Power BI, and SQL, with a strong ability to prepare comprehensive reports"
            "and presentations for stakeholders. Excellent communication and coordination skills, eager to contribute strong analytical"
            "abilities to drive research plans and support data-driven decision-making."
        )
    st.markdown("---")
    st.header("Skills")
    st.write("""
        * Data Analysis & BI: Power BI, Advanced Excel, Power Query.
        * Database & Querying: SQL (PostgreSQL / MySQL), Data Modeling (Star Schema), Advanced Queries (CTEs, Window Functions).
        * Programming & Scripting: Python (Pandas, NumPy, Matplotlib/Seaborn).
        """)
    st.markdown("---")
    st.markdown("### 📈 Key Achievements & Business Impact")

    # عمل 3 أعمدة لعرض الأرقام بجانب بعضها
    m1, m2, m3 = st.columns(3)

    with m1:
        st.metric(
            label="Time Saved via Automation", value="80%", delta="Excel Power Query"
        )

    with m2:
        st.metric(label="Query Performance Lift", value="45%", delta="SQL Optimization")

    with m3:
        st.metric(
            label="Analyzed Dataset Capacity",
            value="20K+ Rows",
            delta="Power BI Star Schema",
        )
    st.markdown("---")
    # عرض فقرة التعليم داخل صندوق أنيق ومميز
    st.markdown("### 🎓 Education & Certifications")
    st.write("""
    **Bachelor of Computer Science**
            : My academic journey provided me with a solid foundation in computational thinking, database management, and algorithmic logic. This computer science background naturally fueled my passion for data analytics, equipping me with the structured problem-solving skills needed to architecture robust data models, optimize complex SQL queries, and build efficient data pipelines, it helped me in
    * Formed a rock-solid foundation in logic, database structures, and analytical problem-solving.
    * Leveraged computational thinking to master data modeling, advanced SQL optimization, and programming.
    * Transformed academic knowledge into building data solutions that bridge the gap between technical complexity and business value.
    """)
    st.write("\n\n")
    st.write("""
        **Digital Egypt Pioneers Initiative (DEPI) – Ministry of Communications and Information Technology (MCIT)**
                """)
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("Pictures/Certificates/Capture.PNG", width=200)
    with col2:
        st.write("""
        **Program Description & Technical Core:**\n
        An intensive, government-sponsored professional training program focused on advanced data analytics methodologies and hands-on business intelligence tools. Equipped with the core technical competencies required to clean, model, analyze, and visualize complex datasets to drive data-driven business decisions:\n
        
        **Advanced Data Analysis via Microsoft Excel:**
        * Utilized Power Query for efficient data cleaning, transformation, and preprocessing of raw datasets.
        * Mastered Pivot Tables and data relationships to build structured models and generate dynamic, automated reports.
        
        **Database Management & Querying via SQL:**
        * Wrote optimized SQL queries for data retrieval and manipulation from relational databases.
        * Solved complex business questions using advanced SQL techniques, including multi-table JOINs, SELECT statements, aggregations, and subqueries.

        **Business Intelligence & Visualization via Microsoft Power BI:**
        * Designed robust Data Models and established proper relationships (Star Schema) between diverse data sources.
        * Proficiently used DAX (Data Analysis Expressions) to write custom measures and calculated columns for advanced business metrics.
        * Developed interactive, user-friendly dashboards and reports that turn complex analytical findings into compelling visual stories for stakeholders.
            """)

    # -----------------------------------------------------------------
    # IBM Certificate: Delivering Quality Work with Agility
    # -----------------------------------------------------------------
    st.write("\n\n")
    st.write("""
        **IBM – Delivering Quality Work with Agility**
        """)
    col_ibm_img, col_ibm_text = st.columns([1, 3])
    with col_ibm_img:
        st.image("Pictures/Certificates/certificate_3.png", width=200)
    with col_ibm_text:
        st.write("""
        **Program Description & Technical Core:**\n
        A professional course offered by IBM via Coursera focusing on agile methodologies, iterative delivery, and maintaining high quality in project workflows:\n
        
        **Agile Practices & Continuous Improvement:**
        * Applied agile methodologies and iterative project execution to enhance analytical deliverables.
        * Integrated feedback loops to streamline analytics development and foster adaptable workflows.
        
        **Quality Assurance & Workflow Optimization:**
        * Employed root-cause analysis and problem-solving strategies to ensure accuracy across reporting pipelines.
        * Focused on cross-functional collaboration and delivering iterative value to product and business teams.
        
        [🔗 Verify Credential](https://coursera.org/verify/5SRWJEFQRVS5)
        """)

        # -----------------------------------------------------------------
    # Google Certificate 1: Foundations of Data Science
    # -----------------------------------------------------------------
    st.write("\n\n")
    st.write("""
        **Google – Foundations of Data Science**
        """)
    col_g1_img, col_g1_text = st.columns([1, 3])
    with col_g1_img:
        st.image("Pictures/Certificates/certificate_4.png", width=200)
    with col_g1_text:
        st.write("""
        **Program Description & Technical Core:**\n
        An authorized professional course offered by Google via Coursera focusing on the core principles of data science and analytical frameworks to support data-driven decision-making:\n
        
        **Data Exploration & Core Methodologies:**
        * Gained a solid understanding of the data science lifecycle, foundational workflows, and career pathways.
        * Learned how to identify data ecosystem roles and manage end-to-end data analytics operations.
        
        **Analytical Impact & Communication:**
        * Explored essential tools and data structures to translate broad business problems into measurable questions.
        * Emphasized project scoping, data ethics, and impactful communication of analytical findings.
        
        [🔗 Verify Credential](https://coursera.org/verify/YW603NW57IVM)
        """)

        # -----------------------------------------------------------------
    # Google Certificate 2: Go Beyond the Numbers
    # -----------------------------------------------------------------
    st.write("\n\n")
    st.write("""
        **Google – Go Beyond the Numbers: Translate Data into Insights**
        """)
    col_g2_img, col_g2_text = st.columns([1, 3])
    with col_g2_img:
        st.image("Pictures/Certificates/certificate_2.png", width=200)
    with col_g2_text:
        st.write("""
        **Program Description & Technical Core:**\n
        An advanced Google professional course dedicated to turning raw quantitative analyses into compelling, actionable business narratives and insights:\n
        
        **Data Storytelling & Insight Extraction:**
        * Mastered executive-level data storytelling by transforming data outputs into actionable recommendations.
        * Structured findings clearly to bridge the gap between technical discovery and management decision-making.
        
        **Business Strategy & Presentation:**
        * Built focused presentations tailored to executive and non-technical stakeholders.
        * Applied structured frameworks to highlight key performance indicators (KPIs) and operational improvements.
        
        [🔗 Verify Credential](https://coursera.org/verify/3J38LZ0PV9WI)
        """)
    st.markdown("---")
    st.markdown("### ✉️ Contact Me & Connect")
    col_conn, col_form = st.columns(2)

    with col_conn:
        st.markdown("""
                    I'm always open to discussions about job opportunities, new projects, or exchanging experiences in the field of data analytics.

                    You can contact me directly through the following platforms:
                    """)
        # روابط التواصل السريعة
        # استبدل الروابط أدناه بروابط حساباتك الحقيقية
        st.markdown(
            "[🔗 Connect on LinkedIn](https://www.linkedin.com/in/mohamed-mostafa1-/?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BfBOnvVJFQTOFPKWPNDElcg%3D%3D)"
        )
        st.markdown("[📧 Send an Email](mailto:mohamedoxl98@gmail.com)")
    with col_form:
        st.markdown("**Or, Send Me a Direct Message:**")

        # استخدام خدمة FormSubmit المجانية لاستقبال الرسائل على إيميلك مباشرة
        # استبدل "your_email@gmail.com" بإيميلك الحقيقي لتصلك الرسائل عليه
        contact_form = """
        <form action="https://formsubmit.co/mohamedoxl98@gmail.com" method="POST" style="background-color: #f0f2f6; padding: 20px; border-radius: 10px;">
            <input type="hidden" name="_captcha" value="false">
            <input type="hidden" name="_next" value="http://localhost:8501">
            <input type="text" name="name" placeholder="Your Name" required style="width: 100%; margin-bottom: 10px; padding: 8px; border-radius: 5px; border: 1px solid #ccc;">
            <input type="email" name="email" placeholder="Your Email" required style="width: 100%; margin-bottom: 10px; padding: 8px; border-radius: 5px; border: 1px solid #ccc;">
            <textarea name="message" placeholder="Your Message Here..." required style="width: 100%; height: 100px; margin-bottom: 10px; padding: 8px; border-radius: 5px; border: 1px solid #ccc;"></textarea>
            <button type="submit" style="background-color: #2dd4bf; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; width: 100%;">Send Message</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)

elif menu == "SQL":
    st.markdown("### ❓ Business Scenario & Core Question")
    with st.chat_message("user", avatar="🏢"):
        st.write("**Management Question:**")
        st.write("""Display
        \na. The name and the gender of the dependence that's gender is Female and depending on Female Employee.
        \nb. And the male dependence that depends on Male Employee.""")
    st.code("""select *
from Dependent d , Employee e
where d.ESSN = e.SSN and d.Sex = 'F' and e.Sex = 'M'

Union

select *
from Dependent d , Employee e
where d.ESSN = e.SSN and e.Sex = 'M' and d.Sex = 'M'""")
    # Place your SQL result image here
    st.success("Output")
    st.image("Pictures/SQL/Capture.PNG")
    st.markdown("---")

    with st.chat_message("user", avatar="🏢"):
        st.write("**Management Question:**")
        st.write(
            """For each project, list the project name and the total hours per week (for all employees) spent on that project."""
        )
    st.code("""select Pno , pname , SUM(hours) as [Total Hours]
from Project inner join Works_for
on Pno = Pnumber
group by Pno , Pname""")
    # Place your SQL result image here
    st.success("Output")
    st.image("Pictures/SQL/Capture2.PNG")
    st.markdown("---")

    with st.chat_message("user", avatar="🏢"):
        st.write("**Management Question:**")
        st.write(
            """Display the data of the department which has the smallest employee ID over all employees' ID."""
        )
    st.code("""select Departments.*
from Departments inner join Employee
on Dno = Dnum
where SSN = ( select MIN(ssn)
			  from Employee )""")
    # Place your SQL result image here
    st.success("Output")
    st.image("Pictures/SQL/Capture3.PNG")
    st.markdown("---")

    with st.chat_message("user", avatar="🏢"):
        st.write("**Management Question:**")
        st.write(
            """For each department, retrieve the department name and the maximum, minimum and average salary of its employees."""
        )
    st.code("""select Dname , MAX(salary) as Maximum , MIN(salary) as Minimum
		, AVG(SALARY) AS AVERAGE
from Departments , Employee
where Dno = Dnum
group by Dname""")
    # Place your SQL result image here
    st.success("Output")
    st.image("Pictures/SQL/Capture4.PNG")
    st.markdown("---")

    with st.chat_message("user", avatar="🏢"):
        st.write("**Management Question:**")
        st.write("""List the last name of all managers who have no dependents.""")
    st.code("""select Lname
from Employee inner join Departments
on SSN = MGRSSN left outer join Dependent
on SSN = ESSN
where ESSN is null""")
    # Place your SQL result image here
    st.success("Output")
    st.image("Pictures/SQL/Capture5.PNG")
    st.markdown("---")

    with st.chat_message("user", avatar="🏢"):
        st.write("**Management Question:**")
        st.write(
            """For each department-- if its average salary is less than the average salary of all employees-- display its number, name and number of its employees."""
        )
    st.code("""select Dnum , Dname , count(ssn) [No. Employees]
from Employee inner join Departments
on dno = Dnum
group by Dnum , Dname
having AVG(salary) < ( select AVG(salary)
					   from Employee )""")
    # Place your SQL result image here
    st.success("Output")
    st.image("Pictures/SQL/Capture6.PNG")
    st.markdown("---")

    with st.chat_message("user", avatar="🏢"):
        st.write("**Management Question:**")
        st.write(
            """Retrieve a list of employees and the projects they are working on ordered by department and within each department, ordered alphabetically by last name, first name."""
        )
    st.code("""select e.Fname + ' ' + Lname [Employee Name] ,
	p.Pname as [Project Name] , Dno
from Employee as e , Project as p , Works_for as w
where e.ssn = w.ESSn and w.Pno = p.Pnumber
order by e.Dno , Lname , Fname""")
    # Place your SQL result image here
    st.success("Output")
    st.image("Pictures/SQL/Capture7.PNG")
    st.markdown("---")

    with st.chat_message("user", avatar="🏢"):
        st.write("**Management Question:**")
        st.write(
            """update all salaries of employees who work in Project ‘Al Rabwah’ by 30%."""
        )
    st.code("""update Employee
set Salary = Salary + Salary * 0.3
where SSN = (
			 select SSN
			 from Employee inner join Works_for
			 on SSN = ESSn inner join Project
			 on Pno = Pnumber
			 where Pname = 'Al Rabwah'
			)
""")
    st.markdown("---")


elif menu == "Power BI":
    st.header("📊 Power BI Business Intelligence Hub")
    st.markdown("---")

    # 1. إنشاء التابات بأسماء المشاريع الخاصة بك
    tab1, tab2, tab3 = st.tabs(
        [
            "🏪 Superstore Sales Dashboard",
            "📈 Project 2: Financial Analysis",
            "👥 Project 3: HR Analytics",
        ]
    )

    # -----------------------------------------------------------------
    # التاب الأول: مشروع Superstore Sales (المشروع الحالي)
    # -----------------------------------------------------------------
    with tab1:
        st.subheader("Superstore Sales Executive Dashboard")
        st.caption(
            "Strategic Business Intelligence Solution for Retail Performance Analysis"
        )

        # تقسيم التاب إلى عمودين: عمود للشرح وعمود للـ Dashboard
        col1, col2 = st.columns([2, 3])

        with col1:
            st.markdown("### Problem Statement & Objective")
            st.write("""
           Transforming the sales data of a large store (containing over 9,800 Row) into a customized interactive dashboard for efficient executive management and the discovery of successful secretaries and creative talents.
            """)

            st.markdown("### DAX code for measure\n\n")
            st.code("Total Sales = SUM('Superstore Sales Dataset'[Sales])")

            st.markdown("### 🛠️ Technical Stack")
            st.markdown("""
            * **Data Modeling:** Star Schema (Fact & Dimension Tables).
            * **Advanced Calculations:** Advanced DAX (Time Intelligence, MoM Growth, YTD).
            * **ETL:** Power Query data cleansing.
            """)

        with col2:
            st.markdown("### Dashboard Preview")
            st.image("Pictures/Power BI/Capture.PNG")
    # -----------------------------------------------------------------
    # التاب الثاني: مشروعك القادم (كمثال)
    # -----------------------------------------------------------------
    with tab2:
        st.subheader("Financial Performance Dashboard")
        col1, col2 = st.columns([2, 3])
        with col1:
            st.markdown("### 🎯 Objective")
            st.write(
                "تحليل القوائم المالية، التدفقات النقدية، ومقارنة الأرباح الفعلية بالميزانية التقديرية."
            )
        # with col2:
        # ضع رابط مشروعك الثاني هنا
        # pbi_url_2 = "https://app.powerbi.com/view?r=رابط_المشروع_الثاني_هنا"
        # components.iframe(pbi_url_2, height=600, scrolling=True)

    # -----------------------------------------------------------------
    # التاب الثالث: مشروع آخر (كمثال)
    # -----------------------------------------------------------------
    with tab3:
        st.subheader("HR & Employee Turnover Analytics")
        col1, col2 = st.columns([2, 3])
        with col1:
            st.markdown("### 🎯 Objective")
            st.write(
                "تحليل معدلات مغادرة الموظفين (Churn) وربطها بسنوات الخبرة، الأقسام، والتقييم السنوي."
            )
        # with col2:
        # ضع رابط مشروعك الثالث هنا
        # pbi_url_3 = "https://app.powerbi.com/view?r=رابط_المشروع_الثالث_هنا"
        # components.iframe(pbi_url_3, height=600, scrolling=True)
elif menu == "Excel":
    st.header("Financial Reporting")
    st.image("assets/excel_dash.png")
    st.write("[Download File](https://github.com/...)")
