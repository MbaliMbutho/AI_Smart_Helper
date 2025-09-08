import streamlit as st
from chores import load_chores, save_chores
from groceries import load_groceries, save_groceries
from homework import load_homework, save_homework

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="AI Smart Helper", layout="centered")
st.title("🧠 AI Smart Helper")

# --- Sidebar for navigation ---
option = st.sidebar.selectbox(
    "Select an option",
    ("Home", "Chores", "Groceries", "Homework")
)

# ------------------ HELPER FUNCTION ------------------
def display_list(items, item_type):
    if items:
        st.subheader(f"{item_type} List")
        if item_type == "Chores":
            for idx, c in enumerate(items):
                st.write(f"{idx+1}. {c['task']} at {c['time']}")
        elif item_type == "Homework":
            for idx, h in enumerate(items):
                st.write(f"{idx+1}. {h['subject']}: {h['task']}")
        else:
            for idx, i in enumerate(items):
                st.write(f"{idx+1}. {i}")
    else:
        st.info(f"No {item_type.lower()} added yet.")

# ------------------ CHORES ------------------
if option == "Chores":
    st.header("🧹 Chores")
    tab1, tab2 = st.tabs(["➕ Add Chore", "📋 View / Delete Chores"])

    with tab1:
        with st.form(key="add_chore_form"):
            task = st.text_input("Chore Name")
            time = st.text_input("Time (HH:MM)")
            submit_chore = st.form_submit_button("Add Chore")

            if submit_chore:
                if task and time:
                    chores = load_chores()
                    chores.append({"task": task, "time": time})
                    save_chores(chores)
                    st.success(f"Chore '{task}' added for {time}")
                else:
                    st.error("Please enter both chore and time")

    with tab2:
        chores = load_chores()
        display_list(chores, "Chores")

        if chores:
            delete_task = st.selectbox("Select a chore to delete:", [f"{c['task']} at {c['time']}" for c in chores])
            if st.button("Delete Chore"):
                chores = [c for c in chores if f"{c['task']} at {c['time']}" != delete_task]
                save_chores(chores)
                st.success(f"Deleted chore: {delete_task}")
                display_list(chores, "Chores")

# ------------------ GROCERIES ------------------
elif option == "Groceries":
    st.header("🛒 Groceries")
    tab1, tab2 = st.tabs(["➕ Add Grocery", "📋 View / Delete Groceries"])

    with tab1:
        with st.form(key="add_grocery_form"):
            item = st.text_input("Grocery Item")
            submit_grocery = st.form_submit_button("Add Grocery")

            if submit_grocery:
                if item:
                    groceries = load_groceries()
                    groceries.append(item)
                    save_groceries(groceries)
                    st.success(f"Added '{item}' to groceries")
                else:
                    st.error("Please enter a grocery item")

    with tab2:
        groceries = load_groceries()
        display_list(groceries, "Groceries")

        if groceries:
            delete_item = st.selectbox("Select a grocery to delete:", groceries)
            if st.button("Delete Grocery"):
                groceries.remove(delete_item)
                save_groceries(groceries)
                st.success(f"Deleted grocery: {delete_item}")
                display_list(groceries, "Groceries")

# ------------------ HOMEWORK ------------------
elif option == "Homework":
    st.header("📚 Homework")
    tab1, tab2 = st.tabs(["➕ Add Homework", "📋 View / Delete Homework"])

    with tab1:
        with st.form(key="add_homework_form"):
            subject = st.text_input("Subject")
            task = st.text_input("Task")
            submit_homework = st.form_submit_button("Add Homework")

            if submit_homework:
                if subject and task:
                    homework = load_homework()
                    homework.append({"subject": subject, "task": task})
                    save_homework(homework)
                    st.success(f"Added homework for {subject}: {task}")
                else:
                    st.error("Please enter both subject and task")

    with tab2:
        homework = load_homework()
        display_list(homework, "Homework")

        if homework:
            delete_homework = st.selectbox("Select homework to delete:", [f"{h['subject']}: {h['task']}" for h in homework])
            if st.button("Delete Homework"):
                homework = [h for h in homework if f"{h['subject']}: {h['task']}" != delete_homework]
                save_homework(homework)
                st.success(f"Deleted homework: {delete_homework}")
                display_list(homework, "Homework")

# ------------------ HOME PAGE ------------------
else:
    st.header("Welcome to 🧠 AI Smart Helper!")
    st.write("Your personal assistant to keep track of **chores, groceries, and homework** all in one place.")

    st.image("https://cdn-icons-png.flaticon.com/512/4715/4715105.png", width=100)

    st.subheader("✨ What you can do here:")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 🧹 Chores")
        st.info("Add daily chores with time reminders and view your full chore list.")

    with col2:
        st.markdown("### 🛒 Groceries")
        st.info("Keep your grocery shopping list updated and never forget an item.")

    with col3:
        st.markdown("### 📚 Homework")
        st.info("Track homework by subject and tasks so you stay on top of schoolwork.")

    st.subheader("🚀 Get Started")
    st.success("Use the **sidebar** to start managing your day more efficiently!")

    st.markdown("---")
    st.caption("Made with ❤️ using Streamlit")
