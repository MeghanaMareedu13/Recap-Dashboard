import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Meghana's 30-Day Technical Challenge - Week 1 Recap",
    page_icon="🚀",
    layout="wide"
)

# Sidebar
with st.sidebar:
    st.title("🚀 Week 1 Complete")
    st.markdown("---")
    st.info("6 Projects | 7 Days | 100% Commitment")
    st.markdown("---")
    st.markdown("### Connect with Me")
    st.markdown("[LinkedIn](https://linkedin.com/in/meghanagoud13)")
    st.markdown("[GitHub](https://github.com/MeghanaMareedu13)")

# Header Section
st.title("🏆 Week 1 Recap: Building Momentum")
st.markdown("""
Welcome to the recap of my first week in the **30-Day Recruiter Attraction Challenge**. 
In 7 days, I've transitioned from high-level planning to building production-ready tools across 
Data Engineering, Backend Development, and Business Intelligence.
""")

# Projects Section
st.header("📂 Week 1 Portfolio")

col1, col2 = st.columns(2)

with col1:
    with st.expander("Day 1: Personal Portfolio Website", expanded=True):
        st.write("**Tech**: HTML, CSS, JavaScript")
        st.write("My digital home base showcasing my background and journey to Texas Tech.")
        st.markdown("[GitHub Repository](https://github.com/MeghanaMareedu13/portfolio-website)")

    with st.expander("Day 3: SQL Mastery Repository", expanded=True):
        st.write("**Tech**: PostgreSQL, SQL")
        st.write("Advance queries including Recursive CTEs, Window Functions, and Schema Design.")
        st.markdown("[GitHub Repository](https://github.com/MeghanaMareedu13/SQL-Mastery-Repository)")

    with st.expander("Day 5: Data Cleaning Framework", expanded=True):
        st.write("**Tech**: Python, Pandas, Numpy")
        st.write("A modular pipeline to transform messy raw data into production-ready datasets.")
        st.markdown("[GitHub Repository](https://github.com/MeghanaMareedu13/Data-Cleaning-Framework)")

with col2:
    with st.expander("Day 2: Python Automation Toolkit", expanded=True):
        st.write("**Tech**: Python, OS, SMTP")
        st.write("Enterprise-grade scripts that reduce manual work by 60%.")
        st.markdown("[GitHub Repository](https://github.com/MeghanaMareedu13/Python-Automation-Toolkit)")

    with st.expander("Day 4: Task Manager REST API", expanded=True):
        st.write("**Tech**: FastAPI, SQLAlchemy, SQLite")
        st.write("Fully documented CRUD API with automatic Swagger/OpenAPI generation.")
        st.markdown("[GitHub Repository](https://github.com/MeghanaMareedu13/Task-Manager-REST-API)")

    with st.expander("Day 6: Interactive Sales Dashboard", expanded=True):
        st.write("**Tech**: Streamlit, Plotly, Pandas")
        st.write("Visualizing business trends and regional performance with real-time filters.")
        st.markdown("[GitHub Repository](https://github.com/MeghanaMareedu13/Interactive-Sales-Dashboard)")

st.divider()

# Impact and Reflections
st.header("🧠 Reflection & Lessons Learned")

tabs = st.tabs(["💡 Biggest Win", "🚧 Major Challenge", "🎯 Next Week's Goal"])

with tabs[0]:
    st.subheader("Consistency is Key")
    st.write("""
    The biggest win this week wasn't just the code, but the **momentum**. 
    Bridging the gap between a Business Analyst mindset and a Software Engineer's toolkit 
    daily has drastically sharpened my technical communication.
    """)

with tabs[1]:
    st.subheader("Data is Messy")
    st.write("""
    Day 5's cleaning project reminded me that 80% of data work is preparation. 
    Building a reusable framework was a direct response to challenges I've faced in 
    past technical internship projects.
    """)

with tabs[2]:
    st.subheader("Deeper Technical Dives")
    st.write("""
    Week 2 will focus on **Technical Depth**. I'll be diving into Real-time Pipelines, 
    Web Scraping, and Database Normalization to show I can handle complex data architectures.
    """)

# Call to Action
st.divider()
st.success("**Recruiters & Tech Leads:** I'm actively seeking entry-level roles where I can apply this drive and technical range. Let's connect!")
